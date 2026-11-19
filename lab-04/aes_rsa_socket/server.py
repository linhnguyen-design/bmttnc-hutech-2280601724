
import socket
import threading
import json
import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

HOST = "127.0.0.1"
PORT = 12345

clients = []
clients_lock = threading.Lock()


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
        "nonce": base64.b64encode(cipher.nonce).decode("utf-8"),
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
        "tag": base64.b64encode(tag).decode("utf-8")
    }


def decrypt_message(key, data):
    nonce = base64.b64decode(data["nonce"])
    ciphertext = base64.b64decode(data["ciphertext"])
    tag = base64.b64decode(data["tag"])

    cipher = AES.new(
        key,
        AES.MODE_GCM,
        nonce=nonce
    )

    plaintext = cipher.decrypt_and_verify(
        ciphertext,
        tag
    )

    return plaintext.decode("utf-8")


def broadcast(sender, message):
    with clients_lock:
        current_clients = clients.copy()

    for client in current_clients:
        if client is sender:
            continue

        try:
            encrypted = encrypt_message(
                client["aes_key"],
                message
            )

            send_json(client["socket"], encrypted)

        except (OSError, ValueError):
            print("Lỗi gửi tin nhắn đến Client.")


def handle_client(client_socket, address):
    print(f"[+] Client kết nối: {address}")

    client_file = client_socket.makefile(
        "r",
        encoding="utf-8"
    )

    client_info = None

    try:
        # Bước 1: Nhận Public Key từ Client
        public_data = receive_json(client_file)

        if not public_data or public_data.get("type") != "public_key":
            raise ValueError("Public Key không hợp lệ.")

        public_key = RSA.import_key(
            base64.b64decode(public_data["key"])
        )

        # Bước 2: Tạo AES Key 256 bit
        aes_key = get_random_bytes(32)

        # Bước 3: Mã hóa AES Key bằng RSA
        rsa_cipher = PKCS1_OAEP.new(public_key)

        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        send_json(client_socket, {
            "type": "aes_key",
            "key": base64.b64encode(
                encrypted_aes_key
            ).decode("utf-8")
        })

        client_info = {
            "socket": client_socket,
            "aes_key": aes_key,
            "address": address
        }

        with clients_lock:
            clients.append(client_info)

        print(f"[+] Trao đổi khóa thành công: {address}")

        # Bước 4: Nhận tin nhắn từ Client
        while True:
            data = receive_json(client_file)

            if data is None:
                break

            message = decrypt_message(aes_key, data)

            print(f"[{address}] {message}")

            if message.lower() == "exit":
                break

            broadcast(
                client_info,
                f"{address}: {message}"
            )

    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"[!] Lỗi Client {address}: {error}")

    finally:
        if client_info:
            with clients_lock:
                if client_info in clients:
                    clients.remove(client_info)

        client_file.close()
        client_socket.close()

        print(f"[-] Client ngắt kết nối: {address}")


def start_server():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server đang chạy tại {HOST}:{PORT}")

    try:
        while True:
            client_socket, address = server.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )

            thread.start()

    except KeyboardInterrupt:
        print("\nServer đang đóng...")

    finally:
        server.close()


if __name__ == "__main__":
    start_server()
