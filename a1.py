# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import win32com.client
from threading import Timer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 271, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 110, 271, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.voice)

        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 160, 271, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.voiceresult = QtWidgets.QLabel(self.centralwidget)
        self.voiceresult.setGeometry(QtCore.QRect(290, 290, 47, 13))
        self.voiceresult.setObjectName("voiceresult")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 460, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 590, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 350, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 350, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.next_question = QtWidgets.QPushButton(self.centralwidget)
        self.next_question.setGeometry(QtCore.QRect(20, 460, 75, 23))
        self.next_question.setObjectName("next_question")
        self.next_question.clicked.connect(self.analys)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.checkBox.setVisible(False)
        self.checkBox_2.setVisible(False)
        self.next_question.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.voiceresult.setVisible(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.list1 = ["Do Have Car?", "Do You Have Bike", "You are age above 45", "Are You Married"]
        self.list2 = ["car", "bike", "above 45", "Married"]
        self.dt=[]
        self.d = 0;
        self.result="";
        global a
    def voice(self):
        data = self.plainTextEdit.toPlainText()
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak("Welcome" + data)
        self.next_question.setVisible(True)
        self.checkBox.setVisible(True)
        self.checkBox_2.setVisible(True)
        self.voiceresult.setVisible(True)

        try:
            if(len(self.list1)>self.d):
                speaker = win32com.client.Dispatch("SAPI.SpVoice")

                speaker.Speak(self.list1[self.d])

                self.voiceresult.setText(self.list1[self.d])

                if (self.checkBox.isChecked() == True):


                    self.result = self.list2[self.d]
                else:
                    self.result = ""
                if (self.checkBox_2.isChecked() == True):
                    print("not seletced")

                    self.result = ""
                else:
                    self.result = self.list2[self.d]


                self.d = self.d + 1
            else:

                speaker = win32com.client.Dispatch("SAPI.SpVoice")

                speaker.Speak("We will give some Insurence Policy list")
                self.checkBox.setVisible(False)
                self.checkBox_2.setVisible(False)
                self.voiceresult.setVisible(False)
                self.next_question.setVisible(False)
                self.pushButton_2.setVisible(True)
                print(self.dt)





        except:
            pass

    def analys(self):
        if (self.checkBox.isChecked() == True):
            print(self.checkBox.text())
            self.dt.append(self.result)
        else:

            pass
        if (self.checkBox_2.isChecked() == True):
            print(self.checkBox_2.text())
            self.dt.append("no")
        else:

            pass
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.voice()












    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Name"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Your Email ID"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.plainTextEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Your Mobile No"))
        self.voiceresult.setText(_translate("MainWindow", "Voice"))
        self.pushButton_2.setText(_translate("MainWindow", "Suggest"))
        self.radioButton_3.setText(_translate("MainWindow", "no"))

        self.checkBox.setText(_translate("MainWindow", "Yes"))
        self.checkBox_2.setText(_translate("MainWindow", "No"))
        self.next_question.setText(_translate("MainWindow", "Analys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

