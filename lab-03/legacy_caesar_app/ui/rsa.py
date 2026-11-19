from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(20, 20, 300, 100))

        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(20, 140, 300, 100))

        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(350, 20, 300, 100))

        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(350, 140, 300, 100))

        self.btngenkeys = QtWidgets.QPushButton("Generate Keys", self.centralwidget)
        self.btngenkeys.setGeometry(QtCore.QRect(20, 270, 150, 40))

        self.btnEncrypt = QtWidgets.QPushButton("Encrypt", self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(180, 270, 100, 40))

        self.btnDecrypt = QtWidgets.QPushButton("Decrypt", self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(290, 270, 100, 40))

        self.btnsign = QtWidgets.QPushButton("Sign", self.centralwidget)
        self.btnsign.setGeometry(QtCore.QRect(400, 270, 100, 40))

        self.btnverify = QtWidgets.QPushButton("Verify", self.centralwidget)
        self.btnverify.setGeometry(QtCore.QRect(510, 270, 100, 40))