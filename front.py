# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from register import Ui_MainWindowRegister
from threading import Timer
from useroption import User_Option_Form

import sys
import dbconn
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(255, 85, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 190, 71, 20))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 150, 118, 23))

        self.progressBar.setObjectName("progressBar")
        self.progress = QtWidgets.QPushButton(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.progress.setObjectName("progress")
        self.progress.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                      "background-color: rgb(170, 255, 0);\n"
                                      "border-color: rgb(85, 85, 0);\n"
                                      "color: rgb(0, 85, 0);")
        self.progress.clicked.connect(self.open)
        self.InsurancePolicy = QtWidgets.QLabel(self.centralwidget)
        self.InsurancePolicy.setGeometry(QtCore.QRect(80, 50, 171, 20))
        self.InsurancePolicy.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.progress.hide()
        self.InsurancePolicy.setObjectName("InsurancePolicy")
        aa =  dbconn.conn()
        print(aa)
        MainWindow.setCentralWidget(self.centralwidget)
        try:
            t = Timer(5.0, self.download)
            t.start()
        except Exception as e:
            print(e)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def download(self):
        self.completed = 0

        while self.completed < 100:


            self.completed += 0.0001
            self.progressBar.setValue(self.completed)



        else:
            self.progress.show()


            # self.close()

            print("exit")


    def open(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = User_Option_Form()
        self.ui.useroptionsetupUi(self.window)

        self.window.show()
        MainWindow.close()
       # sys.exit()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "please wait..."))
        self.progress.setText(_translate("MainWindow", "click here"))
        self.InsurancePolicy.setText(_translate("MainWindow", "Insurance Policy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
