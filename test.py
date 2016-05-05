#!/usr/bin/env python3

from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(['Iuri\'s weird application'])
    main_win = QtWidgets.QWidget()
    org = QtWidgets.QVBoxLayout()
    hello = QtWidgets.QLabel('Olá mundo unicode')
    text = QtWidgets.QTextEdit()
    button = QtWidgets.QPushButton('Quit')
    button.clicked.connect(app.quit)
    org.addWidget(hello)
    org.addWidget(text)
    org.addWidget(button)
    main_win.setLayout(org)
    main_win.show()
    app.exec()
    print('end')
