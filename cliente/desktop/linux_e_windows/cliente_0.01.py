import sys
import webd_library_3.0 as webd
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QUrl

class Client:
    def __init__(self, host, port, rsa_public_key_client, pgp_public_key_client):
        self.host = host
        self.port = port
        self.rsa_public_key_client = rsa_public_key_client
        self.pgp_public_key_client = pgp_public_key_client
        self.client = webd.WEBDClient(host, port, rsa_public_key_client, pgp_public_key_client)
        self.messages = []
        self.posts = []

    def connect(self):
        self.client.connect()

    def send_request(self, request):
        self.client.send_request(request)

    def receive_response(self):
        return self.client.receive_response()

    def add_message(self, message):
        self.messages.append(message)

    def add_post(self, post):
        self.posts.append(post)

    def get_messages(self):
        return self.messages

    def get_posts(self):
        return self.posts

class WebDWidget(QWidget):
    def __init__(self, client):
        super().__init__()

        self.client = client

        self.chat_input = QLineEdit()
        self.chat_input.returnPressed.connect(self.send_chat)

        self.post_input = QLineEdit()
        self.post_input.returnPressed.connect(self.send_post)

        self.chat_button = QPushButton("Send Chat")
        self.chat_button.clicked.connect(self.send_chat)

        self.post_button = QPushButton("Send Post")
        self.post_button.clicked.connect(self.send_post)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_input)
        layout.addWidget(self.chat_button)
        layout.addWidget(self.post_input)
        layout.addWidget(self.post_button)

        self.view = QWebEngineView()
        self.view.setContextMenuPolicy(Qt.NoContextMenu)
        self.view.setWindowTitle("WebD Client")
        self.view.resize(800, 600)
        self.view.load(QUrl("http://localhost:8000"))
        self.view.page().fullScreenRequested.connect(self.handle_full_screen_request)

        layout.addWidget(self.view)

        self.setLayout(layout)

    def send_chat(self):
        message = self.chat_input.text()
        self.client.add_message(message)
        self.chat_input.clear()

    def send_post(self):
        post = self.post_input.text()
        self.client.add_post(post)
        self.post_input.clear()

    def handle_full_screen_request(self, request):
        request.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    rsa_public_key_client = webd.load_rsa_public_key("rsa_public_key_client.pem")
    pgp_public_key_client = webd.load_pgp_public_key("pgp_public_key_client.asc")

    client = Client("localhost", 12345, rsa_public_key_client, pgp_public_key_client)

    widget = WebDWidget(client)
    widget.show()

    # simulate receiving messages and posts from the server
    import time
    for i in range(10):
        time.sleep(1)client.add_message(f"Message {i}")
        client.add_post(f"Post {i}")

    sys.exit(app.exec_())