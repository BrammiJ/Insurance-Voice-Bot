# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddata.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from uiregister import UserRegister
from addpolicy import Ui_policy_MainWindow


class Ui_adddata_Form(object):
    def adddatasetupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        Form.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 40, 241, 41))
        self.plainTextEdit.setStyleSheet("color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 110, 241, 111))
        self.plainTextEdit_2.setStyleSheet("color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 91, 23))
        self.pushButton.setStyleSheet("color: rgb(85, 85, 0);\n"
"font: 75 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save)

        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(160, 250, 91, 23))
        self.clear.setStyleSheet("color: rgb(85, 85, 0);\n"
                                      "font: 75 16pt \"Times New Roman\";\n"
                                      "background-color: rgb(255, 255, 127);\n"
                                      "border-color: rgb(85, 85, 0);")
        self.clear.setObjectName("pushButton")
        self.clear.clicked.connect(self.cleardata)

        self.policy = QtWidgets.QPushButton(Form)
        self.policy.setGeometry(QtCore.QRect(90, 300, 120, 35))
        self.policy.setStyleSheet("color: rgb(85, 85, 0);\n"
                                 "font: 75 16pt \"Times New Roman\";\n"
                                 "background-color: rgb(255, 255, 127);\n"
                                 "border-color: rgb(85, 85, 0);")
        self.policy.setObjectName("pushButton")
        self.policy.clicked.connect(self.addpolicy)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def addpolicy(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ()
        self.ui.policysetupUi(self.window)

        self.window.show()

    def save(self):
        ques =  self.plainTextEdit.toPlainText()
        answ =  self.plainTextEdit_2.toPlainText()
        add =  UserRegister()
        add.insertpolicy(ques,answ)
        print(ques,answ)

    def cleardata(self):
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit_2.setPlainText("")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "Enter the Question"))
        self.plainTextEdit_2.setPlaceholderText(_translate("Form", "Enter the Answer"))
        self.pushButton.setText(_translate("Form", "Add Data"))
        self.clear.setText(_translate("Form", "Clear Data"))
        self.policy.setText(_translate("Form", "Policy Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_adddata_Form()
    ui.adddatasetupUi(Form)
    Form.show()
    sys.exit(app.exec_())

