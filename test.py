#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import hashlib
import iurichat

class SignedTextEdit(QtWidgets.QWidget):
    '''Widget for editing a text while displaying some checksums'''
    textChanged = pyqtSignal(str)
    def __init__(self, initial_text=''):
        '''Creates the widget with optionally an initial text'''
        super().__init__()
        self.my_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.my_layout)
        self.my_text = QtWidgets.QTextEdit(initial_text)
        self.setText = self.my_text.setText
        self.toPlainText = self.my_text.toPlainText
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
    def open_text(self, filename):
        '''Opens a file and sets the text to the contents of the file'''
        with open(filename, 'r') as f:
            contents = f.read()
            self.setText(contents)
    def save_text(self, filename):
        '''Saves the contents of the textEdit to the file'''
        with open(filename, 'w') as f:
            contents = self.toPlainText()
            f.write(contents)

class ButtonPrinterEnder(QtWidgets.QPushButton):
    '''Class for a button that chooses a file, prints a QTextEdit and ends a
    QApplication
    '''
    def __init__(self, application, textedit):
        super().__init__('Print and quit')
        self.app = application
        self.txt = textedit
        self.clicked.connect(self._callback)
    def _choose_file(self):
        '''Just open a dialog and choose a single file for saving'''
        f = QtWidgets.QFileDialog(self, 'Save file')
        f.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        f.setFileMode(QtWidgets.QFileDialog.AnyFile)
        if f.exec() == QtWidgets.QDialog.Accepted:
            return f.selectedFiles()[0]
        else:
            return None
    def _callback(self, **kwargs):
        #print(self._choose_file())
        print(self.txt.toPlainText())
        self.app.closeAllWindows()
        self.app.quit()

class FileMenu(QtWidgets.QMenu):
    '''Why a class for a file menu? Enter the main window as argument'''
    def __init__(self, win):
        self = win.menuBar().addMenu('File')
        self.new_action = QtWidgets.QAction('New', win)
        self.new_action.triggered.connect(win.new_file)
        self.addAction(self.new_action)
        self.open_action = QtWidgets.QAction('Open', win)
        self.open_action.triggered.connect(win.centralWidget().open_file)
        self.addAction(self.open_action)
        self.save_action = QtWidgets.QAction('Save', win)
        self.save_action.triggered.connect(win.centralWidget().save_file)
        self.addAction(self.save_action)

class ApplicationCentralWidget(QtWidgets.QWidget):
    '''The central widget that will be displayed in the main window'''
    def __init__(self, app):
        super().__init__()
        self.org = QtWidgets.QVBoxLayout()
        self.hello = QtWidgets.QLabel('Type some text and click the button')
        self.text = SignedTextEdit()
        self.button = ButtonPrinterEnder(app, self.text)
        self.org.addWidget(self.hello)
        self.org.addWidget(self.text)
        self.org.addWidget(self.button)
        self.setLayout(self.org)
    def clear_text(self):
        '''Let's use it as intermediate'''
        self.text.setText('')
    @pyqtSlot('void')
    def save_file(self):
        '''Shows a dialog for opening a file'''
        d = QtWidgets.QFileDialog(self, 'Save File')
        d.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        d.setFileMode(QtWidgets.QFileDialog.AnyFile)
        if d.exec() == QtWidgets.QDialog.Accepted:
            self.text.save_text(d.selectedFiles()[0])
    @pyqtSlot('void')
    def open_file(self):
        '''Shows a dialog for saving a file'''
        d = QtWidgets.QFileDialog(self, 'Open File')
        d.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        d.setFileMode(QtWidgets.QFileDialog.AnyFile)
        if d.exec() == QtWidgets.QDialog.Accepted:
            self.text.open_text(d.selectedFiles()[0])

class ApplicationMainWindow(QtWidgets.QMainWindow):
    '''This is the main window widget for the application'''
    def __init__(self, app):
        super().__init__()
        self.central = ApplicationCentralWidget(app)
        self.setCentralWidget(self.central)
        self.file_menu = FileMenu(self)
    @pyqtSlot('void')
    def new_file(self):
        '''For now, just clear the TextEdit'''
        self.central.clear_text()

class IurisTestApplication(QtWidgets.QApplication):
    '''The main class for this application. Make it easy for use in main'''
    def __init__(self):
        super().__init__(['Iuri\'s weird application'])
        self.main_win = iurichat.ChatMainWindow(self)
    def start(self):
        '''Start and run the created application'''
        self.main_win.show()
        self.exec()


if __name__ == '__main__':
    app = IurisTestApplication()
    app.start()
