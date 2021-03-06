#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#       Copyright 2010 Andrés Reyes Monge <armonge@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
'''
Created on 07/06/2010

@author: Andrés Reyes Monge
'''
from decimal import  Decimal
import logging

from PyQt4.QtGui import  QSortFilterProxyModel, QTableView, \
QMessageBox, QDataWidgetMapper, QMdiArea, \
qApp, QDialog
from PyQt4.QtCore import pyqtSlot, QTime, QTimer, QModelIndex, Qt, QDateTime
from PyQt4.QtSql import QSqlQueryModel, QSqlQuery

from utility import constantes
from ui.Ui_arqueo import Ui_frmArqueo
from utility.base import Base
from utility.moneyfmt import moneyfmt
from utility.singleselectionmodel import  SingleSelectionModel
from utility.user import dlgSmallUserLogin

from document.arqueo import ArqueoModel, ArqueoProxyModel, ArqueoDelegate
from utility.decorators import if_edit_model


#navmodel
IDDOCUMMENTO, FECHA, NOMBRE, EFECTIVOC, EFECTIVOD, CHEQUEC, CHEQUED, \
DEPOSITOC, DEPOSITOD, TRANSFERENCIAC, TRANSFERENCIAD, \
TARJETAC, TARJETAD = range( 13 )
#detailsmodel
CANTIDAD, DENOMINACION, TOTAL, MONEDA, IDDOCUMMENTOT, \
IDDENOMINACION = range( 6 )
class FrmArqueo( Ui_frmArqueo, Base ):
    '''
    Esta clase implementa el formulario arqueo
    '''
    web = "arqueos.php?doc="
    def __init__( self, datos_sesion, parent, edit = False ):
        u'''
        @param datos_sesion: La información de la sesion de caja
        '''
        super( FrmArqueo, self ).__init__( parent, True )
        self.sesion = datos_sesion
        self.setWindowModality( Qt.WindowModal )
        self.setWindowFlags( Qt.Dialog )
#        self.status = False 

        self.__dolar_proxy = ArqueoProxyModel()
        self.__cordoba_proxy = ArqueoProxyModel()
                    
        
        self.editmodel = None

#        El modelo principal
        self.navmodel = QSqlQueryModel( self )
    #        El modelo que filtra a self.navmodel
        self.navproxymodel = QSortFilterProxyModel( self )
        self.__details_proxymodel_d = QSortFilterProxyModel( self )
        self.__details_proxymodel_c = QSortFilterProxyModel( self )
        
        
        self.navproxymodel.setSourceModel( self.navmodel )
#        Este es el modelo con los datos de la tabla con los detalles
        self.detailsModel = QSqlQueryModel( self )
#        Este es el filtro del modelo anterior
        self.detailsproxymodel = QSortFilterProxyModel( self )
        self.detailsproxymodel.setSourceModel( self.detailsModel )

        #filtrar en dolares y en cordobas
        
        self.__details_proxymodel_d.setSourceModel( self.detailsproxymodel )
        self.__details_proxymodel_d.setFilterKeyColumn( MONEDA )
        self.__details_proxymodel_d.setFilterRegExp( "^%d$" % constantes.IDDOLARES )

    
        self.__details_proxymodel_c.setSourceModel( self.detailsproxymodel )
        self.__details_proxymodel_c.setFilterKeyColumn( MONEDA )
        self.__details_proxymodel_c.setFilterRegExp( "^%d$" % constantes.IDCORDOBAS )
           
        
        
        if edit:
            self.status = False
            self.newDocument()
            self.actionCancel.setVisible(False)
            self.tabWidget.setTabEnabled(1,False)
        else:
            self.status = True
            QTimer.singleShot( 0, self.loadModels )

    def updateModels( self ):
        try:
            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( "No se pudo abrir la base de datos" )

            #TODO: Esta consulta tiene que mejorar para definir realmente quien es el que realiza el arqueo
            query = u"""
            SELECT
                d.iddocumento,
                d.fechacreacion ,
                p.nombre AS 'Arqueador',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOEFECTIVO ) + """ AND mc.idtipomoneda = """ + str( constantes.IDCORDOBAS ) + """, mc.monto, 0)),4) AS 'efectivoc',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOEFECTIVO ) + """ AND mc.idtipomoneda = """ + str( constantes.IDDOLARES ) + """, mc.monto, 0)),4) AS 'efectivod',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOCHEQUE ) + """ AND mc.idtipomoneda = """ + str( constantes.IDCORDOBAS ) + """, mc.monto, 0)),4) AS 'chequec',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOCHEQUE ) + """ AND mc.idtipomoneda = """ + str( constantes.IDDOLARES ) + """, mc.monto, 0)),4) AS 'chequed',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGODEPOSITO ) + """ AND mc.idtipomoneda = """ + str( constantes.IDCORDOBAS ) + """, mc.monto, 0)),4) AS 'depositoc',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGODEPOSITO ) + """ AND mc.idtipomoneda = """ + str( constantes.IDDOLARES ) + """, mc.monto, 0)),4) AS 'depositod',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOTRANSFERENCIA ) + """ AND mc.idtipomoneda = """ + str( constantes.IDCORDOBAS ) + """, mc.monto, 0)),4) AS 'transferenciac',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOTRANSFERENCIA ) + """ AND mc.idtipomoneda = """ + str( constantes.IDDOLARES ) + """, mc.monto, 0)),4) AS 'transferenciad',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOTARJETA ) + """ AND mc.idtipomoneda = """ + str( constantes.IDCORDOBAS ) + """, mc.monto, 0)),4) AS 'tarjetac',
                FORMAT(SUM(IF(mc.idtipomovimiento = """ + str( constantes.IDPAGOTARJETA ) + """ AND mc.idtipomoneda = """ + str( constantes.IDDOLARES ) + """, mc.monto, 0)),4) AS 'tarjetad'
            FROM documentos d
            JOIN movimientoscaja mc ON mc.iddocumento = d.iddocumento
            JOIN tiposmoneda tm ON mc.idtipomoneda = tm.idtipomoneda
            JOIN personasxdocumento pxd ON pxd.iddocumento = d.iddocumento
            JOIN personas p ON p.idpersona = pxd.idpersona
            WHERE d.idtipodoc =  %d
            GROUP BY d.iddocumento
            """ % ( constantes.IDARQUEO )
            self.navmodel.setQuery( query )

            self.detailsModel.setQuery( u"""
            SELECT
                l.cantidad AS 'Cantidad',
                CONCAT_WS(' ',tm.simbolo, CAST(de.valor AS CHAR)) as 'Denominación',
                FORMAT(l.cantidad * de.valor, 4) as 'Total',
                de.idtipomoneda,
                l.iddocumento
            FROM lineasarqueo l
            JOIN denominaciones de ON de.iddenominacion = l.iddenominacion
            JOIN tiposmoneda tm ON de.idtipomoneda = tm.idtipomoneda
            JOIN documentos d ON d.iddocumento = l.iddocumento
            JOIN tiposcambio tc ON d.idtipocambio = tc.idtc
            """ )

            self.mapper.setSubmitPolicy( QDataWidgetMapper.ManualSubmit )
            self.mapper.setModel( self.navproxymodel )
            self.mapper.addMapping( self.dtPicker, FECHA )
            self.mapper.addMapping( self.lblUserName, NOMBRE, "value" )
            self.mapper.addMapping( self.sbCkC, CHEQUEC, "value" )
            self.mapper.addMapping( self.sbCkD, CHEQUED, "value" )
            self.mapper.addMapping( self.sbCardC, TARJETAC, "value" )
            self.mapper.addMapping( self.sbCardD, TARJETAD, "value" )
            self.mapper.addMapping( self.sbDepositC, DEPOSITOC, "value" )
            self.mapper.addMapping( self.sbDepositD, DEPOSITOD, "value" )
            self.mapper.addMapping( self.sbTransferC  , TRANSFERENCIAC, "value" )
            self.mapper.addMapping( self.sbTransferD  , TRANSFERENCIAD, "value" )



        except UserWarning as inst:
            logging.error( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(), unicode( inst ) )
        except Exception as inst:
            logging.critical( unicode( inst ) )
        finally:
            if self.database.isOpen():
                self.database.close()

    def updateDetailFilter( self, index ):
        self.detailsproxymodel.setFilterKeyColumn( IDDOCUMMENTOT )
        self.detailsproxymodel.setFilterRegExp( self.navmodel.record( index ).value( IDDOCUMMENTO ).toString() )
        self.tablenavigation.selectRow( self.mapper.currentIndex() )

    def setControls( self, status ):
        """
        @param status: false = editando true = navegando 
        """
        self.actionPrint.setVisible( status )
        self.tablenavigation.setEnabled( status )
        self.tabnavigation.setEnabled( status )

        self.actionNew.setVisible( status )
        self.actionPreview.setVisible( status )

        self.actionCancel.setVisible( not status )
        self.actionSave.setVisible( not status )
        self.actionGoFirst.setVisible(  status )
        self.actionGoLast.setVisible(  status )
        self.actionGoNext.setVisible(  status )
        self.actionGoPrevious.setVisible(  status )

        self.sbCkD.setReadOnly( status )
        self.sbCkC.setReadOnly( status )
        self.sbCardD.setReadOnly( status )
        self.sbCardC.setReadOnly( status )
        self.sbDepositD.setReadOnly( status )
        self.sbDepositC.setReadOnly( status )
        self.sbTransferD.setReadOnly( status )
        self.sbTransferC.setReadOnly( status )

        self.txtObservations.setReadOnly( status )

        self.tablenavigation.setColumnHidden( IDDOCUMMENTO, True )


        if not self.status:
            self.tabledetailsC.setEditTriggers( QTableView.AllEditTriggers )
            self.tabledetailsC.setColumnHidden( IDDOCUMMENTOT, False )
            self.tabledetailsD.setEditTriggers( QTableView.AllEditTriggers )
            self.tabledetailsD.setColumnHidden( IDDOCUMMENTOT, False )
            self.tabWidget.setCurrentIndex( 0 )

            self.tabledetailsC.setColumnHidden( IDDOCUMMENTOT, True )
            self.tabledetailsC.setColumnHidden( IDDENOMINACION, True )

            self.tabledetailsD.setColumnHidden( IDDOCUMMENTOT, True )
            self.tabledetailsD.setColumnHidden( IDDENOMINACION, True )


#            doublevalidator = QDoubleValidator(0, 99999999, 4, self)

        else:
            self.tabledetailsC.setModel( self.__details_proxymodel_c )
            self.tabledetailsD.setModel( self.__details_proxymodel_d )


            self.tablenavigation.setModel( self.navproxymodel )
            self.tablenavigation.setColumnHidden( IDDOCUMMENTO, True )



            self.tabledetailsC.setColumnHidden( IDDOCUMMENTOT, True )
            self.tabledetailsC.setColumnHidden( IDDENOMINACION, True )

            self.tabledetailsD.setColumnHidden( IDDOCUMMENTOT, True )
            self.tabledetailsD.setColumnHidden( IDDENOMINACION, True )




        self.tabledetailsC.setColumnHidden( MONEDA, True )
        self.tabledetailsD.setColumnHidden( MONEDA, True )

    def updateLabels( self ):
        self.lblCashC.setText( "%s / %s" % ( 
                        moneyfmt( self.editmodel.totalCashC, 4, "C$" ),
                        moneyfmt( self.editmodel.expectedCashC, 4, "C$" ) )
        )
        self.lblCashD.setText( "%s / %s" % ( 
                        moneyfmt( self.editmodel.totalCashD, 4, "US$" ),
                        moneyfmt( self.editmodel.expectedCashD, 4, "US$" ) )
        )

        self.lblCkC.setText( moneyfmt( self.editmodel.expectedCkC, 4, "C$" ) )
        self.lblCkD.setText( moneyfmt( self.editmodel.expectedCkD, 4, "US$" ) )

        self.lblCardC.setText( 
                        moneyfmt( self.editmodel.expectedCardC, 4, "C$" ) )
        self.lblCardD.setText( 
                        moneyfmt( self.editmodel.expectedCardD, 4, "US$" ) )

        self.lblDepositC.setText( 
                         moneyfmt( self.editmodel.expectedDepositC, 4, "C$" ) )
        self.lblDepositD.setText( 
                         moneyfmt( self.editmodel.expectedDepositD, 4, "US$" ) )

        self.lblTransferC.setText( 
                          moneyfmt( self.editmodel.expectedDepositC, 4, "C$" ) )
        self.lblTransferD.setText( 
                          moneyfmt( self.editmodel.expectedDepositD, 4, "US$" ) )

    def newDocument( self ):
        """
        cargar todos los modelos para la edición
        """
        query = QSqlQuery()
        try:
            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( u"No se pudo establecer la conexión con la base de datos" )
            for window in self.parentWindow.findChild( QMdiArea ).subWindowList():
                if window.widget():
                    raise UserWarning( u"Por favor cierre las otras pestañas"
                                       + u" de la aplicación antes de continuar"
                                       + " con el arqueo" )


            self.editmodel = ArqueoModel( self.sesion )

            self.editmodel.datetime.setDate( self.sesion.fecha )
            self.editmodel.datetime.setTime( QTime.currentTime() )


            self.__dolar_proxy.setSourceModel( self.editmodel )
            self.__dolar_proxy.setFilterKeyColumn( MONEDA )
            self.__dolar_proxy.setFilterRegExp( r"^%d$" % constantes.IDDOLARES )
            self.__dolar_proxy.setDynamicSortFilter( True )


            self.__cordoba_proxy.setSourceModel( self.editmodel )
            self.__cordoba_proxy.setFilterKeyColumn( MONEDA )
            self.__cordoba_proxy.setFilterRegExp( r"^%d$" % constantes.IDCORDOBAS )
            self.__cordoba_proxy.setDynamicSortFilter( True )

            self.tabledetailsC.setModel( self.__cordoba_proxy )
            self.tabledetailsD.setModel( self.__dolar_proxy )

            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( "No se pudo conectar con la base de datos" )

            #verificar si hay documentos pendientes de aprobación
            q = """
            SELECT
                CONCAT_WS(' ', td.descripcion, d.ndocimpreso)
            FROM documentos sesion
            JOIN docpadrehijos dpd ON dpd.idpadre = sesion.iddocumento
            JOIN documentos d ON dpd.idhijo  = d.iddocumento
            JOIN tiposdoc td ON td.idtipodoc = d.idtipodoc
            WHERE d.idestado NOT IN ( %d,%d)
            """ % ( constantes.CONFIRMADO,
                    constantes.ANULADO )
            if not query.exec_( q ):
                raise Exception( u"No se pudo ejecutar la consulta para "\
                                 + "determinar si existen documentos "
                                 + "pendientes de aprobación" )
            if not query.size() == 0:
                raise UserWarning( u"Existen documentos pendientes de "\
                                   + "aprobación en la sesión" )


            #Obtener los datos de la sesión
            q = """
            CALL spConsecutivo( %d, NULL )
            """ % constantes.IDARQUEO
            #query.prepare( q )

            if not query.exec_( q ):
                raise Exception( u"No se pudo ejecutar la consulta para "\
                                 + "obtener el numero del arqueo" )
            if not query.size() > 0:
                raise Exception( u"La consulta para obtener el numero del "\
                                 + "arqueo no devolvio ningún valor" )
            query.first()

            self.editmodel.printedDocumentNumber = query.value( 0 ).toString()
            self.editmodel.exchangeRateId = self.sesion.tipoCambioId
            self.editmodel.exchangeRate = self.sesion.tipoCambioOficial

            self.editmodel.datetime.setDate( self.sesion.fecha )

            q = """
            CALL spTotalesSesion(%d);
            """ % self.sesion.sesionId

            if not query.exec_( q ):
                raise UserWarning( u"No se pudieron calcular los totales"\
                                   + " de la sesión" )
            while query.next():
                if query.value( 0 ).toInt()[0] == constantes.IDPAGOEFECTIVO and query.value( 2 ).toInt()[0] == constantes.IDDOLARES:
                    self.editmodel.expectedCashD = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOEFECTIVO and query.value( 2 ).toInt()[0] == constantes.IDCORDOBAS:
                    self.editmodel.expectedCashC = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOCHEQUE and query.value( 2 ).toInt()[0] == constantes.IDDOLARES:
                    self.editmodel.expectedCkD = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOCHEQUE and query.value( 2 ).toInt()[0] == constantes.IDCORDOBAS:
                    self.editmodel.expectedCkC = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGODEPOSITO and query.value( 2 ).toInt()[0] == constantes.IDDOLARES:
                    self.editmodel.expectedDepositD = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGODEPOSITO  and query.value( 2 ).toInt()[0] == constantes.IDCORDOBAS:
                    self.editmodel.expectedDepositC = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOTRANSFERENCIA  and query.value( 2 ).toInt()[0] == constantes.IDDOLARES:
                    self.editmodel.expectedTransferD = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOTRANSFERENCIA  and query.value( 2 ).toInt()[0] == constantes.IDCORDOBAS:
                    self.editmodel.expectedTransferC = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOTARJETA  and query.value( 2 ).toInt()[0] == constantes.IDDOLARES:
                    self.editmodel.expectedCardD = Decimal( query.value( 5 ).toString() )
                elif query.value( 0 ).toInt()[0] == constantes.IDPAGOTARJETA  and query.value( 2 ).toInt()[0] == constantes.IDCORDOBAS:
                    self.editmodel.expectedCardC = Decimal( query.value( 5 ).toString() )

            q = """
            SELECT
                d.iddenominacion,
                CONCAT_WS( ' ',d.valor, m.moneda),
                d.valor,
                d.idtipomoneda,
                m.simbolo
            FROM denominaciones d
            JOIN tiposmoneda m ON d.idtipomoneda = m.idtipomoneda
            WHERE d.activo = 1
            ORDER BY d.idtipomoneda, d.valor
            """
            if not query.exec_( q ):
                raise UserWarning( "No se pudo recuperar la lista de "
                                   + "denominaciones" )
            denominationsmodelC = SingleSelectionModel()
            denominationsmodelC.headers = ["Id",
                                            u"Denominación",
                                            "Valor",
                                            "Id Moneda",
                                            "Simbolo"]
            denominationsmodelD = SingleSelectionModel()
            denominationsmodelD.headers = denominationsmodelC.headers


            while query.next():
                if query.value( 3 ).toInt()[0] == constantes.IDDOLARES:
                    denominationsmodelD.items.append( [
                                                  query.value( 0 ).toInt()[0], #el id del tipo de denominacion
                                                  query.value( 1 ).toString(), #La descripción de la denominación
                                                  query.value( 2 ).toString(), # el valor de la denominación
                                                  query.value( 3 ).toInt()[0], #El id del tipo de moneda
                                                  query.value( 4 ).toString() #El simbolo de la moneda
                                                  ] )
                else:
                    denominationsmodelC.items.append( [
                                                  query.value( 0 ).toInt()[0], #el id del tipo de denominacion
                                                  query.value( 1 ).toString(), #La descripción de la denominación
                                                  query.value( 2 ).toString() , # el valor de la denominación
                                                  query.value( 3 ).toInt()[0], #El id del tipo de moneda
                                                  query.value( 4 ).toString() #El simbolo de la moneda
                                                  ] )

            delegateC = ArqueoDelegate( denominationsmodelC )
            self.tabledetailsC.setItemDelegate( delegateC )

            delegateD = ArqueoDelegate( denominationsmodelD )
            self.tabledetailsD.setItemDelegate( delegateD )

            self.addLine()
            self.addLine()
            self.editmodel.setData( self.editmodel.index( 0, MONEDA ), constantes.IDDOLARES )
            self.editmodel.setData( self.editmodel.index( 1, MONEDA ), constantes.IDCORDOBAS )

            self.dtPicker.setDateTime( self.editmodel.datetime )

            self.lblUserName.setText( self.user.fullname )
            self.editmodel.dataChanged[QModelIndex, QModelIndex].connect( self.updateLabels )

            self.tabledetailsC.setColumnWidth( DENOMINACION, 200 )
            self.tabledetailsD.setColumnWidth( DENOMINACION, 200 )
            self.updateLabels()
            self.status = False

        except UserWarning as inst:
            logging.error( unicode( inst ) )
            logging.error( query.lastError().text() )
            QMessageBox.critical( self,
                                  qApp.organizationName(),
                                  unicode( inst ) )
            self.status = True
        except Exception  as inst:
            logging.critical( unicode( inst ) )
            logging.critical( query.lastError().text() )
            QMessageBox.critical( self,
                                  qApp.organizationName(),
                               "El sistema no pudo iniciar un nuevo arqueo" )
            self.status = True
        finally:
            if self.database.isOpen():
                self.database.close()

    @pyqtSlot( QDateTime )
    def on_dtPicker_dateTimeChanged( self, datetime ):
        pass

    def cancel( self ):
        self.editmodel = None

        self.status = True
        self.navigate( 'last' )

    def save( self ):
        """
        Redefiniendo el metodo save de Base para mostrar 
        advertencias si el arqueo no concuerda
        """
        try:
            errors = []

            if not self.editmodel.totalCashC == self.editmodel.expectedCashC:
                errors.append( u"El total de efectivo en cordobas del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalCashD == self.editmodel.expectedCashD:
                errors.append( u"El total de efectivo en dolares del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalCkD == self.editmodel.expectedCkD:
                errors.append( u"El total de cheques en dolares del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalCkC == self.editmodel.expectedCkC:
                errors.append( u"El total de cheques en cordobas del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalTransferD == self.editmodel.expectedTransferD:
                errors.append( u"El total de transferencias en dolares del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalTransferC == self.editmodel.expectedTransferC:
                errors.append( u"El total de transferencias en cordobas del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalDepositD == self.editmodel.expectedDepositD:
                errors.append( u"El total de depositos en dolares del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalDepositC == self.editmodel.expectedDepositC:
                errors.append( u"El total de depositos en cordobas del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalCardD == self.editmodel.expectedDepositD:
                errors.append( u"El total de pagos en tarjetas en dolares del arqueo no coincide con el de la sesión" )
            if not self.editmodel.totalCardD == self.editmodel.expectedDepositC:
                errors.append( u"El total de pagos en tarjetas en cordobas del arqueo no coincide con el de la sesión" )

            if len( errors ) > 0:
                raise UserWarning( "\n".join( errors ) )
            dlgUser = dlgSmallUserLogin()
            if dlgUser.exec_() == QDialog.Accepted:
                if dlgUser.user.valid and dlgUser.user.hasRole( 'gerencia' ):
                    self.editmodel.authorizationId = dlgUser.user.uid
                    super( FrmArqueo, self ).save( False )
                    self.parentWindow.init()
                    self.close()
                else:
                    QMessageBox.warning( self, qApp.organizationName(), "No se pudo autorizar el arqueo" )
        except UserWarning as inst:
            if not self.editmodel.observations == "":
                if QMessageBox.question( self, qApp.organizationName(), unicode( inst ) + u"\n¿Desea Continuar?", QMessageBox.Yes | QMessageBox.No ) == QMessageBox.Yes:
                    dlgUser = dlgSmallUserLogin()
                    if dlgUser.exec_() == QDialog.Accepted:
                        if dlgUser.user.valid and dlgUser.user.hasRole( 'gerencia' ):
                            self.editmodel.authorizationId = dlgUser.user.uid
                            super( FrmArqueo, self ).save( False )
                            self.parentWindow.init()
                            self.close()
                        else:
                            QMessageBox.warning( self,
                                                 qApp.organizationName(),
                                                 "No se pudo autorizar "
                                                 + "el arqueo" )
            else:
                QMessageBox.warning( self,
                                     qApp.organizationName(),
                                     unicode( inst )\
                                     + u"\n Por favor especifique el motivo"
                                     + " de la diferencia" )

    @property
    def printIdentifier( self ):
        return self.navmodel.record( self.mapper.currentIndex() ).value( "iddocumento" ).toString()

    def navigate( self, to ):
        """
        Esta funcion se encarga de navegar entro los distintos documentos
        @param to: es una string que puede tomar los valores 'next' 'previous' 'first' 'last'
        """
        if self.mapper.currentIndex != -1:
            row = self.mapper.currentIndex()
            if to == "next":
                row += 1
                if row >= self.navproxymodel.rowCount():
                    row = self.navproxymodel.rowCount() - 1
                self.mapper.setCurrentIndex( row )
            elif to == "previous":
                if row <= 1: row = 0
                else: row = row - 1
                self.mapper.setCurrentIndex( row )
            elif to == "first":
                self.mapper.toFirst()
            elif to == "last":
                self.mapper.toLast()
        else:
            self.mapper.toLast()()

        self.tabledetailsC.resizeColumnsToContents()
        self.tabledetailsC.horizontalHeader().setStretchLastSection( True )
        self.tabledetailsD.resizeColumnsToContents()
        self.tabledetailsD.horizontalHeader().setStretchLastSection( True )
        self.tablenavigation.selectRow( self.mapper.currentIndex() )




    @pyqtSlot( float )
    @if_edit_model
    def on_sbCkD_valueChanged( self, value ):
        self.editmodel.totalCkD = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbCkC_valueChanged( self, value ):
        self.editmodel.totalCkC = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbCardD_valueChanged( self, value ):
        self.editmodel.totalCardD = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbCardC_valueChanged( self, value ):
        self.editmodel.totalCardC = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbDepositD_valueChanged( self, value ):
        self.editmodel.totalDepositD = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbDepositC_valueChanged( self, value ):
        self.editmodel.totalDepositC = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbTransferD_valueChanged( self, value ):
        self.editmodel.totalTransferD = Decimal( str( value ) )

    @pyqtSlot( float )
    @if_edit_model
    def on_sbTransferC_valueChanged( self, value ):
        self.editmodel.totalTransferC = Decimal( str( value ) )
