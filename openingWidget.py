from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_opening(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("opening")
        self.resize(476, 101)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.setFixedSize(476, 101)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self, opening):
        _translate = QtCore.QCoreApplication.translate
        opening.setWindowTitle(_translate("opening", "Form"))
        self.pushButton_2.setText(_translate("opening", "Открыть существующего персонажа"))
        self.pushButton.setText(_translate("opening", "Создать нового персонажа"))
