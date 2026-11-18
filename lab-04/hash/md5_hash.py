import math
import struct


def left_rotate(value, shift):
    value &= 0xFFFFFFFF
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF


def md5(message):
    # Chuyển chuỗi thành bytes
    message = message.encode("utf-8")

    original_length = len(message) * 8

    # Padding theo chuẩn MD5
    message += b"\x80"

    while len(message) % 64 != 56:
        message += b"\x00"

    message += struct.pack("<Q", original_length)

    # Giá trị khởi tạo MD5
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Bảng hằng số
    constants = [
        int(abs(math.sin(i + 1)) * (2 ** 32)) & 0xFFFFFFFF
        for i in range(64)
    ]

    shifts = (
        [7, 12, 17, 22] * 4
        + [5, 9, 14, 20] * 4
        + [4, 11, 16, 23] * 4
        + [6, 10, 15, 21] * 4
    )

    # Xử lý từng khối 512 bit
    for offset in range(0, len(message), 64):
        block = message[offset:offset + 64]

        words = struct.unpack("<16I", block)

        a, b, c, d = a0, b0, c0, d0

        for i in range(64):
            if i < 16:
                f = (b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + constants[i] + words[g]) & 0xFFFFFFFF

            a, d, c, b = (
                d,
                c,
                b,
                (b + left_rotate(f, shifts[i])) & 0xFFFFFFFF
            )

        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    return struct.pack("<4I", a0, b0, c0, d0).hex()


if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")

    result = md5(input_string)

    print("Mã băm MD5:", result)
