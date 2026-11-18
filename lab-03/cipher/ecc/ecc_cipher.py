import os
import hashlib
from ecdsa import SigningKey, VerifyingKey, NIST256p
from ecdsa.util import sigencode_string, sigdecode_string


class ECCCipher:

    def __init__(self):
        self.key_folder = os.path.join(
            os.path.dirname(__file__), "keys"
        )
        os.makedirs(self.key_folder, exist_ok=True)

        self.private_path = os.path.join(
            self.key_folder, "privateKey.pem"
        )
        self.public_path = os.path.join(
            self.key_folder, "publicKey.pem"
        )

    def generate_keys(self):
        private_key = SigningKey.generate(
            curve=NIST256p
        )
        public_key = private_key.verifying_key

        with open(self.private_path, "wb") as f:
            f.write(private_key.to_pem())

        with open(self.public_path, "wb") as f:
            f.write(public_key.to_pem())

    def load_keys(self):
        with open(self.private_path, "rb") as f:
            private_key = SigningKey.from_pem(f.read())

        with open(self.public_path, "rb") as f:
            public_key = VerifyingKey.from_pem(f.read())

        return private_key, public_key

    def sign(self, message, private_key):
        signature = private_key.sign(
            message.encode("utf-8"),
            hashfunc=hashlib.sha256,
            sigencode=sigencode_string
        )

        return signature.hex()

    def verify(self, message, signature, public_key):
        try:
            return public_key.verify(
                bytes.fromhex(signature),
                message.encode("utf-8"),
                hashfunc=hashlib.sha256,
                sigdecode=sigdecode_string
            )
        except Exception:
            return False