import sys
import json

from typing import List, Tuple, Dict

import numpy
import pyaudio
import pyximport    # Compile cython and cpp files
pyximport.install(build_in_temp=False, language_level=3, setup_args={"script_args": ["--cython-cplus"]})

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QFileDialog

from ui.headers.ui_MainWindow import Ui_MainWindow

import ui.generators    # Импорт всех генераторов
from  ui.BaseGenerator import BaseGenerator, GENERATOR_LIST

from ui.utils.SignalPlotter import SignalPlotter

from ui.utils import AddToFrame, RemoveFromFrame


SAMPLERATE = 16000
STREAM_BUFFER_SIZE = 1000



class SignalGeneratorApp(QMainWindow):
    generators: List[BaseGenerator] = []

    appAlive = True

    needUpdateSamples = True
    samples = numpy.zeros(SAMPLERATE)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(1000, 800)
        self.setWindowTitle("Генератор сигналов")

        self.generatorsFrame = QFrame()
        layout = QVBoxLayout(self.generatorsFrame)
        layout.setAlignment(Qt.AlignTop)
        self.ui.generatorsScrollArea.setWidget(self.generatorsFrame)

        self.ui.menuSave.triggered.connect(self.saveConfig)
        self.ui.menuLoad.triggered.connect(self.loadConfig)

        # Список генераторов
        for generator in GENERATOR_LIST:
            self.ui.generatorList.addItem(generator.name)

        # Инициализация вывода звука
        self.audio = pyaudio.PyAudio()

        # Список выходов сигнала
        self.deviceIndexes = []
        for i in range(self.audio.get_device_count()):
            dev = self.audio.get_device_info_by_index(i)

            if dev.get('hostApi', -1) == 0 and dev.get("maxOutputChannels", 0) > 0:
                self.ui.outputDevice.addItem(dev.get("name"))
                self.deviceIndexes.append(dev.get("index"))

        self.audioStream = None

        # Инициализация и добавление отображения сигнала
        self.signalPlotter = SignalPlotter(SAMPLERATE, 1.0)
        AddToFrame(self.ui.signalViewer, self.signalPlotter)

        # Callback для добавления сигнала
        self.ui.addGenerator.clicked.connect(self.addGenerator)

        # Callback для смены выхода сигнала
        self.ui.outputDevice.currentIndexChanged.connect(self.initAudioStream)
        self.initAudioStream()

    def saveConfig(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        configPath, _ = QFileDialog.getSaveFileName(self, "Сохранение конфигурации", "", "Config files (*.cfg)", options=options)

        if not configPath: return

        allConfig = []
        for generator in self.generators:
            allConfig.append({"name": generator.name, "config": generator.GetConfig()})

        with open(configPath, "w") as cfgFile:
            cfgFile.write(json.dumps(allConfig))

    def loadConfig(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        configPath, _ = QFileDialog.getOpenFileName(self, "Загрузка конфигурации", "", "Config files (*.cfg)", options=options)

        if not configPath: return

        with open(configPath, "r") as cfgFile:
            try:
                config = json.loads(cfgFile.read())
            except:
                return

        for genInstance in self.generators:
            self.removeGenerator(genInstance)

        for genConfig in config:
            if "name" not in genConfig: continue
            if "config" not in genConfig: continue

            for generator in GENERATOR_LIST:
                if generator.name == genConfig.get("name"):
                    genInstance = generator(SAMPLERATE)
                    genInstance.remove.connect(self.removeGenerator)
                    genInstance.settingsChanged.connect(self.generatorSettingsChanged)

                    self.generators.append(genInstance)
                    AddToFrame(self.generatorsFrame, genInstance)

                    genInstance.LoadConfig(genConfig.get("config"))


    def initAudioStream(self):
        deviceIndex = self.deviceIndexes[self.ui.outputDevice.currentIndex()]

        if self.audioStream is not None:
            self.audio.close(self.audioStream)

        self.audioStream = self.audio.open(format=pyaudio.paFloat32,
                                           channels=1,
                                           rate=SAMPLERATE,
                                           output=True,
                                           output_device_index=deviceIndex,
                                           frames_per_buffer=STREAM_BUFFER_SIZE,
                                           stream_callback=self.generatorStreamCallback)

    # Событие закрытия главного окна
    def closeEvent(self, event: QCloseEvent) -> None:
        self.appAlive = False

        event.accept()

    def addGenerator(self):
        generator: BaseGenerator = GENERATOR_LIST[self.ui.generatorList.currentIndex()]

        genInstance = generator(SAMPLERATE)
        genInstance.remove.connect(self.removeGenerator)
        genInstance.settingsChanged.connect(self.generatorSettingsChanged)

        self.generators.append(genInstance)
        AddToFrame(self.generatorsFrame, genInstance)

        self.generatorSettingsChanged()

    def removeGenerator(self, genInstance: BaseGenerator):
        self.generators.remove(genInstance)
        RemoveFromFrame(self.generatorsFrame, genInstance)

        self.generatorSettingsChanged()

    def generatorSettingsChanged(self):
        # Нулевой сигнал
        samples = numpy.zeros(SAMPLERATE, dtype=float)

        # Сумма сигналов
        for generator in self.generators:
            generator.resetX()
            samples = numpy.sum([samples, generator.gen(len(samples))], axis=0)

        # Отображение сигнала
        self.signalPlotter.setSamples(samples.clip(-1.0, 1.0))

    def generatorStreamCallback(self, in_data, frame_count, time_info, status) -> Tuple[numpy.array, int]:
        # Нулевой сигнал
        samples = numpy.zeros(STREAM_BUFFER_SIZE, dtype=int)

        # Сумма сигналов
        for generator in self.generators:
            samples = numpy.sum([samples, generator.gen(len(samples))], axis=0)

        # Ограничение сигнала
        samples = samples.clip(-1.0, 1.0)

        return (samples.astype(numpy.float32), pyaudio.paContinue)





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SignalGeneratorApp()
    window.show()

    exitId = app.exec()
    sys.exit(exitId)
