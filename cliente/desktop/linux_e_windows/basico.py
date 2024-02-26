import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)
        self.webView = QWebEngineView()
        self.setCentralWidget(self.webView)

        self.button1 = QPushButton('Button 1', self)
        self.button1.clicked.connect(self.loadPage1)
        self.button1.setGeometry(50, 500, 100, 40)

        self.button2 = QPushButton('Button 2', self)
        self.button2.clicked.connect(self.loadPage2)
        self.button2.setGeometry(200, 500, 100, 40)

        # Add more buttons as needed

        self.loadPage1()

    def loadPage1(self):
        self.webView.load(QUrl('file:///path/to/index1.html'))

    def loadPage2(self):
        self.webView.load(QUrl('file:///path/to/index2.html'))

    # Define more methods to load other pages

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())