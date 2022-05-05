from PyQt5 import QtCore, QtWidgets

from GUI.utility.utility import timer

timer_on = False


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(255, 0, 128);")
        self.srt_btn = QtWidgets.QPushButton(Form)
        self.srt_btn.setGeometry(QtCore.QRect(20, 250, 150, 30))
        self.srt_btn.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.srt_btn.setObjectName("srt_btn")
        self.srt_btn.clicked.connect(self.click_start)

        self.stp_btn = QtWidgets.QPushButton(Form)
        self.stp_btn.setGeometry(QtCore.QRect(230, 250, 150, 30))
        self.stp_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.stp_btn.setObjectName("stp_btn")
        self.srt_btn.clicked.connect(self.click_stop)

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
        Form.setWindowTitle(_translate("Form", "Pimodoro Timer"))
        self.srt_btn.setText(_translate("Form", "Start"))
        self.stp_btn.setText(_translate("Form", "Stop"))
        self.lineEdit.setText(_translate("Form", "25:00"))

    def click_start(self):
        """
        Функция при нажатии на кнопку start. Запускает сначала таймер на работу 25 минут, потом таймер на отдых 5 минут
        """
        timer(self.lineEdit, 25)
        timer(self.lineEdit, 5)

    def click_stop(self):
        """
        Функция при на нажатии на кнопку stop. Приостанавливает работу таймера
        """
        # TODO
        pass
