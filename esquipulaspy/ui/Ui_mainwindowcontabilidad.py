# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Workspace\EsquipulasPy\esquipulaspy\ui\mainwindowcontabilidad.ui'
#
# Created: Mon Oct 18 23:26:17 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1151, 708)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(125, 124, 123))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setTabShape(QtGui.QTabWidget.Rounded)
        self.mdiArea.setTabPosition(QtGui.QTabWidget.North)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.horizontalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(230, 158))
        self.dockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents_2)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 214, 620))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBalance = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBalance.sizePolicy().hasHeightForWidth())
        self.btnBalance.setSizePolicy(sizePolicy)
        self.btnBalance.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnBalance.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/res/view-pim-tasks.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBalance.setIcon(icon1)
        self.btnBalance.setIconSize(QtCore.QSize(48, 48))
        self.btnBalance.setAutoDefault(False)
        self.btnBalance.setDefault(False)
        self.btnBalance.setFlat(False)
        self.btnBalance.setObjectName(_fromUtf8("btnBalance"))
        self.gridLayout.addWidget(self.btnBalance, 0, 0, 1, 1)
        self.btnCheques = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCheques.sizePolicy().hasHeightForWidth())
        self.btnCheques.setSizePolicy(sizePolicy)
        self.btnCheques.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnCheques.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/res/account-types-checking.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCheques.setIcon(icon2)
        self.btnCheques.setIconSize(QtCore.QSize(48, 48))
        self.btnCheques.setAutoDefault(False)
        self.btnCheques.setDefault(False)
        self.btnCheques.setFlat(False)
        self.btnCheques.setObjectName(_fromUtf8("btnCheques"))
        self.gridLayout.addWidget(self.btnCheques, 1, 0, 1, 1)
        self.btnEstado = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEstado.sizePolicy().hasHeightForWidth())
        self.btnEstado.setSizePolicy(sizePolicy)
        self.btnEstado.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnEstado.setFont(font)
        self.btnEstado.setIcon(icon1)
        self.btnEstado.setIconSize(QtCore.QSize(48, 48))
        self.btnEstado.setAutoDefault(False)
        self.btnEstado.setDefault(False)
        self.btnEstado.setFlat(False)
        self.btnEstado.setObjectName(_fromUtf8("btnEstado"))
        self.gridLayout.addWidget(self.btnEstado, 2, 0, 1, 1)
        self.btnMovements = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMovements.sizePolicy().hasHeightForWidth())
        self.btnMovements.setSizePolicy(sizePolicy)
        self.btnMovements.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnMovements.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/res/transaction-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMovements.setIcon(icon3)
        self.btnMovements.setIconSize(QtCore.QSize(64, 64))
        self.btnMovements.setAutoDefault(False)
        self.btnMovements.setDefault(False)
        self.btnMovements.setFlat(False)
        self.btnMovements.setObjectName(_fromUtf8("btnMovements"))
        self.gridLayout.addWidget(self.btnMovements, 3, 0, 1, 1)
        self.btnConciliacion = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConciliacion.sizePolicy().hasHeightForWidth())
        self.btnConciliacion.setSizePolicy(sizePolicy)
        self.btnConciliacion.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnConciliacion.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/res/reconcile.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConciliacion.setIcon(icon4)
        self.btnConciliacion.setIconSize(QtCore.QSize(48, 48))
        self.btnConciliacion.setAutoDefault(False)
        self.btnConciliacion.setDefault(False)
        self.btnConciliacion.setFlat(False)
        self.btnConciliacion.setObjectName(_fromUtf8("btnConciliacion"))
        self.gridLayout.addWidget(self.btnConciliacion, 4, 0, 1, 1)
        self.btnNotasCD = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNotasCD.sizePolicy().hasHeightForWidth())
        self.btnNotasCD.setSizePolicy(sizePolicy)
        self.btnNotasCD.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnNotasCD.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/res/view-bank-account-checking.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNotasCD.setIcon(icon5)
        self.btnNotasCD.setIconSize(QtCore.QSize(48, 48))
        self.btnNotasCD.setAutoDefault(False)
        self.btnNotasCD.setDefault(False)
        self.btnNotasCD.setFlat(False)
        self.btnNotasCD.setObjectName(_fromUtf8("btnNotasCD"))
        self.gridLayout.addWidget(self.btnNotasCD, 5, 0, 1, 1)
        self.btnCierreMensual = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCierreMensual.sizePolicy().hasHeightForWidth())
        self.btnCierreMensual.setSizePolicy(sizePolicy)
        self.btnCierreMensual.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnCierreMensual.setFont(font)
        self.btnCierreMensual.setIcon(icon1)
        self.btnCierreMensual.setIconSize(QtCore.QSize(48, 48))
        self.btnCierreMensual.setAutoDefault(False)
        self.btnCierreMensual.setDefault(False)
        self.btnCierreMensual.setFlat(False)
        self.btnCierreMensual.setObjectName(_fromUtf8("btnCierreMensual"))
        self.gridLayout.addWidget(self.btnCierreMensual, 6, 0, 1, 1)
        self.btnCierreAnual = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCierreAnual.sizePolicy().hasHeightForWidth())
        self.btnCierreAnual.setSizePolicy(sizePolicy)
        self.btnCierreAnual.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnCierreAnual.setFont(font)
        self.btnCierreAnual.setIcon(icon1)
        self.btnCierreAnual.setIconSize(QtCore.QSize(48, 48))
        self.btnCierreAnual.setAutoDefault(False)
        self.btnCierreAnual.setDefault(False)
        self.btnCierreAnual.setFlat(False)
        self.btnCierreAnual.setObjectName(_fromUtf8("btnCierreAnual"))
        self.gridLayout.addWidget(self.btnCierreAnual, 7, 0, 1, 1)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 230, 572))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnAccounts = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccounts.sizePolicy().hasHeightForWidth())
        self.btnAccounts.setSizePolicy(sizePolicy)
        self.btnAccounts.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnAccounts.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/view-bank-account.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAccounts.setIcon(icon6)
        self.btnAccounts.setIconSize(QtCore.QSize(48, 48))
        self.btnAccounts.setAutoDefault(False)
        self.btnAccounts.setDefault(False)
        self.btnAccounts.setFlat(False)
        self.btnAccounts.setObjectName(_fromUtf8("btnAccounts"))
        self.verticalLayout_2.addWidget(self.btnAccounts)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionLockSession = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/object-locked.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLockSession.setIcon(icon7)
        self.actionLockSession.setObjectName(_fromUtf8("actionLockSession"))
        self.actionUnlockSession = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/object-unlocked.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnlockSession.setIcon(icon8)
        self.actionUnlockSession.setVisible(False)
        self.actionUnlockSession.setObjectName(_fromUtf8("actionUnlockSession"))
        self.toolBar.addAction(self.actionLockSession)
        self.toolBar.addAction(self.actionUnlockSession)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Llantera Esquipulas: Contabilidad", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Contabilidad", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBalance.setText(QtGui.QApplication.translate("MainWindow", "Balance\n"
"General", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBalance.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCheques.setText(QtGui.QApplication.translate("MainWindow", "Cheques", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCheques.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEstado.setText(QtGui.QApplication.translate("MainWindow", "Estado\n"
"de Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEstado.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMovements.setText(QtGui.QApplication.translate("MainWindow", "Ajustes\n"
"Contables", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMovements.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+1", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConciliacion.setText(QtGui.QApplication.translate("MainWindow", "Conciliación\n"
"Bancaria", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConciliacion.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+3", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNotasCD.setText(QtGui.QApplication.translate("MainWindow", "Movimientos\n"
"Bancarios", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNotasCD.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCierreMensual.setText(QtGui.QApplication.translate("MainWindow", "Cierre Mensual", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCierreMensual.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCierreAnual.setText(QtGui.QApplication.translate("MainWindow", "Cierre Anual", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCierreAnual.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "Operaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAccounts.setText(QtGui.QApplication.translate("MainWindow", "Cuentas\n"
"Contables", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAccounts.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Catalogos", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLockSession.setText(QtGui.QApplication.translate("MainWindow", "Bloquear Sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnlockSession.setText(QtGui.QApplication.translate("MainWindow", "Desbloquear Sesión", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
