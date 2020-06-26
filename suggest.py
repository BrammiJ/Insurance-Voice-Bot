# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suggest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import win32com.client
from threading import Timer
#from fpdf import FPDF
from allregister import Alldata
class Ui_suggest_MainWindow(object):
    def loads(self):
        try:
            all = Alldata()
            a = all.suggestdata(self.dt)
            print(a)
        except Exception as e:
            print(e)
        load = ([1, 2, 8], [1, 4, 9], [1, 7, 6])
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(a):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        print("clicked")
        pass
    def suggestsetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 20, 271, 31))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 0);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(190, 70, 271, 31))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 0);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 180, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 16pt \"Times New Roman\";\n"
"color: rgb(85, 85, 0);\n"
"border-color: rgb(0, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.voice)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(190, 120, 271, 31))
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 0);")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")



        self.voiceresult = QtWidgets.QLabel(self.centralwidget)
        self.voiceresult.setGeometry(QtCore.QRect(260, 230, 471, 24))
        self.voiceresult.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";")
        self.voiceresult.setObjectName("voiceresult")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 310, 91, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 16pt \"Times New Roman\";\n"
"color: rgb(85, 85, 0);\n"
"border-color: rgb(0, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.suggest)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(490, 310, 91, 23))
        self.reset.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                        "font: 16pt \"Times New Roman\";\n"
                                        "color: rgb(85, 85, 0);\n"
                                        "border-color: rgb(0, 85, 0);")
        self.reset.setObjectName("pushButton_2")
        self.reset.clicked.connect(self.resetall)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 590, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(190, 270, 70, 17))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(390, 270, 70, 17))
        self.checkBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.next_question = QtWidgets.QPushButton(self.centralwidget)
        self.next_question.setGeometry(QtCore.QRect(190, 310, 75, 23))
        self.next_question.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 16pt \"Times New Roman\";\n"
"color: rgb(85, 85, 0);\n"
"border-color: rgb(0, 85, 0);")
        self.next_question.setObjectName("next_question")
        self.next_question.clicked.connect(self.analys)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 350, 648, 81))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnWidth(0, 600)
        self.tableWidget.itemClicked.connect(self.mes)
        self.tableWidget.setHorizontalHeaderLabels(('Suggetions', 'Question', 'keys'))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.printq = QtWidgets.QPushButton(self.centralwidget)
        self.printq.setGeometry(QtCore.QRect(290, 470, 75, 23))
        self.printq.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 16pt \"Times New Roman\";\n"
"color: rgb(85, 85, 0);\n"
"border-color: rgb(0, 85, 0);")
        self.printq.setObjectName("print")
        self.printq.clicked.connect(self.printdata)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.printq.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.tableWidget.setVisible(False)
        self.checkBox.setVisible(False)
        self.checkBox_2.setVisible(False)
        self.next_question.setVisible(False)
        self.voiceresult.setVisible(False)
        self.reset.setVisible(False)
        self.list1 = ["Do Have Car?", "Do You Have Bike", "You are age above 45", "Are You Married"]
        self.list2 = ["car", "bike", "above45", "Married"]
        self.dt = []
        self.d = 0
        self.result = ""

    def resetall(self):
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_3.setPlainText("")
        self.d= 0
        self.dt=[]
        self.tableWidget.setVisible(False)
        self.printq.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.reset.setVisible(False)

    def mes(self,item):
        print(item.text())
        self.selected =item.text()
        self.printq.setVisible(True)

    def voice(self):

        data = self.plainTextEdit.toPlainText()
        if(data =="" or self.plainTextEdit_2.toPlainText()=="" or self.plainTextEdit_3.toPlainText()==""):
            speaker = win32com.client.Dispatch("SAPI.SpVoice")

            speaker.Speak("please enter All fields")
        else:

            self.next_question.setVisible(True)
            self.checkBox.setVisible(True)
            self.checkBox_2.setVisible(True)
            self.voiceresult.setVisible(True)

            try:
                if (len(self.list1) > self.d):
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

    def draw_lines(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.line(10, 10, 10, 100)
        pdf.set_line_width(1)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(20, 20, 100, 20)

    def printdata(self):
        pdf = FPDF()
        pdf.add_page(orientation='p');
        name = self.plainTextEdit.toPlainText()
        email = self.plainTextEdit_2.toPlainText()
        mobile = self.plainTextEdit_3.toPlainText()
        pdf.set_font("Arial", size=12)
        #pdf.cell(100, 10, txt="Name : "+name, ln=1, align="C")
        #pdf.cell(100, 10, txt="Email : "+email, ln=1, align="C")
        #pdf.cell(100, 10, txt="Mobile :"+mobile, ln=1, align="C")

        #pdf.cell(100, 10, txt="Policy :"+self.selected, ln=1, align="C")
        pdf.cell(10)
        pdf.cell(0, 5, 'Name : '+name, ln=1)
        pdf.cell(10)
        pdf.cell(0, 5, 'Email :'+email, ln=1)
        pdf.cell(10)
        pdf.cell(0, 5, 'Mobile :'+mobile, ln=1)
        pdf.cell(0, 5, "", ln=1)
        pdf.cell(0, 5, '--------------', ln=1)
        pdf.cell(0, 5, "", ln=1)
        pdf.cell(10)

        pdf.cell(0, 5, 'Policy Type :'+self.selected, ln=1)

        # Line break
        pdf.ln(40)
        try:
            pdf.output(name+".pdf")
            print("printed")
        except Exception as e:
            print(e)

    def analys(self):
        if (self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==True):

            speaker = win32com.client.Dispatch("SAPI.SpVoice")

            speaker.Speak("Choose only one")
        elif(self.checkBox.isChecked()==False and self.checkBox_2.isChecked()==False):
            speaker = win32com.client.Dispatch("SAPI.SpVoice")

            speaker.Speak("Choose atleast one")
        else:
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

    def suggest(self):
        a = Alldata()
        data = self.dt
        print(a.suggestdata(data))
        self.tableWidget.setVisible(True)
        self.reset.setVisible(True)
        self.loads()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Name"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Your Email ID"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.plainTextEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Your Mobile No"))
        self.voiceresult.setText(_translate("MainWindow", "Voice"))
        self.pushButton_2.setText(_translate("MainWindow", "Suggested"))
        self.reset.setText(_translate("MainWindow", "reset"))
        self.radioButton_3.setText(_translate("MainWindow", "no"))
        self.checkBox.setText(_translate("MainWindow", "Yes"))
        self.checkBox_2.setText(_translate("MainWindow", "No"))
        self.next_question.setText(_translate("MainWindow", "Next"))
        self.printq.setText(_translate("MainWindow", "print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_suggest_MainWindow()
    ui.suggestsetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

