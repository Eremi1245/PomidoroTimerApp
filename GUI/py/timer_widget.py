from PyQt5 import QtCore, QtWidgets, QtTest
from GUI.utility.utility import sound_gong

timer_on = True


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(255, 0, 128);")
        self.srt_btn = QtWidgets.QPushButton(Form)
        self.srt_btn.setGeometry(QtCore.QRect(20, 250, 150, 30))
        self.srt_btn.setStyleSheet("background-color: rgb(128, 0, 128);")
        self.srt_btn.setObjectName("srt_btn")
        self.srt_btn.clicked.connect(self.click_start)

        self.stp_btn = QtWidgets.QPushButton(Form)
        self.stp_btn.setGeometry(QtCore.QRect(230, 250, 150, 30))
        self.stp_btn.setStyleSheet("background-color: rgb(124,252,0);")
        self.stp_btn.setObjectName("stp_btn")
        self.stp_btn.clicked.connect(self.click_stop)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 381, 81))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                    "font: 8pt \"Arial\";\n"
                                    "font: 75 36pt \"MS Shell Dlg 2\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pomidoro Timer"))
        self.srt_btn.setText(_translate("Form", "Start/Restart"))
        self.stp_btn.setText(_translate("Form", "Pause/Continue"))
        self.lineEdit.setText(_translate("Form", "25:00"))

    def click_start(self) -> None:
        """
        Функция при нажатии на кнопку start. Запускает сначала таймер на работу 25 минут,
        потом таймер на отдых 5 минут
        """
        self.timer(25)
        self.timer(5)

    def click_stop(self):
        """
        Функция при на нажатии на кнопку stop. Приостанавливает работу таймера и меняет цвет кнопки
        """
        global timer_on
        if timer_on:
            timer_on = False
            self.stp_btn.setStyleSheet("background-color: rgb(255,255,0);")
        else:
            timer_on = True
            self.stp_btn.setStyleSheet("background-color: rgb(124,252,0);")

    def timer(self, minutes: int) -> None:
        """
        Функция запускает таймер и отрисовывает текущее время на виджете
        :param minutes: Количество минут таймера
        """
        global timer_on
        time_in_seconds = minutes * 60
        color_1 = 0
        color_2 = 0
        color_3 = 255
        for i in range(time_in_seconds + 1):
            if timer_on:
                minutes = time_in_seconds // 60
                seconds = time_in_seconds % 60
                self.lineEdit.setText(f"{minutes}:{seconds}")
                time_in_seconds -= 1
                if color_1 < 255:
                    color_1 += 1
                else:
                    if color_2 < 255:
                        color_2 += 1
                    else:
                        if color_3 < 0:
                            color_3 -= 1
                QtTest.QTest.qWait(1000)
            else:
                while timer_on == False:
                    QtTest.QTest.qWait(1000)
        sound_gong()
