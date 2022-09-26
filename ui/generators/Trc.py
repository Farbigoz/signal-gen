import enum
import numpy

from ui.headers.ui_TrcGenerator import Ui_TrcGenerator

from ui.BaseGenerator import BaseGenerator

from signalGenerators.sinGen import SinusGenerator


class FreqEnum(enum.IntEnum):
    F_420_HZ = 420
    F_480_HZ = 480
    F_565_HZ = 565
    F_720_HZ = 720
    F_780_HZ = 780


class ModFreqEnum(enum.IntEnum):
    F_8_HZ = 8
    F_12_HZ = 12


class TrcGenerator(BaseGenerator):
    name = "ТРЦ3 Метро"

    def __init__(self, samplerate):
        super().__init__()

        self.ui = Ui_TrcGenerator()
        self.ui.setupUi(self)

        self.ui.enable.stateChanged.connect(self.stateChanged)
        self.ui.remove.clicked.connect(lambda: self.remove.emit(self))

        # Изменение уровня
        self.ui.levelSlider.valueChanged.connect(self.levelSliderChanged)
        self.ui.levelSpin.valueChanged.connect(self.levelSpinChanged)

        # Изменение несущей частоты
        self.ui.f420.toggled.connect(self.freqChanged)
        self.ui.f480.toggled.connect(self.freqChanged)
        self.ui.f565.toggled.connect(self.freqChanged)
        self.ui.f720.toggled.connect(self.freqChanged)
        self.ui.f780.toggled.connect(self.freqChanged)

        # Изменение частоты модуляции
        self.ui.mf8.toggled.connect(self.modFreqChanged)
        self.ui.mf12.toggled.connect(self.modFreqChanged)

        # Генераторы
        self.generator = SinusGenerator(samplerate)
        self.modulation = SinusGenerator(samplerate)
        self.modulation.setAmp(0.5)

        # Установить частоты по-умолчанию
        self.freqChanged()
        self.modFreqChanged()

    # Эвенты изменения положения слайдеров
    def levelSliderChanged(self):
        value = self.ui.levelSlider.value()
        self.ui.levelSpin.setValue(value)
        self.ampSet(value)

    # Эвенты изменения значения
    def levelSpinChanged(self):
        value = self.ui.levelSpin.value()
        self.ui.levelSlider.setValue(value)
        self.ampSet(value)

    # Извенение частоты несущей
    def freqChanged(self):
        if self.ui.f420.isChecked():
            freq = FreqEnum.F_420_HZ

        elif self.ui.f480.isChecked():
            freq = FreqEnum.F_480_HZ

        elif self.ui.f565.isChecked():
            freq = FreqEnum.F_565_HZ

        elif self.ui.f720.isChecked():
            freq = FreqEnum.F_720_HZ

        elif self.ui.f780.isChecked():
            freq = FreqEnum.F_780_HZ

        else:
            return

        self.freqSet(freq.value)

    # Изменение частоты модуляции
    def modFreqChanged(self):
        if self.ui.mf8.isChecked():
            freq = ModFreqEnum.F_8_HZ

        elif self.ui.mf12.isChecked():
            freq = ModFreqEnum.F_12_HZ

        else:
            return

        self.modFreqSet(freq.value)

    # Установка значения в генератор
    def ampSet(self, amp: int):
        self.generator.setAmp(amp / 100)
        self.settingsChanged.emit()

    def freqSet(self, freq):
        self.generator.setFreq(freq)
        self.settingsChanged.emit()

    def modFreqSet(self, modFreq):
        self.modulation.setFreq(modFreq)
        self.settingsChanged.emit()

    # Включение/выключение генератора
    def stateChanged(self):
        self.settingsChanged.emit()

    def resetX(self):
        self.generator.resetX()
        self.modulation.resetX()

    # Генерация
    def gen(self, sampleCount: int) -> numpy.array:
        if self.ui.enable.isChecked():
            if self.modulation.freq == 0.0:
                return self.generator.gen(sampleCount)
            else:
                return self.generator.gen(sampleCount) * (self.modulation.gen(sampleCount) + 0.5)
        else:
            return numpy.zeros(sampleCount)
