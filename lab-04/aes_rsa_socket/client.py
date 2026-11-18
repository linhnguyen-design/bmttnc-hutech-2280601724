
import socket
import threading
import json
import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

HOST = "127.0.0.1"
PORT = 12345


def send_json(sock, data):
    message = json.dumps(data).encode("utf-8") + b"\n"
    sock.sendall(message)


def receive_json(file):
    line = file.readline()

    if not line:
        return None

    return json.loads(line.decode("utf-8"))


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_GCM)

    ciphertext, tag = cipher.encrypt_and_digest(
        message.encode("utf-8")
    )

    return {
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "tag": base64.b64encode(tag).decode()
    }


def decrypt_message(key, data):
    nonce = base64.b64decode(data["nonce"])
    ciphertext = base64.b64decode(data["ciphertext"])
    tag = base64.b64decode(data["tag"])

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(
        ciphertext, tag
    )

    return plaintext.decode("utf-8")


def receive_messages(client_file, aes_key):
    while True:
        try:
            data = receive_json(client_file)

            if data is None:
                print("\nServer đã ngắt kết nối.")
                break

            message = decrypt_message(aes_key, data)
            print("\nTin nhắn nhận được:", message)

        except Exception as error:
            print("\nLỗi nhận tin nhắn:", error)
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_file = None

    try:
        # Kết nối Server
        client.connect((HOST, PORT))
        print("Đã kết nối Server.")

        client_file = client.makefile("r", encoding="utf-8")

        # Tạo cặp khóa RSA
        private_key = RSA.generate(2048)
        public_key = private_key.publickey()

        # Gửi Public Key cho Server
        public_key_data = base64.b64encode(
            public_key.export_key()
        ).decode("utf-8")

        send_json(client, {
            "type": "public_key",
            "key": public_key_data
        })

        # Nhận AES Key
        response = receive_json(client_file)

        if not response or response.get("type") != "aes_key":
            raise ValueError("Server không gửi AES Key hợp lệ.")

        encrypted_aes_key = base64.b64decode(response["key"])

        # Giải mã AES Key bằng RSA Private Key
        rsa_cipher = PKCS1_OAEP.new(private_key)
        aes_key = rsa_cipher.decrypt(encrypted_aes_key)

        print("Trao đổi khóa RSA thành công.")
        print("AES-GCM đã sẵn sàng.")
        print("Nhập exit để thoát.")

        # Thread nhận tin nhắn
        thread = threading.Thread(
            target=receive_messages,
            args=(client_file, aes_key),
            daemon=True
        )

        thread.start()

        # Gửi tin nhắn
        while True:
            message = input("Bạn: ")

            encrypted = encrypt_message(aes_key, message)
            send_json(client, encrypted)

            if message.lower() == "exit":
                break

    except Exception as error:
        print("Lỗi Client:", error)

    finally:
        if client_file:
            client_file.close()

        client.close()
        print("Đã đóng Client.")


if __name__ == "__main__":
    main()
