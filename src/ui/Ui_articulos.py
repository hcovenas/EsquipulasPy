# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/articulos.ui'
#
# Created: Tue Jul 27 12:35:44 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmArticlesNew(object):
    def setupUi(self, frmArticlesNew):
        frmArticlesNew.setObjectName("frmArticlesNew")
        frmArticlesNew.resize(702, 338)
        self.gridLayout = QtGui.QGridLayout(frmArticlesNew)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtGui.QLabel(frmArticlesNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(frmArticlesNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(frmArticlesNew)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txtComission = QtGui.QLineEdit(frmArticlesNew)
        self.txtComission.setObjectName("txtComission")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtComission)
        self.label_3 = QtGui.QLabel(frmArticlesNew)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtISC = QtGui.QLineEdit(frmArticlesNew)
        self.txtISC.setObjectName("txtISC")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtISC)
        self.label_2 = QtGui.QLabel(frmArticlesNew)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtDAI = QtGui.QLineEdit(frmArticlesNew)
        self.txtDAI.setObjectName("txtDAI")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtDAI)
        self.label_4 = QtGui.QLabel(frmArticlesNew)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtProfit = QtGui.QLineEdit(frmArticlesNew)
        self.txtProfit.setObjectName("txtProfit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtProfit)
        self.gridLayout.addLayout(self.formLayout, 0, 2, 3, 1)
        self.categoriesview = QtGui.QTreeView(frmArticlesNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoriesview.sizePolicy().hasHeightForWidth())
        self.categoriesview.setSizePolicy(sizePolicy)
        self.categoriesview.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.categoriesview.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.categoriesview.setObjectName("categoriesview")
        self.gridLayout.addWidget(self.categoriesview, 1, 0, 2, 1)
        self.brandsview = QtGui.QListView(frmArticlesNew)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brandsview.sizePolicy().hasHeightForWidth())
        self.brandsview.setSizePolicy(sizePolicy)
        self.brandsview.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.brandsview.setObjectName("brandsview")
        self.gridLayout.addWidget(self.brandsview, 1, 1, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtGui.QLabel(frmArticlesNew)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.txtCategorySearch = QtGui.QLineEdit(frmArticlesNew)
        self.txtCategorySearch.setObjectName("txtCategorySearch")
        self.horizontalLayout.addWidget(self.txtCategorySearch)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtGui.QLabel(frmArticlesNew)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.txtBrandSearch = QtGui.QLineEdit(frmArticlesNew)
        self.txtBrandSearch.setObjectName("txtBrandSearch")
        self.horizontalLayout_2.addWidget(self.txtBrandSearch)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(frmArticlesNew)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 1)
        self.label.setBuddy(self.txtComission)
        self.label_3.setBuddy(self.txtISC)
        self.label_2.setBuddy(self.txtDAI)
        self.label_4.setBuddy(self.txtProfit)
        self.label_7.setBuddy(self.txtCategorySearch)
        self.label_8.setBuddy(self.txtBrandSearch)

        self.retranslateUi(frmArticlesNew)
        QtCore.QMetaObject.connectSlotsByName(frmArticlesNew)

    def retranslateUi(self, frmArticlesNew):
        frmArticlesNew.setWindowTitle(QtGui.QApplication.translate("frmArticlesNew", "Añadir Articulos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmArticlesNew", "<b>Categoria</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("frmArticlesNew", "<b>Marca</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("frmArticlesNew", "<b>Comisión</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.txtComission.setText(QtGui.QApplication.translate("frmArticlesNew", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmArticlesNew", "<b>ISC</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.txtISC.setText(QtGui.QApplication.translate("frmArticlesNew", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmArticlesNew", "<b>DAI</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDAI.setText(QtGui.QApplication.translate("frmArticlesNew", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmArticlesNew", "<b>Ganancia</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.txtProfit.setText(QtGui.QApplication.translate("frmArticlesNew", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("frmArticlesNew", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("frmArticlesNew", "Buscar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmArticlesNew = QtGui.QDialog()
    ui = Ui_frmArticlesNew()
    ui.setupUi(frmArticlesNew)
    frmArticlesNew.show()
    sys.exit(app.exec_())

