# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\EsquipulasPy\esquipulaspy\ui\operations.ui'
#
# Created: Wed Nov 24 00:54:43 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmOperations(object):
    def setupUi(self, frmOperations):
        frmOperations.setObjectName(_fromUtf8("frmOperations"))
        frmOperations.resize(800, 600)
        self.centralwidget = QtGui.QWidget(frmOperations)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.txtSearch = QtGui.QLineEdit(self.centralwidget)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.gridLayout_2.addWidget(self.txtSearch, 1, 1, 1, 1)
        self.tableNavigation = QtGui.QTableView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableNavigation.sizePolicy().hasHeightForWidth())
        self.tableNavigation.setSizePolicy(sizePolicy)
        self.tableNavigation.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableNavigation.setAlternatingRowColors(True)
        self.tableNavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableNavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableNavigation.setObjectName(_fromUtf8("tableNavigation"))
        self.gridLayout_2.addWidget(self.tableNavigation, 2, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableDetails = QtGui.QTableView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableDetails.sizePolicy().hasHeightForWidth())
        self.tableDetails.setSizePolicy(sizePolicy)
        self.tableDetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableDetails.setAlternatingRowColors(True)
        self.tableDetails.setObjectName(_fromUtf8("tableDetails"))
        self.gridLayout.addWidget(self.tableDetails, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.dtPicker = QtGui.QDateTimeEdit(self.groupBox)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName(_fromUtf8("dtPicker"))
        self.gridLayout_3.addWidget(self.dtPicker, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.stConcepts = QtGui.QStackedWidget(self.groupBox)
        self.stConcepts.setObjectName(_fromUtf8("stConcepts"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtConcept = QtGui.QLineEdit(self.page_3)
        self.txtConcept.setReadOnly(True)
        self.txtConcept.setObjectName(_fromUtf8("txtConcept"))
        self.horizontalLayout.addWidget(self.txtConcept)
        self.stConcepts.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbConcepts = QtGui.QComboBox(self.page_4)
        self.cbConcepts.setEnabled(False)
        self.cbConcepts.setObjectName(_fromUtf8("cbConcepts"))
        self.horizontalLayout_2.addWidget(self.cbConcepts)
        self.stConcepts.addWidget(self.page_4)
        self.gridLayout_3.addWidget(self.stConcepts, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.buttonBox = QtGui.QDialogButtonBox(self.page)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnAdd = QtGui.QPushButton(self.page_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_3.addWidget(self.btnAdd)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        frmOperations.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(frmOperations)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        frmOperations.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.label.setBuddy(self.dtPicker)
        self.label_3.setBuddy(self.cbConcepts)
        self.label_4.setBuddy(self.txtSearch)

        self.retranslateUi(frmOperations)
        self.stConcepts.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmOperations)

    def retranslateUi(self, frmOperations):
        frmOperations.setWindowTitle(QtGui.QApplication.translate("frmOperations", "Ajustes Contables", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmOperations", "Detalles", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmOperations", "&Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmOperations", "Concepto", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("frmOperations", "Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setShortcut(QtGui.QApplication.translate("frmOperations", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmOperations", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmOperations", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
