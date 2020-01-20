# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flashcards.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_regularpage(object):
    def setupUi(self, regularpage):
        regularpage.setObjectName("regularpage")
        regularpage.resize(800, 600)
        self.index=0
        self.english_list = []
        self.total_list = []
        self.hard = []
        self.centralwidget = QtWidgets.QWidget(regularpage)
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 250, 81, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.hard_list)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 320, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.hide()
        regularpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(regularpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        regularpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(regularpage)
        self.statusbar.setObjectName("statusbar")
        regularpage.setStatusBar(self.statusbar)
        self.word_list_english()
        self.word_list_total()
        self.match()

        self.retranslateUi(regularpage)
        QtCore.QMetaObject.connectSlotsByName(regularpage)

    def word_list_english(self):
        with open('english.txt', 'r', encoding='utf-8') as english:
                lines = english.read().splitlines()
                for line in lines:
                    line.rstrip('\n')
                    self.english_list.append(line)

    def word_list_total(self):
        with open('hebrew.txt', 'r', encoding='utf-8') as hebrew:
                lines = hebrew.read().splitlines()
                i = 0
                for line in lines:
                    line.rstrip('\n')
                    self.total_list.append(line + "|"+self.english_list[i])
                    i += 1
        random.shuffle(self.total_list)

    def match(self):
        field = self.total_list[self.index].split("|")
        hebrew_word = field[0]
        english_word = field[1]
        self.theword.setText(english_word)
        self.label.hide()
        self.label.setText(hebrew_word)

    def next_word(self):
        self.index += 1
        if self.index >= len(self.total_list):
            self.index = 0
        self.match()
        self.label_2.hide()

    def translate(self):
        self.label.show()

    def hard_list(self):
        self.label_2.show()
        word = self.total_list[self.index]
        self.hard.append(word)
        with open('hardlist.txt', 'a', encoding = 'utf-8') as f:
            f.write(word)
            f.write("\n")

    def retranslateUi(self, regularpage):
        _translate = QtCore.QCoreApplication.translate
        regularpage.setWindowTitle(_translate("regularpage", "regularpage"))
        self.head.setText(_translate("regularpage", "Flashcards - Words learning"))
        self.pushButton.setText(_translate("regularpage", "Show Translation"))
        self.pushButton_2.setText(_translate("regularpage", "Next Word"))
        self.pushButton_3.setText(_translate("regularpage", "Mark it"))
        self.label_2.setText(_translate("regularpage", "Added ! "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regularpage = QtWidgets.QMainWindow()
    ui = Ui_regularpage()
    ui.setupUi(regularpage)
    regularpage.show()
    sys.exit(app.exec_())
