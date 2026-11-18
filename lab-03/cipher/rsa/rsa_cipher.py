import rsa
import os
import binascii

class RSACipher:

    def __init__(self):
        self.key_folder = os.path.join(
            os.path.dirname(__file__), "keys"
        )
        os.makedirs(self.key_folder, exist_ok=True)

        self.public_key_path = os.path.join(
            self.key_folder, "publicKey.pem"
        )
        self.private_key_path = os.path.join(
            self.key_folder, "privateKey.pem"
        )

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(2048)

        with open(self.public_key_path, "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))

        with open(self.private_key_path, "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

    def load_keys(self):
        with open(self.public_key_path, "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open(self.private_key_path, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        return public_key, private_key

    def encrypt(self, message, key):
        encrypted = rsa.encrypt(
            message.encode("utf-8"), key
        )
        return binascii.hexlify(encrypted).decode("utf-8")

    def decrypt(self, cipher_text, key):
        encrypted = binascii.unhexlify(cipher_text)
        decrypted = rsa.decrypt(encrypted, key)
        return decrypted.decode("utf-8")

    def sign(self, message, private_key):
        signature = rsa.sign(
            message.encode("utf-8"),
            private_key,
            "SHA-256"
        )
        return binascii.hexlify(signature).decode("utf-8")

    def verify(self, message, signature, public_key):
        try:
            signature_bytes = binascii.unhexlify(signature)

            result = rsa.verify(
                message.encode("utf-8"),
                signature_bytes,
                public_key
            )

            return result == "SHA-256"

        except (rsa.VerificationError, ValueError):
            return False