import numpy


from ui.headers.ui_AmGenerator import Ui_AmGenerator

from ui.BaseGenerator import BaseGenerator, GENERATOR_LIST

from signalGenerators.sinGen import SinusGenerator


class AmGenerator(BaseGenerator):
    name = "АМ"

    def __init__(self, samplerate):
        super().__init__()

        self.ui = Ui_AmGenerator()
        self.ui.setupUi(self)

        self.ui.enable.stateChanged.connect(self.stateChanged)
        self.ui.remove.clicked.connect(lambda: self.remove.emit(self))

        self.ui.levelSlider.valueChanged.connect(self.levelSliderChanged)
        self.ui.freqSlider.valueChanged.connect(self.freqSliderChanged)
        self.ui.modFreqSlider.valueChanged.connect(self.modFreqSliderChanged)

        self.ui.levelSpin.valueChanged.connect(self.levelSpinChanged)
        self.ui.freqSpin.valueChanged.connect(self.freqSpinChanged)
        self.ui.modFreqSpin.valueChanged.connect(self.modFreqSpinChanged)

        self.generator = SinusGenerator(samplerate)
        self.modulation = SinusGenerator(samplerate)
        self.modulation.setAmp(0.5)

    # Эвенты изменения положения слайдеров
    def levelSliderChanged(self):
        value = self.ui.levelSlider.value()
        self.ui.levelSpin.setValue(value)
        self.ampSet(value)

    def freqSliderChanged(self):
        value = self.ui.freqSlider.value()
        self.ui.freqSpin.setValue(value)
        self.freqSet(value)

    def modFreqSliderChanged(self):
        value = self.ui.modFreqSlider.value()
        self.ui.modFreqSpin.setValue(value)
        self.modFreqSet(value)

    # Эвенты изменения значения
    def levelSpinChanged(self):
        value = self.ui.levelSpin.value()
        self.ui.levelSlider.setValue(value)
        self.ampSet(value)

    def freqSpinChanged(self):
        value = self.ui.freqSpin.value()
        self.ui.freqSlider.setValue(value)
        self.freqSet(value)

    def modFreqSpinChanged(self):
        value = self.ui.modFreqSpin.value()
        self.ui.modFreqSlider.setValue(value)
        self.modFreqSet(value)

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
