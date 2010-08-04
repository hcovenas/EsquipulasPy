# -*- coding: utf-8 -*-
"""
Module implementing frmDevolucion.
"""

from PyQt4.QtCore import pyqtSlot, SIGNAL, QModelIndex, Qt, QTimer, \
    SLOT, QDateTime
from PyQt4.QtGui import QMainWindow, QSortFilterProxyModel, QDataWidgetMapper, \
    QDialog, QTableView, QDialogButtonBox, QVBoxLayout, QAbstractItemView, QFormLayout, \
     QLineEdit
from PyQt4.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
from ui.Ui_devolucion import Ui_frmDevoluciones
from utility.base import Base
from decimal import Decimal
from document.devolucion.devoluciondelegate import DevolucionDelegate
from document.devolucion.devolucionmodel import DevolucionModel
from document.devolucion.lineadevolucion import LineaDevolucion
from utility.moneyfmt import moneyfmt
from utility.reports import frmReportes
from utility import constantes



#navmodel
IDDOCUMENTO, NDOCIMPRESO, FACTURA, CLIENTE, OBSERVACION, FECHA, SUBTOTAL, IMPUESTOS, COSTO, TOTAL, TASA = range( 11 )
#detailsmodel
IDARTICULO, DESCRIPCION, CANTIDAD, PRECIO, TOTALPROD, IDDOCUMENTOT = range( 6 )
class frmDevolucion( QMainWindow, Ui_frmDevoluciones, Base ):
    """
    Formulario para crear nuevas devoluciones
    """
    def __init__( self, user, parent = None ):
        """
        Constructor
        """
        super( frmDevolucion, self ).__init__( parent )
        self.setupUi( self )
        self.parentWindow = parent
        Base.__init__( self )


        self.user = user

        self.editmodel = None

        self.status = True

#        las acciones deberian de estar ocultas
        

#        El modelo principal
        self.navmodel = RONavigationModel( self )
#        El modelo que filtra a self.navmodel
        self.navproxymodel = QSortFilterProxyModel( self )
        self.navproxymodel.setSourceModel( self.navmodel )
#        Este es el modelo con los datos de la tabla para navegar
        self.detailsmodel = QSqlQueryModel( self )
#        Este es el filtro del modelo anterior
        self.detailsproxymodel = QSortFilterProxyModel( self )
        self.detailsproxymodel.setSourceModel( self.detailsmodel )



#        Cargar los modelos en un hilo aparte
        QTimer.singleShot( 0, self.loadModels )



    def addLine( self ):
        """
        Redefiniendo addLine, se supone que en una liquidacion no se pueden añadir lineas
        """
        raise RuntimeError( "Las devoluciones no deben de añadir lineas nuevas" )

    def updateModels( self ):
#        El modelo principal
        self.navmodel = RONavigationModel( self )
#        El modelo que filtra a self.navmodel
        self.navproxymodel = QSortFilterProxyModel( self )
        self.navproxymodel.setSourceModel( self.navmodel )
        self.navproxymodel.setFilterKeyColumn( -1 )
        self.navproxymodel.setFilterCaseSensitivity ( Qt.CaseInsensitive )

#        Este es el modelo con de la tabla con los detalles
        self.detailsmodel = QSqlQueryModel( self )
#        Este es el filtro del modelo anterior
        self.detailsproxymodel = QSortFilterProxyModel( self )
        self.detailsproxymodel.setSourceModel( self.detailsmodel )

#        Este objeto mapea una fila del modelo self.navproxymodel a los controles

        self.mapper.setSubmitPolicy( QDataWidgetMapper.ManualSubmit )
        self.mapper.setModel( self.navproxymodel )
        self.mapper.addMapping( self.txtDocumentNumber, NDOCIMPRESO )
        self.mapper.addMapping( self.txtObservations, OBSERVACION )
        self.mapper.addMapping( self.dtPicker, FECHA )
        self.mapper.addMapping( self.txtClient, CLIENTE, "text" )
        self.mapper.addMapping( self.txtBill, FACTURA, "text" )
        self.mapper.addMapping( self.lblTotal, TOTAL, "text" )
        self.mapper.addMapping( self.lblSubtotal, SUBTOTAL, "text" )
        self.mapper.addMapping( self.lblCost, COSTO, "text" )
        self.mapper.addMapping( self.lblTaxes, IMPUESTOS, "text" )

#        asignar los modelos a sus tablas
        self.tablenavigation.setModel( self.navproxymodel )
        self.tabledetails.setModel( self.detailsproxymodel )

        try:

            if not QSqlDatabase.database().isOpen():
                QSqlDatabase.database().open()

            self.navmodel.setQuery( """
            SELECT
                d.iddocumento,
                d.ndocimpreso as 'Numero de Entrada',
                padre.ndocimpreso as padre,
                p.nombre as cliente,
                d.observacion,
                d.fechacreacion as 'Fecha',
                (@subtotald:=(d.total / ( 1 + ( IF( ca.valorcosto IS NOT NULL , ca.valorcosto / 100, 0 ) )) ) ) as subtotald,
                @subtotald * (IF( ca.valorcosto IS NOT NULL , ca.valorcosto / 100, 0 )  ) as ivad,
                SUM( axd.costounit ) as costod,
                d.total as totald,
                tc.tasa
            FROM documentos d
            JOIN docpadrehijos dpd ON dpd.idhijo = d.iddocumento
            JOIN documentos padre ON dpd.idpadre = padre.iddocumento
            JOIN tiposcambio tc ON d.idtipocambio = tc.idtc
            JOIN personas p ON p.idpersona = d.idpersona
            JOIN articulosxdocumento axd ON axd.iddocumento = d.iddocumento
            LEFT JOIN costosxdocumento cxd ON cxd.iddocumento = padre.iddocumento
            LEFT JOIN costosagregados ca ON ca .idcostoagregado = cxd.idcostoagregado
            WHERE d.idtipoDoc = 10
            GROUP BY d.iddocumento
            """ )

            self.detailsmodel.setQuery( u"""
            SELECT 
                ad.idarticulo, 
                ad.descripcion as 'Descripción', 
                axd.unidades as 'Cantidad', 
                axd.precioventa as 'Precio de venta',
                axd.unidades * axd.precioventa as Total,
                axd.iddocumento
            FROM articulosxdocumento axd
            JOIN vw_articulosdescritos ad ON axd.idarticulo = ad.idarticulo
            JOIN documentos d ON d.iddocumento = axd.iddocumento 
            WHERE d.idtipodoc = 10
            """ )


            self.tablenavigation.setColumnHidden( IDDOCUMENTO, True )
            self.tablenavigation.setColumnHidden( OBSERVACION, True )
            self.tablenavigation.setColumnHidden( SUBTOTAL, True )
            self.tablenavigation.setColumnHidden( IMPUESTOS, True )
            self.tablenavigation.setColumnHidden( TASA, True )
            self.tablenavigation.setColumnHidden( COSTO, True )



        except Exception as inst:
            print inst
        finally:
            if QSqlDatabase.database().isOpen():
                QSqlDatabase.database().close()

    def updateDetailFilter( self, index ):
        self.detailsproxymodel.setFilterRegExp( self.navmodel.record( index ).value( "iddocumento" ).toString() )
        self.detailsproxymodel.setFilterKeyColumn( IDDOCUMENTOT )
        self.tablenavigation.selectRow( self.mapper.currentIndex() )

    def updateLabels( self ):
        self.lblTotal.setText( moneyfmt( self.editmodel.totalD, 4, "US$" ) + " / " + moneyfmt( self.editmodel.totalC, 4, "C$" ) )
        self.lblSubtotal.setText( moneyfmt( self.editmodel.subtotalD, 4, "US$" ) + " / " + moneyfmt( self.editmodel.subtotalC, 4, "C$" ) )
        self.lblTaxes.setText( moneyfmt( self.editmodel.ivaD, 4, "US$" ) + " / " + moneyfmt( self.editmodel.ivaC, 4, "C$" ) )
        self.lblCost.setText( moneyfmt( self.editmodel.totalCostD, 4, "US$" ) + " / " + moneyfmt( self.editmodel.totalCostC, 4, "C$" ) )

    def setControls( self, status ):
        """
        En esta funcion cambio el estado enabled de todos los items en el formulario
        @param status: false = editando        true = navegando
        """
        self.actionSave.setVisible( not status )
        self.actionCancel.setVisible( not status )
        self.tabnavigation.setEnabled( status )
        self.actionNew.setVisible( status )
        self.actionGoFirst.setVisible( status )
        self.actionGoPrevious.setVisible( status )
        self.actionGoNext.setVisible( status )
        self.actionGoLast.setVisible( status )
        self.actionPreview.setVisible( status )

        #self.txtDocumentNumber.setReadOnly( status )
        self.txtObservations.setReadOnly( status )
        self.dtPicker.setReadOnly( status )
        
        self.actionSave.setVisible( not status )
        self.actionCancel.setVisible( not status )
        if status:
            
            self.navigate( 'last' )
            self.tabledetails.setEditTriggers( QAbstractItemView.NoEditTriggers )
        else:
            self.txtDocumentNumber.setText( "" )
            self.txtClient.setText( self.editmodel.clientName )
            self.txtObservations.setPlainText( "" )
            self.lblTotal.setText( "US$0.0000 / C$0.0000" )
            self.lblCost.setText( "US$0.0000 / C$0.0000" )
            self.lblTaxes.setText( "US$0.0000 / C$0.0000" )
            self.lblSubtotal.setText( "US$0.0000 / C$0.0000" )
            self.tabledetails.setEditTriggers( QAbstractItemView.AllEditTriggers )
            self.tabWidget.setCurrentIndex( 0 )

#            mostrar las columnas para el modeo edicion u ocultar para navegación
        self.tabledetails.setColumnHidden( IDARTICULO, status )
        self.tabledetails.setColumnHidden( IDDOCUMENTOT, status )

    @pyqtSlot( "QString" )
    def on_txtDocumentNumber_textEdited( self, string ):
        """
        Slot documentation goes here.
        """
        if not self.editmodel is None:
            self.editmodel.printedDocumentNumber = string



    @pyqtSlot(  )
    def on_txtObservations_textChanged( self ):
        """
        Slot documentation goes here.
        """
        if not self.editmodel is None:
            self.editmodel.observations = self.txtObservations.toPlainText()

    @pyqtSlot(  )
    def on_actionNew_activated( self ):
        """
        Slot documentation goes here.
        """
        query = QSqlQuery( )
        try:
            if not QSqlDatabase.database().open():
                raise Exception( u"No se pudo establecer una conexión con la base de datos" )
            
            dlgbill = dlgSelectBill()
            if dlgbill.exec_() == QDialog.Accepted:
                self.editmodel = DevolucionModel()
                self.editmodel.invoiceId = dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 0 ).data().toInt()[0]
                self.editmodel.clientId = dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 5 ).data().toInt()[0]
                self.editmodel.uid = self.user.uid
                self.editmodel.clientName = dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 3 ).data().toString()
                self.editmodel.billPrinted = dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 1 ).data().toString()
    
                self.editmodel.ivaRate = Decimal( dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 6 ).data().toString() )
                self.editmodel.ivaRateId = dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 7 ).data().toInt()[0]
    
                self.editmodel.exchangeRate = Decimal( dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 8 ).data().toString() )
                self.editmodel.exchangeRateId = dlgbill.filtermodel.index( dlgbill.tblBills.selectionModel().currentIndex().row(), 9 ).data().toInt()[0]
    
    
                self.txtBill.setText( self.editmodel.billPrinted )
                query = QSqlQuery( """
                CALL spConsecutivo(%d,NULL);
                """ % constantes.IDDEVOLUCION )
                if not query.exec_():
                    raise UserWarning( u"No se pudo calcular el numero de la devolución" )
                query.first()
                self.editmodel.printedDocumentNumber = query.value( 0 ).toString()

                self.txtDocumentNumber.setText( self.editmodel.printedDocumentNumber)
                
                query.prepare( """
                SELECT 
                    v.idarticulo, 
                    v.descripcion,
                    facs.costounit,
                    facs.precioventa, 
                    -1*SUM(unidades) as existencia
                FROM articulosxdocumento facs
                JOIN vw_articulosdescritos v ON facs.idarticulo = v.idarticulo
                LEFT JOIN docpadrehijos devs ON devs.idhijo = facs.iddocumento
                WHERE facs.iddocumento = %d OR devs.idpadre = %d
                GROUP BY v.idarticulo
                """ % ( self.editmodel.invoiceId, self.editmodel.invoiceId ) )
                if not query.exec_():
                    raise Exception( "Ocurrio un error en la consulta" )
    
                while query.next():
                    linea = LineaDevolucion( self.editmodel )
                    linea.itemId = query.value( 0 ).toInt()[0]
                    linea.itemDescription = query.value( 1 ).toString()
                    linea.itemCost = Decimal( query.value( 2 ).toString() )
                    linea.itemPrice = Decimal( query.value( 3 ).toString() )
                    linea.maxquantity = query.value( 4 ).toInt()[0]
    
    
                    row = self.editmodel.rowCount()
                    self.editmodel.insertRows( row )
    
                    self.editmodel.lines[row] = linea
    
    
                
                self.tabnavigation.setEnabled( False )
                self.tabWidget.setCurrentIndex( 0 )
                self.tabledetails.setModel( self.editmodel )

                delegate = DevolucionDelegate()
                self.tabledetails.setItemDelegate( delegate )

                self.tabledetails.resizeColumnsToContents()
                self.dtPicker.setDateTime( QDateTime.currentDateTime() )
                self.connect( self.editmodel, SIGNAL( "dataChanged(QModelIndex,QModelIndex)" ), self.updateLabels )
                self.status =  False 
        except UserWarning as inst:
            QMessageBox.critical(self, "Llantera Esquipulas", str(inst))
            self.status = True
        except Exception as inst:
            print inst
            self.status = True
        finally:
            if QSqlDatabase.database().isOpen():
                QSqlDatabase.database().close()




    @pyqtSlot(  )
    def on_actionPreview_activated( self ):
        """
        Funcion usada para mostrar el reporte de una entrada compra
        """

        report = frmReportes( "devoluciones.php?doc=%d" % self.navmodel.record( self.mapper.currentIndex() ).value( "iddocumento" ).toInt()[0] , self.user, self )
        report.show()

    @pyqtSlot(  )
    def on_actionCancel_activated( self ):
        self.editmodel = None

        self.tablenavigation.setModel( self.navproxymodel )
        self.tabledetails.setModel( self.detailsproxymodel )


        self.status = True


class dlgSelectBill( QDialog ):
    def __init__( self, parent = None ):
        super( dlgSelectBill, self ).__init__( parent )
        self.billsmodel = QSqlQueryModel()
        self.billsmodel.setQuery( """
        SELECT 
            d.iddocumento, 
            d.ndocimpreso, 
            d.fechacreacion, 
            p.nombre, -1*SUM(unidades) as unittotal, 
            p.idpersona, 
            valorcosto, 
            ca.idcostoagregado,
            tc.tasa,
            tc.idtc
        FROM documentos d
        JOIN tiposcambio tc ON tc.idtc = d.idtipocambio
        LEFT JOIN docpadrehijos dpd ON d.iddocumento = dpd.idpadre
        LEFT JOIN documentos devs ON dpd.idhijo = devs.iddocumento
        LEFT JOIN costosxdocumento cxd ON cxd.iddocumento = d.iddocumento
        LEFT JOIN costosagregados ca ON cxd.idcostoagregado = ca.idcostoagregado
       JOIN personasxdocumento pxd ON pxd.iddocumento = d.iddocumento
        JOIN personas p ON pxd.idpersona = p.idpersona
        JOIN articulosxdocumento axd ON (axd.iddocumento = d.iddocumento OR axd.iddocumento = devs.iddocumento)
        WHERE d.idtipodoc =%d
        GROUP BY d.iddocumento
        HAVING unittotal > 0   
        """ % (constantes.IDFACTURA) )



        self.setWindowTitle( "Seleccione la factura para la devolucion" )
        self.filtermodel = QSortFilterProxyModel()
        self.filtermodel.setSourceModel( self.billsmodel )
        self.filtermodel.setFilterCaseSensitivity( Qt.CaseInsensitive )
        self.filtermodel.setFilterKeyColumn( -1 )

        iddoc, ndocimpreso, fechacreacion, nombre, total, idpersona, valorcosto, idcosto, tasacambio, idcambio = range( 10 )
        self.tblBills = QTableView()
        self.tblBills.setSelectionMode( QAbstractItemView.SingleSelection )
        self.tblBills.setSelectionBehavior( QAbstractItemView.SelectRows )
        self.tblBills.selectRow( 0 )
        self.tblBills.setModel( self.filtermodel )

        self.tblBills.setColumnHidden( iddoc, True )
        self.tblBills.setColumnHidden( idpersona, True )
        self.tblBills.setColumnHidden( total, True )
        self.tblBills.setColumnHidden( valorcosto, True )
        self.tblBills.setColumnHidden( idcosto, True )
        self.tblBills.setColumnHidden( idcambio, True )
        self.tblBills.setColumnHidden( tasacambio, True )

        self.tblBills.horizontalHeader().setStretchLastSection( True )

        self.tblBills.resizeColumnsToContents()
        buttonbox = QDialogButtonBox( QDialogButtonBox.Ok | QDialogButtonBox.Cancel )

        self.txtSearch = QLineEdit()
        formlayout = QFormLayout()

        formlayout.addRow( "&Buscar", self.txtSearch )

        layout = QVBoxLayout()

        layout.addWidget( self.tblBills )
        layout.addLayout( formlayout )
        layout.addWidget( buttonbox )
        self.setLayout( layout )

        self.setMinimumWidth( 400 )
        self.connect( buttonbox, SIGNAL( "accepted()" ), self, SLOT( "accept()" ) )
        self.connect( buttonbox, SIGNAL( "rejected()" ), self, SLOT( "reject()" ) )
        self.connect( self.txtSearch, SIGNAL( "textChanged(QString)" ), self.updateFilter )

#FIXME: Que pasa cuando no hay facturas?
#    def exec_( self ):
#        if self.billsmodel.rowCount() == 0:
#            QMessageBox.critical( None,
#            self.trUtf8( "Llantera Esquipulas: Inventario" ),
#            self.trUtf8( """No hay facturas a las cuales hacer devoluciones""" ),
#            QMessageBox.StandardButtons( \
#                QMessageBox.Ok ) )
#            self.reject()
#        else:
#            QDialog.exec_( self )




    def updateFilter( self, str ):

        self.filtermodel.setFilterWildcard( str )

class RONavigationModel( QSqlQueryModel ):
    """
    basicamente le da formato a la salida de mapper
    """
    def data( self, index, role = Qt.DisplayRole ):
        """
        Esta funcion redefine data en la clase base, es el metodo que se utiliza para mostrar los datos del modelo
        """
        value = QSqlQueryModel.data( self, index, role )
        exchangeRate = Decimal( QSqlQueryModel.data( self, index.model().index( index.row(), TASA ) ).toString() )
        if value.isValid() and role in ( Qt.DisplayRole, Qt.EditRole ):
            if index.column() in ( TOTAL, SUBTOTAL, COSTO, IMPUESTOS ):
                return moneyfmt( Decimal( value.toString() ), 2, "US$" ) + " / " + moneyfmt( Decimal( value.toString() ) * exchangeRate, 2 , "C$" )
        return value
    def headerData( self, section, orientation, role = Qt.DisplayRole ):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int( Qt.AlignLeft | Qt.AlignVCenter )
            return int( Qt.AlignRight | Qt.AlignVCenter )
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            if  section == TOTAL:
                return "Total"
            elif section == SUBTOTAL:
                return "Subtotal"
            elif section == IMPUESTOS:
                return "Impuestos"
            elif section == COSTO:
                return "Costo"
            elif section == IDDOCUMENTO:
                return "Id"
            elif section == NDOCIMPRESO:
                return "Numero de Devolución"
            elif section == FACTURA:
                return "Numero de Factura"

        return QSqlQueryModel.headerData( self, section , orientation, role )
