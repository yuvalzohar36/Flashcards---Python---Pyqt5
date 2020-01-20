# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flashcards.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_hardpage(object):
    def setupUi(self, hardpage):
        hardpage.setObjectName("hardpage")
        hardpage.resize(800, 600)
        self.index = 0
        self.hard_total = []
        self.centralwidget = QtWidgets.QWidget(hardpage)
        self.centralwidget.setObjectName("centralwidget")
        self.head = QtWidgets.QLabel(self.centralwidget)
        self.head.setGeometry(QtCore.QRect(230, 10, 371, 101))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(24)
        self.head.setFont(font)
        self.head.setObjectName("head")
        self.theword = QtWidgets.QLabel(self.centralwidget)
        self.theword.setGeometry(QtCore.QRect(40, 110, 311, 301))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(20)
        self.theword.setFont(font)
        self.theword.setObjectName("theword")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 460, 191, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 460, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.next_word)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 180, 311, 171))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        hardpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hardpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        hardpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hardpage)
        self.statusbar.setObjectName("statusbar")
        hardpage.setStatusBar(self.statusbar)
        self.create_list()
        self.match()


        self.retranslateUi(hardpage)
        QtCore.QMetaObject.connectSlotsByName(hardpage)

    def match(self):
        field = self.hard_total[self.index].split("|")
        hebrew_word = field[0]
        english_word = field[1]
        self.theword.setText(english_word)
        self.label.hide()
        self.label.setText(hebrew_word)

    def next_word(self):
        self.index += 1
        if self.index >= len(self.hard_total):
            self.index = 0
        self.match()

    def translate(self):
        self.label.show()

    def create_list(self):
        with open('hardlist.txt', 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            for line in lines:
                self.hard_total.append(line)
        print(self.hard_total)

    def retranslateUi(self, hardpage):
        _translate = QtCore.QCoreApplication.translate
        hardpage.setWindowTitle(_translate("hardpage", "hardpage"))
        self.head.setText(_translate("hardpage", "Flashcards - Words learning"))
        self.pushButton.setText(_translate("hardpage", "Show Translation"))
        self.pushButton_2.setText(_translate("hardpage", "Next Word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hardpage = QtWidgets.QMainWindow()
    ui = Ui_hardpage()
    ui.setupUi(hardpage)
    hardpage.show()
    sys.exit(app.exec_())
