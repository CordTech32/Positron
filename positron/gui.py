from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class Chromium(QMainWindow):

    def __init__(self, flaskified, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.app = flaskified

    def setup(self, flaskified):
        self.window = QWidget()
        self.window.setWindowTitle(flaskified.title)

        self.window.setGeometry(50,50, 700, 500)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.__browser = QWebEngineView(self)

        self.layout.addWidget(self.__browser)
        print(flaskified.S_ADDR)
        self.__browser.setUrl(QUrl("http://"+flaskified.S_ADDR))

        self.window.setLayout(self.layout)
        self.window.show()
    

    def run(self):
        self.setup(self.app)
        app.exec_()

app = QApplication([])
