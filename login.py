# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from adddata import Ui_adddata_Form
from uiregister import UserRegister

class Login_Form(object):
    def loginsetupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        Form.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.username = QtWidgets.QPlainTextEdit(Form)
        self.username.setGeometry(QtCore.QRect(60, 90, 181, 41))
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 85, 0);\n"
"color: rgb(255, 85, 0);")
        self.username.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.username.setTabChangesFocus(True)
        self.username.setObjectName("username")
        self.paasword = QtWidgets.QPlainTextEdit(Form)
        self.paasword.setGeometry(QtCore.QRect(60, 150, 181, 41))
        self.paasword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 85, 0);\n"
"color: rgb(255, 85, 0);")
        self.paasword.setTabChangesFocus(True)
        self.paasword.setObjectName("paasword")
        self.loginbtn = QtWidgets.QPushButton(Form)
        self.loginbtn.setGeometry(QtCore.QRect(30, 230, 75, 31))
        self.loginbtn.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 16pt \"Times New Roman\";")
        self.loginbtn.setObjectName("loginbtn")
        self.loginbtn.clicked.connect(self.loginlogic)
        self.cancelbtn = QtWidgets.QPushButton(Form)
        self.cancelbtn.setGeometry(QtCore.QRect(190, 230, 75, 31))
        self.cancelbtn.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 16pt \"Times New Roman\";")
        self.cancelbtn.setObjectName("cancelbtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 29, 141, 31))
        self.label.setStyleSheet("font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(120, 270, 60, 23))
        self.result.setStyleSheet("color: rgb(255, 255, 0);")
        self.result.setObjectName("result")
        self.result.setVisible(False)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def loginlogic(self):
        username=  self.username.toPlainText()
        password=  self.paasword.toPlainText()
        login =  UserRegister()
        result = login.loginuser(username,password)
        print(result)
        if result:
            try:
                self.window1 = QtWidgets.QMainWindow();
                self.ui =Ui_adddata_Form();
                self.ui.adddatasetupUi(self.window1)

                # Form.hide()
                self.window1.show()
            except Exception as e:
                print(e)
        else:
            self.result.setVisible(True)
            self.result.setText("login failed")
            print('login failed')



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setPlaceholderText(_translate("Form", "Enter Username"))
        self.paasword.setPlaceholderText(_translate("Form", "Enter Password"))
        self.loginbtn.setText(_translate("Form", "Login"))
        self.cancelbtn.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Login Form"))
        self.result.setText(_translate("Form", "result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login_Form()
    ui.loginsetupUi(Form)
    Form.show()
    sys.exit(app.exec_())

