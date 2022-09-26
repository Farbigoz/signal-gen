import enum
import numpy

from ui.headers.ui_KrlGenerator import Ui_KrlGenerator

from ui.BaseGenerator import BaseGenerator

from signalGenerators.KrlGen import CPPKrlGen


class FreqEnum(enum.IntEnum):
    F_475_HZ = 0
    F_525_HZ = 1
    F_575_HZ = 2
    F_625_HZ = 3
    F_675_HZ = 4
    F_725_HZ = 5
    F_775_HZ = 6
    F_825_HZ = 7
    F_875_HZ = 8
    F_925_HZ = 9


BAUER_CODES = [0x00, 0x2C, 0x32, 0x4A, 0x54, 0x67, 0x79, 0x86, 0x98, 0xAB, 0xB5, 0xCD, 0xD3]


class KrlGenerator(BaseGenerator):
    name = "КРЛ"

    def __init__(self, samplerate):
        super().__init__()

        self.ui = Ui_KrlGenerator()
        self.ui.setupUi(self)

        # Список кодов бауэра
        for code in BAUER_CODES:
            self.ui.codeList.addItem(hex(code))

        # Включить/ Выключить
        self.ui.enable.stateChanged.connect(self.stateChanged)
        # Удалить
        self.ui.remove.clicked.connect(lambda: self.remove.emit(self))

        self.ui.codeList.currentIndexChanged.connect(self.codeChanged)

        # Изменение уровня
        self.ui.levelSlider.valueChanged.connect(self.levelSliderChanged)
        self.ui.levelSpin.valueChanged.connect(self.levelSpinChanged)

        # Изменение несущей частоты
        self.ui.f475.toggled.connect(self.freqChanged)
        self.ui.f525.toggled.connect(self.freqChanged)
        self.ui.f575.toggled.connect(self.freqChanged)
        self.ui.f625.toggled.connect(self.freqChanged)
        self.ui.f675.toggled.connect(self.freqChanged)
        self.ui.f725.toggled.connect(self.freqChanged)
        self.ui.f775.toggled.connect(self.freqChanged)
        self.ui.f825.toggled.connect(self.freqChanged)
        self.ui.f875.toggled.connect(self.freqChanged)
        self.ui.f925.toggled.connect(self.freqChanged)

        # Генераторы
        self.generator = CPPKrlGen(samplerate)

        # Установить частоты по-умолчанию
        self.freqChanged()

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

    # Код изменён
    def codeChanged(self):
        codeNum = self.ui.codeList.currentIndex()
        code = BAUER_CODES[codeNum]
        self.codeSet(code)

    # Извенение частоты несущей
    def freqChanged(self):
        if self.ui.f475.isChecked():
            freq = FreqEnum.F_475_HZ

        elif self.ui.f525.isChecked():
            freq = FreqEnum.F_525_HZ

        elif self.ui.f575.isChecked():
            freq = FreqEnum.F_575_HZ

        elif self.ui.f625.isChecked():
            freq = FreqEnum.F_625_HZ

        elif self.ui.f675.isChecked():
            freq = FreqEnum.F_675_HZ

        elif self.ui.f725.isChecked():
            freq = FreqEnum.F_725_HZ

        elif self.ui.f775.isChecked():
            freq = FreqEnum.F_775_HZ

        elif self.ui.f825.isChecked():
            freq = FreqEnum.F_825_HZ

        elif self.ui.f875.isChecked():
            freq = FreqEnum.F_875_HZ

        elif self.ui.f925.isChecked():
            freq = FreqEnum.F_925_HZ

        else:
            return

        self.freqSet(freq)

    # Установка значения в генератор
    def ampSet(self, amp: int):
        self.generator.SetAmp(int((amp / 100) * 0x7fff))
        self.settingsChanged.emit()

    def freqSet(self, freq: FreqEnum):
        self.generator.SetCarrier(freq.value)
        self.settingsChanged.emit()

    def codeSet(self, code: int):
        self.generator.SetCode(code)
        self.settingsChanged.emit()

    # Включение/выключение генератора
    def stateChanged(self):
        self.settingsChanged.emit()

    # Генерация
    def gen(self, sampleCount: int) -> numpy.array:
        if self.ui.enable.isChecked():
            return numpy.array([self.generator.Out() / 0x7fff for _ in range(sampleCount)])
        else:
            return numpy.zeros(sampleCount)
