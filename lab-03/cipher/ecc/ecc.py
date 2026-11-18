import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 55, 16))
        self.label_3.setObjectName("label_3")
        self.txt_Info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Info.setGeometry(QtCore.QRect(120, 120, 491, 87))
        self.txt_Info.setObjectName("txt_Info")
        self.txt_Signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Signature.setGeometry(QtCore.QRect(120, 260, 491, 87))
        self.txt_Signature.setObjectName("txt_Signature")
        self.btn_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Sign.setGeometry(QtCore.QRect(90, 390, 93, 28))
        self.btn_Sign.setObjectName("btn_Sign")
        self.btn_Verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Verify.setGeometry(QtCore.QRect(540, 390, 93, 28))
        self.btn_Verify.setObjectName("btn_Verify")
        self.btn_Generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Generate.setGeometry(QtCore.QRect(480, 30, 93, 28))
        self.btn_Generate.setObjectName("btn_Generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "informationl"))
        self.label_2.setText(_translate("MainWindow", "ECC CIPHER"))
        self.label_3.setText(_translate("MainWindow", "Signature"))
        self.btn_Sign.setText(_translate("MainWindow", "Sign"))
        self.btn_Verify.setText(_translate("MainWindow", "Verify"))
        self.btn_Generate.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
