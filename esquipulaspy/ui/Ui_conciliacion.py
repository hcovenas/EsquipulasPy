# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\EsquipulasPy\esquipulaspy\ui\conciliacion.ui'
#
# Created: Sun May 08 18:49:35 2011
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmConciliacion(object):
    def setupUi(self, frmConciliacion):
        frmConciliacion.setObjectName(_fromUtf8("frmConciliacion"))
        frmConciliacion.resize(723, 545)
        frmConciliacion.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(frmConciliacion)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabdetails = QtGui.QWidget()
        self.tabdetails.setObjectName(_fromUtf8("tabdetails"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabdetails)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.splitter_2 = QtGui.QSplitter(self.tabdetails)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.groupBox = QtGui.QGroupBox(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lblfecha = QtGui.QLabel(self.groupBox)
        self.lblfecha.setMinimumSize(QtCore.QSize(0, 15))
        self.lblfecha.setText(_fromUtf8(""))
        self.lblfecha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblfecha.setObjectName(_fromUtf8("lblfecha"))
        self.verticalLayout_7.addWidget(self.lblfecha)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtbanco = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtbanco.sizePolicy().hasHeightForWidth())
        self.txtbanco.setSizePolicy(sizePolicy)
        self.txtbanco.setReadOnly(True)
        self.txtbanco.setObjectName(_fromUtf8("txtbanco"))
        self.gridLayout.addWidget(self.txtbanco, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.txtcuentabanco = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtcuentabanco.sizePolicy().hasHeightForWidth())
        self.txtcuentabanco.setSizePolicy(sizePolicy)
        self.txtcuentabanco.setReadOnly(True)
        self.txtcuentabanco.setObjectName(_fromUtf8("txtcuentabanco"))
        self.gridLayout.addWidget(self.txtcuentabanco, 0, 5, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.txtmoneda = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtmoneda.sizePolicy().hasHeightForWidth())
        self.txtmoneda.setSizePolicy(sizePolicy)
        self.txtmoneda.setReadOnly(True)
        self.txtmoneda.setObjectName(_fromUtf8("txtmoneda"))
        self.gridLayout.addWidget(self.txtmoneda, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)
        self.txtcuenta = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtcuenta.sizePolicy().hasHeightForWidth())
        self.txtcuenta.setSizePolicy(sizePolicy)
        self.txtcuenta.setReadOnly(True)
        self.txtcuenta.setObjectName(_fromUtf8("txtcuenta"))
        self.gridLayout.addWidget(self.txtcuenta, 0, 7, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.tabledetails = QtGui.QTableView(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabledetails.sizePolicy().hasHeightForWidth())
        self.tabledetails.setSizePolicy(sizePolicy)
        self.tabledetails.setMinimumSize(QtCore.QSize(200, 70))
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setObjectName(_fromUtf8("tabledetails"))
        self.horizontalLayout_11.addWidget(self.tabledetails)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnAdd = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setMaximumSize(QtCore.QSize(22, 16777215))
        self.btnAdd.setStyleSheet(_fromUtf8(""))
        self.btnAdd.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_3.addWidget(self.btnAdd)
        self.btnRemove = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemove.sizePolicy().hasHeightForWidth())
        self.btnRemove.setSizePolicy(sizePolicy)
        self.btnRemove.setMaximumSize(QtCore.QSize(22, 16777215))
        self.btnRemove.setStyleSheet(_fromUtf8(""))
        self.btnRemove.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon1)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.verticalLayout_3.addWidget(self.btnRemove)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 240))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.spbsaldobanco = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spbsaldobanco.sizePolicy().hasHeightForWidth())
        self.spbsaldobanco.setSizePolicy(sizePolicy)
        self.spbsaldobanco.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spbsaldobanco.setMinimum(-1000000000.0)
        self.spbsaldobanco.setMaximum(1000000000.0)
        self.spbsaldobanco.setProperty(_fromUtf8("value"), 0.0)
        self.spbsaldobanco.setObjectName(_fromUtf8("spbsaldobanco"))
        self.horizontalLayout_2.addWidget(self.spbsaldobanco)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lbltotallibro_2 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotallibro_2.sizePolicy().hasHeightForWidth())
        self.lbltotallibro_2.setSizePolicy(sizePolicy)
        self.lbltotallibro_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltotallibro_2.setObjectName(_fromUtf8("lbltotallibro_2"))
        self.horizontalLayout_5.addWidget(self.lbltotallibro_2)
        self.txtdeposito = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtdeposito.sizePolicy().hasHeightForWidth())
        self.txtdeposito.setSizePolicy(sizePolicy)
        self.txtdeposito.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtdeposito.setReadOnly(True)
        self.txtdeposito.setObjectName(_fromUtf8("txtdeposito"))
        self.horizontalLayout_5.addWidget(self.txtdeposito)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.tablalibromas = QtGui.QTableView(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablalibromas.sizePolicy().hasHeightForWidth())
        self.tablalibromas.setSizePolicy(sizePolicy)
        self.tablalibromas.setMinimumSize(QtCore.QSize(0, 50))
        self.tablalibromas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablalibromas.setObjectName(_fromUtf8("tablalibromas"))
        self.verticalLayout_4.addWidget(self.tablalibromas)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lbltotallibro_3 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotallibro_3.sizePolicy().hasHeightForWidth())
        self.lbltotallibro_3.setSizePolicy(sizePolicy)
        self.lbltotallibro_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltotallibro_3.setObjectName(_fromUtf8("lbltotallibro_3"))
        self.horizontalLayout_7.addWidget(self.lbltotallibro_3)
        self.txtcheque = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtcheque.sizePolicy().hasHeightForWidth())
        self.txtcheque.setSizePolicy(sizePolicy)
        self.txtcheque.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtcheque.setReadOnly(True)
        self.txtcheque.setObjectName(_fromUtf8("txtcheque"))
        self.horizontalLayout_7.addWidget(self.txtcheque)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.tablalibromenos = QtGui.QTableView(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablalibromenos.sizePolicy().hasHeightForWidth())
        self.tablalibromenos.setSizePolicy(sizePolicy)
        self.tablalibromenos.setMinimumSize(QtCore.QSize(0, 50))
        self.tablalibromenos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablalibromenos.setObjectName(_fromUtf8("tablalibromenos"))
        self.verticalLayout_4.addWidget(self.tablalibromenos)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lbltotallibro = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotallibro.sizePolicy().hasHeightForWidth())
        self.lbltotallibro.setSizePolicy(sizePolicy)
        self.lbltotallibro.setMinimumSize(QtCore.QSize(0, 8))
        self.lbltotallibro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotallibro.setObjectName(_fromUtf8("lbltotallibro"))
        self.horizontalLayout_10.addWidget(self.lbltotallibro)
        self.txttotallibro = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txttotallibro.sizePolicy().hasHeightForWidth())
        self.txttotallibro.setSizePolicy(sizePolicy)
        self.txttotallibro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txttotallibro.setReadOnly(True)
        self.txttotallibro.setObjectName(_fromUtf8("txttotallibro"))
        self.horizontalLayout_10.addWidget(self.txttotallibro)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.groupBox_3 = QtGui.QGroupBox(self.splitter)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 240))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.txtsaldolibro = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtsaldolibro.sizePolicy().hasHeightForWidth())
        self.txtsaldolibro.setSizePolicy(sizePolicy)
        self.txtsaldolibro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtsaldolibro.setReadOnly(True)
        self.txtsaldolibro.setObjectName(_fromUtf8("txtsaldolibro"))
        self.horizontalLayout_3.addWidget(self.txtsaldolibro)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lbltotallibro_4 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotallibro_4.sizePolicy().hasHeightForWidth())
        self.lbltotallibro_4.setSizePolicy(sizePolicy)
        self.lbltotallibro_4.setMinimumSize(QtCore.QSize(0, 8))
        self.lbltotallibro_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltotallibro_4.setObjectName(_fromUtf8("lbltotallibro_4"))
        self.horizontalLayout_6.addWidget(self.lbltotallibro_4)
        self.txtnotacredito = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtnotacredito.sizePolicy().hasHeightForWidth())
        self.txtnotacredito.setSizePolicy(sizePolicy)
        self.txtnotacredito.setMinimumSize(QtCore.QSize(0, 0))
        self.txtnotacredito.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtnotacredito.setReadOnly(True)
        self.txtnotacredito.setObjectName(_fromUtf8("txtnotacredito"))
        self.horizontalLayout_6.addWidget(self.txtnotacredito)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tablabancomas = QtGui.QTableView(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablabancomas.sizePolicy().hasHeightForWidth())
        self.tablabancomas.setSizePolicy(sizePolicy)
        self.tablabancomas.setMinimumSize(QtCore.QSize(0, 50))
        self.tablabancomas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablabancomas.setObjectName(_fromUtf8("tablabancomas"))
        self.verticalLayout_5.addWidget(self.tablabancomas)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.lbltotallibro_5 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotallibro_5.sizePolicy().hasHeightForWidth())
        self.lbltotallibro_5.setSizePolicy(sizePolicy)
        self.lbltotallibro_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbltotallibro_5.setObjectName(_fromUtf8("lbltotallibro_5"))
        self.horizontalLayout_8.addWidget(self.lbltotallibro_5)
        self.txtnotadebito = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtnotadebito.sizePolicy().hasHeightForWidth())
        self.txtnotadebito.setSizePolicy(sizePolicy)
        self.txtnotadebito.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtnotadebito.setReadOnly(True)
        self.txtnotadebito.setObjectName(_fromUtf8("txtnotadebito"))
        self.horizontalLayout_8.addWidget(self.txtnotadebito)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.tablabancomenos = QtGui.QTableView(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablabancomenos.sizePolicy().hasHeightForWidth())
        self.tablabancomenos.setSizePolicy(sizePolicy)
        self.tablabancomenos.setMinimumSize(QtCore.QSize(0, 50))
        self.tablabancomenos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablabancomenos.setObjectName(_fromUtf8("tablabancomenos"))
        self.verticalLayout_5.addWidget(self.tablabancomenos)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lbltotalbanco = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotalbanco.sizePolicy().hasHeightForWidth())
        self.lbltotalbanco.setSizePolicy(sizePolicy)
        self.lbltotalbanco.setMinimumSize(QtCore.QSize(0, 8))
        self.lbltotalbanco.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotalbanco.setObjectName(_fromUtf8("lbltotalbanco"))
        self.horizontalLayout_9.addWidget(self.lbltotalbanco)
        self.txttotalbanco = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txttotalbanco.sizePolicy().hasHeightForWidth())
        self.txttotalbanco.setSizePolicy(sizePolicy)
        self.txttotalbanco.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txttotalbanco.setReadOnly(True)
        self.txttotalbanco.setObjectName(_fromUtf8("txttotalbanco"))
        self.horizontalLayout_9.addWidget(self.txttotalbanco)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.lbldiferencia = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbldiferencia.sizePolicy().hasHeightForWidth())
        self.lbldiferencia.setSizePolicy(sizePolicy)
        self.lbldiferencia.setMinimumSize(QtCore.QSize(0, 10))
        self.lbldiferencia.setAlignment(QtCore.Qt.AlignCenter)
        self.lbldiferencia.setObjectName(_fromUtf8("lbldiferencia"))
        self.verticalLayout_6.addWidget(self.lbldiferencia)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabdetails, icon2, _fromUtf8(""))
        self.tabnavigation = QtGui.QWidget()
        self.tabnavigation.setObjectName(_fromUtf8("tabnavigation"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabnavigation)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tablenavigation = QtGui.QTableView(self.tabnavigation)
        self.tablenavigation.setAlternatingRowColors(True)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setObjectName(_fromUtf8("tablenavigation"))
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.tablenavigation.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.tabnavigation)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.txtSearch = QtGui.QLineEdit(self.tabnavigation)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.horizontalLayout.addWidget(self.txtSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabnavigation, icon3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        frmConciliacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(frmConciliacion)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        frmConciliacion.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(frmConciliacion)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        frmConciliacion.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.label_4.setBuddy(self.txtSearch)

        self.retranslateUi(frmConciliacion)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmConciliacion)
        frmConciliacion.setTabOrder(self.tablenavigation, self.txtSearch)

    def retranslateUi(self, frmConciliacion):
        frmConciliacion.setWindowTitle(QtGui.QApplication.translate("frmConciliacion", "Conciliacion Bancaria", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmConciliacion", "Libro Mayor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmConciliacion", "Banco", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmConciliacion", "Cuenta Bancaria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmConciliacion", "Moneda", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmConciliacion", "Cuenta Contable", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setToolTip(QtGui.QApplication.translate("frmConciliacion", "Agregar notas de crédito o débito", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setShortcut(QtGui.QApplication.translate("frmConciliacion", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmConciliacion", "Libro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmConciliacion", "Saldo del banco", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotallibro_2.setText(QtGui.QApplication.translate("frmConciliacion", "MÁS: DEPOSITOS EN TRANSITO", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotallibro_3.setText(QtGui.QApplication.translate("frmConciliacion", "MENOS: CHEQUES EN TRANSITO", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotallibro.setText(QtGui.QApplication.translate("frmConciliacion", "Total Disponible:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("frmConciliacion", "Banco", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("frmConciliacion", "Saldo del auxiliar de la empresa", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotallibro_4.setText(QtGui.QApplication.translate("frmConciliacion", "MÁS: NOTAS DE CREDITO", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotallibro_5.setText(QtGui.QApplication.translate("frmConciliacion", "MENOS: NOTAS DE DEBITO", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotalbanco.setText(QtGui.QApplication.translate("frmConciliacion", "Total Disponible:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbldiferencia.setText(QtGui.QApplication.translate("frmConciliacion", "Diferencia C$ 0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), "")
        self.label_4.setText(QtGui.QApplication.translate("frmConciliacion", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation),"" )
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmConciliacion", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
