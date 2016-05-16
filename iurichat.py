#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class ChatView(QtWebEngineWidgets.QWebEngineView):
    '''Try to make a simple HTML class'''
    header_css = '''<html>
    <head>
    <style type='text/css'>
    .me {
        text-align: right;
        color: blue;
    }
    .other {
        text-align: left;
        color: red;
    }
    </style>
    </head>
    <body>'''
    footer = '</body></html>'
    def __init__(self):
        super().__init__()
        self.chatHtmlContent = ''
        self.setHtml(self.header_css+self.chatHtmlContent+self.footer)
        self.setZoomFactor(2)

class TypeBox(QtWidgets.QWidget):
    '''A text box and a button for submitting'''
    def __init__(self, button_text):
        super().__init__()
        self.input = QtWidgets.QTextEdit()
        self.button = QtWidgets.QPushButton(button_text)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addWidget(self.input)
        self.layout().addWidget(self.button)

class MainChatWidget(QtWidgets.QWidget):
    '''A widget for a running chat'''
    def __init__(self):
        super().__init__()
        self.chat = ChatView()
        self.textInput = TypeBox('Submit')
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.chat)
        self.layout().addWidget(self.textInput)

class ChatMainWindow(QtWidgets.QMainWindow):
    '''The main window for a simple chat'''
    def __init__(self, app):
        super().__init__()
        self.chat = MainChatWidget()
        self.setCentralWidget(self.chat)

if __name__ == '__main__':
    print('This is supposed to be a module')
