import enum
import numpy

from ui.headers.ui_ArsGenerator import Ui_ArsGenerator

from ui.BaseGenerator import BaseGenerator

from signalGenerators.sinGen import SinusGenerator


class FreqEnum(enum.IntEnum):
    F_75_HZ = 75
    F_125_HZ = 125
    F_175_HZ = 175
    F_225_HZ = 225
    F_275_HZ = 275
    F_325_HZ = 325


class ArsGenerator(BaseGenerator):
    name = "АРС"

    def __init__(self, samplerate):
        super().__init__()

        self.ui = Ui_ArsGenerator()
        self.ui.setupUi(self)

        self.ui.enable.stateChanged.connect(self.stateChanged)
        self.ui.remove.clicked.connect(lambda: self.remove.emit(self))

        # Изменение уровня
        self.ui.levelSlider_1.valueChanged.connect(self.levelSliderChanged)
        self.ui.levelSlider_2.valueChanged.connect(self.levelSliderChanged)
        self.ui.levelSpin_1.valueChanged.connect(self.levelSpinChanged)
        self.ui.levelSpin_2.valueChanged.connect(self.levelSpinChanged)

        # Изменение несущей частоты
        self.ui.f75_1.toggled.connect(self.freqChanged)
        self.ui.f125_1.toggled.connect(self.freqChanged)
        self.ui.f175_1.toggled.connect(self.freqChanged)
        self.ui.f225_1.toggled.connect(self.freqChanged)
        self.ui.f275_1.toggled.connect(self.freqChanged)
        self.ui.f325_1.toggled.connect(self.freqChanged)
        self.ui.f75_2.toggled.connect(self.freqChanged)
        self.ui.f125_2.toggled.connect(self.freqChanged)
        self.ui.f175_2.toggled.connect(self.freqChanged)
        self.ui.f225_2.toggled.connect(self.freqChanged)
        self.ui.f275_2.toggled.connect(self.freqChanged)
        self.ui.f325_2.toggled.connect(self.freqChanged)

        # Генераторы
        self.generator_1 = SinusGenerator(samplerate)
        self.generator_2 = SinusGenerator(samplerate)

        # Установить частоты по-умолчанию
        self.freqChanged()

    # Эвенты изменения положения слайдеров
    def levelSliderChanged(self):
        value_1 = self.ui.levelSlider_1.value()
        self.ui.levelSpin_1.setValue(value_1)

        value_2 = self.ui.levelSlider_2.value()
        self.ui.levelSpin_2.setValue(value_2)

        self.ampSet(value_1, value_2)

    # Эвенты изменения значения
    def levelSpinChanged(self):
        value_1 = self.ui.levelSpin_1.value()
        self.ui.levelSlider_1.setValue(value_1)

        value_2 = self.ui.levelSpin_2.value()
        self.ui.levelSlider_2.setValue(value_2)

        self.ampSet(value_1, value_2)

    # Извенение частоты несущей
    def freqChanged(self):
        if self.ui.f75_1.isChecked():
            freq_1 = FreqEnum.F_75_HZ

        elif self.ui.f125_1.isChecked():
            freq_1 = FreqEnum.F_125_HZ

        elif self.ui.f175_1.isChecked():
            freq_1 = FreqEnum.F_175_HZ

        elif self.ui.f225_1.isChecked():
            freq_1 = FreqEnum.F_225_HZ

        elif self.ui.f275_1.isChecked():
            freq_1 = FreqEnum.F_275_HZ

        elif self.ui.f325_1.isChecked():
            freq_1 = FreqEnum.F_325_HZ

        else:  # ???
            return

        if self.ui.f75_2.isChecked():
            freq_2 = FreqEnum.F_75_HZ

        elif self.ui.f125_2.isChecked():
            freq_2 = FreqEnum.F_125_HZ

        elif self.ui.f175_2.isChecked():
            freq_2 = FreqEnum.F_175_HZ

        elif self.ui.f225_2.isChecked():
            freq_2 = FreqEnum.F_225_HZ

        elif self.ui.f275_2.isChecked():
            freq_2 = FreqEnum.F_275_HZ

        elif self.ui.f325_2.isChecked():
            freq_2 = FreqEnum.F_325_HZ

        else:  # ???
            return
        
        self.freqSet(freq_1.value, freq_2.value)

    # Установка значения в генератор
    def ampSet(self, amp_1: int, amp_2: int):
        self.generator_1.setAmp(amp_1 / 100)
        self.generator_2.setAmp(amp_2 / 100)

        self.settingsChanged.emit()

    def freqSet(self, freq_1, freq_2):
        self.generator_1.setFreq(freq_1)
        self.generator_2.setFreq(freq_2)

        self.settingsChanged.emit()

    # Включение/выключение генератора
    def stateChanged(self):
        self.settingsChanged.emit()

    def resetX(self):
        self.generator_1.resetX()
        self.generator_2.resetX()

    # Генерация
    def gen(self, sampleCount: int) -> numpy.array:
        if self.ui.enable.isChecked():
            return self.generator_1.gen(sampleCount) + self.generator_2.gen(sampleCount)
        else:
            return numpy.zeros(sampleCount)
