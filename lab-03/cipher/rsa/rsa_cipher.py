import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btngenkeys.clicked.connect(self.call_api_gen_keys)
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btnsign.clicked.connect(self.call_api_sign)
        self.ui.btnverify.clicked.connect(self.call_api_verify)

    # Generate RSA Keys
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                QMessageBox.information(
                    self,
                    "Generate Keys",
                    data["message"]
                )
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print("Error:", e)


    # Encrypt
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"

        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_cipher_text.setText(
                    data["encrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Encrypt",
                    "Encrypted Successfully"
                )

            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print("Error:", e)


    # Decrypt
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"

        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_plain_text.setText(
                    data["decrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Decrypt",
                    "Decrypted Successfully"
                )

            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print("Error:", e)


    # Sign
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"

        payload = {
            "message": self.ui.txt_info.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_sign.setText(
                    data["signature"]
                )

                QMessageBox.information(
                    self,
                    "Sign",
                    "Signed Successfully"
                )

            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print("Error:", e)


    # Verify
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"

        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                if data["is_verified"]:
                    QMessageBox.information(
                        self,
                        "Verify",
                        "Verified Successfully"
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Verify",
                        "Verified Failed"
                    )

            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print("Error:", e)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())