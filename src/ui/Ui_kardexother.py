# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/kardexother.ui'
#
# Created: Sat Aug  7 13:56:12 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmKardexOther(object):
    def setupUi(self, frmKardexOther):
        frmKardexOther.setObjectName("frmKardexOther")
        frmKardexOther.resize(800, 600)
        self.centralwidget = QtGui.QWidget(frmKardexOther)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.txtPrintedDocumentNumber = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPrintedDocumentNumber.sizePolicy().hasHeightForWidth())
        self.txtPrintedDocumentNumber.setSizePolicy(sizePolicy)
        self.txtPrintedDocumentNumber.setReadOnly(True)
        self.txtPrintedDocumentNumber.setObjectName("txtPrintedDocumentNumber")
        self.gridLayout.addWidget(self.txtPrintedDocumentNumber, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.dtPicker = QtGui.QDateTimeEdit(self.tab)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.gridLayout.addWidget(self.dtPicker, 0, 4, 1, 1)
        self.tabledetails = QtGui.QTableView(self.tab)
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setAlternatingRowColors(True)
        self.tabledetails.setObjectName("tabledetails")
        self.gridLayout.addWidget(self.tabledetails, 1, 0, 1, 5)
        self.swConcept = QtGui.QStackedWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swConcept.sizePolicy().hasHeightForWidth())
        self.swConcept.setSizePolicy(sizePolicy)
        self.swConcept.setObjectName("swConcept")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtConcept = QtGui.QLineEdit(self.page_3)
        self.txtConcept.setReadOnly(True)
        self.txtConcept.setObjectName("txtConcept")
        self.horizontalLayout_2.addWidget(self.txtConcept)
        self.swConcept.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbConcept = QtGui.QComboBox(self.page_4)
        self.cbConcept.setEditable(True)
        self.cbConcept.setObjectName("cbConcept")
        self.verticalLayout_3.addWidget(self.cbConcept)
        self.swConcept.addWidget(self.page_4)
        self.gridLayout.addWidget(self.swConcept, 0, 3, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablenavigation = QtGui.QTableView(self.tab_2)
        self.tablenavigation.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tablenavigation.setAlternatingRowColors(True)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setSortingEnabled(True)
        self.tablenavigation.setObjectName("tablenavigation")
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.verticalLayout.addWidget(self.tabWidget)
        frmKardexOther.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(frmKardexOther)
        self.statusbar.setObjectName("statusbar")
        frmKardexOther.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(frmKardexOther)
        self.toolBar.setObjectName("toolBar")
        frmKardexOther.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionNew = QtGui.QAction(frmKardexOther)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionPreview = QtGui.QAction(frmKardexOther)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/res/document-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreview.setIcon(icon3)
        self.actionPreview.setObjectName("actionPreview")
        self.actionGoFirst = QtGui.QAction(frmKardexOther)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/res/go-first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoFirst.setIcon(icon4)
        self.actionGoFirst.setObjectName("actionGoFirst")
        self.actionGoPrevious = QtGui.QAction(frmKardexOther)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/res/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoPrevious.setIcon(icon5)
        self.actionGoPrevious.setObjectName("actionGoPrevious")
        self.actionGoNext = QtGui.QAction(frmKardexOther)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/res/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoNext.setIcon(icon6)
        self.actionGoNext.setObjectName("actionGoNext")
        self.actionGoLast = QtGui.QAction(frmKardexOther)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/res/go-last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoLast.setIcon(icon7)
        self.actionGoLast.setObjectName("actionGoLast")
        self.actionSave = QtGui.QAction(frmKardexOther)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/res/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon8)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtGui.QAction(frmKardexOther)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/res/document-print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon9)
        self.actionPrint.setObjectName("actionPrint")
        self.actionCancel = QtGui.QAction(frmKardexOther)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/res/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCancel.setIcon(icon10)
        self.actionCancel.setObjectName("actionCancel")
        self.actionEditar = QtGui.QAction(frmKardexOther)
        self.actionEditar.setIcon(icon)
        self.actionEditar.setObjectName("actionEditar")
        self.actionDelete = QtGui.QAction(frmKardexOther)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/res/edit-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon11)
        self.actionDelete.setObjectName("actionDelete")
        self.actionCopy = QtGui.QAction(frmKardexOther)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/res/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon12)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtGui.QAction(frmKardexOther)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/res/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon13)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtGui.QAction(frmKardexOther)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/res/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon14)
        self.actionPaste.setObjectName("actionPaste")
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionCancel)
        self.toolBar.addAction(self.actionPreview)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGoFirst)
        self.toolBar.addAction(self.actionGoPrevious)
        self.toolBar.addAction(self.actionGoNext)
        self.toolBar.addAction(self.actionGoLast)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(frmKardexOther)
        self.tabWidget.setCurrentIndex(1)
        self.swConcept.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmKardexOther)

    def retranslateUi(self, frmKardexOther):
        frmKardexOther.setWindowTitle(QtGui.QApplication.translate("frmKardexOther", "Otros Movimientos de Kardex", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmKardexOther", "Numero de Kardex:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmKardexOther", "Concepto:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), None)
        self.label.setText(QtGui.QApplication.translate("frmKardexOther", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), None)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmKardexOther", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("frmKardexOther", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("frmKardexOther", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setText(QtGui.QApplication.translate("frmKardexOther", "Previsualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoFirst.setText(QtGui.QApplication.translate("frmKardexOther", "Ir al Primer Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoPrevious.setText(QtGui.QApplication.translate("frmKardexOther", "Ir al Registro Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoNext.setText(QtGui.QApplication.translate("frmKardexOther", "Ir al siguiente registro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoLast.setText(QtGui.QApplication.translate("frmKardexOther", "Ir al ultimo registro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("frmKardexOther", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("frmKardexOther", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setText(QtGui.QApplication.translate("frmKardexOther", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar.setText(QtGui.QApplication.translate("frmKardexOther", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar.setShortcut(QtGui.QApplication.translate("frmKardexOther", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("frmKardexOther", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("frmKardexOther", "Copiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("frmKardexOther", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("frmKardexOther", "Cortar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("frmKardexOther", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("frmKardexOther", "Pegar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmKardexOther = QtGui.QMainWindow()
    ui = Ui_frmKardexOther()
    ui.setupUi(frmKardexOther)
    frmKardexOther.show()
    sys.exit(app.exec_())

