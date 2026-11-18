import hashlib


def calculate_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode("utf-8"))

    return sha256_hash.hexdigest()


if __name__ == "__main__":
    data = input("Nhập chuỗi cần băm SHA-256: ")

    result = calculate_sha256(data)

    print("Giá trị băm SHA-256:", result)
