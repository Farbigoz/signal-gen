import numpy

from ui.headers.ui_NoiseGenerator import Ui_NoiseGenerator

from ui.BaseGenerator import BaseGenerator


class NoiseGenerator(BaseGenerator):
    name = "Шум"

    def __init__(self, samplerate):
        super().__init__()

        self.ui = Ui_NoiseGenerator()
        self.ui.setupUi(self)

        self.ui.enable.stateChanged.connect(self.stateChanged)
        self.ui.remove.clicked.connect(lambda: self.remove.emit(self))

        self.ui.levelSlider.valueChanged.connect(self.levelSliderChanged)

        self.ui.levelSpin.valueChanged.connect(self.levelSpinChanged)

        self.amp = 0

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

    # Установка значения в генератор
    def ampSet(self, amp: int):
        self.amp = amp
        self.settingsChanged.emit()

    # Включение/выключение генератора
    def stateChanged(self):
        self.settingsChanged.emit()

    # Генерация
    def gen(self, sampleCount: int) -> numpy.array:
        if self.ui.enable.isChecked():
            return (numpy.random.random_integers(-self.amp, self.amp, sampleCount)) / 100
        else:
            return numpy.zeros(sampleCount)
