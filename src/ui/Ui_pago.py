# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\EsquipulasPy\src\ui\pago.ui'
#
# Created: Sat Sep 11 21:49:37 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmPago(object):
    def setupUi(self, FrmPago):
        FrmPago.setObjectName("frmPago")
        FrmPago.resize(672, 465)
        self.centralwidget = QtGui.QWidget(FrmPago)
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
        self.groupBox_4 = QtGui.QGroupBox(self.tabdetails)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 130))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lblnpago = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblnpago.sizePolicy().hasHeightForWidth())
        self.lblnpago.setSizePolicy(sizePolicy)
        self.lblnpago.setStyleSheet("border:1px solid #000")
        self.lblnpago.setAlignment(QtCore.Qt.AlignCenter)
        self.lblnpago.setObjectName("lblnpago")
        self.gridLayout_2.addWidget(self.lblnpago, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.dtPicker = QtGui.QDateTimeEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtPicker.sizePolicy().hasHeightForWidth())
        self.dtPicker.setSizePolicy(sizePolicy)
        self.dtPicker.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.gridLayout_2.addWidget(self.dtPicker, 0, 5, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.swbeneficiario = QtGui.QStackedWidget(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swbeneficiario.sizePolicy().hasHeightForWidth())
        self.swbeneficiario.setSizePolicy(sizePolicy)
        self.swbeneficiario.setStyleSheet("padding:0px;")
        self.swbeneficiario.setObjectName("swbeneficiario")
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName("page_7")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.page_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbbeneficiario = QtGui.QComboBox(self.page_7)
        self.cbbeneficiario.setMinimumSize(QtCore.QSize(0, 20))
        self.cbbeneficiario.setEditable(True)
        self.cbbeneficiario.setObjectName("cbbeneficiario")
        self.horizontalLayout_6.addWidget(self.cbbeneficiario)
        self.swbeneficiario.addWidget(self.page_7)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName("page_8")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtbeneficiario = QtGui.QLineEdit(self.page_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtbeneficiario.sizePolicy().hasHeightForWidth())
        self.txtbeneficiario.setSizePolicy(sizePolicy)
        self.txtbeneficiario.setMinimumSize(QtCore.QSize(0, 20))
        self.txtbeneficiario.setStyleSheet("padding:0px;")
        self.txtbeneficiario.setDragEnabled(True)
        self.txtbeneficiario.setReadOnly(True)
        self.txtbeneficiario.setObjectName("txtbeneficiario")
        self.horizontalLayout_3.addWidget(self.txtbeneficiario)
        self.swbeneficiario.addWidget(self.page_8)
        self.gridLayout_2.addWidget(self.swbeneficiario, 1, 1, 1, 5)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.swconcepto = QtGui.QStackedWidget(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swconcepto.sizePolicy().hasHeightForWidth())
        self.swconcepto.setSizePolicy(sizePolicy)
        self.swconcepto.setMaximumSize(QtCore.QSize(16777215, 30))
        self.swconcepto.setObjectName("swconcepto")
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbconcepto = QtGui.QComboBox(self.page_5)
        self.cbconcepto.setMinimumSize(QtCore.QSize(0, 20))
        self.cbconcepto.setEditable(True)
        self.cbconcepto.setObjectName("cbconcepto")
        self.verticalLayout_4.addWidget(self.cbconcepto)
        self.swconcepto.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtconcepto = QtGui.QLineEdit(self.page_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtconcepto.sizePolicy().hasHeightForWidth())
        self.txtconcepto.setSizePolicy(sizePolicy)
        self.txtconcepto.setMinimumSize(QtCore.QSize(0, 20))
        self.txtconcepto.setStyleSheet("None")
        self.txtconcepto.setDragEnabled(True)
        self.txtconcepto.setReadOnly(True)
        self.txtconcepto.setObjectName("txtconcepto")
        self.horizontalLayout_2.addWidget(self.txtconcepto)
        self.swconcepto.addWidget(self.page_6)
        self.gridLayout_2.addWidget(self.swconcepto, 2, 1, 1, 2)
        self.ckretener = QtGui.QCheckBox(self.groupBox_4)
        self.ckretener.setEnabled(False)
        self.ckretener.setChecked(False)
        self.ckretener.setObjectName("ckretener")
        self.gridLayout_2.addWidget(self.ckretener, 2, 4, 1, 1)
        self.swtasaret = QtGui.QStackedWidget(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swtasaret.sizePolicy().hasHeightForWidth())
        self.swtasaret.setSizePolicy(sizePolicy)
        self.swtasaret.setMaximumSize(QtCore.QSize(80, 50))
        self.swtasaret.setObjectName("swtasaret")
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.page_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cbtasaret = QtGui.QComboBox(self.page_9)
        self.cbtasaret.setEnabled(False)
        self.cbtasaret.setMinimumSize(QtCore.QSize(0, 20))
        self.cbtasaret.setEditable(False)
        self.cbtasaret.setObjectName("cbtasaret")
        self.horizontalLayout_9.addWidget(self.cbtasaret)
        self.label_8 = QtGui.QLabel(self.page_9)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.swtasaret.addWidget(self.page_9)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.page_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.txttasaret = QtGui.QLineEdit(self.page_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txttasaret.sizePolicy().hasHeightForWidth())
        self.txttasaret.setSizePolicy(sizePolicy)
        self.txttasaret.setMinimumSize(QtCore.QSize(0, 20))
        self.txttasaret.setStyleSheet("None")
        self.txttasaret.setText("")
        self.txttasaret.setAlignment(QtCore.Qt.AlignCenter)
        self.txttasaret.setDragEnabled(True)
        self.txttasaret.setReadOnly(True)
        self.txttasaret.setObjectName("txttasaret")
        self.horizontalLayout_10.addWidget(self.txttasaret)
        self.swtasaret.addWidget(self.page_10)
        self.gridLayout_2.addWidget(self.swtasaret, 2, 5, 1, 1)
        self.ckiva = QtGui.QCheckBox(self.groupBox_4)
        self.ckiva.setEnabled(False)
        self.ckiva.setChecked(True)
        self.ckiva.setObjectName("ckiva")
        self.gridLayout_2.addWidget(self.ckiva, 2, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.txttipocambio = QtGui.QLineEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txttipocambio.sizePolicy().hasHeightForWidth())
        self.txttipocambio.setSizePolicy(sizePolicy)
        self.txttipocambio.setMinimumSize(QtCore.QSize(0, 20))
        self.txttipocambio.setStyleSheet("None")
        self.txttipocambio.setAlignment(QtCore.Qt.AlignCenter)
        self.txttipocambio.setDragEnabled(True)
        self.txttipocambio.setReadOnly(True)
        self.txttipocambio.setObjectName("txttipocambio")
        self.gridLayout_2.addWidget(self.txttipocambio, 0, 3, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.sbtotalc = QtGui.QDoubleSpinBox(self.tabdetails)
        self.sbtotalc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbtotalc.setReadOnly(True)
        self.sbtotalc.setDecimals(4)
        self.sbtotalc.setMaximum(100000.0)
        self.sbtotalc.setObjectName("sbtotalc")
        self.gridLayout.addWidget(self.sbtotalc, 0, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 4, 1, 1)
        self.sbtotald = QtGui.QDoubleSpinBox(self.tabdetails)
        self.sbtotald.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbtotald.setReadOnly(True)
        self.sbtotald.setDecimals(4)
        self.sbtotald.setMaximum(100000.0)
        self.sbtotald.setObjectName("sbtotald")
        self.gridLayout.addWidget(self.sbtotald, 0, 5, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.groupcuentas = QtGui.QGroupBox(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupcuentas.sizePolicy().hasHeightForWidth())
        self.groupcuentas.setSizePolicy(sizePolicy)
        self.groupcuentas.setObjectName("groupcuentas")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupcuentas)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabledetails = QtGui.QTableView(self.groupcuentas)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabledetails.sizePolicy().hasHeightForWidth())
        self.tabledetails.setSizePolicy(sizePolicy)
        self.tabledetails.setMinimumSize(QtCore.QSize(0, 60))
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setObjectName("tabledetails")
        self.horizontalLayout_7.addWidget(self.tabledetails)
        self.verticalLayout_3.addWidget(self.groupcuentas)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 1, 1, 1)
        self.lblretencion = QtGui.QLabel(self.tabdetails)
        self.lblretencion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblretencion.setObjectName("lblretencion")
        self.gridLayout_3.addWidget(self.lblretencion, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)
        self.lbltotalpago = QtGui.QLabel(self.tabdetails)
        self.lbltotalpago.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotalpago.setObjectName("lbltotalpago")
        self.gridLayout_3.addWidget(self.lbltotalpago, 2, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.lbltotal = QtGui.QLabel(self.tabdetails)
        self.lbltotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotal.setObjectName("lbltotal")
        self.gridLayout_3.addWidget(self.lbltotal, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.label_22 = QtGui.QLabel(self.tabdetails)
        self.label_22.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_3.addWidget(self.label_22)
        self.txtobservaciones = QtGui.QPlainTextEdit(self.tabdetails)
        self.txtobservaciones.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtobservaciones.sizePolicy().hasHeightForWidth())
        self.txtobservaciones.setSizePolicy(sizePolicy)
        self.txtobservaciones.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txtobservaciones.setReadOnly(True)
        self.txtobservaciones.setObjectName("txtobservaciones")
        self.verticalLayout_3.addWidget(self.txtobservaciones)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabdetails, icon, "")
        self.tabnavigation = QtGui.QWidget()
        self.tabnavigation.setObjectName("tabnavigation")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabnavigation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablenavigation = QtGui.QTableView(self.tabnavigation)
        self.tablenavigation.setAlternatingRowColors(True)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setObjectName("tablenavigation")
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.tablenavigation.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(self.tabnavigation)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.txtSearch = QtGui.QLineEdit(self.tabnavigation)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout.addWidget(self.txtSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabnavigation, icon1, "")
        self.verticalLayout.addWidget(self.tabWidget)
        FrmPago.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FrmPago)
        self.statusbar.setObjectName("statusbar")
        FrmPago.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(FrmPago)
        self.toolBar.setObjectName("toolBar")
        FrmPago.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.label_5.setBuddy(self.dtPicker)
        self.label_6.setBuddy(self.txtconcepto)
        self.label_9.setBuddy(self.txtconcepto)
        self.label_11.setBuddy(self.txtconcepto)
        self.label_12.setBuddy(self.txtconcepto)
        self.label_4.setBuddy(self.txtSearch)

        self.retranslateUi(FrmPago)
        self.tabWidget.setCurrentIndex(0)
        self.swbeneficiario.setCurrentIndex(0)
        self.swconcepto.setCurrentIndex(1)
        self.swtasaret.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FrmPago)
        FrmPago.setTabOrder(self.cbbeneficiario, self.cbconcepto)
        FrmPago.setTabOrder(self.cbconcepto, self.ckiva)
        FrmPago.setTabOrder(self.ckiva, self.ckretener)
        FrmPago.setTabOrder(self.ckretener, self.cbtasaret)
        FrmPago.setTabOrder(self.cbtasaret, self.sbtotalc)
        FrmPago.setTabOrder(self.sbtotalc, self.sbtotald)
        FrmPago.setTabOrder(self.sbtotald, self.tabledetails)
        FrmPago.setTabOrder(self.tabledetails, self.txtobservaciones)
        FrmPago.setTabOrder(self.txtobservaciones, self.dtPicker)
        FrmPago.setTabOrder(self.dtPicker, self.tabWidget)
        FrmPago.setTabOrder(self.tabWidget, self.txtSearch)
        FrmPago.setTabOrder(self.txtSearch, self.tablenavigation)
        FrmPago.setTabOrder(self.tablenavigation, self.txtbeneficiario)
        FrmPago.setTabOrder(self.txtbeneficiario, self.txtconcepto)
        FrmPago.setTabOrder(self.txtconcepto, self.txttasaret)

    def retranslateUi(self, FrmPago):
        FrmPago.setWindowTitle(QtGui.QApplication.translate("frmPago", "Comprobante de Pago", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("frmPago", "Datos del comprobante de pago", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Comprobante No.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblnpago.setText(QtGui.QApplication.translate("frmPago", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmPago", "&<b>Fecha</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.dtPicker.setDisplayFormat(QtGui.QApplication.translate("frmPago", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Pagamos a:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmPago", "<b>En concepto de:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.ckretener.setText(QtGui.QApplication.translate("frmPago", "Retener", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("frmPago", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.ckiva.setText(QtGui.QApplication.translate("frmPago", "Con IVA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tipo de Cambio</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Total</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sbtotalc.setPrefix(QtGui.QApplication.translate("frmPago", "C$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Total</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sbtotald.setPrefix(QtGui.QApplication.translate("frmPago", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupcuentas.setTitle(QtGui.QApplication.translate("frmPago", "Cuentas Contables", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Retención   -</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblretencion.setText(QtGui.QApplication.translate("frmPago", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Total Pagado</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotalpago.setText(QtGui.QApplication.translate("frmPago", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("frmPago", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Total</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotal.setText(QtGui.QApplication.translate("frmPago", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("frmPago", "<b>Observaciones </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), None)
        self.label_4.setText(QtGui.QApplication.translate("frmPago", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation), None)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmPago", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
