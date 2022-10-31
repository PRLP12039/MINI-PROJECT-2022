# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 304)
        MainWindow.setStyleSheet("color: rgb(0, 170, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 230, 351, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(959, 40, 21, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(959, 80, 21, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(959, 120, 21, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(959, 160, 21, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 761, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 841, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 811, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 831, 31))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 791, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(960, 200, 20, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(819, 1, 161, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Other Factors"))
        self.pushButton.setText(_translate("MainWindow", "Store Other Factors in Database"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "No.of Industrial Units,growing during last 10 financial quarters? (0 for No, 1 for Yes)"))
        self.label_4.setText(_translate("MainWindow", "Stock Market Standard Indices,growing during last 10 financial quarters? (0 for No, 1 for Yes)"))
        self.label_5.setText(_translate("MainWindow", "Human Capital Index(HCE),growing during last 10 financial quarters?(0 for No, 1 for Yes)"))
        self.label_6.setText(_translate("MainWindow", "No.of Stock Market listings,growing during last 10 financial quarters? (0 for No, 1 for Yes)"))
        self.label_2.setText(_translate("MainWindow", "Energy Consumption(EC),growing during last 10 financial quarters? (0 for No, 1 for Yes)"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.lineEdit_9.setText(_translate("MainWindow", "000001"))
        self.label_7.setText(_translate("MainWindow", "City ID:"))


