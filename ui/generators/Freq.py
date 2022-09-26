import numpy


from ui.headers.ui_FreqGenerator import Ui_FreqGenerator

from ui.BaseGenerator import BaseGenerator

from signalGenerators.sinGen import SinusGenerator


class FreqGenerator(BaseGenerator):
    name = "Несущая"

    def __init__(self, samplerate):
        super().__init__()

        self.ui = Ui_FreqGenerator()
        self.ui.setupUi(self)

        self.ui.enable.stateChanged.connect(self.stateChanged)
        self.ui.remove.clicked.connect(lambda: self.remove.emit(self))

        self.ui.levelSlider.valueChanged.connect(self.levelSliderChanged)
        self.ui.freqSlider.valueChanged.connect(self.freqSliderChanged)

        self.ui.levelSpin.valueChanged.connect(self.levelSpinChanged)
        self.ui.freqSpin.valueChanged.connect(self.freqSpinChanged)

        self.generator = SinusGenerator(samplerate)

    # Эвенты изменения положения слайдеров
    def levelSliderChanged(self):
        value = self.ui.levelSlider.value()
        self.ui.levelSpin.setValue(value)
        self.ampSet(value)

    def freqSliderChanged(self):
        value = self.ui.freqSlider.value()
        self.ui.freqSpin.setValue(value)
        self.freqSet(value)

    # Эвенты изменения значения
    def levelSpinChanged(self):
        value = self.ui.levelSpin.value()
        self.ui.levelSlider.setValue(value)
        self.ampSet(value)

    def freqSpinChanged(self):
        value = self.ui.freqSpin.value()
        self.ui.freqSlider.setValue(value)
        self.freqSet(value)

    # Установка значения в генератор
    def ampSet(self, amp: int):
        self.generator.setAmp(amp / 100)
        self.settingsChanged.emit()

    def freqSet(self, freq):
        self.generator.setFreq(freq)
        self.settingsChanged.emit()

    # Включение/выключение генератора
    def stateChanged(self):
        self.settingsChanged.emit()

    def resetX(self):
        self.generator.resetX()

    # Генерация
    def gen(self, sampleCount: int) -> numpy.array:
        if self.ui.enable.isChecked():
            return self.generator.gen(sampleCount)
        else:
            return numpy.zeros(sampleCount)
