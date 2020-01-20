# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'title.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from flashcards import Ui_regularpage
from hardflashcards import Ui_hardpage


class Ui_MainWindow(object):
    def open_regular(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_regularpage()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def open_hard_page(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hardpage()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def open_hard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hardpage()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 611, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.marked = QtWidgets.QPushButton(self.centralwidget)
        self.marked.setGeometry(QtCore.QRect(630, 230, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.marked.setFont(font)
        self.marked.setObjectName("marked")
        self.marked.clicked.connect(self.open_hard_page)
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(300, 450, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.quit.setFont(font)
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.quit_window)
        self.regular = QtWidgets.QPushButton(self.centralwidget)
        self.regular.setGeometry(QtCore.QRect(80, 230, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.regular.setFont(font)
        self.regular.setObjectName("regular")
        self.regular.clicked.connect(self.open_regular)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @staticmethod
    def quit_window():
        app.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Flash Cards @yuvalzohar"))
        self.marked.setText(_translate("MainWindow", "Marked list"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.regular.setText(_translate("MainWindow", "Regular list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
