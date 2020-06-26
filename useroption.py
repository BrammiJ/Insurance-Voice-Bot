# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'useroption.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from login import Login_Form
from userregister import Ui_Register_Form

import sys
from useradmin import User_Admin_Form
from scroll import Main

class User_Option_Form(object):

    def useroptionsetupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        Form.setStyleSheet("background-color: rgb(255, 85, 0);")

        self.userchoice = QtWidgets.QPushButton(Form)
        self.userchoice.setGeometry(QtCore.QRect(90, 200, 130, 31))
        self.userchoice.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                     "background-color: rgb(170, 255, 0);\n"
                                     "border-color: rgb(85, 85, 0);\n"
                                     "color: rgb(0, 85, 0);")
        self.userchoice.setObjectName("pushButton_3")
        self.useradmin = QtWidgets.QPushButton(Form)
        self.useradmin.setGeometry(QtCore.QRect(90, 140, 130, 31))
        self.useradmin.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                      "background-color: rgb(170, 255, 0);\n"
                                      "border-color: rgb(85, 85, 0);\n"
                                      "color: rgb(0, 85, 0);")
        self.useradmin.setObjectName("pushButton_4")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 201, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Times New Roman\";")
        self.label.setObjectName("label")

        self.userchoice.clicked.connect(self.viewdata)
        self.useradmin.clicked.connect(self.openwindow)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def viewdata(self):
        try:
            #self.window2 = QtWidgets.QMainWindow();
            #self.ui2 = Ui_data_Form();
            #self.ui2.datasetupUi(self.window2)

            #Form.hide()
            #self.window2.show()
            #self.myWidget = Main()
          #  Form.hide()
            #self.myWidget.show()
            self.myWidget = Main()
            #  Form.hide()
            self.myWidget.show()
            pass
        except Exception as  e:
            print(e)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.userchoice.setText(_translate("Form", "Guest"))
        self.useradmin.setText(_translate("Form", "Admin"))
        self.label.setText(_translate("Form", "Insurance Policy"))

    def openwindow(self):
        self.window= QtWidgets.QMainWindow();
        self.ui =User_Admin_Form();
        self.ui.useradminsetupUi(self.window)
        #Form.close()
        self.window.show()

        pass
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = User_Option_Form()
    ui.useroptionsetupUi(Form)
    Form.show()
    sys.exit(app.exec_())

