# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\EsquipulasPy\src\ui\dlgmovimientosbancarios.ui'
#
# Created: Wed Jul 14 11:31:30 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgMovimientosBancarios(object):
    def setupUi(self, dlgMovimientosBancarios):
        dlgMovimientosBancarios.setObjectName("dlgMovimientosBancarios")
        dlgMovimientosBancarios.resize(529, 439)
        dlgMovimientosBancarios.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgMovimientosBancarios.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(dlgMovimientosBancarios)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtGui.QGridLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_27 = QtGui.QLabel(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27, 0, 0, 1, 1)
        self.swcuenta = QtGui.QStackedWidget(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swcuenta.sizePolicy().hasHeightForWidth())
        self.swcuenta.setSizePolicy(sizePolicy)
        self.swcuenta.setMinimumSize(QtCore.QSize(0, 40))
        self.swcuenta.setObjectName("swcuenta")
        self.page_17 = QtGui.QWidget()
        self.page_17.setObjectName("page_17")
        self.horizontalLayout_32 = QtGui.QHBoxLayout(self.page_17)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.swcuenta.addWidget(self.page_17)
        self.page_18 = QtGui.QWidget()
        self.page_18.setObjectName("page_18")
        self.horizontalLayout_33 = QtGui.QHBoxLayout(self.page_18)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.txtcuenta = QtGui.QLineEdit(self.page_18)
        self.txtcuenta.setAlignment(QtCore.Qt.AlignCenter)
        self.txtcuenta.setReadOnly(True)
        self.txtcuenta.setObjectName("txtcuenta")
        self.horizontalLayout_33.addWidget(self.txtcuenta)
        self.swcuenta.addWidget(self.page_18)
        self.horizontalLayout_4.addWidget(self.swcuenta, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_25 = QtGui.QLabel(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_31.addWidget(self.label_25)
        self.cbtipodoc = QtGui.QComboBox(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbtipodoc.sizePolicy().hasHeightForWidth())
        self.cbtipodoc.setSizePolicy(sizePolicy)
        self.cbtipodoc.setEditable(True)
        self.cbtipodoc.setObjectName("cbtipodoc")
        self.horizontalLayout_31.addWidget(self.cbtipodoc)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)
        self.label_26 = QtGui.QLabel(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_30.addWidget(self.label_26)
        self.dtPicker = QtGui.QDateTimeEdit(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtPicker.sizePolicy().hasHeightForWidth())
        self.dtPicker.setSizePolicy(sizePolicy)
        self.dtPicker.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dtPicker.setReadOnly(False)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.horizontalLayout_30.addWidget(self.dtPicker)
        self.verticalLayout.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_23 = QtGui.QLabel(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_28.addWidget(self.label_23)
        self.swconcepto = QtGui.QStackedWidget(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swconcepto.sizePolicy().hasHeightForWidth())
        self.swconcepto.setSizePolicy(sizePolicy)
        self.swconcepto.setMaximumSize(QtCore.QSize(16777215, 30))
        self.swconcepto.setObjectName("swconcepto")
        self.page_15 = QtGui.QWidget()
        self.page_15.setObjectName("page_15")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.page_15)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.cbconcepto = QtGui.QComboBox(self.page_15)
        self.cbconcepto.setMinimumSize(QtCore.QSize(0, 20))
        self.cbconcepto.setEditable(True)
        self.cbconcepto.setObjectName("cbconcepto")
        self.verticalLayout_12.addWidget(self.cbconcepto)
        self.swconcepto.addWidget(self.page_15)
        self.page_16 = QtGui.QWidget()
        self.page_16.setObjectName("page_16")
        self.horizontalLayout_29 = QtGui.QHBoxLayout(self.page_16)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.txtconcepto = QtGui.QLineEdit(self.page_16)
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
        self.horizontalLayout_29.addWidget(self.txtconcepto)
        self.swconcepto.addWidget(self.page_16)
        self.horizontalLayout_28.addWidget(self.swconcepto)
        self.verticalLayout.addLayout(self.horizontalLayout_28)
        self.label_22 = QtGui.QLabel(dlgMovimientosBancarios)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.splitter_4 = QtGui.QSplitter(dlgMovimientosBancarios)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.tabledetails = QtGui.QTableView(self.splitter_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabledetails.sizePolicy().hasHeightForWidth())
        self.tabledetails.setSizePolicy(sizePolicy)
        self.tabledetails.setMinimumSize(QtCore.QSize(300, 150))
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setObjectName("tabledetails")
        self.layoutWidget_17 = QtGui.QWidget(self.splitter_4)
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.layoutWidget_17)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_24 = QtGui.QLabel(self.layoutWidget_17)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_13.addWidget(self.label_24)
        self.txtobservaciones = QtGui.QTextEdit(self.layoutWidget_17)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtobservaciones.sizePolicy().hasHeightForWidth())
        self.txtobservaciones.setSizePolicy(sizePolicy)
        self.txtobservaciones.setMinimumSize(QtCore.QSize(0, 40))
        self.txtobservaciones.setObjectName("txtobservaciones")
        self.verticalLayout_13.addWidget(self.txtobservaciones)
        self.verticalLayout.addWidget(self.splitter_4)
        self.buttonBox = QtGui.QDialogButtonBox(dlgMovimientosBancarios)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_27.setBuddy(self.txtcuenta)
        self.label_26.setBuddy(self.dtPicker)
        self.label_23.setBuddy(self.txtconcepto)

        self.retranslateUi(dlgMovimientosBancarios)
        self.swcuenta.setCurrentIndex(0)
        self.cbtipodoc.setCurrentIndex(-1)
        self.swconcepto.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlgMovimientosBancarios)

    def retranslateUi(self, dlgMovimientosBancarios):
        dlgMovimientosBancarios.setWindowTitle(QtGui.QApplication.translate("dlgMovimientosBancarios", "Notas de Credito o Debito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("dlgMovimientosBancarios", "Cuenta Bancaria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("dlgMovimientosBancarios", "Tipo de Doc.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("dlgMovimientosBancarios", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.dtPicker.setDisplayFormat(QtGui.QApplication.translate("dlgMovimientosBancarios", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("dlgMovimientosBancarios", "En concepto de:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("dlgMovimientosBancarios", "Cuentas que afecta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("dlgMovimientosBancarios", "Observaciones", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
