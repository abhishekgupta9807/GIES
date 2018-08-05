# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pandas as pd
import re
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

class Ui_StockWindow(object):
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

    def loadValue(self):
        string=''
        try:
            if os.path.isfile("stock.csv"):
                self.stock=pd.read_csv('stock.csv')
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





if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    StockWindow = QtGui.QMainWindow()
    ui = Ui_StockWindow()
    ui.setupUi(StockWindow)
    StockWindow.show()
    sys.exit(app.exec_())

