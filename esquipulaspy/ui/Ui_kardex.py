# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/kardex.ui'
#
# Created: Mon Aug 23 02:45:02 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmKardex(object):
    def setupUi(self, frmKardex):
        frmKardex.setObjectName("frmKardex")
        frmKardex.resize(800, 600)
        self.centralwidget = QtGui.QWidget(frmKardex)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tabdetails = QtGui.QWidget()
        self.tabdetails.setObjectName("tabdetails")
        self.gridLayout = QtGui.QGridLayout(self.tabdetails)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.tabdetails)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.txtParentPrintedDocumentNumber = QtGui.QLineEdit(self.tabdetails)
        self.txtParentPrintedDocumentNumber.setReadOnly(True)
        self.txtParentPrintedDocumentNumber.setObjectName("txtParentPrintedDocumentNumber")
        self.horizontalLayout_2.addWidget(self.txtParentPrintedDocumentNumber)
        self.label_6 = QtGui.QLabel(self.tabdetails)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.txtPrintedDocumentNumber = QtGui.QLineEdit(self.tabdetails)
        self.txtPrintedDocumentNumber.setReadOnly(True)
        self.txtPrintedDocumentNumber.setObjectName("txtPrintedDocumentNumber")
        self.horizontalLayout_2.addWidget(self.txtPrintedDocumentNumber)
        self.label_7 = QtGui.QLabel(self.tabdetails)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.txtWarehouse = QtGui.QLineEdit(self.tabdetails)
        self.txtWarehouse.setReadOnly(True)
        self.txtWarehouse.setObjectName("txtWarehouse")
        self.horizontalLayout_2.addWidget(self.txtWarehouse)
        self.label_2 = QtGui.QLabel(self.tabdetails)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dtPicker = QtGui.QDateTimeEdit(self.tabdetails)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.horizontalLayout_2.addWidget(self.dtPicker)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.tabledetails = QtGui.QTableView(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabledetails.sizePolicy().hasHeightForWidth())
        self.tabledetails.setSizePolicy(sizePolicy)
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setAlternatingRowColors(True)
        self.tabledetails.setObjectName("tabledetails")
        self.tabledetails.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tabledetails, 1, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.tabdetails)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.txtKardexObservation = QtGui.QPlainTextEdit(self.tabdetails)
        self.txtKardexObservation.setReadOnly(True)
        self.txtKardexObservation.setObjectName("txtKardexObservation")
        self.gridLayout.addWidget(self.txtKardexObservation, 4, 0, 1, 1)
        self.txtDocObservation = QtGui.QPlainTextEdit(self.tabdetails)
        self.txtDocObservation.setReadOnly(True)
        self.txtDocObservation.setObjectName("txtDocObservation")
        self.gridLayout.addWidget(self.txtDocObservation, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tabdetails)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabdetails, icon, "")
        self.tabnavigation = QtGui.QWidget()
        self.tabnavigation.setObjectName("tabnavigation")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabnavigation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablenavigation = QtGui.QTableView(self.tabnavigation)
        self.tablenavigation.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tablenavigation.setAlternatingRowColors(True)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setSortingEnabled(True)
        self.tablenavigation.setObjectName("tablenavigation")
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.tablenavigation.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.tabnavigation)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.tabnavigation)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabnavigation, icon1, "")
        self.verticalLayout.addWidget(self.tabWidget)
        frmKardex.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(frmKardex)
        self.statusbar.setObjectName("statusbar")
        frmKardex.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(frmKardex)
        self.toolBar.setObjectName("toolBar")
        frmKardex.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.label_2.setBuddy(self.dtPicker)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(frmKardex)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmKardex)

    def retranslateUi(self, frmKardex):
        frmKardex.setWindowTitle(QtGui.QApplication.translate("frmKardex", "Kardex", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmKardex", "<b>Documento: </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmKardex", "<b>Kardex: </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("frmKardex", "<b>Bodega</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmKardex", "<b>&Fecha</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmKardex", "<b>Observaciones del Documento</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmKardex", "<b>Observaciones de Kardex</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), None)
        self.label.setText(QtGui.QApplication.translate("frmKardex", "<b>&Buscar</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation), None)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmKardex", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmKardex = QtGui.QMainWindow()
    ui = Ui_frmKardex()
    ui.setupUi(frmKardex)
    frmKardex.show()
    sys.exit(app.exec_())

