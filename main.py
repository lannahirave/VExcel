# table app
# maintains second.py source code
# creates MAIN window 
from second import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeyEvent, QKeySequence

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        if self.ui.LineEdit.hasFocus() and event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            print("ENTER-line event")
            self.ui.onTextChanged()
        if self.ui.tableWidget.hasFocus() and event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            print("ENTER-table event")
            self.ui.update()
        elif self.ui.tableWidget.hasFocus() and event.key() in (QtCore.Qt.Key_Backspace, QtCore.Qt.Key_Delete):
            print("Delete event")
            self.ui.deleteContent()

    def closeEvent(self, event):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        save = QMessageBox.Save
        #box.setWindowTitle('TITLE!')
        box.setText("Зберігти зміни?")
        box.setStandardButtons(QMessageBox.Save|QMessageBox.Close| QMessageBox.Cancel)
        save = box.button(QMessageBox.Save)
        save.setText('Зберігти')
        dont_save = box.button(QMessageBox.Close)
        dont_save.setText("Не змінювати")
        cancel = box.button(QMessageBox.Cancel)
        cancel.setText("Скасувати")
        box.exec()

        if box.clickedButton() == dont_save:
            event.accept()
        elif box.clickedButton() == save:
            self.ui.save()
        else:
            event.ignore()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = myapp()
    application.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()