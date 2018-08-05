# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import datetime
import csv
import os

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

class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        ExportWindow.setObjectName(_fromUtf8("ExportWindow"))
        ExportWindow.resize(802, 525)
        font = QtGui.QFont()
        font.setItalic(False)
        ExportWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(ExportWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.itemWeightLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemWeightLabel.sizePolicy().hasHeightForWidth())
        self.itemWeightLabel.setSizePolicy(sizePolicy)
        self.itemWeightLabel.setObjectName(_fromUtf8("itemWeightLabel"))
        self.gridLayout.addWidget(self.itemWeightLabel, 3, 0, 1, 2)
        self.formLabel = QtGui.QLabel(self.centralwidget)
        self.formLabel.setObjectName(_fromUtf8("formLabel"))
        self.gridLayout.addWidget(self.formLabel, 0, 1, 1, 3)
        self.priceLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLabel.sizePolicy().hasHeightForWidth())
        self.priceLabel.setSizePolicy(sizePolicy)
        self.priceLabel.setObjectName(_fromUtf8("priceLabel"))
        self.gridLayout.addWidget(self.priceLabel, 4, 0, 1, 1)
        self.priceLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLineEdit.sizePolicy().hasHeightForWidth())
        self.priceLineEdit.setSizePolicy(sizePolicy)
        self.priceLineEdit.setObjectName(_fromUtf8("priceLineEdit"))
        self.gridLayout.addWidget(self.priceLineEdit, 4, 3, 1, 1)
        self.shopNoLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shopNoLabel.sizePolicy().hasHeightForWidth())
        self.shopNoLabel.setSizePolicy(sizePolicy)
        self.shopNoLabel.setObjectName(_fromUtf8("shopNoLabel"))
        self.gridLayout.addWidget(self.shopNoLabel, 1, 0, 1, 3)
        self.shopLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shopLineEdit.sizePolicy().hasHeightForWidth())
        self.shopLineEdit.setSizePolicy(sizePolicy)
        self.shopLineEdit.setObjectName(_fromUtf8("shopLineEdit"))
        self.gridLayout.addWidget(self.shopLineEdit, 1, 3, 1, 1)
        self.itemNameLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemNameLabel.sizePolicy().hasHeightForWidth())
        self.itemNameLabel.setSizePolicy(sizePolicy)
        self.itemNameLabel.setObjectName(_fromUtf8("itemNameLabel"))
        self.gridLayout.addWidget(self.itemNameLabel, 2, 0, 1, 2)
        self.dateLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.gridLayout.addWidget(self.dateLabel, 5, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 5, 3, 1, 1)
        self.itemNameLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemNameLineEdit.sizePolicy().hasHeightForWidth())
        self.itemNameLineEdit.setSizePolicy(sizePolicy)
        self.itemNameLineEdit.setObjectName(_fromUtf8("itemNameLineEdit"))
        self.gridLayout.addWidget(self.itemNameLineEdit, 2, 3, 1, 1)
        self.itemWeightLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemWeightLineEdit.sizePolicy().hasHeightForWidth())
        self.itemWeightLineEdit.setSizePolicy(sizePolicy)
        self.itemWeightLineEdit.setObjectName(_fromUtf8("itemWeightLineEdit"))
        self.gridLayout.addWidget(self.itemWeightLineEdit, 3, 3, 1, 1)
        self.enterButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy)
        self.enterButton.setObjectName(_fromUtf8("enterButton"))
        self.gridLayout.addWidget(self.enterButton, 6, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.systemLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.systemLabel.setFont(font)
        self.systemLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.systemLabel.setObjectName(_fromUtf8("systemLabel"))
        self.gridLayout_2.addWidget(self.systemLabel, 0, 0, 1, 5)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 1, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 1, 3, 1, 1)
        self.shopLabel = QtGui.QLabel(self.centralwidget)
        self.shopLabel.setObjectName(_fromUtf8("shopLabel"))
        self.gridLayout_2.addWidget(self.shopLabel, 2, 0, 1, 3)
        self.gstLabel = QtGui.QLabel(self.centralwidget)
        self.gstLabel.setObjectName(_fromUtf8("gstLabel"))
        self.gridLayout_2.addWidget(self.gstLabel, 3, 0, 1, 3)
        self.ownerLabel = QtGui.QLabel(self.centralwidget)
        self.ownerLabel.setObjectName(_fromUtf8("ownerLabel"))
        self.gridLayout_2.addWidget(self.ownerLabel, 4, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 10, 14);\n"
"color: rgb(0, 0, 0);"))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout_2.addWidget(self.quitButton, 4, 3, 1, 1)
        ExportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ExportWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        ExportWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ExportWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ExportWindow.setStatusBar(self.statusbar)
        self.subMenuImport = QtGui.QAction(ExportWindow)
        self.subMenuImport.setObjectName(_fromUtf8("subMenuImport"))
        self.subMenuExport = QtGui.QAction(ExportWindow)
        self.subMenuExport.setObjectName(_fromUtf8("subMenuExport"))
        self.subMenuStock = QtGui.QAction(ExportWindow)
        self.subMenuStock.setObjectName(_fromUtf8("subMenuStock"))
        self.subMenuBalanceShaeet = QtGui.QAction(ExportWindow)
        self.subMenuBalanceShaeet.setObjectName(_fromUtf8("subMenuBalanceShaeet"))
        self.menuHome.addAction(self.subMenuImport)
        self.menuHome.addAction(self.subMenuExport)
        self.menuHome.addAction(self.subMenuStock)
        self.menuHome.addAction(self.subMenuBalanceShaeet)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

		#self.enterButton.clicked.connect(self.saveExportData)

        self.retranslateUi(ExportWindow)
        QtCore.QMetaObject.connectSlotsByName(ExportWindow)

    def retranslateUi(self, ExportWindow):
        ExportWindow.setWindowTitle(_translate("ExportWindow", "ExportWindow", None))
        self.itemWeightLabel.setText(_translate("ExportWindow", "Item Weight :", None))
        self.formLabel.setText(_translate("ExportWindow", "Enter Details Of Trancation", None))
        self.priceLabel.setText(_translate("ExportWindow", "Price :", None))
        self.shopNoLabel.setText(_translate("ExportWindow", "GST No. /Shop No.  :", None))
        self.itemNameLabel.setText(_translate("ExportWindow", "Item Name : ", None))
        self.dateLabel.setText(_translate("ExportWindow", "Date :", None))
        self.enterButton.setText(_translate("ExportWindow", "Enter", None))
        self.systemLabel.setText(_translate("ExportWindow", "GRAIN IMPORT/EXPORT SYSTEM", None))
        self.shopLabel.setText(_translate("ExportWindow", "Shop No. : 1980", None))
        self.gstLabel.setText(_translate("ExportWindow", "GST No. :TIN00029938", None))
        self.ownerLabel.setText(_translate("ExportWindow", "OWNER : XYZ", None))
        self.quitButton.setText(_translate("ExportWindow", "Quit", None))
        self.menuHome.setTitle(_translate("ExportWindow", "Home", None))
        self.menuView.setTitle(_translate("ExportWindow", "View", None))
        self.menuSetting.setTitle(_translate("ExportWindow", "Setting", None))
        self.menuHelp.setTitle(_translate("ExportWindow", "Help", None))
        self.subMenuImport.setText(_translate("ExportWindow", "Import", None))
        self.subMenuExport.setText(_translate("ExportWindow", "Export", None))
        self.subMenuStock.setText(_translate("ExportWindow", "Stock", None))
        self.subMenuBalanceShaeet.setText(_translate("ExportWindow", "BalanceShaeet", None))




    def saveExportData(self):
        date = datetime.datetime.now().date()

        self.todayDate = str(date.day) + '/' + str(date.month) + '/' + str(date.year)

        self.itemName = str(self.itemNameLineEdit.text()).upper()

        self.shopName=str(self.shopLineEdit.text()).upper()
        #date = self.dateEdit.text()

        try:
            if not self.itemName:
                raise ValueError
            if not self.shopName:
                raise ValueError

            self.itemWeight = float(self.itemWeightLineEdit.text())
            self.itemPrice = float(self.priceLineEdit.text())
            self.list = [self.itemName,self.itemWeight,self.itemPrice, self.date,self.shopName]

        except:
            self.error()


        try:
            if os.path.isfile("export.csv"):
                file=open("export.csv",'w',newline='')
                write=csv.writer(file)
                write.writerow(["ITEM NAME",'ITEM WEIGHT','ITEM PRICE','DATE','GST No.'])
                file.close()


            file = open("export.csv", 'a', newline='')
            write = csv.writer(file)
            write.writerow(self.list)

        finally:
            file.close()

        self.statusbar.showMessage("SUCCESS!!!\t PAYMENT={}$".format(self.itemWeight*self.itemWeight))

    def error(self):
        self.statusbar.showMessage("WARNING !!!Somthing is going wrong please enter valid details")

if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    ImportWindow = QtGui.QMainWindow()
    ui = Ui_ExportWindow()
    ui.setupUi(ImportWindow)
    ImportWindow.show()
    sys.exit(app.exec_())

