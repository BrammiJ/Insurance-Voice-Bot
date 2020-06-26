# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.pushButton = QtWidgets.QPushButton(Form)

        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("wecome")
        self.mainLayout = QtWidgets.QVBoxLayout()


        self.scrollLayout = QtWidgets.QFormLayout(Form)

        # scroll area widget contents
        self.scrollWidget = QtWidgets.QWidget(Form)
        self.scrollWidget.setLayout(self.scrollLayout)


        # scroll area
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        self.mainLayout.addChildWidget(self.pushButton)
        self.mainLayout.addChildWidget(self.scrollArea)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

