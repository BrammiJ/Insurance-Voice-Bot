
import sys

from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import *
import time
from threading import Timer
import win32com.client
from  allregister import Alldata
from  suggest import Ui_suggest_MainWindow
class Main(QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)

        # main button
        self.addButton = QPushButton('send')
        self.addButton.clicked.connect(self.addWidget)
        self.addButton.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                      "background-color: rgb(170, 255, 0);\n"
                      "border-color: rgb(85, 85, 0);\n"
                      "color: rgb(0, 85, 0);")
        self.addButton1 = QPushButton('Suggest Page')
        self.addButton1.setGeometry(QRect(30, 110, 241, 111))
        self.addButton1.clicked.connect(self.next)
        self.addButton1.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                     "background-color: rgb(170, 255, 0);\n"
                                     "border-color: rgb(85, 85, 0);\n"
                                     "color: rgb(0, 85, 0);")

        self.getdata = QPlainTextEdit()
        self.getdata.setMaximumSize(QSize(300,30))
        self.getdata.setStyleSheet("font: 24 12pt \"Times New Roman\";\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(85, 85, 0);\n"
                                        "color: rgb(0, 85, 0);")

        self.layout = QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(self.getdata)

        self.layout.addWidget(self.addButton)



        # scroll area widget contents - layout
        self.scrollLayout = QFormLayout()

        # scroll area widget contents
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.scrollWidget.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(85, 85, 0);\n"
                                     "color: rgb(0, 85, 0);")


        # scroll area
        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        # main layout
        self.mainLayout = QVBoxLayout()


        # add all main to the main vLayout

        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addLayout(self.layout)
        self.mainLayout.addWidget(self.addButton1)


        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.centralWidget.setMinimumWidth(400)
        self.centralWidget.setMinimumHeight(400)
        self.centralWidget.setStyleSheet("background-color: rgb(255, 85, 0);")
        # set central widget
        self.setCentralWidget(self.centralWidget)
    def next(self):
        self.window = QMainWindow();
        self.ui = Ui_suggest_MainWindow();
        self.ui.suggestsetupUi(self.window)

        self.window.show()
        pass
    def addWidget(self):
        a =  self.getdata.toPlainText()
        all = Alldata()
        if(a==""):
            print("enter data first")
            choice = QMessageBox.question(self, "Alert", "Please Enter Your Query",
                                                    QMessageBox.Ok)

            pass
        else:

            b = all.singlelikedatareturn(a)
            print(a)
           # b="the value is the value is the value is the value is the value is "
            self.scrollLayout.addRow(Test(a,b))




class Test(QWidget):
  a ='';
  b ='';
  def __init__( self, a,b,parent=None,):
      self.a =  a;
      self.b =  b;
      super(Test, self).__init__(parent)

      self.pushButton = QLabel("You :\n"+a)

      self.pushButton.move(30, 50)
      self.pushButton1 = QLabel()

      self.pushButton1.setText("Computer :\n"+b)




      layout = QVBoxLayout()
      layout.addWidget(self.pushButton)
      self.setLayout(layout)

      layout.addWidget(self.pushButton1)
      try:
          t = Timer(5.0, self.speak(b))
          t.start()
      except Exception as e:
          print(e)

  def speak(self, b):
      speaker = win32com.client.Dispatch("SAPI.SpVoice")

      speaker.Speak(b)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()
