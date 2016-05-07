#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import hashlib

class SignedTextEdit(QtWidgets.QWidget):
    '''Widget for editing a text while displaying some checksums'''
    textChanged = pyqtSignal(str)
    def __init__(self, initial_text=''):
        '''Creates the widget with optionally an initial text'''
        QtWidgets.QWidget.__init__(self)
        self.my_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.my_layout)
        self.my_text = QtWidgets.QTextEdit(initial_text)
        self.my_layout.addWidget(self.my_text)
        self.sha1label = QtWidgets.QLabel(self._sha1_string())
        self.my_layout.addWidget(self.sha1label)
        self.my_text.textChanged.connect(self._update_label)
    def _sha1_string(self):
        '''Computes the string to be displayed on the label'''
        text = self.my_text.toPlainText()
        return 'SHA1: '+hashlib.sha1(text.encode()).hexdigest()
    @pyqtSlot('void', name='update_label', result='void')
    def _update_label(self):
        '''Slot to update the label'''
        self.sha1label.setText(self._sha1_string())
        self.textChanged.emit(self.toPlainText())
    def toPlainText(self):
        '''Wrapper'''
        return self.my_text.toPlainText()


class button_printer_ender(QtWidgets.QPushButton):
    '''Class for a button that prints a QTextEdit and ends a QApplication'''
    def __init__(self, application, textedit):
        QtWidgets.QPushButton.__init__(self, 'Print and quit')
        self.app = application
        self.txt = textedit
        self.clicked.connect(self._callback)
    def _callback(self, **kwargs):
        print(self.txt.toPlainText())
        self.app.quit()

class application_central_widget(QtWidgets.QWidget):
    '''The central widget that will be displayed in the main window'''
    def __init__(self, app):
        QtWidgets.QWidget.__init__(self)
        self.org = QtWidgets.QVBoxLayout()
        self.hello = QtWidgets.QLabel('Type some text and click the button')
        self.text = SignedTextEdit()
        self.button = button_printer_ender(app, self.text)
        self.org.addWidget(self.hello)
        self.org.addWidget(self.text)
        self.org.addWidget(self.button)
        self.setLayout(self.org)

class iuris_test_application(QtWidgets.QApplication):
    '''The main class for this application. Make it easy for use in main'''
    def __init__(self):
        QtWidgets.QApplication.__init__(self, ['Iuri\'s weird application'])
        self.main_win = QtWidgets.QMainWindow()
        self.central = application_central_widget(self)
        self.main_win.setCentralWidget(self.central)
    def start(self):
        self.main_win.show()
        self.exec()


if __name__ == '__main__':
    app = iuris_test_application()
    app.start()
