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
    def addMsg(self, msg, who = None):
        '''Add a new message to the chat view. When who is None,
        it is considered from the sender itself
        '''
        htmlClass = 'me' if who == None else 'other'
        #TODO: treat XML code on msg
        self.chatHtmlContent += "<div class='%s'>%s</div>"%(htmlClass, msg)
        self.setHtml(self.header_css+self.chatHtmlContent+self.footer)
        self.setZoomFactor(2)


class TypeBox(QtWidgets.QWidget):
    '''A text box and a button for submitting'''
    textSubmitted = pyqtSignal(str)
    def __init__(self, button_text):
        super().__init__()
        self.input = QtWidgets.QLineEdit()
        self.input.returnPressed.connect(self.requestedSubmission)
        self.button = QtWidgets.QPushButton(button_text)
        self.button.clicked.connect(self.requestedSubmission)

        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addWidget(self.input)
        self.layout().addWidget(self.button)
    #@pyqtSlot('void')
    def requestedSubmission(self):
        '''Called upon button press'''
        text = self.input.text()
        self.input.setText('')
        self.textSubmitted.emit(text)
    def refocus(self):
        self.input.setFocus(0)


class MainChatWidget(QtWidgets.QWidget):
    '''A widget for a running chat'''
    def __init__(self):
        super().__init__()
        self.chat = ChatView()
        self.textInput = TypeBox('Submit')
        self.textInput.textSubmitted.connect(self._send_msg)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.chat)
        self.layout().addWidget(self.textInput)
    @pyqtSlot(str)
    def _send_msg(self, msg):
        '''Used to send messages when user submits text
        via the TypeBox
        '''
        self.chat.addMsg(msg)
        self.textInput.refocus()

class ChatMainWindow(QtWidgets.QMainWindow):
    '''The main window for a simple chat'''
    def __init__(self, app):
        super().__init__()
        self.chat = MainChatWidget()
        self.setCentralWidget(self.chat)

if __name__ == '__main__':
    print('This is supposed to be a module')
