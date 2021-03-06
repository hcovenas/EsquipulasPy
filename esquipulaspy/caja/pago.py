# -*- coding: utf-8 -*-
'''
Created on 25/05/2010

@author: Luis Carlos Mejia
'''


from PyQt4.QtCore import  pyqtSlot, Qt, QTimer, QDate, QDateTime
from PyQt4.QtGui import QDataWidgetMapper, QSortFilterProxyModel, QMessageBox, \
    QCompleter, qApp
from PyQt4.QtSql import QSqlQueryModel, QSqlQuery, QSqlDatabase
from decimal import Decimal
from document.pago.pagomodel import PagoModel
from ui.Ui_pago import Ui_frmPago
from utility import constantes
from utility.base import Base
from utility.decorators import if_edit_model
from utility.moneyfmt import moneyfmt
import logging



#from PyQt4.QtGui import QMainWindow

#controles
IDDOCUMENTO, NDOCIMPRESO, FECHA, NOMBREBENEFICIARIO, CONCEPTO, TOTALPAGADO, CONIVA, CONRETENCION, TASARETENCION, TOTALC, TOTALD, TOTAL, TOTALRETENCION, OBSERVACION, TIPOCAMBIO = range( 15 )

class FrmPago( Ui_frmPago, Base ):
    """
    Implementacion de la interfaz grafica para entrada compra
    """
    web = "recibos.php?doc="

    def __init__( self , sesion, parent ):
        '''
        Constructor
        @param sesion: Los datos de la sesión actual de caja
        @param parent: La ventana padre del formulario
        @type sesion: DatosSesion
        '''
        super( FrmPago, self ).__init__( parent, True )
        self.setWindowModality( Qt.WindowModal )
        self.setWindowFlags( Qt.Dialog )
        self.sesion = sesion
        self.tabledetails = None


        self.editmodel = None

        self.groupcuentas.setVisible( False )

        self.actionSave.setVisible( False )
        self.actionCancel.setVisible( False )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#        El modelo principal
        self.navmodel = QSqlQueryModel( self )
#        El modelo que filtra a self.navmodel
        self.navproxymodel = QSortFilterProxyModel( self )
        self.navproxymodel.setSourceModel( self.navmodel )
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

#        Este es el modelo con los datos de la con los detalles
        self.detailsmodel = QSqlQueryModel( self )
#        Este es el filtro del modelo anterior
        self.detailsproxymodel = QSortFilterProxyModel( self )

        self.sbtotalc.setValue( 0 )
        self.sbtotald.setValue( 0 )

        self.conceptosModel = QSqlQueryModel()

        QTimer.singleShot( 0, self.loadModels )


    def cancel( self ):
        """
        Aca se cancela la edicion del documento
        """
        self.status = True


    def newDocument( self ):
        """
        activar todos los controles, llenar los modelos necesarios, 
        crear el modelo Pago, aniadir una linea a la tabla
        """
        if not self.database.isOpen():
            if not self.database.open():
                raise UserWarning( u"No se pudo establecer la conexión con "\
                                   + "la base de datos" )
        query = QSqlQuery()
        try:

#            Rellenar el combobox de las CONCEPTOS

            self.conceptosModel.setQuery( """
               SELECT idconcepto, descripcion FROM conceptos c WHERE idtipodoc = %d;
            """ % constantes.IDPAGO )

            if self.conceptosModel.rowCount() == 0:
                raise UserWarning( u"No existen conceptos en la base de "\
                                   + "datos para los pagos" )

            self.beneficiariosModel = QSqlQueryModel()
            self.beneficiariosModel.setQuery( """
            SELECT
            s.idpersona,
            s.nombre
            FROM personas s
            WHERE s.tipopersona <> %d
            ORDER BY s.nombre
            """ % constantes.AUTOR )

            if self.beneficiariosModel.rowCount() == 0:
                raise UserWarning( u"No existen personas en la base de datos" )

            #            Rellenar el combobox de las retenciones
            self.retencionModel = QSqlQueryModel()
            self.retencionModel.setQuery( """
                    SELECT 
                        idcostoagregado, 
                        FORMAT(valorcosto,0) as tasa
                    FROM costosagregados 
                    WHERE 
                    idtipocosto IN (%d,%d) AND 
                    activo=1 
                    ORDER BY valorcosto desc; 
                    """ % ( constantes.RETENCIONPROFESIONALES,
                            constantes.RETENCIONFUENTE ) )
            if self.retencionModel.rowCount() == 0:
                raise UserWarning( u"No existe ninguna tasa de retención en "\
                                   + "la base de datos" )
            query = QSqlQuery( 
            """
            SELECT
                SUM(IF(m.idtipomoneda = %d,m.monto,0)) as totalC,
                SUM(IF(m.idtipomoneda = %d,m.monto,0)) as totalD
            FROM
            movimientoscaja m
            JOIN documentos d ON d.iddocumento = m.iddocumento
            WHERE d.idcaja = %d AND m.idtipomovimiento=%d
            ;
            """ % ( constantes.IDCORDOBAS,
                    constantes.IDDOLARES,
                    self.sesion.cajaId,
                    constantes.IDPAGOEFECTIVO ) )
            if not query.exec_():
                raise UserWarning( u"No pudo obtenerse de la base de datos la cantidad de dinero en caja" )
            query.first()
            maxCordoba = Decimal( query.value( 0 ).toString() )
            maxDolar = Decimal( query.value( 1 ).toString() )

            if maxCordoba <= 0 and maxDolar <= 0:
                raise UserWarning( u"No hay Efectivo en Caja" )


            query = QSqlQuery( "SELECT fnCONSECUTIVO(%d,null);" % constantes.IDPAGO )
            if not query.exec_():
                raise UserWarning( u"No pudo obtenerse el número del comprobante" )
            query.first()
            ndoc = query.value( 0 ).toString()
            self.lblnpago.setText( ndoc )

            self.txttipocambio.setText( moneyfmt( self.sesion.tipoCambioBanco, 4 ) )

            self.cbtasaret.setModel( self.retencionModel )
            self.cbtasaret.setModelColumn( 1 )
            self.cbtasaret.setCurrentIndex( -1 )
            self.retencionId = 0



            self.cbbeneficiario.setModel( self.beneficiariosModel )
            self.cbbeneficiario.setCurrentIndex( -1 )
            self.cbbeneficiario.setModelColumn( 1 )
            completer = QCompleter()
            completer.setCaseSensitivity( Qt.CaseInsensitive )
            completer.setModel( self.beneficiariosModel )
            completer.setCompletionColumn( 1 )


            self.cbconcepto.setModel( self.conceptosModel )
            self.cbconcepto.setCurrentIndex( -1 )
            self.cbconcepto.setModelColumn( 1 )
            completerconcepto = QCompleter()
            completerconcepto.setCaseSensitivity( Qt.CaseInsensitive )
            completerconcepto.setModel( self.conceptosModel )
            completerconcepto.setCompletionColumn( 1 )

            self.editmodel = PagoModel( self.sesion )
            self.editmodel.docImpreso = ndoc

            self.editmodel.maxCordoba = maxCordoba
            self.editmodel.maxDolar = maxDolar
            self.sbtotalc.setToolTip( "Max= " + moneyfmt( maxCordoba, 4, 'C$' ) )
            self.sbtotald.setToolTip( "Max= " + moneyfmt( maxDolar, 4, 'US$' ) )
            self.sbtotalc.setMaximum( maxCordoba )
            self.sbtotald.setMaximum( maxDolar )

            query = QSqlQuery( """
            SELECT idcostoagregado, valorcosto 
            FROM costosagregados c  
            WHERE idtipocosto = %d AND activo = 1;
            """ % constantes.IVA )
            if not query.exec_():
                raise UserWarning( u"No pudo obtenerse la tasa de IVA" )
            query.first()
            self.editmodel.ivaId = query.value( 0 ).toInt()[0]
            self.editmodel.ivaTasa = Decimal( query.value( 1 ).toString() )



            self.ckiva.setToolTip( query.value( 1 ).toString() + '%' )


            self.status = False

        except UserWarning as inst:
            QMessageBox.critical( self, qApp.organizationName(), unicode( inst ) )
            logging.error( unicode( inst ) )
            logging.error( query.lastError().text() )
#        except Exception as inst:
#            QMessageBox.critical( self, qApp.organizationName(),
#                                   "Hubo un problema al tratar de crear"\
#                                   + " el nuevo pago" )
#            logging.critical( unicode( inst ) )
#            logging.error( query.lastError().text() )
        finally:
            if QSqlDatabase.database().isOpen():
                QSqlDatabase.database().close()

    @property
    def printIdentifier( self ):
        return self.navmodel.record( self.mapper.currentIndex() ).value( "iddocumento" ).toString()

    def save( self ):
        """
        Slot documentation goes here.
        """
        if self.valid:
            if QMessageBox.question( self, qApp.organizationName(), u"¿Esta seguro que desea guardar el pago?", QMessageBox.Yes | QMessageBox.No ) == QMessageBox.Yes:
                if not QSqlDatabase.database().isOpen():
                    QSqlDatabase.database().open()

                self.editmodel.observaciones = self.txtobservaciones.toPlainText()
                if self.editmodel.save():
                    QMessageBox.information( None,
                        self.trUtf8( qApp.organizationName() ),
                        self.trUtf8( u"""El pago se ha guardado con éxito""" ) )
                    self.editmodel = None
                    self.updateModels()
                    self.navigate( 'last' )
                    self.status = True
                else:
                    QMessageBox.critical( None,
                        self.trUtf8( qApp.organizationName() ),
                        self.trUtf8( """Ha ocurrido un error al guardar el pago""" ) )

                if QSqlDatabase.database().isOpen():
                    QSqlDatabase.database().close()

    @property
    def valid( self ):
        mensaje = "Ocurrio un Error al guardar"
        if self.editmodel.beneficiarioId == 0:
            mensaje = "Por favor elija el beneficiario"
            self.cbbeneficiario.setFocus()
        elif self.editmodel.conceptoId == 0:
            mensaje = "Por favor elija el concepto del pago"
            self.cbconcepto.setFocus()
        elif self.editmodel.totalD == 0 and self.editmodel.totalC == 0:
            mensaje = "Por favor escriba el monto del pago"
            if self.editmodel.maxCordoba > 0 :
                self.sbtotalc.setFocus()
            else:
                self.sbtotald.setFocus()
        else:
            return True

        QMessageBox.information( None, "Guardar Pago", mensaje )
        return False

    @pyqtSlot( int )
    @if_edit_model
    def on_cbbeneficiario_currentIndexChanged( self, index ):
        """
        asignar proveedor al objeto self.editmodel
        """
        self.editmodel.beneficiarioId = self.beneficiariosModel.record( index ).value( "idpersona" ).toInt()[0] if index != -1 else - 1
#            self.tableabonos.setEnabled( index != -1 )
#            self.frbotones.setEnabled( index != -1 )
#            self.abonoeditmodel.removeRows( 0, self.tablefacturas, self.abonoeditmodel.rowCount() )
#            self.abonoeditmodel.idbeneficiario = self.datosRecibo.beneficiarioId
#            self.updateFacturasFilter()
        self.updateLabels()

    @pyqtSlot( int )
    @if_edit_model
    def on_cbconcepto_currentIndexChanged( self, index ):
        """
        asignar la concepto al objeto self.editmodel
        """
        self.editmodel.conceptoId = self.conceptosModel.record( index ).value( "idconcepto" ).toInt()[0]

    @pyqtSlot( int )
    @if_edit_model
    def on_cbtasaret_currentIndexChanged( self, index ):
        """
        asignar la retencion al objeto self.editmodel
        """

        self.editmodel.retencionId = self.retencionModel.record( index ).value( "idcostoagregado" ).toInt()[0]
        value = self.retencionModel.record( index ).value( "tasa" ).toString()
        self.editmodel.retencionTasa = Decimal( value if value != "" else 0 )
        self.updateLabels()

# MANEJO EL EVENTO  DE SELECCION EN EL RADIOBUTTON
    @pyqtSlot( bool )
    @if_edit_model
    def on_ckretener_toggled( self, on ):
        """
        """
        self.editmodel.aplicarRet = on
        self.cbtasaret.setEnabled( on )
        self.cbtasaret.setCurrentIndex( -1 )

    @pyqtSlot( bool )
    @if_edit_model
    def on_ckiva_toggled( self, on ):
        """
        """
        self.editmodel.aplicarIva = on
        self.updateLabels()


    @pyqtSlot( QDateTime )
    def on_dtPicker_dateTimeChanged( self, datetime ):
        pass

    @pyqtSlot( float )
    @if_edit_model
    def on_sbtotalc_valueChanged ( self, value ):
        self.editmodel.totalC = Decimal( str( value ) )
        self.updateLabels()

    @pyqtSlot( float )
    @if_edit_model
    def on_sbtotald_valueChanged ( self, value ):
        self.editmodel.totalD = Decimal( str( value ) )
        self.updateLabels()

    def setControls( self, status ):
        """
        @param status: false = editando        true = navegando
        """
        self.actionPrint.setVisible( status )
        self.dtPicker.setReadOnly( True )
#        self.ckretener.setEnabled( ( not status ) )
        self.txtobservaciones.setReadOnly( status )
        self.actionSave.setVisible( not status )
        self.actionCancel.setVisible( not status )
        self.tabnavigation.setEnabled( status )
        self.actionNew.setVisible( status )
        self.actionGoFirst.setVisible( status )
        self.actionGoPrevious.setVisible( status )
        self.actionGoNext.setVisible( status )
        self.actionGoLast.setVisible( status )
        self.actionPreview.setVisible( status )


        self.ckretener.setEnabled( False )
        self.ckiva.setEnabled( not status )

        self.sbtotalc.setReadOnly( status )
        self.sbtotald.setReadOnly( status )

#        self.txtretencion.setReadOnly(status)

        if status:
            self.editmodel = None
#            self.frbotones.setVisible( False )
            self.tablenavigation.setModel( self.navproxymodel )
#            self.tabledetails.setModel( self.detailsproxymodel )
#            self.tableabonos.setModel( self.abonosproxymodel )

#            self.tabledetails.setColumnHidden( IDPAGO, True )
#            self.tabledetails.setColumnHidden( IDMONEDA, True )
#            self.tabledetails.setColumnHidden( IDDOCUMENTOT, True )
#            
            self.swbeneficiario.setCurrentIndex( 1 )
            self.swconcepto.setCurrentIndex( 1 )
            self.swtasaret.setCurrentIndex( 1 )
#            self.tabledetails.setEditTriggers( QAbstractItemView.NoEditTriggers )
#            self.tableabonos.setEditTriggers( QAbstractItemView.NoEditTriggers )
        else:
            self.tabWidget.setCurrentIndex( 0 )
            self.dtPicker.setDate( self.sesion.fecha )
            self.cbbeneficiario.setCurrentIndex( -1 )
            self.swbeneficiario.setCurrentIndex( 0 )
            self.swconcepto.setCurrentIndex( 0 )
            self.swtasaret.setCurrentIndex( 0 )
            self.txtobservaciones.setPlainText( "" )
            self.sbtotalc.setValue( 0 )
            self.sbtotald.setValue( 0 )
            self.lbltotal.setText( "US$ 0.0000" )
            self.lblretencion.setText( "US$ 0.0000" )
            self.lbltotalpago.setText( "US$ 0.0000" )

            self.cbbeneficiario.setFocus()
            self.ckretener.setChecked( False )
#            self.tabledetails.setEditTriggers( QAbstractItemView.EditKeyPressed | QAbstractItemView.AnyKeyPressed | QAbstractItemView.DoubleClicked )
#            self.tableabonos.setEditTriggers( QAbstractItemView.EditKeyPressed | QAbstractItemView.AnyKeyPressed | QAbstractItemView.DoubleClicked )


#        self.tableabonos.setColumnHidden(IDDOCUMENTO,True)
#        
#        self.tabledetails.setColumnWidth(DESCRIPCION,250)
#        self.tabledetails.setColumnWidth(MONTO,150)
#        self.tabledetails.setColumnWidth(MONTODOLAR,150)
#        self.tabledetails.setColumnWidth(REFERENCIA,150)
#    

    def updateDetailFilter( self, index ):
        record = self.navmodel.record( index )
        self.dtPicker.setDate( 
                      QDate.fromString( 
                               record.value( "Fecha" ).toString(),
                               "dd/MM/yyyy" ) )
        valor = Decimal( record.value( "totalc" ).toString() )
        self.sbtotalc.setMaximum( valor )
        self.sbtotalc.setValue( valor )

        valor = Decimal( record.value( "totald" ).toString() )
        self.sbtotald.setMaximum( valor )
        self.sbtotald.setValue( valor )

        self.tablenavigation.selectRow( self.mapper.currentIndex() )


    def updateLabels( self ):
        """
        """
        self.ckretener.setEnabled( self.editmodel.tieneRetencion )
        retencion = self.editmodel.retencionCordoba
        self.lblretencion.setText( moneyfmt( retencion / self.sesion.tipoCambioBanco, 4, "US$ " ) )
        self.lblretencion.setToolTip( moneyfmt( retencion, 4, "C$ " ) )


        self.lbltotal.setText( moneyfmt( self.editmodel.totalDolar, 4, "US$ " ) )
        self.lbltotal.setToolTip( moneyfmt( self.editmodel.totalCordoba, 4, "C$ " ) )

        total = self.editmodel.totalCordoba - retencion
        self.lbltotalpago.setText( moneyfmt( total / self.sesion.tipoCambioBanco , 4, "US$ " ) )
        self.lbltotalpago.setToolTip( moneyfmt( total, 4, "C$ " ) )


    def updateModels( self ):
        """
        Recargar todos los modelos
        """
        try:

            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( u"No se pudo conectar con la base de datos" )

            query = """
            SELECT
                pago.iddocumento,
                pago.ndocimpreso  as 'No. Comprobante',
               pago.Fecha,
                pago.nombre as Beneficiario,
                pago.Concepto,
                CONCAT('US$',FORMAT(pago.total,4)),
                IF(SUM(IF(ca.idtipocosto=1,1,0))>0,1,0) as coniva,
                IF(SUM(IF(ca.idtipocosto in (8,9),1,0))>0,1,0) as conret,
                SUM(IF(ca.idtipocosto in (8,9),ca.valorcosto,0)) as tasaret,
                SUM(IF(mc.idtipomoneda =1,-mc.monto,0)) as totalc,
                SUM(IF(mc.idtipomoneda =2,-mc.monto,0)) as totald,
                CONCAT('US$',FORMAT(ROUND(pago.total + (pago.total / (1 +SUM(IF(ca.idtipocosto=1,ca.valorcosto/100,0))) ) * SUM(IF(ca.idtipocosto in (8,9),ca.valorcosto/100,0)),4),4)) as total,
                -- pago.total / (1 +SUM(IF(ca.idtipocosto=1,ca.valorcosto/100,0))) as subtotal,
                CONCAT('US$',FORMAT(ROUND((pago.total / (1 +SUM(IF(ca.idtipocosto=1,ca.valorcosto/100,0))) ) * SUM(IF(ca.idtipocosto in (8,9),ca.valorcosto/100,0)),4),4)) as retencion,
                pago.observacion,
                pago.tasa

                FROM costosagregados ca
                JOIN costosxdocumento cxd ON ca.idcostoagregado = cxd.idcostoagregado
                JOIN movimientoscaja mc ON mc.iddocumento = cxd.iddocumento
                JOIN
                (
                SELECT
                d.iddocumento,
                d.ndocimpreso,
                GROUP_CONCAT(IF(pxd.idaccion=2,p.nombre,'') SEPARATOR '') as nombre,
                DATE_FORMAT(d.fechacreacion,'%d/%m/%Y') AS fecha,
                d.observacion,
                con.descripcion as concepto,
                tc.tasa,
                d.total
                FROM documentos d
                JOIN conceptos con ON con.idconcepto = d.idconcepto
                JOIN personasxdocumento pxd ON pxd.iddocumento = d.iddocumento
                JOIN personas p ON p.idpersona = pxd.idpersona
                JOIN tiposcambio tc ON tc.idtc=d.idtipocambio
                WHERE d.idtipodoc=30
                GROUP BY d.iddocumento
                ) pago on pago.iddocumento = cxd.iddocumento
                GROUP BY pago.iddocumento
                ; """ # % ( constantes.IDCORDOBAS, constantes.IDDOLARES, constantes.IVA, constantes.IVA, constantes.RETENCIONFUENTE, constantes.RETENCIONPROFESIONALES, constantes.PROVEEDOR, '%d/%m/%Y', constantes.IDPAGO )

            self.navmodel.setQuery( query )

            self.navproxymodel = QSortFilterProxyModel( self )
            self.navproxymodel.setSourceModel( self.navmodel )
            self.navproxymodel.setFilterKeyColumn( -1 )
            self.navproxymodel.setFilterCaseSensitivity ( Qt.CaseInsensitive )

    #        Este es el modelo con los datos de la tabla para navegar
#FIXME: Se el simbolo de la moneda deberia de salir desde la tabla tiposmoneda    
            self.detailsmodel.setQuery( """
                SELECT
                p.iddocumento,
                CONCAT(tp.descripcion, ' ' , tm.moneda) as 'Tipo de Pago',
                 p.refexterna as 'No. Referencia',
                 b.descripcion as Banco,
                 CONCAT(tm.simbolo,' ',FORMAT(monto,4)) as 'Monto',
                 CONCAT('US$ ',FORMAT(monto / IF(p.idtipomoneda=2,1,IFNULL(tc.tasaBanco,tc.tasa)),4)) as 'Monto US$'
            FROM movimientoscaja p
            JOIN documentos d ON d.iddocumento=p.iddocumento AND d.idtipodoc=18
            JOIN tiposcambio tc ON tc.idtc=d.idtipocambio
            JOIN tiposmoneda tm ON tm.idtipomoneda=p.idtipomoneda
            JOIN tiposmovimientocaja tp ON tp.idtipomovimiento=p.idtipomovimiento
            LEFT JOIN bancos b ON b.idbanco = p.idbanco
            ORDER BY p.nlinea
            ;
            """ )

    #        Este es el filtro del modelo anterior
            self.detailsproxymodel = QSortFilterProxyModel( self )
            self.detailsproxymodel.setSourceModel( self.detailsmodel )
            self.detailsproxymodel.setFilterKeyColumn( IDDOCUMENTO )
            self.detailsproxymodel.setFilterRegExp( '^0$' )
# ESTE ES EL MODELO CON LOS DATOS DE Los ABONOS PARA NAVEGAR
            self.abonosmodel = QSqlQueryModel( self )
            self.abonosmodel.setQuery( """
           SELECT
            d.idhijo as idrecibo,
            padre.ndocimpreso as 'No. Factura',
            CONCAT('US$ ',FORMAT(d.monto,4)) as 'Saldo'
            FROM docpadrehijos d
            JOIN documentos padre ON d.idpadre=padre.iddocumento
            WHERE padre.idtipodoc=%d and d.monto is not null
            ORDER BY d.nlinea
;
            """ % constantes.IDFACTURA )

    #        Este es el filtro del modelo anterior
#            self.abonosproxymodel.setSourceModel( self.abonosmodel )


    #        Este objeto mapea una fila del modelo self.navproxymodel a los controles
            self.mapper.setSubmitPolicy( QDataWidgetMapper.ManualSubmit )
            self.mapper.setModel( self.navproxymodel )
            self.mapper.addMapping( self.lblnpago, NDOCIMPRESO , "text" )
#            self.mapper.addMapping( self.txtretencion, NRETENCION , "text" )

            self.mapper.addMapping( self.txtobservaciones, OBSERVACION )
#            self.mapper.addMapping( self.dtPicker, FECHA )
            self.mapper.addMapping( self.txtbeneficiario, NOMBREBENEFICIARIO, "text" )
            self.mapper.addMapping( self.txtconcepto, CONCEPTO, "text" )
            self.mapper.addMapping( self.txttasaret, TASARETENCION, "text" )
            self.mapper.addMapping( self.lbltotalpago, TOTALPAGADO, "text" )
            self.mapper.addMapping( self.lbltotal, TOTAL, "text" )
            self.mapper.addMapping( self.lblretencion, TOTALRETENCION, "text" )
            self.mapper.addMapping( self.ckretener, CONRETENCION, "checked" )
            self.mapper.addMapping( self.ckiva, CONIVA, "checked" )
#            self.mapper.addMapping( self.sbtotalc, TOTALC, "value" )

            self.tablenavigation.setColumnHidden( IDDOCUMENTO, True )
            self.tablenavigation.setColumnHidden( TOTALRETENCION, True )
            self.tablenavigation.setColumnHidden( CONRETENCION, True )
        except UserWarning as inst:
            logging.error( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(),
                                   unicode( inst ) )
        except Exception as inst:
            logging.critical( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(),
                            u"Hubo un error al tratar de obtener los datos" )
        finally:
            if self.database.isOpen():
                self.database.close()

