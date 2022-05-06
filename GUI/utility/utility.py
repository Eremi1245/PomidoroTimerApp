import winsound
from PyQt5 import QtTest
from PyQt5.QtWidgets import QLineEdit


def sound_gong() -> None:
    """
    Функция проигрывает звук оповещения об окончании таймера
    """
    winsound.PlaySound("gong1.wav", winsound.SND_FILENAME)
