#!/usr/bin/env python3

from PyQt5 import QtWidgets


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
    text = QtWidgets.QTextEdit()
    button = button_printer_ender(app, text)
    org.addWidget(hello)
    org.addWidget(text)
    org.addWidget(button)
    main_win.setLayout(org)
    main_win.show()
    app.exec()
