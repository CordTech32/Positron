import threading
import typing

class Flask:
    def __init__(self, config:dict):
        self.title = config["name"]
        self.S_ADDR = config["flask_address"]
        self.app = config["flask_app"]

    def run_server(self, port=80):
        t = threading.Thread(target=lambda: self.app.run(self.S_ADDR.strip("http://"), port))
        t.start()