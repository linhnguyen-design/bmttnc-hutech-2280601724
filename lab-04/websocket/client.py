
import tornado.ioloop
import tornado.websocket


SERVER_URL = "ws://localhost:8888/ws"


async def main():
    print("Đang kết nối đến WebSocket server...")

    try:
        websocket = await tornado.websocket.websocket_connect(
            SERVER_URL
        )

        print("Đã kết nối thành công.")
        print("Đang chờ dữ liệu từ server...\n")

        while True:
            message = await websocket.read_message()

            if message is None:
                print("Server đã đóng kết nối.")
                break

            print("Nhận được trái cây:", message)

    except Exception as error:
        print("Lỗi kết nối:", error)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
