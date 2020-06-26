# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userregister.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from  uiregister import UserRegister
from  allregister import Alldata
class Ui_Register_Form(QtWidgets.QMainWindow):
    def registersetupUi(self, Forms):
        Forms.setObjectName("Form")
        Forms.resize(300, 500)
        Forms.setStyleSheet("border-color: rgb(85, 85, 0);\n"
"background-color: rgb(255, 85, 0);")
        self.rfullname = QtWidgets.QPlainTextEdit(Forms)
        self.rfullname.setGeometry(QtCore.QRect(56, 110, 201, 31))
        self.rfullname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.rfullname.setObjectName("rfullname")
        self.rlastanme = QtWidgets.QPlainTextEdit(Forms)
        self.rlastanme.setGeometry(QtCore.QRect(56, 170, 201, 31))
        self.rlastanme.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.rlastanme.setObjectName("rlastanme")
        self.remail = QtWidgets.QPlainTextEdit(Forms)
        self.remail.setGeometry(QtCore.QRect(56, 230, 201, 31))
        self.remail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.remail.setObjectName("remail")
        self.rmobile = QtWidgets.QPlainTextEdit(Forms)
        self.rmobile.setGeometry(QtCore.QRect(56, 290, 201, 31))
        self.rmobile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.rmobile.setObjectName("rmobile")
        self.rpassword = QtWidgets.QPlainTextEdit(Forms)
        self.rpassword.setGeometry(QtCore.QRect(56, 350, 201, 31))
        self.rpassword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.rpassword.setObjectName("rpassword")
        self.r_register = QtWidgets.QPushButton(Forms)
        self.r_register.setGeometry(QtCore.QRect(46, 410, 81, 31))
        self.r_register.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 16pt \"Times New Roman\";\n"
"color: rgb(0, 85, 0);")
        self.r_register.setObjectName("r_register")
        self.r_register.clicked.connect(self.registeruser)
        self.r_cancel = QtWidgets.QPushButton(Forms)
        self.r_cancel.setGeometry(QtCore.QRect(180, 410, 81, 31))
        self.r_cancel.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 16pt \"Times New Roman\";\n"
"color: rgb(0, 85, 0);")
        self.r_cancel.setObjectName("r_cancel")
        self.r_cancel.clicked.connect(self.closepage);
        self.label = QtWidgets.QLabel(Forms)
        self.label.setGeometry(QtCore.QRect(66, 40, 181, 31))
        self.label.setStyleSheet("font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Forms)
        QtCore.QMetaObject.connectSlotsByName(Forms)
    def registeruser(self):
        print('regisfrer')

        fname = self.rfullname.toPlainText();
        lname = self.rlastanme.toPlainText();
        email = self.remail.toPlainText();
        mobile = self.rmobile.toPlainText();
        password = self.rpassword.toPlainText();
        if(fname=="" or lname== ""or email=="" or mobile=="" or password==""):
            print ("insert all data")
            try:
                choice = QtWidgets.QMessageBox.question(self, "Alert", "Enter All fields",
                                                    QtWidgets.QMessageBox.Ok)
            except Exception as e:
                print(e)



        else:
            try:
                data =  UserRegister()
                view = data.insert(fname,lname,email,mobile,password)
                print(view)
            except Exception as e:
                print(e)
    def closepage(self):
        self.rfullname.setPlainText("");
        self.rlastanme.setPlainText("");
        self.remail.setPlainText("");
        self.rmobile.setPlainText("");
        self.rpassword.setPlainText("");



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rfullname.setPlaceholderText(_translate("Form", "FirstName"))
        self.rlastanme.setPlaceholderText(_translate("Form", "LastName"))
        self.remail.setPlaceholderText(_translate("Form", "Email"))
        self.rmobile.setPlaceholderText(_translate("Form", "Mobile"))
        self.rpassword.setPlaceholderText(_translate("Form", "password"))
        self.r_register.setText(_translate("Form", "Register"))
        self.r_cancel.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Register Form"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Forms = QtWidgets.QMainWindow()
    ui = Ui_Register_Form()
    ui.registersetupUi(Forms)
    Forms.show()
    sys.exit(app.exec_())

