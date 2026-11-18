import hashlib

def calculate_blake2(data):
    blake2_hash = hashlib.blake2b()
    blake2_hash.update(data.encode("utf-8"))

    return blake2_hash.hexdigest()


if __name__ == "__main__":
    data = input("Nhập chuỗi cần băm Blake2: ")

    result = calculate_blake2(data)

    print("Giá trị băm Blake2:", result)
