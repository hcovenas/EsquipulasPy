# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/liquidacion.ui'
#
# Created: Sat Aug  7 13:56:20 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmLiquidacion(object):
    def setupUi(self, frmLiquidacion):
        frmLiquidacion.setObjectName("frmLiquidacion")
        frmLiquidacion.resize(879, 592)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmLiquidacion.sizePolicy().hasHeightForWidth())
        frmLiquidacion.setSizePolicy(sizePolicy)
        frmLiquidacion.setMinimumSize(QtCore.QSize(879, 0))
        frmLiquidacion.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(frmLiquidacion)
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
        self.groupBox_3.setMinimumSize(QtCore.QSize(550, 0))
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
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtAgency = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAgency.sizePolicy().hasHeightForWidth())
        self.txtAgency.setSizePolicy(sizePolicy)
        self.txtAgency.setReadOnly(True)
        self.txtAgency.setObjectName("txtAgency")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtAgency)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtStore = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtStore.sizePolicy().hasHeightForWidth())
        self.txtStore.setSizePolicy(sizePolicy)
        self.txtStore.setReadOnly(True)
        self.txtStore.setObjectName("txtStore")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtStore)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.txtPaperWork = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPaperWork.sizePolicy().hasHeightForWidth())
        self.txtPaperWork.setSizePolicy(sizePolicy)
        self.txtPaperWork.setReadOnly(True)
        self.txtPaperWork.setObjectName("txtPaperWork")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtPaperWork)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.txtTransportation = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTransportation.sizePolicy().hasHeightForWidth())
        self.txtTransportation.setSizePolicy(sizePolicy)
        self.txtTransportation.setReadOnly(True)
        self.txtTransportation.setObjectName("txtTransportation")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtTransportation)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.ckISO = QtGui.QCheckBox(self.groupBox_3)
        self.ckISO.setEnabled(False)
        self.ckISO.setObjectName("ckISO")
        self.verticalLayout_4.addWidget(self.ckISO)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.tabdetails)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(276, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.txtWeight = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtWeight.sizePolicy().hasHeightForWidth())
        self.txtWeight.setSizePolicy(sizePolicy)
        self.txtWeight.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtWeight.setReadOnly(True)
        self.txtWeight.setObjectName("txtWeight")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtWeight)
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_13)
        self.txtFreight = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFreight.sizePolicy().hasHeightForWidth())
        self.txtFreight.setSizePolicy(sizePolicy)
        self.txtFreight.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtFreight.setReadOnly(True)
        self.txtFreight.setObjectName("txtFreight")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtFreight)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.txtInsurance = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInsurance.sizePolicy().hasHeightForWidth())
        self.txtInsurance.setSizePolicy(sizePolicy)
        self.txtInsurance.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtInsurance.setReadOnly(True)
        self.txtInsurance.setObjectName("txtInsurance")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtInsurance)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_15)
        self.txtOther = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOther.sizePolicy().hasHeightForWidth())
        self.txtOther.setSizePolicy(sizePolicy)
        self.txtOther.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtOther.setReadOnly(True)
        self.txtOther.setObjectName("txtOther")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtOther)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.tabledetails = QtGui.QTableView(self.tabdetails)
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
        frmLiquidacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(frmLiquidacion)
        self.statusbar.setObjectName("statusbar")
        frmLiquidacion.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(frmLiquidacion)
        self.toolBar.setObjectName("toolBar")
        frmLiquidacion.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.xdockWidget = XDockWidget(frmLiquidacion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xdockWidget.sizePolicy().hasHeightForWidth())
        self.xdockWidget.setSizePolicy(sizePolicy)
        self.xdockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.xdockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.xdockWidget.setObjectName("xdockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_2 = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget_2.setObjectName("tabWidget_2")
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
        self.tabWidget_2.addTab(self.tabaccounts, "")
        self.tabtotals = QtGui.QWidget()
        self.tabtotals.setObjectName("tabtotals")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabtotals)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabletotals = QtGui.QTableView(self.tabtotals)
        self.tabletotals.setObjectName("tabletotals")
        self.tabletotals.horizontalHeader().setStretchLastSection(True)
        self.tabletotals.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tabletotals)
        self.tabWidget_2.addTab(self.tabtotals, "")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.xdockWidget.setWidget(self.dockWidgetContents)
        frmLiquidacion.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.xdockWidget)
        self.actionNew = QtGui.QAction(frmLiquidacion)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/res/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionPreview = QtGui.QAction(frmLiquidacion)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/res/document-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreview.setIcon(icon3)
        self.actionPreview.setObjectName("actionPreview")
        self.actionGoFirst = QtGui.QAction(frmLiquidacion)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/res/go-first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoFirst.setIcon(icon4)
        self.actionGoFirst.setObjectName("actionGoFirst")
        self.actionGoPrevious = QtGui.QAction(frmLiquidacion)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/res/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoPrevious.setIcon(icon5)
        self.actionGoPrevious.setObjectName("actionGoPrevious")
        self.actionGoNext = QtGui.QAction(frmLiquidacion)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/res/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoNext.setIcon(icon6)
        self.actionGoNext.setObjectName("actionGoNext")
        self.actionGoLast = QtGui.QAction(frmLiquidacion)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/res/go-last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoLast.setIcon(icon7)
        self.actionGoLast.setObjectName("actionGoLast")
        self.actionSave = QtGui.QAction(frmLiquidacion)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/res/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon8)
        self.actionSave.setVisible(False)
        self.actionSave.setObjectName("actionSave")
        self.actionCancel = QtGui.QAction(frmLiquidacion)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/res/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCancel.setIcon(icon9)
        self.actionCancel.setVisible(False)
        self.actionCancel.setObjectName("actionCancel")
        self.actionEditar = QtGui.QAction(frmLiquidacion)
        self.actionEditar.setIcon(icon)
        self.actionEditar.setObjectName("actionEditar")
        self.actionDeleteRow = QtGui.QAction(frmLiquidacion)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/res/edit-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteRow.setIcon(icon10)
        self.actionDeleteRow.setObjectName("actionDeleteRow")
        self.actionCopy = QtGui.QAction(frmLiquidacion)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/res/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon11)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtGui.QAction(frmLiquidacion)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/res/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon12)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtGui.QAction(frmLiquidacion)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/res/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon13)
        self.actionPaste.setObjectName("actionPaste")
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionCancel)
        self.toolBar.addAction(self.actionPreview)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGoFirst)
        self.toolBar.addAction(self.actionGoPrevious)
        self.toolBar.addAction(self.actionGoNext)
        self.toolBar.addAction(self.actionGoLast)
        self.label_2.setBuddy(self.txtPolicy)
        self.label_4.setBuddy(self.dtPicker)
        self.label_10.setBuddy(self.txtExchangeRate)
        self.label_11.setBuddy(self.txtSource)
        self.label_6.setBuddy(self.txtAgency)
        self.label_7.setBuddy(self.txtStore)
        self.label_8.setBuddy(self.txtPaperWork)
        self.label_9.setBuddy(self.txtTransportation)
        self.label_12.setBuddy(self.txtWeight)
        self.label_13.setBuddy(self.txtFreight)
        self.label_14.setBuddy(self.txtInsurance)
        self.label_15.setBuddy(self.txtOther)
        self.label.setBuddy(self.txtSearch)

        self.retranslateUi(frmLiquidacion)
        self.tabWidget.setCurrentIndex(1)
        self.swProvider.setCurrentIndex(0)
        self.swWarehouse.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmLiquidacion)
        frmLiquidacion.setTabOrder(self.txtPolicy, self.cbProvider)
        frmLiquidacion.setTabOrder(self.cbProvider, self.dtPicker)
        frmLiquidacion.setTabOrder(self.dtPicker, self.txtSource)
        frmLiquidacion.setTabOrder(self.txtSource, self.cbWarehouse)
        frmLiquidacion.setTabOrder(self.cbWarehouse, self.ckISO)
        frmLiquidacion.setTabOrder(self.ckISO, self.txtAgency)
        frmLiquidacion.setTabOrder(self.txtAgency, self.txtStore)
        frmLiquidacion.setTabOrder(self.txtStore, self.txtPaperWork)
        frmLiquidacion.setTabOrder(self.txtPaperWork, self.txtTransportation)
        frmLiquidacion.setTabOrder(self.txtTransportation, self.txtWeight)
        frmLiquidacion.setTabOrder(self.txtWeight, self.txtFreight)
        frmLiquidacion.setTabOrder(self.txtFreight, self.txtInsurance)
        frmLiquidacion.setTabOrder(self.txtInsurance, self.txtOther)
        frmLiquidacion.setTabOrder(self.txtOther, self.tabledetails)
        frmLiquidacion.setTabOrder(self.tabledetails, self.tabWidget)
        frmLiquidacion.setTabOrder(self.tabWidget, self.txtProvider)
        frmLiquidacion.setTabOrder(self.txtProvider, self.txtWarehouse)
        frmLiquidacion.setTabOrder(self.txtWarehouse, self.txtExchangeRate)
        frmLiquidacion.setTabOrder(self.txtExchangeRate, self.tablenavigation)
        frmLiquidacion.setTabOrder(self.tablenavigation, self.txtSearch)
        frmLiquidacion.setTabOrder(self.txtSearch, self.tabWidget_2)
        frmLiquidacion.setTabOrder(self.tabWidget_2, self.tableaccounts)
        frmLiquidacion.setTabOrder(self.tableaccounts, self.tabletotals)

    def retranslateUi(self, frmLiquidacion):
        frmLiquidacion.setWindowTitle(QtGui.QApplication.translate("frmLiquidacion", "Liquidación", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("frmLiquidacion", "Datos de declaración", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmLiquidacion", "No. Poliza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmLiquidacion", "Proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmLiquidacion", "Fecha Poliza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("frmLiquidacion", "TC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("frmLiquidacion", "Procedencia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmLiquidacion", "Bodega", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmLiquidacion", "Agencia ( US$ )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("frmLiquidacion", "Almacen ( US$ )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("frmLiquidacion", "Papeleria ( % )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("frmLiquidacion", "Transporte ( % )", None, QtGui.QApplication.UnicodeUTF8))
        self.ckISO.setText(QtGui.QApplication.translate("frmLiquidacion", "Aplicar ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmLiquidacion", "Totales de declaración", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("frmLiquidacion", "Peso ( Kg )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("frmLiquidacion", "Flete ( US$ )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("frmLiquidacion", "Seguro ( US$ )", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("frmLiquidacion", "Otros Gastos ( US$ )", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), None)
        self.label.setText(QtGui.QApplication.translate("frmLiquidacion", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation), None)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmLiquidacion", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.xdockWidget.setWindowTitle(QtGui.QApplication.translate("frmLiquidacion", "Detalles", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabaccounts), QtGui.QApplication.translate("frmLiquidacion", "Movimientos Contables", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabtotals), QtGui.QApplication.translate("frmLiquidacion", "Totales", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("frmLiquidacion", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("frmLiquidacion", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setText(QtGui.QApplication.translate("frmLiquidacion", "Previsualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoFirst.setText(QtGui.QApplication.translate("frmLiquidacion", "Ir al Primer Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoPrevious.setText(QtGui.QApplication.translate("frmLiquidacion", "Ir al Registro Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoNext.setText(QtGui.QApplication.translate("frmLiquidacion", "Ir al siguiente registro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoLast.setText(QtGui.QApplication.translate("frmLiquidacion", "Ir al ultimo registro", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("frmLiquidacion", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCancel.setText(QtGui.QApplication.translate("frmLiquidacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar.setText(QtGui.QApplication.translate("frmLiquidacion", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar.setShortcut(QtGui.QApplication.translate("frmLiquidacion", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteRow.setText(QtGui.QApplication.translate("frmLiquidacion", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteRow.setShortcut(QtGui.QApplication.translate("frmLiquidacion", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("frmLiquidacion", "Copiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("frmLiquidacion", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("frmLiquidacion", "Cortar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("frmLiquidacion", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("frmLiquidacion", "Pegar", None, QtGui.QApplication.UnicodeUTF8))

from utility.widgets.xdockwidget import XDockWidget
import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmLiquidacion = QtGui.QMainWindow()
    ui = Ui_frmLiquidacion()
    ui.setupUi(frmLiquidacion)
    frmLiquidacion.show()
    sys.exit(app.exec_())

