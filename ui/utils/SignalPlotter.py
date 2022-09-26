from typing import List

import pyqtgraph

from PyQt5.QtWidgets import QWidget, QVBoxLayout


class SignalPlotter(QWidget):
    def __init__(self, samplerate, maxLevel: float):
        super().__init__()

        self.graphWidget = pyqtgraph.PlotWidget()
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(-maxLevel, maxLevel)

        layout = QVBoxLayout()
        layout.addWidget(self.graphWidget)

        self.x = [0]

        pen = pyqtgraph.mkPen(color="#55cc11")
        self.line = self.graphWidget.plot(self.x, [0], pen=pen)

        self.setLayout(layout)

        xStep = 1 / samplerate
        self.x = [xStep * k for k in range(samplerate)]

    def setSamples(self, samples: List[int]):
        self.line.setData(self.x, samples)
