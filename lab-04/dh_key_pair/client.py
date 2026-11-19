from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes


def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    return private_key, public_key


def derive_shared_secret(private_key, peer_public_key):
    # Tính bí mật chung Diffie-Hellman
    shared_key = private_key.exchange(peer_public_key)

    # Dẫn xuất khóa có độ dài 32 byte
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"dh-key-pair-demo"
    ).derive(shared_key)

    return derived_key


def main():
    # Đọc khóa công khai của server
    with open("server_public_key.pem", "rb") as file:
        server_public_key = serialization.load_pem_public_key(
            file.read()
        )

    # Lấy tham số DH từ khóa công khai server
    parameters = server_public_key.parameters()

    # Tạo cặp khóa của client
    client_private_key, client_public_key = (
        generate_client_key_pair(parameters)
    )

    # Tính khóa bí mật chung
    shared_secret = derive_shared_secret(
        client_private_key,
        server_public_key
    )

    print("Khóa công khai của client:")
    print(
        client_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode("utf-8")
    )

    print("Thông điệp bí mật được tạo từ khóa chung:")
    print(shared_secret.hex())


if __name__ == "__main__":
    main()
