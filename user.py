# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userchoice.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from threading import Timer
import win32com.client
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.caryes = QtWidgets.QRadioButton(self.centralwidget)
        self.caryes.setGeometry(QtCore.QRect(30, 80, 82, 17))
        self.caryes.setObjectName("caryes")
        self.carno = QtWidgets.QRadioButton(self.centralwidget)
        self.carno.setGeometry(QtCore.QRect(180, 80, 82, 17))
        self.carno.setObjectName("carno")
        self.bikeyes = QtWidgets.QRadioButton(self.centralwidget)
        self.bikeyes.setGeometry(QtCore.QRect(30, 140, 82, 17))
        self.bikeyes.setObjectName("bikeyes")
        self.bikeno = QtWidgets.QRadioButton(self.centralwidget)
        self.bikeno.setGeometry(QtCore.QRect(190, 140, 82, 17))
        self.bikeno.setObjectName("bikeno")
        self.ageabove = QtWidgets.QRadioButton(self.centralwidget)
        self.ageabove.setGeometry(QtCore.QRect(30, 200, 82, 17))
        self.ageabove.setObjectName("ageabove")
        self.agebelow = QtWidgets.QRadioButton(self.centralwidget)
        self.agebelow.setGeometry(QtCore.QRect(190, 200, 82, 17))
        self.agebelow.setObjectName("agebelow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak("Welcome to word")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.caryes.setVisible(False)
        self.carno.setVisible(False)
        self.bikeyes.setVisible(False)
        self.bikeno.setVisible(False)
        self.ageabove.setVisible(False)
        self.agebelow.setVisible(False)

        try:
            t = Timer(3.0, self.speak)
            t.start()
        except Exception as e:
            print(e)
    def speak(self):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak("Do you have car??")
        self.caryes.setVisible(True)
        self.carno.setVisible(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.caryes.setText(_translate("MainWindow", "yes"))
        self.carno.setText(_translate("MainWindow", "no"))
        self.bikeyes.setText(_translate("MainWindow", "yes"))
        self.bikeno.setText(_translate("MainWindow", "no"))
        self.ageabove.setText(_translate("MainWindow", "above 50"))
        self.agebelow.setText(_translate("MainWindow", "below 50"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

