# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\codespace\ReverseToolsDevelop\CodeGen/CodeGen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonGen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGen.setGeometry(QtCore.QRect(410, 10, 111, 41))
        self.pushButtonGen.setObjectName("pushButtonGen")
        self.lineEditSignature = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSignature.setGeometry(QtCore.QRect(20, 10, 381, 41))
        self.lineEditSignature.setObjectName("lineEditSignature")
        self.plainTextEditCode = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditCode.setGeometry(QtCore.QRect(20, 60, 501, 411))
        self.plainTextEditCode.setObjectName("plainTextEditCode")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Just Fucking"))
        self.pushButtonGen.setText(_translate("MainWindow", "生   成"))
