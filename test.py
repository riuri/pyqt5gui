#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import hashlib

class SignedTextEdit(QtWidgets.QWidget):
    '''Widget for editing a text while displaying some checksums'''
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(['Iuri\'s weird application'])
    main_win = QtWidgets.QWidget()
    org = QtWidgets.QVBoxLayout()
    hello = QtWidgets.QLabel('Type some text and click the button')
    text = SignedTextEdit()
    button = button_printer_ender(app, text)
    org.addWidget(hello)
    org.addWidget(text)
    org.addWidget(button)
    main_win.setLayout(org)
    main_win.show()
    app.exec()
