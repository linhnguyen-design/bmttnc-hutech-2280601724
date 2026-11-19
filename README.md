# Bảo mật thông tin – HUTECH

Repository lưu trữ bài thực hành môn **Bảo mật thông tin**. Các bài được chia theo từng lab để dễ tìm mã nguồn, cài thư viện và chạy chương trình.

## Mục lục

- [Cấu trúc repository](#cấu-trúc-repository)
- [Yêu cầu môi trường](#yêu-cầu-môi-trường)
- [Cách chạy từng lab](#cách-chạy-từng-lab)
- [Lưu ý bảo mật](#lưu-ý-bảo-mật)
- [Tiến độ nội dung](#tiến-độ-nội-dung)

## Cấu trúc repository

```text
.
├── lab-01/                 # Bài tập Python cơ bản
│   ├── ex01/
│   ├── ex02/
│   ├── ex03/
│   └── ex04/
├── lab-02/                 # Caesar và các thuật toán mật mã cổ điển
│   ├── cipher/
│   ├── ex01/
│   └── templates/
├── lab-03/                 # Giao diện và API RSA, ECC, Caesar
│   ├── cipher/
│   ├── ui/
│   └── legacy_caesar_app/  # Bản Lab 3 cũ được giữ lại để tham khảo
├── lab-04/                 # Socket, Diffie-Hellman, Hash, WebSocket
│   ├── aes_rsa_socket/
│   ├── dh_key_pair/
│   ├── hash/
│   └── websocket/
├── README.md
└── .gitignore
```

> Các thư mục `lab-05` và `lab-06` chưa có trong bản ZIP được cung cấp nên chưa được tạo thêm.

## Yêu cầu môi trường

- Python 3.10 trở lên (khuyến nghị).
- Windows, macOS hoặc Linux.
- Terminal hoặc VS Code.

Nên tạo môi trường ảo riêng cho từng lab để tránh xung đột phiên bản thư viện.

### Tạo môi trường ảo trên Windows PowerShell

```powershell
cd lab-02
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell không cho phép kích hoạt, có thể gọi Python trong môi trường ảo bằng đường dẫn đầy đủ:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Cách chạy từng lab

### Lab 1 – Python cơ bản

Mở file cần thực hành trong `lab-01` và chạy:

```powershell
python .\ex01\hello.py
```

Các bài còn lại nằm trong `ex02`, `ex03` và `ex04`.

### Lab 2 – Caesar và mật mã cổ điển

Cài thư viện theo bài:

```powershell
cd lab-02
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install Flask requests
```

Chạy API Caesar:

```powershell
python .\app.py
```

Một số bài có thư mục `ex01` riêng và file `requirements.txt` riêng; hãy cài đúng requirements của thư mục bài đó.

### Lab 3 – RSA và ECC

```powershell
cd lab-03
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Chạy API:

```powershell
python .\api.py
```

Giao diện và các chương trình thực hành được đặt trong `ui/`, `cipher/` và các file Python ở thư mục `lab-03`. Kiểm tra tên file giao diện và module tương ứng trước khi chạy từng ứng dụng.

### Lab 4 – Socket, Diffie-Hellman, Hash và WebSocket

Mỗi phần có requirements riêng. Ví dụ:

```powershell
cd lab-04\aes_rsa_socket
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Mở hai Terminal:
- Terminal 1: chạy `server.py`.
- Terminal 2: chạy `client.py`.

Làm tương tự với `dh_key_pair/` và `websocket/`. Các chương trình hash trong `hash/` có thể chạy riêng theo từng file.

## Lưu ý bảo mật

- Không commit private key, token, mật khẩu hoặc file `.env`.
- Khóa RSA được tạo lại tại máy cá nhân khi cần; private key đã có trong bản ZIP gốc được loại khỏi bản sắp xếp để tránh chia sẻ khóa riêng.
- `server_public_key.pem` là khóa công khai dùng trong bài Diffie-Hellman nên được giữ lại.
- MD5 và các mật mã cổ điển chỉ phù hợp cho mục đích học tập, không dùng để bảo vệ dữ liệu thực tế.
- Các ví dụ trong repository là bài thực hành, cần rà soát và gia cố trước khi triển khai thật.

## Tiến độ nội dung

| Lab | Nội dung trong bản ZIP |
|---|---|
| Lab 1 | Python cơ bản |
| Lab 2 | Caesar, Playfair, Transposition, Vigenère, Rail Fence |
| Lab 3 | RSA, ECC, giao diện desktop và API |
| Lab 4 | Socket, AES/RSA, Diffie-Hellman, Hash, WebSocket |
| Lab 5 | Chưa có trong ZIP |
| Lab 6 | Chưa có trong ZIP |

---

**Sinh viên:** Nguyen Ha Linh  
**Mã số sinh viên:** 2280601724
