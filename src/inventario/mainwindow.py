# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow, QIcon
from PyQt4.QtCore import pyqtSlot, Qt, SIGNAL, SLOT
from entradacompra import frmEntradaCompra
from catalogos import frmCatProveedores, frmCatMarcas,  frmCatConceptos
from liquidacion import frmLiquidacion
from categorias import frmCategorias
from kardex import frmKardex
from kardexother import frmKardexOther
from ui.Ui_mainwindowinventario import Ui_MainWindow
from articulos import frmArticulos
from utility.mainwindowbase import MainWindowBase
from utility.persona import frmPersona
from utility import constantes

class MainWindow( QMainWindow, Ui_MainWindow, MainWindowBase ):
    """
    Class documentation goes here.
    """
    ROL = constantes.ROLINVENTARIO
    def __init__( self, user, parent = None ):
        """
        Constructor
        """
        self.user = user
        QMainWindow.__init__( self, parent )
        self.setupUi( self )
        MainWindowBase.__init__( self)
        self.init()
        
    def init(self):
        if not self.user.hasRole("bodega"):
            #Quitar la pestaña de compras
            self.widget.setVisible(False)
            self.toolBox.removeItem(1)
        if not self.user.hasRole("inventario"):
            self.page.setVisible(False)
            self.toolBox.removeItem(2)
            
            self.page_2.setVisible(False)
            self.toolBox.removeItem(0)

        
            



        
    def closeEvent( self, event ):
        u"""
        Guardar el tamaño, la posición en la pantalla y la posición de la barra de tareas
        Preguntar si realmente se desea cerrar la pestaña cuando se esta en modo edición
        """
        for hijo in self.mdiArea.subWindowList():
            if not hijo.close():
                event.ignore()
                return
    def setControls( self, state ):
        """
        En esta funcion cambio el estado enabled de todos los items en el formulario
        @param state: false = bloqueado        true = activado
        """
        self.btnArticles.setEnabled( state )
        self.btnBrands.setEnabled( state )
        self.btnCategories.setEnabled( state )
        self.btnEntries.setEnabled( state )
        self.btnLiquidations.setEnabled( state )
        self.btnProviders.setEnabled( state )

        self.mdiArea.setEnabled( state )
        self.mdiArea.setVisible( state )
        
        self.btnKEntries.setEnabled(state)
        self.btnKExits.setEnabled(state)
        self.btnKOther.setEnabled(state)

        self.actionLockSession.setVisible( state )
        self.actionUnlockSession.setVisible( not state )

    @pyqtSlot( )
    def on_btnConceptos_clicked( self ):
        """
        Slot documentation goes here.
        """
        conceptos = frmCatConceptos( 4,self )
        self.mdiArea.addSubWindow( conceptos )
        conceptos.show()   
    
    @pyqtSlot(  )
    def on_btnEntries_clicked( self ):
        """
        Slot documentation goes here.
        """
        entradacompra = frmEntradaCompra( self.user, self )
        self.mdiArea.addSubWindow( entradacompra )
        entradacompra.show()

    @pyqtSlot(  )
    def on_btnArticles_clicked( self ):
        """
        Slot documentation goes here.
        """
        catproducts = frmArticulos( self )
        self.mdiArea.addSubWindow( catproducts )
        catproducts.show()


    @pyqtSlot(  )
    def on_btnCategories_clicked( self ):
        """
        Slot documentation goes here.
        """

        catcategorias = frmCategorias( self )
        self.mdiArea.addSubWindow( catcategorias )
        catcategorias.show()

    @pyqtSlot(  )
    def on_btnBrands_clicked( self ):
        """
        Slot documentation goes here.
        """

        catmarcas = frmCatMarcas( self )
        self.mdiArea.addSubWindow( catmarcas )
        catmarcas.show()

    @pyqtSlot(  )
    def on_btnProviders_clicked( self ):
        """
        Slot documentation goes here.
        """
        dialog = frmPersona(constantes.PROVEEDOR,"Proveedor",self)
        dialog.show()
#        catproveedores = frmCatProveedores( self )
#        self.mdiArea.addSubWindow( catproveedores )
#        catproveedores.show()

    @pyqtSlot(  )
    def on_btnLiquidations_clicked( self ):
        """
        Slot documentation goes here.
        """
        liquidacion = frmLiquidacion( self.user, self )
        self.mdiArea.addSubWindow( liquidacion )
        liquidacion.show()

    @pyqtSlot(  )
    def on_btnKEntries_clicked( self ):
        """
        Slot documentation goes here.
        """
        kardex = frmKardex( self.user,[7,10,21], self )
        self.mdiArea.addSubWindow( kardex )
        kardex.show()
        
    @pyqtSlot()
    def on_btnKOther_clicked(self):
        """
        Slot documentation goes here
        """
        kardex = frmKardexOther(self.user, self)
        self.mdiArea.addSubWindow( kardex )
        kardex.show()
        
    @pyqtSlot(  )
    def on_btnKExits_clicked( self ):
        """
        Slot documentation goes here.
        """
        kardex = frmKardex( self.user,[5], self, False )
        self.mdiArea.addSubWindow( kardex )
        kardex.show()