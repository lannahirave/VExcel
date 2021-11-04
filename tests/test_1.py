import unittest
from PyQt5 import QtWidgets
import sys
import os
#import bcolors
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import second
#from second import Ui_MainWindow

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = second.Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
application = myapp()

class Tests(unittest.TestCase):
    def test_binary(self):
        """
        Test that it can do basic math
        """
        data = ['==1+1', '==1/0', '==2*6', '==1.5-2.5', '==1*0']
        answers = ['2', '#Zero division error: ==1/0', '12', '-1.0', '0']
        print('----------------------------------------------------------------------')
        for i in range(len(data)):
            answer = application.ui.processer(data[i])
            #print("TEST", data[i], answer)
            print('Asserting that output of command "' + data[i] + '" is equal "' + answers[i] + '".', end=' ')
            try:
                self.assertEqual(answer, answers[i])
                print(bcolors.OKGREEN + "SUCCESS." + bcolors.ENDC)
            except AssertionError:
                print(bcolors.WARNING + "FAILED." + bcolors.ENDC)

    def test_mod(self):
        """
        Test that it can do mod and div operations
        """
        data = ['==4 mod 5', '==4 div 3', '==4 div 0', '==4 mod 1', '==4mod2']
        answers = ['4', '1', '#Zero division error: ==4 div 0', '0', '0']
        print('----------------------------------------------------------------------')
        for i in range(len(data)):
            answer = application.ui.processer(data[i])
            #print("TEST", data[i], answer)
            print('Asserting that output of command "' + data[i] + '" is equal "' + answers[i] + '".', end=' ')
            try:
                self.assertEqual(answer, answers[i])
                print(bcolors.OKGREEN + "SUCCESS." + bcolors.ENDC)
            except AssertionError:
                print(bcolors.WARNING + "FAILED." + bcolors.ENDC)

    def test_mmax(self):
        """
        Test that it can do mmax and mmin
        """
        data = ['==mmax(-1, 5, 123, 1234+5)', '==mmax(-1, 123,0, 424', '==mmin(-1, mmin(-2, 5))']
        answers = ['1239', '#Bad expression: ==mmax(-1, 123,0, 424', '-2']
        print('----------------------------------------------------------------------')

        for i in range(len(data)):
            answer = application.ui.processer(data[i])
            #print("TEST", data[i], answer)
            print('Asserting that output of command "' + data[i] + '" is equal "' + answers[i] + '".', end=' ')
            try:
                self.assertEqual(answer, answers[i])
                print(bcolors.OKGREEN + "SUCCESS." + bcolors.ENDC)
            except AssertionError:
                print(bcolors.WARNING + "FAILED." + bcolors.ENDC)


if __name__ == '__main__':
    unittest.main()