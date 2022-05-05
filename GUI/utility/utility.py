import winsound
from PyQt5 import QtTest
from PyQt5.QtWidgets import QLineEdit


def sound_gong() -> None:
    """
    Функция проигрывает звук оповещения об окончании таймера
    """
    winsound.PlaySound("gong1.wav", winsound.SND_FILENAME)


def timer(QtWidget: QLineEdit, minutes: int) -> None:
    """
    Функция запускает таймер и отрисовывает текущее время на виджете
    :param QtWidget: Передается объект QLineEdit
    :param minutes: Количество минут таймера
    """
    time_in_seconds = minutes * 60
    color_1 = 0
    color_2 = 0
    color_3 = 255
    for i in range(time_in_seconds + 1):
        minutes = time_in_seconds // 60
        seconds = time_in_seconds % 60
        QtWidget.setText(f"{minutes}:{seconds}")
        time_in_seconds -= 1
        QtWidget.setStyleSheet(f"background-color: rgb({color_1}, {color_2}, {color_3});\n"
                               "font: 8pt \"Arial\";\n"
                               "font: 75 36pt \"MS Shell Dlg 2\";")
        if color_1 < 255:
            color_1 += 1
        else:
            if color_2 < 255:
                color_2 += 1
            else:
                if color_3 < 0:
                    color_3 -= 1
        QtTest.QTest.qWait(1000)
    sound_gong()
