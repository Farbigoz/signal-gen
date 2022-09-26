# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoiseGeneratorEyOzId.app'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_NoiseGenerator(object):
    def setupUi(self, NoiseGenerator):
        if not NoiseGenerator.objectName():
            NoiseGenerator.setObjectName(u"NoiseGenerator")
        NoiseGenerator.resize(754, 76)
        NoiseGenerator.setMinimumSize(QSize(0, 0))
        NoiseGenerator.setMaximumSize(QSize(16777215, 1000))
        self.verticalLayout = QVBoxLayout(NoiseGenerator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QGroupBox(NoiseGenerator)
        self.root.setObjectName(u"root")
        self.root.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.root)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.enable = QCheckBox(self.root)
        self.enable.setObjectName(u"enable")
        self.enable.setMinimumSize(QSize(70, 0))
        self.enable.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.enable, 0, 4, 1, 1)

        self.levelLabel = QLabel(self.root)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.levelLabel, 0, 1, 1, 1)

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

        self.remove = QPushButton(self.root)
        self.remove.setObjectName(u"remove")
        self.remove.setMinimumSize(QSize(70, 0))
        self.remove.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.remove, 2, 4, 1, 1)


        self.verticalLayout.addWidget(self.root, 0, Qt.AlignTop)


        self.retranslateUi(NoiseGenerator)

        QMetaObject.connectSlotsByName(NoiseGenerator)
    # setupUi

    def retranslateUi(self, NoiseGenerator):
        NoiseGenerator.setWindowTitle(QCoreApplication.translate("NoiseGenerator", u"Form", None))
        self.root.setTitle(QCoreApplication.translate("NoiseGenerator", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0428\u0443\u043c\u0430", None))
        self.enable.setText(QCoreApplication.translate("NoiseGenerator", u"\u0412\u043a\u043b\u044e\u0447\u0451\u043d", None))
        self.levelLabel.setText(QCoreApplication.translate("NoiseGenerator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.remove.setText(QCoreApplication.translate("NoiseGenerator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

