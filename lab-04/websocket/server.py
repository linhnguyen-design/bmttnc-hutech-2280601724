import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Danh sách trái cây
fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grape",
    "Watermelon",
    "Pineapple",
    "Strawberry"
]

# Danh sách client đang kết nối
clients = set()

class FruitWebSocket(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        # Cho phép client kết nối trong bài thực hành
        return True

    def open(self):
        clients.add(self)
        print("Client đã kết nối.")

    def on_message(self, message):
        print("Nhận từ client:", message)

    def on_close(self):
        clients.discard(self)
        print("Client đã ngắt kết nối.")


async def broadcast_fruit():
    fruit = random.choice(fruits)

    print("Server gửi:", fruit)

    # Gửi dữ liệu đến tất cả client
    disconnected = []

    for client in list(clients):
        try:
            await client.write_message(fruit)
        except tornado.websocket.WebSocketClosedError:
            disconnected.append(client)

    for client in disconnected:
        clients.discard(client)


def make_app():
    return tornado.web.Application([
        (r"/ws", FruitWebSocket),
    ])


def main():
    app = make_app()
    app.listen(8888)

    print("WebSocket server đang chạy tại ws://localhost:8888/ws")

    # Cứ 3 giây gửi một loại trái cây
    callback = tornado.ioloop.PeriodicCallback(
        broadcast_fruit,
        3000
    )

    callback.start()

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
