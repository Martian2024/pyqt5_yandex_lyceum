from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton


class Ui_MainMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(1321, 695)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 80, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 110, 231, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 110, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 50, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 80, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 110, 231, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(790, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(840, 50, 91, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 170, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(690, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(840, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(680, 170, 111, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(820, 170, 111, 22))
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_10 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_10.setGeometry(QtCore.QRect(680, 200, 111, 22))
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_11 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_11.setGeometry(QtCore.QRect(820, 200, 111, 22))
        self.spinBox_11.setObjectName("spinBox_11")
        self.spinBox_12 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_12.setGeometry(QtCore.QRect(680, 230, 111, 22))
        self.spinBox_12.setObjectName("spinBox_12")
        self.spinBox_13 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_13.setGeometry(QtCore.QRect(820, 230, 111, 22))
        self.spinBox_13.setObjectName("spinBox_13")
        self.spinBox_14 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_14.setGeometry(QtCore.QRect(680, 260, 111, 22))
        self.spinBox_14.setObjectName("spinBox_14")
        self.spinBox_15 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_15.setGeometry(QtCore.QRect(820, 260, 111, 22))
        self.spinBox_15.setObjectName("spinBox_15")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(590, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(560, 230, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(580, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.spinBox_16 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_16.setGeometry(QtCore.QRect(680, 290, 111, 22))
        self.spinBox_16.setObjectName("spinBox_16")
        self.spinBox_17 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_17.setGeometry(QtCore.QRect(820, 290, 111, 22))
        self.spinBox_17.setObjectName("spinBox_17")
        self.spinBox_19 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_19.setGeometry(QtCore.QRect(820, 320, 111, 22))
        self.spinBox_19.setObjectName("spinBox_19")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(590, 290, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(600, 320, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.spinBox_21 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_21.setGeometry(QtCore.QRect(680, 320, 111, 22))
        self.spinBox_21.setObjectName("spinBox_21")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1020, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(1160, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(1160, 80, 101, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(1160, 110, 101, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(1160, 140, 101, 22))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(1160, 170, 101, 22))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(1160, 200, 101, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_9 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_9.setGeometry(QtCore.QRect(1160, 230, 101, 22))
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_18 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_18.setGeometry(QtCore.QRect(1160, 260, 101, 22))
        self.spinBox_18.setObjectName("spinBox_18")
        self.spinBox_20 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_20.setGeometry(QtCore.QRect(1160, 290, 101, 22))
        self.spinBox_20.setObjectName("spinBox_20")
        self.spinBox_22 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_22.setGeometry(QtCore.QRect(1160, 320, 101, 22))
        self.spinBox_22.setObjectName("spinBox_22")
        self.spinBox_23 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_23.setGeometry(QtCore.QRect(1160, 350, 101, 22))
        self.spinBox_23.setObjectName("spinBox_23")
        self.spinBox_24 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_24.setGeometry(QtCore.QRect(1160, 380, 101, 22))
        self.spinBox_24.setObjectName("spinBox_24")
        self.spinBox_25 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_25.setGeometry(QtCore.QRect(1160, 410, 101, 22))
        self.spinBox_25.setObjectName("spinBox_25")
        self.spinBox_26 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_26.setGeometry(QtCore.QRect(1160, 440, 101, 22))
        self.spinBox_26.setObjectName("spinBox_26")
        self.spinBox_27 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_27.setGeometry(QtCore.QRect(1160, 470, 101, 22))
        self.spinBox_27.setObjectName("spinBox_27")
        self.spinBox_28 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_28.setGeometry(QtCore.QRect(1160, 500, 101, 22))
        self.spinBox_28.setObjectName("spinBox_28")
        self.spinBox_29 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_29.setGeometry(QtCore.QRect(1160, 530, 101, 22))
        self.spinBox_29.setObjectName("spinBox_29")
        self.spinBox_30 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_30.setGeometry(QtCore.QRect(1160, 560, 101, 22))
        self.spinBox_30.setObjectName("spinBox_30")
        self.spinBox_31 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_31.setGeometry(QtCore.QRect(1160, 590, 101, 22))
        self.spinBox_31.setObjectName("spinBox_31")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(580, 350, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.spinBox_32 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_32.setGeometry(QtCore.QRect(700, 350, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_32.setFont(font)
        self.spinBox_32.setObjectName("spinBox_32")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(770, 350, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.spinBox_33 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_33.setGeometry(QtCore.QRect(890, 350, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_33.setFont(font)
        self.spinBox_33.setObjectName("spinBox_33")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(570, 400, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.spinBox_34 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_34.setGeometry(QtCore.QRect(670, 520, 101, 22))
        self.spinBox_34.setObjectName("spinBox_34")
        self.spinBox_35 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_35.setGeometry(QtCore.QRect(670, 430, 101, 22))
        self.spinBox_35.setObjectName("spinBox_35")
        self.spinBox_36 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_36.setGeometry(QtCore.QRect(670, 460, 101, 22))
        self.spinBox_36.setObjectName("spinBox_36")
        self.spinBox_37 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_37.setGeometry(QtCore.QRect(670, 550, 101, 22))
        self.spinBox_37.setObjectName("spinBox_37")
        self.spinBox_38 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_38.setGeometry(QtCore.QRect(670, 490, 101, 22))
        self.spinBox_38.setObjectName("spinBox_38")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(670, 400, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.spinBox_39 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_39.setGeometry(QtCore.QRect(670, 580, 101, 22))
        self.spinBox_39.setObjectName("spinBox_39")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(800, 400, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(800, 430, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(820, 460, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.spinBox_40 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_40.setGeometry(QtCore.QRect(910, 400, 42, 22))
        self.spinBox_40.setObjectName("spinBox_40")
        self.spinBox_41 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_41.setGeometry(QtCore.QRect(910, 430, 42, 22))
        self.spinBox_41.setObjectName("spinBox_41")
        self.spinBox_42 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_42.setGeometry(QtCore.QRect(910, 460, 42, 22))
        self.spinBox_42.setObjectName("spinBox_42")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(350, 630, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(630, 630, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(920, 630, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.spinBox_43 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_43.setGeometry(QtCore.QRect(560, 630, 42, 22))
        self.spinBox_43.setObjectName("spinBox_43")
        self.spinBox_44 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_44.setGeometry(QtCore.QRect(850, 630, 42, 22))
        self.spinBox_44.setObjectName("spinBox_44")
        self.spinBox_45 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_45.setGeometry(QtCore.QRect(1050, 630, 42, 22))
        self.spinBox_45.setObjectName("spinBox_45")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(550, 380, 391, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(780, 400, 20, 201))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1110, 630, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 401, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(70, 160, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(220, 370, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 400, 531, 171))
        self.listWidget.setObjectName("listWidget")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(800, 510, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(840, 540, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(830, 570, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.spinBox_46 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_46.setGeometry(QtCore.QRect(890, 540, 42, 22))
        self.spinBox_46.setObjectName("spinBox_46")
        self.spinBox_47 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_47.setGeometry(QtCore.QRect(890, 570, 42, 22))
        self.spinBox_47.setObjectName("spinBox_47")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(420, 190, 131, 141))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(410, 150, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(960, 60, 16, 561))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(20, 20, 1281, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 0, 191, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(570, 430, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(570, 460, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(570, 490, 91, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(570, 520, 81, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(570, 550, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(570, 580, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(1010, 80, 121, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(1010, 110, 121, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(1010, 140, 111, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(1010, 170, 131, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(1010, 200, 121, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(1010, 230, 141, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(1010, 260, 121, 17))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(1010, 290, 131, 17))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(1010, 350, 141, 17))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(1010, 380, 121, 17))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(1010, 320, 131, 17))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(1010, 410, 131, 17))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(1010, 440, 131, 17))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(1010, 470, 151, 17))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_21.setGeometry(QtCore.QRect(1010, 530, 121, 17))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_22.setGeometry(QtCore.QRect(1010, 500, 131, 17))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_23.setGeometry(QtCore.QRect(1010, 560, 121, 17))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_28 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_28.setGeometry(QtCore.QRect(1010, 590, 131, 17))
        self.checkBox_28.setObjectName("checkBox_28")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 150, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 160, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 370, 31, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 0, 231, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.setFixedSize(1321, 695)

        self.comboBox.addItems(['Бард', 'Варвар', 'Воин', 'Волшебник', 'Друид', 'Жрец',
                                'Изобретатель', 'Колдун', 'Монах', 'Напарник БОЕЦ', 'Напарник ЗАКЛИНАТЕЛЬ',
                                'Напарник ЭКСПЕРТ', 'Паладин', 'Плут', 'Следопыт', 'Чародей'])
        self.comboBox_2.addItems(['Аазимары', 'Гномы', 'Дварфы', 'Дженази', 'Люди', 'Тифлинги', 'Халфлинги',
                                  'Элдарин', 'Эльфы'])
        self.basic = [self.lineEdit, self.comboBox, self.comboBox_2, self.lineEdit_2, self.lineEdit_3,
                      self.lineEdit_4, self.spinBox]
        self.main = [[self.spinBox_2, self.spinBox_8], [self.spinBox_10, self.spinBox_11],
                     [self.spinBox_12, self.spinBox_13],
                     [self.spinBox_14, self.spinBox_15],
                     [self.spinBox_16, self.spinBox_17],
                     [self.spinBox_21, self.spinBox_19]]
        self.bonuses = [self.spinBox_32, self.spinBox_33]
        self.challenges = {self.checkBox: self.spinBox_35, self.checkBox_2: self.spinBox_36,
                           self.checkBox_3: self.spinBox_38, self.checkBox_4: self.spinBox_34,
                           self.checkBox_5: self.spinBox_37, self.checkBox_6: self.spinBox_39}
        self.health = {self.label_32: self.spinBox_43, self.label_33: self.spinBox_44, self.label_34: self.spinBox_45}
        self.skills = {self.checkBox_7: self.spinBox_3, self.checkBox_8: self.spinBox_4,
                       self.checkBox_9: self.spinBox_5, self.checkBox_10: self.spinBox_6,
                       self.checkBox_11: self.spinBox_7, self.checkBox_12: self.spinBox_9,
                       self.checkBox_13: self.spinBox_18, self.checkBox_14: self.spinBox_20,
                       self.checkBox_17: self.spinBox_22, self.checkBox_15: self.spinBox_23,
                       self.checkBox_16: self.spinBox_24, self.checkBox_18: self.spinBox_25,
                       self.checkBox_19: self.spinBox_26, self.checkBox_20: self.spinBox_27,
                       self.checkBox_22: self.spinBox_28, self.checkBox_21: self.spinBox_29,
                       self.checkBox_23: self.spinBox_30, self.checkBox_28: self.spinBox_31}
        self.deathchallenges = {self.label_38: self.spinBox_46, self.label_39: self.spinBox_47}
        self.categories = [self.basic, self.main, self.bonuses, self.challenges, self.health, self.skills]

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Имя персонажа"))
        self.label_2.setText(_translate("MainWindow", "Класс"))
        self.label_3.setText(_translate("MainWindow", "Раса"))
        self.label_4.setText(_translate("MainWindow", "Имя игрока"))
        self.label_5.setText(_translate("MainWindow", "Происхождение"))
        self.label_6.setText(_translate("MainWindow", "Мировоззрение"))
        self.label_7.setText(_translate("MainWindow", "Опыт"))
        self.label_8.setText(_translate("MainWindow", "Сила"))
        self.label_16.setText(_translate("MainWindow", "Модификатор"))
        self.label_17.setText(_translate("MainWindow", "Значение"))
        self.label_18.setText(_translate("MainWindow", "Ловкость"))
        self.label_19.setText(_translate("MainWindow", "Выносливость"))
        self.label_20.setText(_translate("MainWindow", "Интеллект"))
        self.label_22.setText(_translate("MainWindow", "Мудрость"))
        self.label_23.setText(_translate("MainWindow", "Харизма"))
        self.label_21.setText(_translate("MainWindow", "Навыки"))
        self.label_24.setText(_translate("MainWindow", "Модификатор"))
        self.label_25.setText(_translate("MainWindow", "Вдохновение"))
        self.label_26.setText(_translate("MainWindow", "Бонус умения"))
        self.label_27.setText(_translate("MainWindow", "Испытания"))
        self.label_28.setText(_translate("MainWindow", "Модификатор"))
        self.label_29.setText(_translate("MainWindow", "Класс брони"))
        self.label_30.setText(_translate("MainWindow", "Инициатива"))
        self.label_31.setText(_translate("MainWindow", "Скорость"))
        self.label_32.setText(_translate("MainWindow", " Текущие пункты здоровья"))
        self.label_33.setText(_translate("MainWindow", "Временные пункты здоровья"))
        self.label_34.setText(_translate("MainWindow", " Кости здоровья"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.label_35.setText(_translate("MainWindow", "Атаки и заклинания"))
        self.label_36.setText(_translate("MainWindow", "Снаряжение"))
        self.label_37.setText(_translate("MainWindow", "Испытания против смерти"))
        self.label_38.setText(_translate("MainWindow", "Успехи"))
        self.label_39.setText(_translate("MainWindow", "Провалы"))
        self.label_40.setText(_translate("MainWindow", "Умения и языки"))
        self.pushButton_3.setText(_translate("MainWindow", "к образу >>"))
        self.checkBox.setText(_translate("MainWindow", "Сила"))
        self.checkBox_2.setText(_translate("MainWindow", "Ловкость"))
        self.checkBox_3.setText(_translate("MainWindow", "Выносливость"))
        self.checkBox_4.setText(_translate("MainWindow", "Интеллект"))
        self.checkBox_5.setText(_translate("MainWindow", "Мудрость"))
        self.checkBox_6.setText(_translate("MainWindow", "Харизма"))
        self.checkBox_7.setText(_translate("MainWindow", "Акробатика (Лвк.)"))
        self.checkBox_8.setText(_translate("MainWindow", "Атлетика (Сил.)"))
        self.checkBox_9.setText(_translate("MainWindow", "Внимание (Мдр.)"))
        self.checkBox_10.setText(_translate("MainWindow", "Выживание (Мдр.)"))
        self.checkBox_11.setText(_translate("MainWindow", "Дрессировка (Мдр.)"))
        self.checkBox_12.setText(_translate("MainWindow", "Запугивание (Хар.)"))
        self.checkBox_13.setText(_translate("MainWindow", "Исполнение (Хар.)"))
        self.checkBox_14.setText(_translate("MainWindow", "История (Инт.)"))
        self.checkBox_15.setText(_translate("MainWindow", "Магия (Инт.)"))
        self.checkBox_16.setText(_translate("MainWindow", "Медицина (Мдр.)"))
        self.checkBox_17.setText(_translate("MainWindow", "Ловкость рук (Лвк.)"))
        self.checkBox_18.setText(_translate("MainWindow", "Обман (Хар.)"))
        self.checkBox_19.setText(_translate("MainWindow", "Природа (Инт.)"))
        self.checkBox_20.setText(_translate("MainWindow", "Проницательность (Мдр.)"))
        self.checkBox_21.setText(_translate("MainWindow", "Религия (Инт.)"))
        self.checkBox_22.setText(_translate("MainWindow", "Расследование (Инт.)"))
        self.checkBox_23.setText(_translate("MainWindow", "Скрытность (Лвк.)"))
        self.checkBox_28.setText(_translate("MainWindow", "Убеждение (Хар.)"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "Возврат к начальному экрану"))
