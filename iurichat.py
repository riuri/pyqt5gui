#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class ChatView(QtWebEngineWidgets.QWebEngineView):
    '''Try to make a simple HTML class'''
    def __init__(self):
        super().__init__()
        self.setUrl(QtCore.QUrl('http://www-scf.usc.edu/~lrezende/'))
        self.setZoomFactor(2)
    def toPlainText(self):
        return None

class ChatMainWindow(QtWidgets.QMainWindow):
    '''The main window for a simple chat'''
    def __init__(self, app):
        super().__init__()

if __name__ == '__main__':
    print('This is supposed to be a module')
