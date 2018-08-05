#!/usr/bin/env python3
""""
********************************************************************
//File name:  gies.py
//Creator: Abhishek gupta
//Stand alone GUI Desktop aplliction
//Last chang: 05/08/2018
********************************************************************
"""

# importing external modules into our application

from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,re,datetime,csv
import pandas as pd
import sys





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



# Making Main Window Class using PyQt4


class Ui_MainWindow(object):

    #init method to Creat Data Files when our application will run first time

    def __init__(self):
        if os.path.isfile("data_files/import.csv") != True:
            file = open("data_files/import.csv", 'w', newline='')
            write = csv.writer(file)
            write.writerow(['ITEM NAME', 'ITEM WEIGHT', 'ITEM PRICE', 'DATE'])
            file.close()


        if os.path.isfile("data_files/export.csv") != True:
            file = open("data_files/export.csv", 'w', newline='')
            write = csv.writer(file)
            write.writerow(["ITEM NAME", 'ITEM WEIGHT', 'ITEM PRICE', 'DATE', 'GST No.'])
            file.close()

        if os.path.isfile("data_files/stock.csv") != True:
            file= open("data_files/stock.csv",'w',newline='')
            write =csv.writer(file)
            write.writerow(['ITEM NAME','IMPORT WEIGHT','AVG IMPORT PRICE','EXPORT WEIGHT','AVG EXPORT PRICE','STOCK','profit'])
            file.close()

    # settingUp Window size and  attributes Size,color, position,hight, width

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(777, 566)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/gies_logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalBottomLayout = QtGui.QHBoxLayout()
        self.horizontalBottomLayout.setObjectName(_fromUtf8("horizontalBottomLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gstLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gstLabel.sizePolicy().hasHeightForWidth())
        self.gstLabel.setSizePolicy(sizePolicy)
        self.gstLabel.setObjectName(_fromUtf8("gstLabel"))
        self.gridLayout.addWidget(self.gstLabel, 0, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quitButton.setAutoFillBackground(False)
        self.quitButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);"))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 6, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.ownerLabel = QtGui.QLabel(self.centralwidget)
        self.ownerLabel.setObjectName(_fromUtf8("ownerLabel"))
        self.gridLayout.addWidget(self.ownerLabel, 6, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.shop_noLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shop_noLabel.sizePolicy().hasHeightForWidth())
        self.shop_noLabel.setSizePolicy(sizePolicy)
        self.shop_noLabel.setObjectName(_fromUtf8("shop_noLabel"))
        self.verticalLayout_6.addWidget(self.shop_noLabel)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalBottomLayout.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalBottomLayout, 3, 0, 1, 1)
        self.horizonOptiontalLayout = QtGui.QHBoxLayout()
        self.horizonOptiontalLayout.setObjectName(_fromUtf8("horizonOptiontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizonOptiontalLayout.addItem(spacerItem4)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizonOptiontalLayout.addWidget(self.line)
        self.importButton = QtGui.QPushButton(self.centralwidget)
        self.importButton.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(20, 255, 98);"))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.horizonOptiontalLayout.addWidget(self.importButton)
        self.exportButton = QtGui.QPushButton(self.centralwidget)
        self.exportButton.setStyleSheet(_fromUtf8("background-color: rgb(51, 0, 255);\n"
"background-color: rgb(255, 52, 26);\n"
"color: rgb(0, 0, 0);"))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizonOptiontalLayout.addWidget(self.exportButton)
        self.stockButton = QtGui.QPushButton(self.centralwidget)
        self.stockButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);"))
        self.stockButton.setObjectName(_fromUtf8("stockButton"))
        self.horizonOptiontalLayout.addWidget(self.stockButton)
        self.balanceSheetButton = QtGui.QPushButton(self.centralwidget)
        self.balanceSheetButton.setStyleSheet(_fromUtf8("background-color: rgb(21, 5, 255);\n"
"color: rgb(0, 0, 0);"))
        self.balanceSheetButton.setObjectName(_fromUtf8("balanceSheetButton"))
        self.horizonOptiontalLayout.addWidget(self.balanceSheetButton)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizonOptiontalLayout.addWidget(self.line_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizonOptiontalLayout.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizonOptiontalLayout, 2, 0, 1, 1)
        self.systemTitleLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.systemTitleLabel.setFont(font)
        self.systemTitleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.systemTitleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.systemTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.systemTitleLabel.setObjectName(_fromUtf8("systemTitleLabel"))
        self.gridLayout_2.addWidget(self.systemTitleLabel, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setStyleSheet(_fromUtf8(""))
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.subMenuImport = QtGui.QAction(MainWindow)
        self.subMenuImport.setObjectName(_fromUtf8("subMenuImport"))
        self.subMenuExport = QtGui.QAction(MainWindow)
        self.subMenuExport.setObjectName(_fromUtf8("subMenuExport"))
        self.subMenuStock = QtGui.QAction(MainWindow)
        self.subMenuStock.setObjectName(_fromUtf8("subMenuStock"))
        self.subMenuBalanceSheet = QtGui.QAction(MainWindow)
        self.subMenuBalanceSheet.setObjectName(_fromUtf8("subMenuBalanceSheet"))
        self.menuHome.addAction(self.subMenuImport)
        self.menuHome.addAction(self.subMenuExport)
        self.menuHome.addAction(self.subMenuStock)
        self.menuHome.addAction(self.subMenuBalanceSheet)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.subMenuImport.triggered.connect(self.importUI)
        self.subMenuExport.triggered.connect(self.exportUI)
        self.subMenuStock.triggered.connect(self.stock)

        self.importButton.clicked.connect(self.importUI)
        self.exportButton.clicked.connect(self.exportUI)
        self.stockButton.clicked.connect(self.stock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GIES", None))
        self.gstLabel.setText(_translate("MainWindow", "GST No. :TIN00920", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.ownerLabel.setText(_translate("MainWindow", "OWNER : XYZ", None))
        self.shop_noLabel.setText(_translate("MainWindow", "SHOP No. : 1980", None))
        self.importButton.setText(_translate("MainWindow", "Import", None))
        self.exportButton.setText(_translate("MainWindow", "Export", None))
        self.stockButton.setText(_translate("MainWindow", "Stock", None))
        self.balanceSheetButton.setText(_translate("MainWindow", "BalanceSheet", None))
        self.systemTitleLabel.setText(_translate("MainWindow", "Grain Import/Export System", None))
        self.menuHome.setTitle(_translate("MainWindow", "Home", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.subMenuImport.setText(_translate("MainWindow", "Import", None))
        self.subMenuExport.setText(_translate("MainWindow", "Export", None))
        self.subMenuStock.setText(_translate("MainWindow", "Stock", None))
        self.subMenuBalanceSheet.setText(_translate("MainWindow", "BalanceSheet", None))

    # On click event on menu

    def importUI(self):
        self.import_window=Ui_ImportWindow()
        self.import_window.setupUi(MainWindow)
        self.import_window.enterButton.clicked.connect(self.import_window.saveImportData)



    def exportUI(self):
        self.export_window=Ui_ExportWindow()
        self.export_window.setupUi(MainWindow)
        self.export_window.enterButton.clicked.connect(self.export_window.saveExportData)

    def stock(self):
        self.stock_window=Ui_StockWindow()
        self.stock_window.setupUi(MainWindow)









# Making Import Window Class



class Ui_ImportWindow(object):

    # SettingUp Window size ,elements ,color,height,width

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

        self.subMenuExport.triggered.connect(self.exportUI)
        self.subMenuStock.triggered.connect(self.stock)


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

    # funtion to Save imported Data into import.csv file

    def saveImportData(self):

        #retriving Data into the applicatiion

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



            file=open("data_files/import.csv",'a',newline='')
            write=csv.writer(file)
            write.writerow(self.list)
            #updateStock()

        finally:
            file.close()

        self.statusbar.showMessage("SUCCESS!!\t PAYMENT={}$".format(self.itemWeight*self.itemPrice))

    def error(self):

        # ERROR message on Wrong Input

        self.statusbar.showMessage("Something is going WRONG!! PLEASE enter correct details")


    # on click event

    def exportUI(self):
        self.export_window=Ui_ExportWindow()
        self.export_window.setupUi(MainWindow)
        self.export_window.enterButton.clicked.connect(self.export_window.saveExportData)

    def stock(self):
        self.stock_window=Ui_StockWindow()
        self.stock_window.setupUi(MainWindow)








# Making Export Window class

class Ui_ExportWindow(object):

    #SettingUp Window size, elements ,height, width color

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

        self.subMenuImport.triggered.connect(self.importUI)
        self.subMenuStock.triggered.connect(self.stock)

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


    # function to save exported data into export.csv file

    def saveExportData(self):
        date = datetime.datetime.now().date()

        self.todayDate = str(date.day) + '/' + str(date.month) + '/' + str(date.year)

        self.itemName = str(self.itemNameLineEdit.text()).upper()

        self.shopName=str(self.shopLineEdit.text()).upper()
        #date = self.dateEdit.text()

        try:
            if not self.itemName:
                raise ValueError
            #if not self.shopName:
            #    raise ValueError

            self.itemWeight = float(self.itemWeightLineEdit.text())
            self.itemPrice = float(self.priceLineEdit.text())
            self.list = [self.itemName,self.itemWeight,self.itemPrice, self.todayDate,self.shopName]

        except:
            self.error()


        try:



            file = open("data_files/export.csv", 'a', newline='')
            write = csv.writer(file)
            write.writerow(self.list)
            #updateStock()

        finally:
            file.close()

        self.statusbar.showMessage("SUCCESS!!!\t PAYMENT={}$".format(self.itemWeight*self.itemPrice))

    def error(self):
        self.statusbar.showMessage("WARNING !!!Somthing is going wrong please enter valid details")



    def importUI(self):
        self.import_window=Ui_ImportWindow()
        self.import_window.setupUi(MainWindow)
        self.import_window.enterButton.clicked.connect(self.import_window.saveImportData)



    def stock(self):
        self.stock_window=Ui_StockWindow()
        self.stock_window.setupUi(MainWindow)






# stock window class


class Ui_StockWindow(object):

    #settingUp window size, elements, color

    def setupUi(self, StockWindow):
        StockWindow.setObjectName(_fromUtf8("StockWindow"))
        StockWindow.resize(810, 563)
        self.centralwidget = QtGui.QWidget(StockWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Lsystemabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Lsystemabel.setFont(font)
        self.Lsystemabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Lsystemabel.setObjectName(_fromUtf8("Lsystemabel"))
        self.gridLayout.addWidget(self.Lsystemabel, 0, 0, 1, 1)
        self.stockTableView = QtGui.QTableWidget(self.centralwidget)
        self.stockTableView.setObjectName(_fromUtf8("stockTableView"))

        self.stockTableView.setRowCount(100)
        self.stockTableView.setColumnCount(7)

        self.stockTableView.setItem(0,0,QtGui.QTableWidgetItem("ITEM NAME"))
        self.stockTableView.setItem(0,1,QtGui.QTableWidgetItem("IMPORT WEIGHT"))
        self.stockTableView.setItem(0, 2, QtGui.QTableWidgetItem("AVG IMPORT PRICE"))
        self.stockTableView.setItem(0, 3, QtGui.QTableWidgetItem("EXPORT WEIGHT"))
        self.stockTableView.setItem(0,4,QtGui.QTableWidgetItem("AVG EXPORT PRICE"))
        self.stockTableView.setItem(0,5,QtGui.QTableWidgetItem("STOCK"))
        self.stockTableView.setItem(0, 6, QtGui.QTableWidgetItem("PROFIT/LOSS"))

        self.gridLayout.addWidget(self.stockTableView, 1, 0, 1, 2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gstLabel = QtGui.QLabel(self.centralwidget)
        self.gstLabel.setObjectName(_fromUtf8("gstLabel"))
        self.verticalLayout.addWidget(self.gstLabel)
        self.shopLabel = QtGui.QLabel(self.centralwidget)
        self.shopLabel.setObjectName(_fromUtf8("shopLabel"))
        self.verticalLayout.addWidget(self.shopLabel)
        self.userLabel = QtGui.QLabel(self.centralwidget)
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.verticalLayout.addWidget(self.userLabel)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        StockWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(StockWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        StockWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(StockWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        StockWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(StockWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        StockWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(StockWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        StockWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.subMenuImport = QtGui.QAction(StockWindow)
        self.subMenuImport.setObjectName(_fromUtf8("subMenuImport"))
        self.subMenuExport = QtGui.QAction(StockWindow)
        self.subMenuExport.setObjectName(_fromUtf8("subMenuExport"))
        self.subMenuStock = QtGui.QAction(StockWindow)
        self.subMenuStock.setObjectName(_fromUtf8("subMenuStock"))
        self.subMenuBalanceSheet = QtGui.QAction(StockWindow)
        self.subMenuBalanceSheet.setObjectName(_fromUtf8("subMenuBalanceSheet"))
        self.menuHome.addAction(self.subMenuImport)
        self.menuHome.addAction(self.subMenuExport)
        self.menuHome.addAction(self.subMenuStock)
        self.menuHome.addAction(self.subMenuBalanceSheet)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.subMenuImport.triggered.connect(self.importUI)
        self.subMenuExport.triggered.connect(self.exportUI)

        self.loadValue()

        self.retranslateUi(StockWindow)
        QtCore.QMetaObject.connectSlotsByName(StockWindow)



    def retranslateUi(self, StockWindow):
        StockWindow.setWindowTitle(_translate("StockWindow", "StockWindow", None))
        self.Lsystemabel.setText(_translate("StockWindow", "Grain Import/Export System", None))
        self.gstLabel.setText(_translate("StockWindow", "GST No. : TIN000298982", None))
        self.shopLabel.setText(_translate("StockWindow", "Shop No. : 1998", None))
        self.userLabel.setText(_translate("StockWindow", "USER : XYZ", None))
        self.quitButton.setText(_translate("StockWindow", "Quit", None))
        self.menuHome.setTitle(_translate("StockWindow", "Home", None))
        self.menuView.setTitle(_translate("StockWindow", "View", None))
        self.menuSetting.setTitle(_translate("StockWindow", "Setting", None))
        self.menuHelp.setTitle(_translate("StockWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("StockWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("StockWindow", "toolBar_2", None))
        self.subMenuImport.setText(_translate("StockWindow", "Import", None))
        self.subMenuExport.setText(_translate("StockWindow", "Export", None))
        self.subMenuStock.setText(_translate("StockWindow", "Stock", None))
        self.subMenuBalanceSheet.setText(_translate("StockWindow", "BalanceSheet", None))

    #this fuction will read stock.csv file and load data into Stock Window


    def loadValue(self):
        string=''
        try:
            if os.path.isfile("data_files/stock.csv"):
                updateStock()
                self.stock=pd.read_csv('data_files/stock.csv')
            else:
                raise ValueError()
        except:
            self.error()

        for x in range(len(self.stock)):
            row=re.sub("\s+","$",self.stock.iloc[x][0])
            list=[]
            row=row+'$'
            for y in row:
                if y=='$':
                    list.append(string)
                    string=''
                else:
                    string=string+y
            count=0
            for z in range(1,len(list)):
                self.stockTableView.setItem(x+1,count,QtGui.QTableWidgetItem(list[z]))
                count+=1

    def error(self):
        self.statusbar.showMessage("Data not found")

    def importUI(self):
        self.import_window=Ui_ImportWindow()
        self.import_window.setupUi(MainWindow)
        self.import_window.enterButton.clicked.connect(self.import_window.saveImportData)



    def exportUI(self):
        self.export_window=Ui_ExportWindow()
        self.export_window.setupUi(MainWindow)
        self.export_window.enterButton.clicked.connect(self.export_window.saveExportData)


''' /*Update Stock function*/
/
// # it will load all the transaction from both import/export.csv files and apply some logics to write available stocks into the stock.csv file 
'''

def updateStock():

    #reading import.csv file into pandas dataframe

    import_data=pd.read_csv('data_files/import.csv')

    item_list=pd.Series(import_data['ITEM NAME']).unique()


    import_stock=[]

    for x in item_list:
        row=[]
        item=import_data[import_data['ITEM NAME']==x]
        avg_price=item['ITEM PRICE'].mean()
        item_weight=item['ITEM WEIGHT'].sum()
        item=str(x)
        row.append(item)
        row.append(item_weight)
        row.append(avg_price)
        import_stock.append(row)



    import_dataframe=pd.DataFrame(import_stock,columns=['ITEM NAME','IMPORT WEIGHT','AVG IMPORT PRICE'])

    # reading export.csv file into pandas dataframe

    export_data=pd.read_csv('data_files/export.csv')

    item_list=pd.Series(export_data['ITEM NAME']).unique()

    export_stock=[]
    for x in item_list:
        row=[]
        item=export_data[export_data['ITEM NAME']==x]
        avg_price=item['ITEM PRICE'].mean()
        item_weight=item['ITEM WEIGHT'].sum()
        item=str(x)
        row.append(item)
        row.append(item_weight)
        row.append(avg_price)
        export_stock.append(row)


    export_dataframe=pd.DataFrame(export_stock,columns=['ITEM NAME','EXPORT WEIGHT','AVG EXPORT PRICE'])

    # merging two dataframes

    stock=pd.merge(import_dataframe,export_dataframe,on='ITEM NAME',how="outer")

    stock['STOCK']=stock['IMPORT WEIGHT']-stock['EXPORT WEIGHT']

    stock['profit']=stock['EXPORT WEIGHT']*stock['AVG EXPORT PRICE']-stock['EXPORT WEIGHT']*stock['AVG IMPORT PRICE']

    # writing stock dataframe into stock.csv file.

    stock.to_csv('data_files/stock.csv',sep='\t')


''' Start of the Main program'''

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


"""
***********************************************************************
//EOF: gies.py
***********************************************************************
"""