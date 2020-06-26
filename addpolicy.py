# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addpolicy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from allregister import Alldata
from PyQt5.QtWidgets import QMessageBox
class Ui_policy_MainWindow(QtWidgets.QMainWindow):
    def loads(self):
        try:
            all = Alldata()
            a = all.allpolicyreturn()
            print(a)
        except Exception as e:
            print(e)
        load = ([1, 2, 8], [1, 4, 9], [1, 7, 6])
        self.all_data.setRowCount(0)

        for row_number, row_data in enumerate(a):
            self.all_data.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.all_data.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        print("clicked")
        pass
    def policysetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 619)
        MainWindow.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(460, 0, 20, 311))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.delete_policy_number = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.delete_policy_number.setGeometry(QtCore.QRect(570, 30, 81, 31))
        self.delete_policy_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.delete_policy_number.setObjectName("delete_policy_number")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 40, 81, 16))
        self.label.setObjectName("label")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(670, 30, 75, 23))
        self.btn_delete.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 14pt \"Arial\";\n"
"color: rgb(0, 85, 0);")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.delete)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(470, 80, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.add_policy_number = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.add_policy_number.setGeometry(QtCore.QRect(20, 20, 171, 31))
        self.add_policy_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.add_policy_number.setObjectName("add_policy_number")
        self.add_policy = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.add_policy.setGeometry(QtCore.QRect(20, 70, 381, 81))
        self.add_policy.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.add_policy.setObjectName("add_policy")

        self.choose_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.choose_dropdown.setGeometry(QtCore.QRect(20, 170, 101, 31))
        self.choose_dropdown.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.choose_dropdown.setObjectName("choose_dropdown")
        self.choose_dropdown.currentIndexChanged.connect(self.selectionchange)
        self.save_keyword = QtWidgets.QPushButton(self.centralwidget)
        self.save_keyword.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.save_keyword.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 14pt \"Arial\";\n"
"color: rgb(0, 85, 0);")
        self.save_keyword.setObjectName("save_keyword")
        self.save_keyword.clicked.connect(self.addkeywords)
        self.savepolicy = QtWidgets.QPushButton(self.centralwidget)
        self.savepolicy.setGeometry(QtCore.QRect(20, 220, 81, 31))
        self.savepolicy.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 14pt \"Arial\";\n"
"color: rgb(0, 85, 0);")
        self.savepolicy.setObjectName("savepolicy")
        self.savepolicy.clicked.connect(self.save)
        self.update_polocy_number = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.update_polocy_number.setGeometry(QtCore.QRect(480, 110, 104, 31))
        self.update_polocy_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.update_polocy_number.setObjectName("update_polocy_number")
        self.update_policy = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.update_policy.setGeometry(QtCore.QRect(480, 150, 291, 71))
        self.update_policy.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.update_policy.setObjectName("update_policy")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 240, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-color: rgb(85, 85, 0);\n"
"font: 75 14pt \"Arial\";\n"
"color: rgb(0, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 300, 821, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.all_data = QtWidgets.QTableWidget(self.centralwidget)
        self.all_data.setGeometry(QtCore.QRect(0, 300, 801, 301))
        self.all_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.all_data.setRowCount(1)
        self.all_data.setColumnCount(3)
        self.all_data.setObjectName("all_data")
        self.all_data.setColumnWidth(1, 600)
        self.all_data.setColumnWidth(2, 200)
        self.all_data.setHorizontalHeaderLabels(('S.No', 'Question','keys'))
        item = QtWidgets.QTableWidgetItem()
        self.all_data.setItem(0, 1, item)
        self.all_data.itemClicked.connect(self.mes)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loads()
        self.loads1()
        self.allkeys=""
    def selectionchange(self, i):

        try:
            for count in range(self.choose_dropdown.count()):
                self.allkwyqords=self.choose_dropdown.currentText();
            self.allkeys += self.allkwyqords+","
            pass
        except Exception as e:
            print(e)
    def addkeywords(self):
        print(self.allkeys)
        pass
    def save(self):
        print(self.allkeys)
        num =  self.add_policy_number.toPlainText()
        policy =  self.add_policy.toPlainText()
        if(num=="" or policy==""):
            pass
        else:

            a =  Alldata()
            a.insertpolicy(num,policy,self.allkeys)
            self.loads()
            self.allkeys=""
            self.add_policy_number.setPlainText("")
            self.add_policy.setPlainText("")
            self.choose_dropdown.clear()
            self.loads1()

    def loads1(self):
        data = ["Choose plan","car","bike","above45","married"]
        self.choose_dropdown.addItems(data)

    def update(self):
        num =  self.update_polocy_number.toPlainText()
        policy =  self.update_policy.toPlainText()
        if(num=="" or policy==""):
            pass
        else:
            a = Alldata()
            print(a.updatepolicy(num,policy))
            da = a.updatepolicy(num,policy)
            print(da)
            if (da):
                choice = QtWidgets.QMessageBox.question(self, "Alert", "Updated successfully",
                                                        QtWidgets.QMessageBox.Ok)

                if choice == QtWidgets.QMessageBox.Ok:
                    self.loads()

                else:
                    pass
            else:
                pass
            pass
    def delete(self):
        print(self.delete_policy_number.toPlainText())
        data = self.delete_policy_number.toPlainText()


        try:
            if(data==""):

                choice = QtWidgets.QMessageBox.question(self, "Alert", "Please enter the Policy number", QtWidgets.QMessageBox.Ok )

                if choice == QtWidgets.QMessageBox.Ok:
                    pass

                else:
                    pass
            else:
                a = Alldata()
                print(a.deletepolicy(data))
                da = a.deletepolicy(data)
                print(da)
                if(da):
                    choice = QtWidgets.QMessageBox.question(self, "Alert", "Deleted successfully",
                                                            QtWidgets.QMessageBox.Ok)

                    if choice == QtWidgets.QMessageBox.Ok:
                        self.loads()

                    else:
                        pass

                else:
                    choice = QtWidgets.QMessageBox.question(self, "Alert", "Sorry Not deleted",
                                                            QtWidgets.QMessageBox.Ok)

                    if choice == QtWidgets.QMessageBox.Ok:
                        pass

                    else:
                        pass

        except Exception as e:
            print(e)

    def mes(self,item):
        print(item.text())
        try:
            a =  Alldata()
            print(a.singlepolicyreturn(item.text()))
            data = a.singlepolicyreturn(item.text())
            print (data[0][0])

            self.update_polocy_number.setPlainText(str(data[0][0]))
            self.update_policy.setPlainText(str(data[0][1]))
            self.delete_policy_number.setPlainText(str(data[0][0]))
        except Exception as e:
            print(e)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.delete_policy_number.setPlaceholderText(_translate("MainWindow", "policy number"))
        self.label.setText(_translate("MainWindow", "Delete Policy"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.add_policy_number.setPlaceholderText(_translate("MainWindow", "policy number"))
        self.add_policy.setPlaceholderText(_translate("MainWindow", "policy"))
        self.save_keyword.setText(_translate("MainWindow", "Add"))
        self.savepolicy.setText(_translate("MainWindow", "Save"))
        self.update_polocy_number.setPlaceholderText(_translate("MainWindow", "policy number"))
        self.update_policy.setPlaceholderText(_translate("MainWindow", "policy"))
        self.pushButton.setText(_translate("MainWindow", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_policy_MainWindow()
    ui.policysetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

