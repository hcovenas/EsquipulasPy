# -*- coding: utf-8 -*-
'''
Created on 07/06/2010

@author: Andrés Reyes Monge
'''
#FIXME: EL arqueo no muestra todavia el total de la sesión
from decimal import  Decimal
from PyQt4.QtGui import QMainWindow, QSortFilterProxyModel, QTableView, QMessageBox, QDataWidgetMapper, QPrinter
from PyQt4.QtCore import pyqtSlot, SIGNAL, QDateTime, QTimer, QModelIndex
from PyQt4.QtSql import QSqlQueryModel, QSqlQuery
from ui.Ui_arqueo import Ui_frmArqueo
from utility.base import Base
from utility.moneyfmt import moneyfmt
from utility.singleselectionmodel import  SingleSelectionModel
from document.arqueo.arqueomodel import ArqueoModel
from document.arqueo.arqueodelegate import ArqueoDelegate

from utility import constantes
from utility.reports import frmReportes
#navmodel
IDDOCUMMENTO, NDOCIMPRESO, FECHA, NOMBRE, TOTAL, TOTALSESION = range( 6 )
#detailsmodel
CANTIDAD, DENOMINACION, MONEDA, TOTALP, IDDOCUMMENTOT = range( 5 )
class frmArqueo( QMainWindow, Ui_frmArqueo, Base ):
    '''
    Esta clase implementa el formulario arqueo
    '''
    def __init__( self, user, parent = None ):
        '''
        Constructor
        '''
        super( frmArqueo, self ).__init__( parent )
        self.setupUi( self )
        self.parentWindow = parent
        Base.__init__( self )



        self.editmodel = None
        self.user = user
        self.parent = parent

#        El modelo principal
        self.navmodel = QSqlQueryModel( self )
#        El modelo que filtra a self.navmodel
        self.navproxymodel = QSortFilterProxyModel( self )
        self.navproxymodel.setSourceModel( self.navmodel )
#        Este es el modelo con los datos de la tabla con los detalles
        self.detailsModel = QSqlQueryModel( self )
#        Este es el filtro del modelo anterior
        self.detailsproxymodel = QSortFilterProxyModel( self )
        self.detailsproxymodel.setSourceModel( self.detailsModel )

        self.status = True
        QTimer.singleShot( 0, self.loadModels )

    def updateModels( self ):
        try:
            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( "No se pudo abrir la base de datos" )
            self.navmodel.setQuery( """
            SELECT
                d.iddocumento, 
                d.ndocimpreso AS 'Numero de Arqueo', 
                d.fechacreacion AS 'Fecha', 
                p.nombre AS 'Arqueador', 
                CONCAT('US$',FORMAT(d.total,4))  as 'Total US$'
            FROM documentos d  
            JOIN tiposcambio tc ON tc.idtc = d.idtipocambio
            JOIN personasxdocumento pxd ON pxd.iddocumento = d.iddocumento
            JOIN personas p ON p.idpersona = pxd.idpersona AND p.tipopersona = %d
            WHERE d.idtipodoc = %d
            """ % ( constantes.USUARIO, constantes.IDARQUEO))
            
            #FIXME: El simbolo de la moneda deberia de venir de la tabla tiposmoneda
            self.detailsModel.setQuery( u"""
            SELECT 
                l.cantidad AS 'Cantidad',
                CONCAT_WS(' ', tm.simbolo, de.valor) as 'Denominación',
                tm.moneda as 'Moneda',
                CONCAT("US$", FORMAT(l.cantidad * IF(de.idtipomoneda = 1, de.valor * tc.tasa, de.valor), 4)) as 'Total US$',
                l.iddocumento
            FROM lineasarqueo l
            JOIN denominaciones de ON de.iddenominacion = l.iddenominacion
            JOIN tiposmoneda tm ON de.idtipomoneda = tm.idtipomoneda
            JOIN documentos d ON d.iddocumento = l.iddocumento
            JOIN tiposcambio tc ON d.idtipocambio = tc.idtc
            """ )

            self.mapper.setSubmitPolicy( QDataWidgetMapper.ManualSubmit )
            self.mapper.setModel( self.navproxymodel )
            self.mapper.addMapping( self.lblPrintedDocumentNumber, NDOCIMPRESO, "text" )
            self.mapper.addMapping( self.dtPicker, FECHA )
            self.mapper.addMapping( self.lblUserName, NOMBRE, "text" )
            self.mapper.addMapping( self.lblTotalArqueo, TOTAL, "text" )

            
        except UserWarning as inst:
            QMessageBox.critical(self, "Llantera Esquipulas", unicode(inst))
        except Exception as inst:
            print inst
        finally:
            if self.database.isOpen():
                self.database.close()

    def updateDetailFilter( self, index ):
        self.detailsproxymodel.setFilterKeyColumn( IDDOCUMMENTOT )
        self.detailsproxymodel.setFilterRegExp( self.navmodel.record( index ).value( "iddocumento" ).toString() )
        self.tablenavigation.selectRow( self.mapper.currentIndex() )

    def setControls( self, status ):
        """
        @param status: false = editando true = navegando 
        """
        self.tablenavigation.setEnabled( status )
        self.tabnavigation.setEnabled( status )

        self.actionNew.setVisible( status )
        self.actionPreview.setVisible( status )

        self.actionCancel.setVisible( not status )
        self.actionSave.setVisible( not status )
        if not self.status:
            self.tabledetails.setEditTriggers( QTableView.AllEditTriggers )
            self.tabledetails.addAction( self.actionDeleteRow )
            self.tabWidget.setCurrentIndex( 0 )
            self.tabledetails.setColumnHidden( IDDOCUMMENTOT, False )
            self.tablenavigation.setColumnHidden( IDDOCUMMENTO, False )
            self.lblTotalArqueo.setText( "US$0.0000" )
        else:
            self.tabledetails.removeAction( self.actionDeleteRow )
            self.tabledetails.setModel( self.detailsproxymodel )
            self.tablenavigation.setModel( self.navproxymodel )
            self.tablenavigation.setColumnHidden( IDDOCUMMENTO, True )
            self.tabledetails.setColumnHidden( IDDOCUMMENTOT, True )

    def updateLabels( self ):
        self.lblTotalArqueo.setText( moneyfmt( self.editmodel.total, 4, "US$" ) )

    @pyqtSlot( )
    def on_actionNew_activated( self ):
        """
        cargar todos los modelos para la edición
        """
        try:
            self.editmodel = ArqueoModel()
            self.editmodel.uid = self.user.uid
            self.tabledetails.setModel( self.editmodel )

            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( "No se pudo conectar con la base de datos" )


            #Obtener los datos de la sesión
            query = QSqlQuery( """
            SELECT 
                IF(SUM(d.total) IS NOT NULL, SUM(d.total), 0) + p.total as 'totalsesion' 
            FROM documentos p
            LEFT JOIN docpadrehijos dpd ON dpd.idpadre = p.iddocumento
            LEFT JOIN documentos d ON dpd.idhijo = d.iddocumento
            JOIN tiposcambio tc ON tc.idtc = p.idtipocambio
            WHERE d.escontado = 1 AND p.iddocumento = %d
            """ % self.parent.datosSesion.sesionId )


            if not query.exec_() or not query.size() > 0:
                raise UserWarning( u"Error al obtener el total de la sesión")
            query.first()
            self.editmodel.expectedTotal = Decimal( query.value( 0 ).toString() )

            self.editmodel.exchangeRateId = self.parent.datosSesion.tipoCambioId
            self.editmodel.exchangeRate = self.parent.datosSesion.tipoCambioOficial
            
            self.editmodel.datetime = self.parent.datosSesion.fecha
            
            query = QSqlQuery( """
            CALL spConsecutivo(%d,NULL);
            """ % constantes.IDARQUEO )
            if not query.exec_():
                raise UserWarning( "No se pudo calcular el numero del arqueo" )
            query.first()
            self.editmodel.printedDocumentNumber = query.value( 0 ).toString()

            self.lblTotalSesion.setText( moneyfmt( self.editmodel.expectedTotal, 4, "US$" ) )
            self.lblPrintedDocumentNumber.setText( self.editmodel.printedDocumentNumber )

            query = QSqlQuery( """
            SELECT 
                d.iddenominacion, 
                CONCAT_WS( ' ',d.valor, m.moneda), 
                d.valor, 
                d.idtipomoneda
            FROM denominaciones d
            JOIN tiposmoneda m ON d.idtipomoneda = m.idtipomoneda
            WHERE d.activo = 1
            ORDER BY d.idtipomoneda
            """ )
            if not query.exec_():
                raise UserWarning( "No se pudo recuperar la lista de denominaciones" )
            denominationsmodel = SingleSelectionModel()
            while query.next():
                denominationsmodel.items.append( [
                                                  query.value( 0 ).toInt()[0], #el id del tipo de denominacion
                                                  query.value( 1 ).toString(), #La descripción de la denominación
                                                  Decimal( query.value( 2 ).toString() ), # el valor de la denominación
                                                  query.value( 3 ).toInt()[0] #El id del tipo de moneda
                                                  ] )

            delegate = ArqueoDelegate(denominationsmodel)
            self.tabledetails.setItemDelegate( delegate )

            self.addLine()
            self.dtPicker.setDateTime( QDateTime.currentDateTime() )

            self.lblUserName.setText( self.user.fullname )
            self.editmodel.dataChanged[QModelIndex,QModelIndex].connect(self.updateLabels)
            self.status = False
            
        except UserWarning as inst:
            QMessageBox.critical(self, "Llantera Esquipulas", unicode(inst))
            self.status = True
        except Exception  as e:
            print e
            QMessageBox.critical(self, "Llantera Esquipulas", "El sistema no pudo iniciar un nuevo arqueo")
            self.status = True
        finally:
            if self.database.isOpen():
                self.database.close()

    @pyqtSlot( "QDateTime" )
    def on_dtPicker_dateTimeChanged( self, datetime ):
        if not self.editmodel is None:
            self.editmodel.datetime = datetime

    @pyqtSlot(  )
    def on_actionCancel_activated( self ):
        self.editmodel = None
        self.tablenavigation.setModel( self.navproxymodel )
        self.tabledetails.setModel( self.detailsproxymodel )
        self.status = True
        self.navigate( 'last' )

    @pyqtSlot(  )
    def on_actionSave_activated( self ):
        """
        Redefiniendo el metodo save de Base para mostrar advertencias si el arqueo no concuerda
        """
        if self.editmodel.total == self.editmodel.expectedTotal or QMessageBox.question( self, "Llantera Esquipulas: Caja", u"El total de la sesión no coincide con el total del arqueo\n ¿Desea continuar?", QMessageBox.Yes | QMessageBox.No ) == QMessageBox.Yes:
            super(frmArqueo, self).on_actionSave_activated()

    @pyqtSlot(  )
    def on_actionPreview_activated( self ):
        """
        Funcion usada para mostrar el reporte de una entrada compra
        """
        printer = QPrinter()
        printer.setPageSize(QPrinter.Letter)
        web = "arqueos.php?doc=%d" % self.navmodel.record( self.mapper.currentIndex() ).value( "iddocumento" ).toInt()[0] 
        report = frmReportes( web , self.parentWindow.user, printer, self )
        report.exec_()

