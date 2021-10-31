#launcher source code
import sys
import os
import app_rc #app_recources
from PyQt5 import QtCore, QtGui, QtWidgets

# Stable version of first launching window


class Ui_main(QtWidgets.QDialog):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(226, 366)
        main.setMinimumSize(QtCore.QSize(226, 366))
        main.setMaximumSize(QtCore.QSize(226, 366))
        main.setMouseTracking(True)
        main.setTabletTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/sheet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setStyleSheet("background-color: rgba(217,250,224,255)")
        main.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        main.setProperty("WindowTitleHint", False)
        self.layoutWidget = QtWidgets.QWidget(main)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 212, 340))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setEnabled(True)
        self.label_5.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("background-color: rgba(217,250,224,255)")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
    "    color: #333;\n"
    "    border: 2px solid #555;\n"
    "    border-radius: 20px;\n"
    "    border-style: outset;\n"
    "   \n"
    "    background-color: rgba(176,227,200,255);\n"
    "    padding: 5px;\n"
    "    }\n"
    "\n"
    "\n"
    "QPushButton:pressed {\n"
    "    border-style: inset;\n"
    "   \n"
    "    background-color: rgba(102,169,118,255);\n"
    "    }")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
    "    color: #333;\n"
    "    border: 2px solid #555;\n"
    "    border-radius: 20px;\n"
    "    border-style: outset;\n"
    "   \n"
    "    background-color: rgba(176,227,200,255);\n"
    "    padding: 5px;\n"
    "    }\n"
    "\n"
    "\n"
    "QPushButton:pressed {\n"
    "    border-style: inset;\n"
    "   \n"
    "    background-color: rgba(102,169,118,255);\n"
    "    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "VExcel"))
        self.label.setText(_translate("main", "Вікно для запуску VExcel"))
        self.label_2.setText(_translate("main", "Додаток представляє собою простий"))
        self.label_3.setText(_translate("main", "табличний калькулятор."))
        self.label_4.setText(_translate("main", "Варіант лабораторної № 28."))
        self.label_5.setText(_translate("main", "Нікітін Р. В. У. К-24"))
        self.label_6.setText(_translate("main", "<html><head/><body><p><img src=\":/logo/images/VExcel.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("main", "Запуск"))
        self.pushButton_2.setText(_translate("main", "Вихід"))
        self.pushButton.clicked.connect(lambda: [self.start_program()])
        self.pushButton_2.clicked.connect(sys.exit)

    def start_program(self):
        # self.close()
        stream = os.popen("python main.py")
        sys.exit()
