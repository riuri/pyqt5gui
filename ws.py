#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore

class WebSocketTestApp(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(['Testing WebSockets'])
        #self.socket =

if __name__ == "__main__":
    app = WebSocketTestApp()
    app.start()
