from cipher.rsa import RSACipher

if __name__ == "__main__":

    rsa = RSACipher()

    print("=== RSA ENCRYPTION ===")

    # Tạo khóa
    rsa.generate_keys()

    # Đọc khóa
    public_key, private_key = rsa.load_keys()

    # Nhập plaintext
    message = input("Enter plaintext: ")

    # Mã hóa bằng public key
    encrypted = rsa.encrypt(message, public_key)

    print("\nCiphertext:")
    print(encrypted)

    # Giải mã bằng private key
    decrypted = rsa.decrypt(encrypted, private_key)

    print("\nDecrypted text:")
    print(decrypted)