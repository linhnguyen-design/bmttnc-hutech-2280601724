
import sys
import requests

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

from ui.caesar import Ui_MainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    # Kiem tra Key
    def get_key(self):
        key_text = self.ui.lineEdit.text().strip()

        try:
            return int(key_text)

        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Key",
                "Vui long nhap Key la so nguyen!"
            )
            return None

    # Ma hoa Caesar
    def call_api_encrypt(self):
        key = self.get_key()

        if key is None:
            return

        url = "http://127.0.0.1:5000/api/caesar/encrypt"

        payload = {
            "plain_text": self.ui.textEdit.toPlainText(),
            "key": key
        }

        try:
            response = requests.post(
                url,
                json=payload,
                timeout=10
            )

            print("Encrypt status:", response.status_code)
            print("Encrypt response:", response.text)

            if response.status_code == 200:
                data = response.json()

                self.ui.textEdit_2.setPlainText(
                    data["encrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Encrypted Successfully"
                )

            else:
                QMessageBox.warning(
                    self,
                    "API Error",
                    response.text
                )

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self,
                "Connection Error",
                str(e)
            )

    # Giai ma Caesar
    def call_api_decrypt(self):
        key = self.get_key()

        if key is None:
            return

        cipher_text = self.ui.textEdit_2.toPlainText().strip()

        if not cipher_text:
            QMessageBox.warning(
                self,
                "Warning",
                "Vui long nhap Cipher Text!"
            )
            return

        url = "http://127.0.0.1:5000/api/caesar/decrypt"

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(
                url,
                json=payload,
                timeout=10
            )

            print("Decrypt status:", response.status_code)
            print("Decrypt response:", response.text)

            if response.status_code == 200:
                data = response.json()

                self.ui.textEdit.setPlainText(
                    data["decrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Decrypted Successfully"
                )

            else:
                QMessageBox.warning(
                    self,
                    "API Error",
                    response.text
                )

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self,
                "Connection Error",
                str(e)
            )

        except (ValueError, KeyError) as e:
            QMessageBox.critical(
                self,
                "Response Error",
                str(e)
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())
