# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/liquidacion.ui'
#
# Created by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FrmLiquidacion(object):
    def setupUi(self, FrmLiquidacion):
        FrmLiquidacion.setObjectName("FrmLiquidacion")
        FrmLiquidacion.resize(833, 592)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrmLiquidacion.sizePolicy().hasHeightForWidth())
        FrmLiquidacion.setSizePolicy(sizePolicy)
        FrmLiquidacion.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(FrmLiquidacion)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tabdetails = QtGui.QWidget()
        self.tabdetails.setObjectName("tabdetails")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabdetails)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_3 = QtGui.QGroupBox(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.txtPolicy = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPolicy.sizePolicy().hasHeightForWidth())
        self.txtPolicy.setSizePolicy(sizePolicy)
        self.txtPolicy.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtPolicy.setReadOnly(True)
        self.txtPolicy.setObjectName("txtPolicy")
        self.gridLayout.addWidget(self.txtPolicy, 0, 1, 1, 3)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.swProvider = QtGui.QStackedWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swProvider.sizePolicy().hasHeightForWidth())
        self.swProvider.setSizePolicy(sizePolicy)
        self.swProvider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.swProvider.setObjectName("swProvider")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txtProvider = QtGui.QLineEdit(self.page)
        self.txtProvider.setReadOnly(True)
        self.txtProvider.setObjectName("txtProvider")
        self.horizontalLayout_5.addWidget(self.txtProvider)
        self.swProvider.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbProvider = QtGui.QComboBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbProvider.sizePolicy().hasHeightForWidth())
        self.cbProvider.setSizePolicy(sizePolicy)
        self.cbProvider.setEditable(True)
        self.cbProvider.setObjectName("cbProvider")
        self.horizontalLayout_6.addWidget(self.cbProvider)
        self.swProvider.addWidget(self.page_2)
        self.gridLayout.addWidget(self.swProvider, 1, 1, 1, 3)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.dtPicker = QtGui.QDateEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtPicker.sizePolicy().hasHeightForWidth())
        self.dtPicker.setSizePolicy(sizePolicy)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.gridLayout.addWidget(self.dtPicker, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.txtExchangeRate = QtGui.QLineEdit(self.groupBox_3)
        self.txtExchangeRate.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtExchangeRate.sizePolicy().hasHeightForWidth())
        self.txtExchangeRate.setSizePolicy(sizePolicy)
        self.txtExchangeRate.setMaximumSize(QtCore.QSize(83, 16777215))
        self.txtExchangeRate.setReadOnly(True)
        self.txtExchangeRate.setObjectName("txtExchangeRate")
        self.gridLayout.addWidget(self.txtExchangeRate, 2, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.txtSource = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSource.sizePolicy().hasHeightForWidth())
        self.txtSource.setSizePolicy(sizePolicy)
        self.txtSource.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtSource.setReadOnly(True)
        self.txtSource.setObjectName("txtSource")
        self.gridLayout.addWidget(self.txtSource, 3, 1, 1, 3)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.swWarehouse = QtGui.QStackedWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swWarehouse.sizePolicy().hasHeightForWidth())
        self.swWarehouse.setSizePolicy(sizePolicy)
        self.swWarehouse.setMaximumSize(QtCore.QSize(200, 16777215))
        self.swWarehouse.setObjectName("swWarehouse")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cbWarehouse = QtGui.QComboBox(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbWarehouse.sizePolicy().hasHeightForWidth())
        self.cbWarehouse.setSizePolicy(sizePolicy)
        self.cbWarehouse.setEditable(True)
        self.cbWarehouse.setObjectName("cbWarehouse")
        self.verticalLayout_6.addWidget(self.cbWarehouse)
        self.swWarehouse.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.page_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txtWarehouse = QtGui.QLineEdit(self.page_4)
        self.txtWarehouse.setReadOnly(True)
        self.txtWarehouse.setObjectName("txtWarehouse")
        self.horizontalLayout_7.addWidget(self.txtWarehouse)
        self.swWarehouse.addWidget(self.page_4)
        self.gridLayout.addWidget(self.swWarehouse, 4, 1, 1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.sbAgency = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.sbAgency.setMinimumSize(QtCore.QSize(157, 0))
        self.sbAgency.setMaximum(999999999.0)
        self.sbAgency.setObjectName("sbAgency")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.sbAgency)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.sbStore = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.sbStore.setMinimumSize(QtCore.QSize(157, 0))
        self.sbStore.setMaximum(999999999.0)
        self.sbStore.setObjectName("sbStore")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbStore)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.sbPaperWork = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.sbPaperWork.setMinimumSize(QtCore.QSize(157, 0))
        self.sbPaperWork.setMaximum(100.0)
        self.sbPaperWork.setObjectName("sbPaperWork")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.sbPaperWork)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.sbTransportation = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.sbTransportation.setMinimumSize(QtCore.QSize(157, 0))
        self.sbTransportation.setMaximum(100.0)
        self.sbTransportation.setObjectName("sbTransportation")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.sbTransportation)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 2)
        self.ckISO = QtGui.QCheckBox(self.groupBox_3)
        self.ckISO.setEnabled(False)
        self.ckISO.setObjectName("ckISO")
        self.gridLayout_2.addWidget(self.ckISO, 1, 0, 1, 1)
        self.ckTaxes = QtGui.QCheckBox(self.groupBox_3)
        self.ckTaxes.setEnabled(False)
        self.ckTaxes.setObjectName("ckTaxes")
        self.gridLayout_2.addWidget(self.ckTaxes, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.tabdetails)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.formLayout.setObjectName("formLayout")
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_15)
        self.sbWeight = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sbWeight.setMinimumSize(QtCore.QSize(157, 0))
        self.sbWeight.setMaximum(999999999.0)
        self.sbWeight.setObjectName("sbWeight")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sbWeight)
        self.sbFreight = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sbFreight.setMinimumSize(QtCore.QSize(157, 0))
        self.sbFreight.setMaximum(999999999.0)
        self.sbFreight.setObjectName("sbFreight")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbFreight)
        self.sbInsurance = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sbInsurance.setMinimumSize(QtCore.QSize(157, 0))
        self.sbInsurance.setMaximum(999999999.0)
        self.sbInsurance.setObjectName("sbInsurance")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sbInsurance)
        self.sbOther = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.sbOther.setMinimumSize(QtCore.QSize(157, 0))
        self.sbOther.setMaximum(999999999.0)
        self.sbOther.setObjectName("sbOther")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sbOther)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.tabledetails = OrderedEditTable(self.tabdetails)
        self.tabledetails.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setAlternatingRowColors(True)
        self.tabledetails.setObjectName("tabledetails")
        self.tabledetails.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tabledetails)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabdetails, icon, "")
        self.tabnavigation = QtGui.QWidget()
        self.tabnavigation.setObjectName("tabnavigation")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabnavigation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablenavigation = QtGui.QTableView(self.tabnavigation)
        self.tablenavigation.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablenavigation.setAlternatingRowColors(True)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setObjectName("tablenavigation")
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.tablenavigation.verticalHeader().setVisible(False)
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
        FrmLiquidacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FrmLiquidacion)
        self.statusbar.setObjectName("statusbar")
        FrmLiquidacion.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(FrmLiquidacion)
        self.toolBar.setObjectName("toolBar")
        FrmLiquidacion.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.xdockWidget = QtGui.QDockWidget(FrmLiquidacion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xdockWidget.sizePolicy().hasHeightForWidth())
        self.xdockWidget.setSizePolicy(sizePolicy)
        self.xdockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.xdockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.xdockWidget.setObjectName("xdockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabTotalsAccounts = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabTotalsAccounts.setMinimumSize(QtCore.QSize(0, 200))
        self.tabTotalsAccounts.setObjectName("tabTotalsAccounts")
        self.tabaccounts = QtGui.QWidget()
        self.tabaccounts.setObjectName("tabaccounts")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tabaccounts)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableaccounts = QtGui.QTableView(self.tabaccounts)
        self.tableaccounts.setAlternatingRowColors(True)
        self.tableaccounts.setObjectName("tableaccounts")
        self.tableaccounts.horizontalHeader().setStretchLastSection(True)
        self.tableaccounts.verticalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.tableaccounts)
        self.tabTotalsAccounts.addTab(self.tabaccounts, "")
        self.tabtotals = QtGui.QWidget()
        self.tabtotals.setObjectName("tabtotals")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabtotals)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabletotals = QtGui.QTableView(self.tabtotals)
        self.tabletotals.setObjectName("tabletotals")
        self.tabletotals.horizontalHeader().setStretchLastSection(True)
        self.tabletotals.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tabletotals)
        self.tabTotalsAccounts.addTab(self.tabtotals, "")
        self.verticalLayout_3.addWidget(self.tabTotalsAccounts)
        self.xdockWidget.setWidget(self.dockWidgetContents)
        FrmLiquidacion.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.xdockWidget)
        self.label_2.setBuddy(self.txtPolicy)
        self.label_4.setBuddy(self.dtPicker)
        self.label_10.setBuddy(self.txtExchangeRate)
        self.label_11.setBuddy(self.txtSource)
        self.label_6.setBuddy(self.sbAgency)
        self.label_7.setBuddy(self.sbStore)
        self.label_8.setBuddy(self.sbPaperWork)
        self.label_9.setBuddy(self.sbTransportation)
        self.label_12.setBuddy(self.sbWeight)
        self.label_13.setBuddy(self.sbFreight)
        self.label_14.setBuddy(self.sbInsurance)
        self.label_15.setBuddy(self.sbOther)
        self.label.setBuddy(self.txtSearch)

        self.retranslateUi(FrmLiquidacion)
        self.tabWidget.setCurrentIndex(1)
        self.swProvider.setCurrentIndex(0)
        self.swWarehouse.setCurrentIndex(1)
        self.tabTotalsAccounts.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FrmLiquidacion)
        FrmLiquidacion.setTabOrder(self.txtPolicy, self.cbProvider)
        FrmLiquidacion.setTabOrder(self.cbProvider, self.dtPicker)
        FrmLiquidacion.setTabOrder(self.dtPicker, self.txtSource)
        FrmLiquidacion.setTabOrder(self.txtSource, self.cbWarehouse)
        FrmLiquidacion.setTabOrder(self.cbWarehouse, self.sbAgency)
        FrmLiquidacion.setTabOrder(self.sbAgency, self.sbStore)
        FrmLiquidacion.setTabOrder(self.sbStore, self.sbPaperWork)
        FrmLiquidacion.setTabOrder(self.sbPaperWork, self.sbTransportation)
        FrmLiquidacion.setTabOrder(self.sbTransportation, self.ckISO)
        FrmLiquidacion.setTabOrder(self.ckISO, self.ckTaxes)
        FrmLiquidacion.setTabOrder(self.ckTaxes, self.sbWeight)
        FrmLiquidacion.setTabOrder(self.sbWeight, self.sbFreight)
        FrmLiquidacion.setTabOrder(self.sbFreight, self.sbInsurance)
        FrmLiquidacion.setTabOrder(self.sbInsurance, self.sbOther)
        FrmLiquidacion.setTabOrder(self.sbOther, self.tabledetails)
        FrmLiquidacion.setTabOrder(self.tabledetails, self.tabletotals)
        FrmLiquidacion.setTabOrder(self.tabletotals, self.tableaccounts)
        FrmLiquidacion.setTabOrder(self.tableaccounts, self.txtProvider)
        FrmLiquidacion.setTabOrder(self.txtProvider, self.txtWarehouse)
        FrmLiquidacion.setTabOrder(self.txtWarehouse, self.txtExchangeRate)
        FrmLiquidacion.setTabOrder(self.txtExchangeRate, self.tablenavigation)
        FrmLiquidacion.setTabOrder(self.tablenavigation, self.txtSearch)
        FrmLiquidacion.setTabOrder(self.txtSearch, self.tabTotalsAccounts)
        FrmLiquidacion.setTabOrder(self.tabTotalsAccounts, self.tabWidget)

    def retranslateUi(self, FrmLiquidacion):
        FrmLiquidacion.setWindowTitle(QtGui.QApplication.translate("FrmLiquidacion", "Liquidación", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("FrmLiquidacion", "Datos de declaración", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FrmLiquidacion", "No. Poliza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FrmLiquidacion", "Proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FrmLiquidacion", "Fecha Poliza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("FrmLiquidacion", "TC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("FrmLiquidacion", "Procedencia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FrmLiquidacion", "Bodega", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FrmLiquidacion", "Agencia", None, QtGui.QApplication.UnicodeUTF8))
        self.sbAgency.setPrefix(QtGui.QApplication.translate("FrmLiquidacion", "C$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FrmLiquidacion", "Almacen", None, QtGui.QApplication.UnicodeUTF8))
        self.sbStore.setPrefix(QtGui.QApplication.translate("FrmLiquidacion", "C$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FrmLiquidacion", "Papeleria", None, QtGui.QApplication.UnicodeUTF8))
        self.sbPaperWork.setSuffix(QtGui.QApplication.translate("FrmLiquidacion", " %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("FrmLiquidacion", "Transporte", None, QtGui.QApplication.UnicodeUTF8))
        self.sbTransportation.setSuffix(QtGui.QApplication.translate("FrmLiquidacion", " %", None, QtGui.QApplication.UnicodeUTF8))
        self.ckISO.setText(QtGui.QApplication.translate("FrmLiquidacion", "Aplicar ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.ckTaxes.setText(QtGui.QApplication.translate("FrmLiquidacion", "Exonerar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FrmLiquidacion", "Totales de declaración", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("FrmLiquidacion", "Peso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("FrmLiquidacion", "Flete ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("FrmLiquidacion", "Seguro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("FrmLiquidacion", "Otros Gastos", None, QtGui.QApplication.UnicodeUTF8))
        self.sbWeight.setSuffix(QtGui.QApplication.translate("FrmLiquidacion", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.sbFreight.setPrefix(QtGui.QApplication.translate("FrmLiquidacion", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.sbInsurance.setPrefix(QtGui.QApplication.translate("FrmLiquidacion", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.sbOther.setPrefix(QtGui.QApplication.translate("FrmLiquidacion", "US$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), "")
        self.label.setText(QtGui.QApplication.translate("FrmLiquidacion", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation), "")
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("FrmLiquidacion", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.xdockWidget.setWindowTitle(QtGui.QApplication.translate("FrmLiquidacion", "Detalles", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTotalsAccounts.setTabText(self.tabTotalsAccounts.indexOf(self.tabaccounts), QtGui.QApplication.translate("FrmLiquidacion", "Movimientos Contables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTotalsAccounts.setTabText(self.tabTotalsAccounts.indexOf(self.tabtotals), QtGui.QApplication.translate("FrmLiquidacion", "Totales", None, QtGui.QApplication.UnicodeUTF8))

from utility.widgets import OrderedEditTable
import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmLiquidacion = QtGui.QMainWindow()
    ui = Ui_FrmLiquidacion()
    ui.setupUi(FrmLiquidacion)
    FrmLiquidacion.show()
    sys.exit(app.exec_())

