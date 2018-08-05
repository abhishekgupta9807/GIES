# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from import_ui import *
from PyQt4.QtCore import *
from export_ui import *
from stock_ui import *

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(777, 566)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("hello.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

