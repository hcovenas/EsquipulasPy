# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\EsquipulasPy\src\ui\apertura.ui'
#
# Created: Thu Aug 19 16:27:08 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgApertura(object):
    def setupUi(self, dlgApertura):
        dlgApertura.setObjectName("dlgApertura")
        dlgApertura.setWindowModality(QtCore.Qt.ApplicationModal)
        dlgApertura.resize(346, 276)
        dlgApertura.setMaximumSize(QtCore.QSize(16777215, 276))
        self.verticalLayout = QtGui.QVBoxLayout(dlgApertura)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(dlgApertura)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtUsuario = QtGui.QLineEdit(dlgApertura)
        self.txtUsuario.setReadOnly(False)
        self.txtUsuario.setObjectName("txtUsuario")
        self.gridLayout.addWidget(self.txtUsuario, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(dlgApertura)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.dtFechaTime = QtGui.QDateTimeEdit(dlgApertura)
        self.dtFechaTime.setCalendarPopup(True)
        self.dtFechaTime.setObjectName("dtFechaTime")
        self.gridLayout.addWidget(self.dtFechaTime, 1, 1, 1, 1)
        self.label = QtGui.QLabel(dlgApertura)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.swcaja = QtGui.QStackedWidget(dlgApertura)
        self.swcaja.setMaximumSize(QtCore.QSize(16777215, 200))
        self.swcaja.setObjectName("swcaja")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbcaja = QtGui.QComboBox(self.page)
        self.cbcaja.setObjectName("cbcaja")
        self.horizontalLayout.addWidget(self.cbcaja)
        self.swcaja.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtcaja = QtGui.QLineEdit(self.page_2)
        self.txtcaja.setReadOnly(False)
        self.txtcaja.setObjectName("txtcaja")
        self.horizontalLayout_2.addWidget(self.txtcaja)
        self.swcaja.addWidget(self.page_2)
        self.gridLayout.addWidget(self.swcaja, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(dlgApertura)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.txtSaldoC = QtGui.QDoubleSpinBox(dlgApertura)
        self.txtSaldoC.setDecimals(4)
        self.txtSaldoC.setMaximum(1000000000.0)
        self.txtSaldoC.setObjectName("txtSaldoC")
        self.gridLayout.addWidget(self.txtSaldoC, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(dlgApertura)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.txtSaldoD = QtGui.QDoubleSpinBox(dlgApertura)
        self.txtSaldoD.setDecimals(4)
        self.txtSaldoD.setMaximum(1000000000.0)
        self.txtSaldoD.setObjectName("txtSaldoD")
        self.gridLayout.addWidget(self.txtSaldoD, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(dlgApertura)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.txtUser = QtGui.QLineEdit(self.groupBox)
        self.txtUser.setReadOnly(False)
        self.txtUser.setObjectName("txtUser")
        self.gridLayout_2.addWidget(self.txtUser, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.groupBox)
        self.txtPassword.setReadOnly(False)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout_2.addWidget(self.txtPassword, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(dlgApertura)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dlgApertura)
        self.swcaja.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgApertura.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgApertura.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgApertura)
        dlgApertura.setTabOrder(self.cbcaja, self.txtSaldoC)
        dlgApertura.setTabOrder(self.txtSaldoC, self.txtSaldoD)
        dlgApertura.setTabOrder(self.txtSaldoD, self.txtUser)
        dlgApertura.setTabOrder(self.txtUser, self.txtPassword)
        dlgApertura.setTabOrder(self.txtPassword, self.buttonBox)
        dlgApertura.setTabOrder(self.buttonBox, self.dtFechaTime)
        dlgApertura.setTabOrder(self.dtFechaTime, self.txtUsuario)
        dlgApertura.setTabOrder(self.txtUsuario, self.txtcaja)

    def retranslateUi(self, dlgApertura):
        dlgApertura.setWindowTitle(QtGui.QApplication.translate("dlgApertura", "Apertura de Caja", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dlgApertura", "Cajero:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlgApertura", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgApertura", "Caja", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlgApertura", "Monto C$", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlgApertura", "Monto US$", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("dlgApertura", "Autorizacion Por:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dlgApertura", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dlgApertura", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))

