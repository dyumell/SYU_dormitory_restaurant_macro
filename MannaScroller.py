# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mannaui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import pyautogui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(112, 193)
        Form.setStyleSheet("background-color: rgb(211, 205, 201);")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 111, 191))
        self.frame_2.setStyleSheet("background-color: rgb(178, 172, 168);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 66, 25))
        self.label_4.setStyleSheet("font: 13pt \"휴먼엑스포\";\n"
"background-color: transparent;\n"
"color: rgb(82, 140, 91);")
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 0, 91, 151))
        self.frame_3.setStyleSheet("background-color: rgb(133, 125, 117);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 71, 51))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius : 22px;\n"
"background-color: rgb(77, 70, 63);\n"
"font: 12pt \"휴먼엑스포\";\n"
"color: rgb(235, 229, 225);\n"
"border: 3px solid #EBE5E1;")
        self.pushButton.setAutoRepeatDelay(150)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 71, 51))
        self.pushButton_2.setStyleSheet("border-radius : 22px;\n"
"background-color: rgb(77, 70, 63);\n"
"font: 12pt \"휴먼엑스포\";\n"
"color: rgb(235, 229, 225);\n"
"border: 3px solid #EBE5E1;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.frame.setStyleSheet("background-color: rgb(35, 31, 32);\n"
"border-top-right-radius: 20px;\n"
"border-top-left-radius: 20px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 351, 41))
        self.label.setStyleSheet("font: 17pt \"휴먼엑스포\";\n"
"color: rgb(235, 229, 225);\n"
"text-shadow: 22px 22px 22px rgba(0, 0, 0, 225);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "중단됨"))
        self.pushButton.setText(_translate("Form", "갱신"))
        self.pushButton_2.setText(_translate("Form", "중단"))



class MyApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(50, 50)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.simulate_click)
        self.pushButton.clicked.connect(self.start_update)
        self.pushButton_2.clicked.connect(self.stop_update)
        QtWidgets.QApplication.instance().installEventFilter(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.simulate_scroll)


    def simulate_click(self):
        x = 1003  # 적절한 x 좌표로 수정
        y = 150  # 적절한 y 좌표로 수정
        pyautogui.click(x,y)

    def start_update(self):
        self.label_4.setText("갱신중")
        # 1초마다 클릭 시뮬레이션 시작
        self.timer.start(1000) 


    def stop_update(self):
        self.label_4.setText("중단됨")
        # 타이머 중단
        self.timer.stop()

    def simulate_scroll(self):
        # 클릭 시뮬레이션
        pyautogui.scroll(10000)
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if self.dragPosition is not None:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = None
            event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())