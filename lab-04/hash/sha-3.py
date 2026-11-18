import hashlib


def calculate_sha3(data):
    sha3_hash = hashlib.sha3_256()
    sha3_hash.update(data.encode("utf-8"))

    return sha3_hash.hexdigest()


if __name__ == "__main__":
    data = input("Nhập chuỗi cần băm SHA-3: ")

    result = calculate_sha3(data)

    print("Giá trị băm SHA-3:", result)
