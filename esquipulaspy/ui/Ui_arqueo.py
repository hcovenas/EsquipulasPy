# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/arqueo.ui'
#
# Created: Mon Aug 23 01:17:26 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmArqueo(object):
    def setupUi(self, FrmArqueo):
        FrmArqueo.setObjectName("frmArqueo")
        FrmArqueo.resize(800, 664)
        self.centralwidget = QtGui.QWidget(FrmArqueo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tabdetails = QtGui.QWidget()
        self.tabdetails.setObjectName("tabdetails")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabdetails)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lblUserName = QtGui.QLineEdit(self.tabdetails)
        self.lblUserName.setReadOnly(True)
        self.lblUserName.setObjectName("lblUserName")
        self.horizontalLayout_2.addWidget(self.lblUserName)
        self.dtPicker = QtGui.QDateTimeEdit(self.tabdetails)
        self.dtPicker.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtPicker.sizePolicy().hasHeightForWidth())
        self.dtPicker.setSizePolicy(sizePolicy)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.horizontalLayout_2.addWidget(self.dtPicker)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.tabdetails)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.tabdetails)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.tabledetailsD = QtGui.QTableView(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabledetailsD.sizePolicy().hasHeightForWidth())
        self.tabledetailsD.setSizePolicy(sizePolicy)
        self.tabledetailsD.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabledetailsD.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetailsD.setAlternatingRowColors(True)
        self.tabledetailsD.setObjectName("tabledetailsD")
        self.tabledetailsD.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tabledetailsD, 1, 0, 1, 1)
        self.tabledetailsC = QtGui.QTableView(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabledetailsC.sizePolicy().hasHeightForWidth())
        self.tabledetailsC.setSizePolicy(sizePolicy)
        self.tabledetailsC.setObjectName("tabledetailsC")
        self.gridLayout.addWidget(self.tabledetailsC, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtGui.QGroupBox(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtObservations = QtGui.QPlainTextEdit(self.groupBox_2)
        self.txtObservations.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtObservations.sizePolicy().hasHeightForWidth())
        self.txtObservations.setSizePolicy(sizePolicy)
        self.txtObservations.setReadOnly(True)
        self.txtObservations.setObjectName("txtObservations")
        self.gridLayout_3.addWidget(self.txtObservations, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 12, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.lblCkC = QtGui.QLabel(self.groupBox)
        self.lblCkC.setObjectName("lblCkC")
        self.gridLayout_2.addWidget(self.lblCkC, 9, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 4, 1, 2)
        self.lblCardC = QtGui.QLabel(self.groupBox)
        self.lblCardC.setObjectName("lblCardC")
        self.gridLayout_2.addWidget(self.lblCardC, 12, 5, 1, 1)
        self.lblCashC = QtGui.QLabel(self.groupBox)
        self.lblCashC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCashC.setObjectName("lblCashC")
        self.gridLayout_2.addWidget(self.lblCashC, 1, 4, 1, 2)
        self.lblDepositC = QtGui.QLabel(self.groupBox)
        self.lblDepositC.setObjectName("lblDepositC")
        self.gridLayout_2.addWidget(self.lblDepositC, 14, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 3)
        self.lblCashD = QtGui.QLabel(self.groupBox)
        self.lblCashD.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCashD.setObjectName("lblCashD")
        self.gridLayout_2.addWidget(self.lblCashD, 1, 1, 1, 2)
        self.lblCkD = QtGui.QLabel(self.groupBox)
        self.lblCkD.setObjectName("lblCkD")
        self.gridLayout_2.addWidget(self.lblCkD, 9, 2, 1, 1)
        self.lblCardD = QtGui.QLabel(self.groupBox)
        self.lblCardD.setObjectName("lblCardD")
        self.gridLayout_2.addWidget(self.lblCardD, 12, 2, 1, 1)
        self.lblDepositD = QtGui.QLabel(self.groupBox)
        self.lblDepositD.setObjectName("lblDepositD")
        self.gridLayout_2.addWidget(self.lblDepositD, 14, 2, 1, 1)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setLineWidth(22)
        self.line.setMidLineWidth(22)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 3, 17, 1)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 3)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 5, 4, 1, 2)
        self.line_4 = QtGui.QFrame(self.groupBox)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 11, 0, 1, 3)
        self.line_5 = QtGui.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 11, 4, 1, 2)
        self.line_6 = QtGui.QFrame(self.groupBox)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 13, 0, 1, 3)
        self.line_7 = QtGui.QFrame(self.groupBox)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 13, 4, 1, 2)
        self.sbCkD = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbCkD.sizePolicy().hasHeightForWidth())
        self.sbCkD.setSizePolicy(sizePolicy)
        self.sbCkD.setDecimals(4)
        self.sbCkD.setMaximum(999999999.0)
        self.sbCkD.setObjectName("sbCkD")
        self.gridLayout_2.addWidget(self.sbCkD, 9, 1, 1, 1)
        self.sbCardD = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbCardD.sizePolicy().hasHeightForWidth())
        self.sbCardD.setSizePolicy(sizePolicy)
        self.sbCardD.setDecimals(4)
        self.sbCardD.setMaximum(999999999.0)
        self.sbCardD.setObjectName("sbCardD")
        self.gridLayout_2.addWidget(self.sbCardD, 12, 1, 1, 1)
        self.sbDepositD = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbDepositD.sizePolicy().hasHeightForWidth())
        self.sbDepositD.setSizePolicy(sizePolicy)
        self.sbDepositD.setDecimals(4)
        self.sbDepositD.setMaximum(999999999.0)
        self.sbDepositD.setObjectName("sbDepositD")
        self.gridLayout_2.addWidget(self.sbDepositD, 14, 1, 1, 1)
        self.sbCkC = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbCkC.sizePolicy().hasHeightForWidth())
        self.sbCkC.setSizePolicy(sizePolicy)
        self.sbCkC.setSuffix("")
        self.sbCkC.setDecimals(4)
        self.sbCkC.setMaximum(999999999.0)
        self.sbCkC.setObjectName("sbCkC")
        self.gridLayout_2.addWidget(self.sbCkC, 9, 4, 1, 1)
        self.sbCardC = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbCardC.sizePolicy().hasHeightForWidth())
        self.sbCardC.setSizePolicy(sizePolicy)
        self.sbCardC.setSuffix("")
        self.sbCardC.setDecimals(4)
        self.sbCardC.setMaximum(999999999.0)
        self.sbCardC.setObjectName("sbCardC")
        self.gridLayout_2.addWidget(self.sbCardC, 12, 4, 1, 1)
        self.sbDepositC = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbDepositC.sizePolicy().hasHeightForWidth())
        self.sbDepositC.setSizePolicy(sizePolicy)
        self.sbDepositC.setSuffix("")
        self.sbDepositC.setDecimals(4)
        self.sbDepositC.setMaximum(999999999.0)
        self.sbDepositC.setObjectName("sbDepositC")
        self.gridLayout_2.addWidget(self.sbDepositC, 14, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 16, 0, 1, 1)
        self.line_8 = QtGui.QFrame(self.groupBox)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 15, 0, 1, 3)
        self.sbTransferD = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbTransferD.sizePolicy().hasHeightForWidth())
        self.sbTransferD.setSizePolicy(sizePolicy)
        self.sbTransferD.setDecimals(4)
        self.sbTransferD.setMaximum(999999999.0)
        self.sbTransferD.setObjectName("sbTransferD")
        self.gridLayout_2.addWidget(self.sbTransferD, 16, 1, 1, 1)
        self.sbTransferC = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbTransferC.sizePolicy().hasHeightForWidth())
        self.sbTransferC.setSizePolicy(sizePolicy)
        self.sbTransferC.setSuffix("")
        self.sbTransferC.setDecimals(4)
        self.sbTransferC.setMaximum(999999999.0)
        self.sbTransferC.setObjectName("sbTransferC")
        self.gridLayout_2.addWidget(self.sbTransferC, 16, 4, 1, 1)
        self.line_9 = QtGui.QFrame(self.groupBox)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 15, 4, 1, 2)
        self.lblTransferD = QtGui.QLabel(self.groupBox)
        self.lblTransferD.setObjectName("lblTransferD")
        self.gridLayout_2.addWidget(self.lblTransferD, 16, 2, 1, 1)
        self.lblTransferC = QtGui.QLabel(self.groupBox)
        self.lblTransferC.setObjectName("lblTransferC")
        self.gridLayout_2.addWidget(self.lblTransferC, 16, 5, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
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
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.tabnavigation)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtSearch = QtGui.QLineEdit(self.tabnavigation)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout.addWidget(self.txtSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabnavigation, icon1, "")
        self.verticalLayout.addWidget(self.tabWidget)
        FrmArqueo.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FrmArqueo)
        self.statusbar.setObjectName("statusbar")
        FrmArqueo.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(FrmArqueo)
        self.toolBar.setObjectName("toolBar")
        FrmArqueo.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.label.setBuddy(self.txtSearch)

        self.retranslateUi(FrmArqueo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FrmArqueo)

    def retranslateUi(self, FrmArqueo):
        FrmArqueo.setWindowTitle(QtGui.QApplication.translate("frmArqueo", "Arqueo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmArqueo", "<b>Arqueado por:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmArqueo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Dolares</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmArqueo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Cordobas</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmArqueo", "Observaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("frmArqueo", "El valor a la derecha de la pleca es lo que se espera haya en caja según\n"
"los datos del sistema, el valor a la izquierda es lo que el cajero ha\n"
"ingresado.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("frmArqueo", "<b>Cheques</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("frmArqueo", "<b>Tarjeta</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("frmArqueo", "<b>Depositos</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("frmArqueo", "<b>Efectivo</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCkC.setText(QtGui.QApplication.translate("frmArqueo", "C$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmArqueo", "<b>Cordobas</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCardC.setText(QtGui.QApplication.translate("frmArqueo", "C$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCashC.setText(QtGui.QApplication.translate("frmArqueo", "C$ 0.0000 / C$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDepositC.setText(QtGui.QApplication.translate("frmArqueo", "C$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmArqueo", "<b>Dolares</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCashD.setText(QtGui.QApplication.translate("frmArqueo", "US$ 0.0000 / US$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCkD.setText(QtGui.QApplication.translate("frmArqueo", "US$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCardD.setText(QtGui.QApplication.translate("frmArqueo", "US$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDepositD.setText(QtGui.QApplication.translate("frmArqueo", "US$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.sbCkD.setPrefix(QtGui.QApplication.translate("frmArqueo", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.sbCardD.setPrefix(QtGui.QApplication.translate("frmArqueo", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.sbDepositD.setPrefix(QtGui.QApplication.translate("frmArqueo", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.sbCkC.setPrefix(QtGui.QApplication.translate("frmArqueo", "C$", None, QtGui.QApplication.UnicodeUTF8))
        self.sbCardC.setPrefix(QtGui.QApplication.translate("frmArqueo", "C$", None, QtGui.QApplication.UnicodeUTF8))
        self.sbDepositC.setPrefix(QtGui.QApplication.translate("frmArqueo", "C$", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("frmArqueo", "<b>Transferencias</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.sbTransferD.setPrefix(QtGui.QApplication.translate("frmArqueo", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.sbTransferC.setPrefix(QtGui.QApplication.translate("frmArqueo", "C$", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTransferD.setText(QtGui.QApplication.translate("frmArqueo", "US$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTransferC.setText(QtGui.QApplication.translate("frmArqueo", "C$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), None)
        self.label.setText(QtGui.QApplication.translate("frmArqueo", "<b>&Buscar</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation), None)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmArqueo", "Arqueo", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmArqueo = QtGui.QMainWindow()
    ui = Ui_frmArqueo()
    ui.setupUi(FrmArqueo)
    FrmArqueo.show()
    sys.exit(app.exec_())

