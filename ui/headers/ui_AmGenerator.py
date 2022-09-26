# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AmGeneratorDXatCe.app'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_AmGenerator(object):
    def setupUi(self, AmGenerator):
        if not AmGenerator.objectName():
            AmGenerator.setObjectName(u"AmGenerator")
        AmGenerator.resize(754, 104)
        AmGenerator.setMinimumSize(QSize(0, 0))
        AmGenerator.setMaximumSize(QSize(16777215, 1000))
        self.verticalLayout = QVBoxLayout(AmGenerator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QGroupBox(AmGenerator)
        self.root.setObjectName(u"root")
        self.root.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.root)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.levelSlider = QSlider(self.root)
        self.levelSlider.setObjectName(u"levelSlider")
        self.levelSlider.setMinimumSize(QSize(100, 0))
        self.levelSlider.setMaximum(100)
        self.levelSlider.setPageStep(1)
        self.levelSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.levelSlider, 0, 2, 1, 1)

        self.levelSpin = QSpinBox(self.root)
        self.levelSpin.setObjectName(u"levelSpin")
        self.levelSpin.setMinimumSize(QSize(80, 0))
        self.levelSpin.setMaximumSize(QSize(16777215, 16777215))
        self.levelSpin.setMaximum(100)
        self.levelSpin.setSingleStep(1)

        self.gridLayout.addWidget(self.levelSpin, 0, 3, 1, 1)

        self.freqLabel = QLabel(self.root)
        self.freqLabel.setObjectName(u"freqLabel")
        self.freqLabel.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.freqLabel, 1, 1, 1, 1)

        self.modFreqSlider = QSlider(self.root)
        self.modFreqSlider.setObjectName(u"modFreqSlider")
        self.modFreqSlider.setMinimumSize(QSize(100, 0))
        self.modFreqSlider.setMaximum(100)
        self.modFreqSlider.setPageStep(1)
        self.modFreqSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.modFreqSlider, 3, 2, 1, 1)

        self.modFreqSpin = QSpinBox(self.root)
        self.modFreqSpin.setObjectName(u"modFreqSpin")
        self.modFreqSpin.setMinimumSize(QSize(80, 0))
        self.modFreqSpin.setMaximum(100)
        self.modFreqSpin.setSingleStep(1)

        self.gridLayout.addWidget(self.modFreqSpin, 3, 3, 1, 1)

        self.enable = QCheckBox(self.root)
        self.enable.setObjectName(u"enable")
        self.enable.setMinimumSize(QSize(70, 0))
        self.enable.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.enable, 0, 4, 1, 1)

        self.freqSlider = QSlider(self.root)
        self.freqSlider.setObjectName(u"freqSlider")
        self.freqSlider.setMinimumSize(QSize(100, 0))
        self.freqSlider.setMaximum(2000)
        self.freqSlider.setPageStep(1)
        self.freqSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.freqSlider, 1, 2, 1, 1)

        self.levelLabel = QLabel(self.root)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.levelLabel, 0, 1, 1, 1)

        self.modFreqLabel = QLabel(self.root)
        self.modFreqLabel.setObjectName(u"modFreqLabel")
        self.modFreqLabel.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.modFreqLabel, 3, 1, 1, 1)

        self.freqSpin = QSpinBox(self.root)
        self.freqSpin.setObjectName(u"freqSpin")
        self.freqSpin.setMinimumSize(QSize(80, 0))
        self.freqSpin.setMaximum(2000)
        self.freqSpin.setSingleStep(1)

        self.gridLayout.addWidget(self.freqSpin, 1, 3, 1, 1)

        self.remove = QPushButton(self.root)
        self.remove.setObjectName(u"remove")
        self.remove.setMinimumSize(QSize(70, 0))
        self.remove.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.remove, 3, 4, 1, 1)


        self.verticalLayout.addWidget(self.root, 0, Qt.AlignTop)


        self.retranslateUi(AmGenerator)

        QMetaObject.connectSlotsByName(AmGenerator)
    # setupUi

    def retranslateUi(self, AmGenerator):
        AmGenerator.setWindowTitle(QCoreApplication.translate("AmGenerator", u"Form", None))
        self.root.setTitle(QCoreApplication.translate("AmGenerator", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0410\u041c", None))
        self.freqLabel.setText(QCoreApplication.translate("AmGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.enable.setText(QCoreApplication.translate("AmGenerator", u"\u0412\u043a\u043b\u044e\u0447\u0451\u043d", None))
        self.levelLabel.setText(QCoreApplication.translate("AmGenerator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.modFreqLabel.setText(QCoreApplication.translate("AmGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 AM \u043c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.remove.setText(QCoreApplication.translate("AmGenerator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

