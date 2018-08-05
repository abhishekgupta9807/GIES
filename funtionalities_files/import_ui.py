# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import datetime
import os
import csv

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImportWindow(object):
    def setupUi(self, ImportWindow):
        ImportWindow.setObjectName(_fromUtf8("ImportWindow"))
        ImportWindow.resize(804, 526)
        self.centralwidget = QtGui.QWidget(ImportWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.shopLabel = QtGui.QLabel(self.centralwidget)
        self.shopLabel.setObjectName(_fromUtf8("shopLabel"))
        self.gridLayout_2.addWidget(self.shopLabel, 14, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 4, 2, 1, 1)
        self.formLabel = QtGui.QLabel(self.centralwidget)
        self.formLabel.setObjectName(_fromUtf8("formLabel"))
        self.gridLayout.addWidget(self.formLabel, 0, 2, 1, 2)
        self.nameLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.gridLayout.addWidget(self.nameLineEdit, 1, 2, 1, 1)
        self.priceLineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLineEdit_3.sizePolicy().hasHeightForWidth())
        self.priceLineEdit_3.setSizePolicy(sizePolicy)
        self.priceLineEdit_3.setObjectName(_fromUtf8("priceLineEdit_3"))
        self.gridLayout.addWidget(self.priceLineEdit_3, 3, 2, 1, 1)
        self.itemWeightLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemWeightLabel.sizePolicy().hasHeightForWidth())
        self.itemWeightLabel.setSizePolicy(sizePolicy)
        self.itemWeightLabel.setObjectName(_fromUtf8("itemWeightLabel"))
        self.gridLayout.addWidget(self.itemWeightLabel, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(300, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.priceLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLabel.sizePolicy().hasHeightForWidth())
        self.priceLabel.setSizePolicy(sizePolicy)
        self.priceLabel.setObjectName(_fromUtf8("priceLabel"))
        self.gridLayout.addWidget(self.priceLabel, 3, 1, 1, 1)
        self.itemNameLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemNameLabel.sizePolicy().hasHeightForWidth())
        self.itemNameLabel.setSizePolicy(sizePolicy)
        self.itemNameLabel.setObjectName(_fromUtf8("itemNameLabel"))
        self.gridLayout.addWidget(self.itemNameLabel, 1, 1, 1, 1)
        self.dateLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.gridLayout.addWidget(self.dateLabel, 4, 1, 1, 1)
        self.weightLineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightLineEdit_2.sizePolicy().hasHeightForWidth())
        self.weightLineEdit_2.setSizePolicy(sizePolicy)
        self.weightLineEdit_2.setObjectName(_fromUtf8("weightLineEdit_2"))
        self.gridLayout.addWidget(self.weightLineEdit_2, 2, 2, 1, 1)
        self.enterButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy)
        self.enterButton.setObjectName(_fromUtf8("enterButton"))
        self.gridLayout.addWidget(self.enterButton, 5, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 1)
        self.systemLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.systemLabel.setFont(font)
        self.systemLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.systemLabel.setObjectName(_fromUtf8("systemLabel"))
        self.gridLayout_2.addWidget(self.systemLabel, 1, 0, 2, 2)
        self.ownerLabel = QtGui.QLabel(self.centralwidget)
        self.ownerLabel.setObjectName(_fromUtf8("ownerLabel"))
        self.gridLayout_2.addWidget(self.ownerLabel, 16, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 12, 24);\n"
"color: rgb(0, 0, 0);"))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout_2.addWidget(self.quitButton, 16, 1, 1, 1)
        self.gstLabel = QtGui.QLabel(self.centralwidget)
        self.gstLabel.setObjectName(_fromUtf8("gstLabel"))
        self.gridLayout_2.addWidget(self.gstLabel, 13, 0, 1, 1)
        ImportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ImportWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        ImportWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ImportWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ImportWindow.setStatusBar(self.statusbar)
        self.subMenuImport = QtGui.QAction(ImportWindow)
        self.subMenuImport.setObjectName(_fromUtf8("subMenuImport"))
        self.subMenuExport = QtGui.QAction(ImportWindow)
        self.subMenuExport.setObjectName(_fromUtf8("subMenuExport"))
        self.subMenuStock = QtGui.QAction(ImportWindow)
        self.subMenuStock.setObjectName(_fromUtf8("subMenuStock"))
        self.subMenuBalanceSheet = QtGui.QAction(ImportWindow)
        self.subMenuBalanceSheet.setObjectName(_fromUtf8("subMenuBalanceSheet"))
        self.menuHome.addAction(self.subMenuImport)
        self.menuHome.addAction(self.subMenuExport)
        self.menuHome.addAction(self.subMenuStock)
        self.menuHome.addAction(self.subMenuBalanceSheet)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())




        #self.enterButton.clicked.connect(self.saveImportData)

        self.retranslateUi(ImportWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportWindow)

    def retranslateUi(self, ImportWindow):
        ImportWindow.setWindowTitle(_translate("ImportWindow", "ImportWindow", None))
        self.shopLabel.setText(_translate("ImportWindow", "Shop No. :1980", None))
        self.formLabel.setText(_translate("ImportWindow", "Enter Details of Trancation", None))
        self.itemWeightLabel.setText(_translate("ImportWindow", "Item Weight :", None))
        self.priceLabel.setText(_translate("ImportWindow", "Price :", None))
        self.itemNameLabel.setText(_translate("ImportWindow", "Item Name :", None))
        self.dateLabel.setText(_translate("ImportWindow", "Date :", None))
        self.enterButton.setText(_translate("ImportWindow", "Enter", None))
        self.systemLabel.setText(_translate("ImportWindow", "Grain Import/Export System", None))
        self.ownerLabel.setText(_translate("ImportWindow", "OWNER :XYZ", None))
        self.quitButton.setText(_translate("ImportWindow", "Quit", None))
        self.gstLabel.setText(_translate("ImportWindow", "GST No. :TIN0009293", None))
        self.menuHome.setTitle(_translate("ImportWindow", "Home", None))
        self.menuView.setTitle(_translate("ImportWindow", "View", None))
        self.menuSetting.setTitle(_translate("ImportWindow", "Setting", None))
        self.menuHelp.setTitle(_translate("ImportWindow", "Help", None))
        self.subMenuImport.setText(_translate("ImportWindow", "Import", None))
        self.subMenuExport.setText(_translate("ImportWindow", "Export", None))
        self.subMenuStock.setText(_translate("ImportWindow", "Stock", None))
        self.subMenuBalanceSheet.setText(_translate("ImportWindow", "BalanceSheet", None))

    def saveImportData(self):

        date=datetime.datetime.now().date()

        self.todayDate=str(date.day)+'/'+str(date.month)+'/'+str(date.year)

        self.itemName=self.nameLineEdit.text().upper()


        try:
            if not self.itemName:
                raise ValueError()
            self.itemWeight=float(self.weightLineEdit_2.text())
            self.itemPrice=float(self.priceLineEdit_3.text())
            self.list=[self.itemName,self.itemWeight,self.itemPrice,self.todayDate]

        except ValueError:
            self.error()


        try:
            if os.path.isfile("import.csv")!=True:
                file = open("import.csv", 'w', newline='')
                write = csv.writer(file)
                write.writerow(['ITEM NAME', 'ITEM WEIGHT', 'ITEM PRICE', 'DATE'])
                file.close()


            file=open("import.csv",'a',newline='')
            write=csv.writer(file)
            write.writerow(self.list)

        finally:
            file.close()

        self.statusbar.showMessage("SUCCESS!!\t PAYMENT={}$".format(self.itemWeight*self.itemPrice))

    def error(self):

        self.statusbar.showMessage("Something is going WRONG!! PLEASE enter correct details")


if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    ImportWindow = QtGui.QMainWindow()
    ui = Ui_ImportWindow()
    ui.setupUi(ImportWindow)
    ImportWindow.show()
    sys.exit(app.exec_())

