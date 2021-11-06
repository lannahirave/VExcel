# start window
# maintains first.py source code
# creates launcher window
from first import Ui_main
import sys
from PyQt5 import QtWidgets

# Stable version of launcher

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()