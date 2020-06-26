# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewdata.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  allregister import Alldata
import win32com.client
import re
from time import sleep
import sys
from scroll import Main
class Ui_data_Form(object):
    def loads(self):
        try:
            all = Alldata()
            a = all.alldatareturn()
            print (a)
        except Exception as e:
            print(e)
        load = ([1,2,8],[1,4,9],[1,7,6])
        self.tableWidget.setRowCount(0)



        for row_number,row_data in enumerate(a):
            self.tableWidget.insertRow(row_number)


            for column_number,data in enumerate(row_data):

                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        print("clicked")
        pass
    def mes(self,item):
        print(item.text())
        s = item.text()
        all = Alldata()

        a = all.singledatareturn(s)

        self.label.setText(re.sub("(.{50})", "\\1\n", a, 0, re.DOTALL))
        print(re.sub("(.{50})", "\\1\n", a, 0, re.DOTALL))
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak(a)

    def datasetupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        Form.setStyleSheet("border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 85, 0);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 110, 500, 261))
        self.tableWidget.setStyleSheet("font: 14pt \"Times New Roman\";background-color: rgb(255, 255, 255)")
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(1,1260)
        self.tableWidget.setHorizontalHeaderLabels(('S.No', 'Question'))
        #self.tableWidget.setHorizontalHeaderItem(0,QtWidgets.QTableWidget("name"));
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 390, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 16pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loads)
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(300, 390, 75, 23))
        self.pushButton2.setStyleSheet("color: rgb(0, 85, 0);\n"
                                      "background-color: rgb(255, 255, 127);\n"
                                      "border-color: rgb(85, 85, 0);\n"
                                      "font: 75 16pt \"Times New Roman\";")
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.chat)
        self.tableWidget.itemClicked.connect(self.mes)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 420, 500, 160))
        self.label.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"border-color: rgb(85, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.getdata = QtWidgets.QPlainTextEdit(Form)
        self.getdata.setGeometry(QtCore.QRect(20, 50, 331, 31))
        self.getdata.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "color: rgb(255, 85, 0);")
        self.getdata.setObjectName("getdata")
        self.getquery = QtWidgets.QPushButton(Form)
        self.getquery.setGeometry(QtCore.QRect(370, 55, 75, 23))
        self.getquery.setStyleSheet("color: rgb(0, 85, 0);\n"
                                    "font: 75 16pt \"Times New Roman\";\n"
                                    "background-color: rgb(255, 255, 127);")
        self.getquery.setObjectName("getquery")
        self.getquery.clicked.connect(self.filter)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def filter(self):
        data =  self.getdata.toPlainText();
        print(data)

        all = Alldata()

        a = all.singlelikedatareturn(data)
        print(a)
        full =""
        self.label.setText(re.sub("(.{50})", "\\1\n", a, 0, re.DOTALL))
        print(re.sub("(.{50})", "\\1\n", a, 0, re.DOTALL))
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak(a)
    def chat(self):
        print('chats')
        try:
            # self.window2 = QtWidgets.QMainWindow();
            #  self.ui2 = Ui_data_Form();
            #  self.ui2.datasetupUi(self.window2)

            # Form.hide()
            #  self.window2.show()
            self.myWidget = Main()
            #  Form.hide()
            self.myWidget.show()
            pass
        except Exception as  e:
            print(e)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setSortingEnabled(True)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "view"))
        self.pushButton2.setText(_translate("Form", "Chat"))
        self.label.setText(_translate("Form", "tap to the view buttion see that options"))
        self.getdata.setPlaceholderText(_translate("Form", "Enter the Questions"))
        self.getquery.setText(_translate("Form", "GET"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_data_Form()
    ui.datasetupUi(Form)
    Form.show()
    sys.exit(app.exec_())

