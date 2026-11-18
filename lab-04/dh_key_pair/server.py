from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization


def generate_dh_parameters():
    # Tạo tham số Diffie-Hellman
    parameters = dh.generate_parameters(
        generator=2,
        key_size=2048
    )
    return parameters


def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    return private_key, public_key


def main():
    parameters = generate_dh_parameters()

    private_key, public_key = generate_server_key_pair(
        parameters
    )

    # Lưu khóa công khai của server
    with open("server_public_key.pem", "wb") as file:
        file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("Đã tạo khóa Diffie-Hellman.")
    print("Đã lưu khóa công khai vào server_public_key.pem")


if __name__ == "__main__":
    main()
