import numpy

from typing import List

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QCheckBox, QSlider, QSpinBox, QRadioButton, QComboBox


GENERATOR_LIST: List["BaseGenerator"] = []


class BaseGenerator(QWidget):
    name: str = "None"

    ui = None

    settingsChanged = pyqtSignal()
    remove = pyqtSignal(object)

    def __init__(self, samplerate=0):
        super().__init__()

    def GetConfig(self) -> dict:
        if self.ui == None: return {}

        config = {}
        for objName in dir(self.ui):
            obj = getattr(self.ui, objName)

            if isinstance(obj, QCheckBox):
                config[objName] = obj.checkState()

            elif isinstance(obj, QSpinBox):
                config[objName] = obj.value()

            elif isinstance(obj, QSlider):
                config[objName] = obj.value()

            elif isinstance(obj, QRadioButton):
                config[objName] = obj.isChecked()

            elif isinstance(obj, QComboBox):
                config[objName] = obj.currentIndex()

        return config

    def LoadConfig(self, config: dict):
        if self.ui == None: return {}

        for objName, objValue in config.items():
            obj = getattr(self.ui, objName)

            if isinstance(obj, QCheckBox):
                obj.setChecked(objValue)

            elif isinstance(obj, QSpinBox):
                obj.setValue(objValue)

            elif isinstance(obj, QSlider):
                obj.setValue(objValue)

            elif isinstance(obj, QRadioButton):
                obj.setChecked(objValue)

            elif isinstance(obj, QComboBox):
                obj.setCurrentIndex(objValue)

    # Включение/выключение генератора
    def stateChanged(self):
        self.settingsChanged.emit()

    def resetX(self):
        pass

    # Генерация
    def gen(self, sampleCount: int) -> numpy.array:
        return numpy.zeros(sampleCount)

