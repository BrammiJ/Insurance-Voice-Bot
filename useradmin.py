# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'useroption.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from login import Login_Form
from userregister import Ui_Register_Form
from viewdata import Ui_data_Form
import sys

class User_Admin_Form(object):

    def useradminsetupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        Form.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.userregister = QtWidgets.QPushButton(Form)
        self.userregister.setGeometry(QtCore.QRect(40, 140, 75, 31))
        self.userregister.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"background-color: rgb(170, 255, 0);\n"
"border-color: rgb(85, 85, 0);\n"
"color: rgb(0, 85, 0);")
        self.userregister.clicked.connect(self.registerpage)
        self.userregister.setObjectName("pushButton")
        self.userlogin = QtWidgets.QPushButton(Form)
        self.userlogin.setGeometry(QtCore.QRect(190, 140, 75, 31))
        self.userlogin.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"background-color: rgb(170, 255, 0);\n"
"border-color: rgb(85, 85, 0);\n"
"color: rgb(0, 85, 0);")
        self.userlogin.setObjectName("pushButton_2")



        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.userlogin.clicked.connect(self.loginpage)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def viewdata(self):
        try:
            self.window2 = QtWidgets.QMainWindow();
            self.ui2 = Ui_data_Form();
            self.ui2.datasetupUi(self.window2)

            #Form.hide()
            self.window2.show()
        except Exception as  e:
            print(e)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userregister.setText(_translate("Form", "Register"))
        self.userlogin.setText(_translate("Form", "Login"))

        self.label.setText(_translate("Form", "Insurance Policy"))
    def registerpage(self):
        print('register clicked')
        try:
            self.openwindow();
        except Exception as e:
            print(e)

    def loginpage(self):
        try:
            self.window1 = QtWidgets.QMainWindow();
            self.ui = Login_Form();
            self.ui.loginsetupUi(self.window1)

           # Form.hide()
            self.window1.show()
        except Exception as e:
            print(e)
    def openwindow(self):
        self.window= QtWidgets.QMainWindow();
        self.ui =Ui_Register_Form();
        self.ui.registersetupUi(self.window)
        #Form.close()
        self.window.show()

        pass
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = User_Admin_Form()
    ui.useradminsetupUi(Form)
    Form.show()
    sys.exit(app.exec_())

