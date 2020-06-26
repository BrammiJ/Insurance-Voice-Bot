# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
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
        self.pushButton.clicked.connect(self.voice);
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 160, 271, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.voiceresult = QtWidgets.QLabel(self.centralwidget)
        self.voiceresult.setGeometry(QtCore.QRect(120, 290, 70, 50))
        self.voiceresult.setObjectName("voiceresult")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 350, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 350, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 460, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.next);

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.voiceresult.setVisible(False);
        self.radioButton.setVisible(False);
        self.radioButton_2.setVisible(False);
        self.pushButton_2.setVisible(False);
        self.d = 0;
        global  a
        self.list1 = ["Do Have Car?", "Do You Have Bike", "You are age above 45", "Are You Married"]
        self.list2 = ["car", "bike", "above 45", "Married"]


    def btnstate(self,b):
        #print(b.text() =="Yes")
     #   list1 = ["Do Have Car?", "Do You Have Bike", "You are age above 45", "Are You Married"]

        if b.text() == "yes":
            if b.isChecked() == True:
                print( b.text() + " is selected")

                try:
                    b.isChecked() == False
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Speak(self.list1[self.d])

                    self.voiceresult.setText(self.list1[self.d])

                    print(self.d);
                    print(self.list2[self.d])
                    self.radioButton.setVisible(False)
                    self.radioButton_2.setVisible(False)
                    try:
                        t = Timer(1.0, self.show)
                        t.start()
                    except Exception as e:
                        print(e)
                    self.d = self.d + 1;

                except Exception:
                    print('error')
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Speak("We suggest you best Insurence policy ")
                    self.pushButton_2.setVisible(True)

            else:
                print(b.text() + " is deselected")


        if b.text() == "no":
            if b.isChecked() == True:


                print(b.text() + " is selected")

                try:
                    b.isChecked() == False
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Speak(self.list1[self.d])

                    self.voiceresult.setText(self.list1[self.d])
                    self.radioButton.setVisible(False)
                    self.radioButton_2.setVisible(False)
                    try:
                        t = Timer(1.0, self.show)
                        t.start()
                    except Exception as e:
                        print(e)
                    print(self.d);
                    self.d = self.d + 1;

                except Exception:
                    print('error')
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Speak("We suggest you best Insurence policy ")
                    self.pushButton_2.setVisible(True)


            else:
                print(b.text() + " is deselected")

    def show(self):

        self.radioButton.setVisible(True)
        self.radioButton_2.setVisible(True)
    def voice(self):
        data =  self.plainTextEdit.toPlainText()
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak("Welcome"+data)
        self.voiceresult.setVisible(True)
        self.radioButton.setVisible(True)
        self.radioButton_2.setVisible(True)
        try:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")

            speaker.Speak(self.list1[self.d])

            self.voiceresult.setText(self.list1[self.d])
            print(self.d);
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)
            try:
                t = Timer(1.0, self.show)
                t.start()
            except Exception as e:
                print(e)
            print(self.d);
            self.d = self.d + 1;
        except Exception as e:
            print(e)
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("We suggest you best Insurence policy ")
            self.pushButton_2.setVisible(True)
    def next(self):
        pass




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Name"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Your Email ID"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.plainTextEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Your Mobile No"))
        self.voiceresult.setText(_translate("MainWindow", "Voice"))
        self.radioButton.setText(_translate("MainWindow", "yes"))
        self.radioButton_2.setText(_translate("MainWindow", "no"))
        self.pushButton_2.setText(_translate("MainWindow", "view"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

