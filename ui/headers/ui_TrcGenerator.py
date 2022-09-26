# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrcGeneratorpCXonb.app'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_TrcGenerator(object):
    def setupUi(self, TrcGenerator):
        if not TrcGenerator.objectName():
            TrcGenerator.setObjectName(u"TrcGenerator")
        TrcGenerator.resize(754, 101)
        TrcGenerator.setMinimumSize(QSize(0, 0))
        TrcGenerator.setMaximumSize(QSize(16777215, 1000))
        self.verticalLayout = QVBoxLayout(TrcGenerator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QGroupBox(TrcGenerator)
        self.root.setObjectName(u"root")
        self.root.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.root)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.freqLabel = QLabel(self.root)
        self.freqLabel.setObjectName(u"freqLabel")

        self.gridLayout.addWidget(self.freqLabel, 2, 1, 1, 1)

        self.enable = QCheckBox(self.root)
        self.enable.setObjectName(u"enable")
        self.enable.setMinimumSize(QSize(70, 0))
        self.enable.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.enable, 0, 4, 1, 1)

        self.remove = QPushButton(self.root)
        self.remove.setObjectName(u"remove")
        self.remove.setMinimumSize(QSize(70, 0))
        self.remove.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.remove, 4, 4, 1, 1)

        self.levelLabel = QLabel(self.root)
        self.levelLabel.setObjectName(u"levelLabel")
        self.levelLabel.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.levelLabel, 0, 1, 1, 1)

        self.modFreqLabel = QLabel(self.root)
        self.modFreqLabel.setObjectName(u"modFreqLabel")

        self.gridLayout.addWidget(self.modFreqLabel, 4, 1, 1, 1)

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

        self.freqFrame = QFrame(self.root)
        self.freqFrame.setObjectName(u"freqFrame")
        self.freqFrame.setFrameShape(QFrame.StyledPanel)
        self.freqFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.freqFrame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.f420 = QRadioButton(self.freqFrame)
        self.f420.setObjectName(u"f420")
        self.f420.setChecked(True)

        self.gridLayout_4.addWidget(self.f420, 0, 0, 1, 1)

        self.f480 = QRadioButton(self.freqFrame)
        self.f480.setObjectName(u"f480")

        self.gridLayout_4.addWidget(self.f480, 0, 1, 1, 1)

        self.f565 = QRadioButton(self.freqFrame)
        self.f565.setObjectName(u"f565")

        self.gridLayout_4.addWidget(self.f565, 0, 2, 1, 1)

        self.f720 = QRadioButton(self.freqFrame)
        self.f720.setObjectName(u"f720")

        self.gridLayout_4.addWidget(self.f720, 0, 3, 1, 1)

        self.f780 = QRadioButton(self.freqFrame)
        self.f780.setObjectName(u"f780")

        self.gridLayout_4.addWidget(self.f780, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.freqFrame, 2, 2, 1, 2)

        self.modFreqFrame = QFrame(self.root)
        self.modFreqFrame.setObjectName(u"modFreqFrame")
        self.modFreqFrame.setFrameShape(QFrame.StyledPanel)
        self.modFreqFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.modFreqFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mf12 = QRadioButton(self.modFreqFrame)
        self.mf12.setObjectName(u"mf12")

        self.gridLayout_3.addWidget(self.mf12, 0, 1, 1, 1)

        self.mf8 = QRadioButton(self.modFreqFrame)
        self.mf8.setObjectName(u"mf8")
        self.mf8.setChecked(True)

        self.gridLayout_3.addWidget(self.mf8, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.modFreqFrame, 4, 2, 1, 2)


        self.verticalLayout.addWidget(self.root, 0, Qt.AlignTop)


        self.retranslateUi(TrcGenerator)

        QMetaObject.connectSlotsByName(TrcGenerator)
    # setupUi

    def retranslateUi(self, TrcGenerator):
        TrcGenerator.setWindowTitle(QCoreApplication.translate("TrcGenerator", u"Form", None))
        self.root.setTitle(QCoreApplication.translate("TrcGenerator", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0422\u0420\u0426", None))
        self.freqLabel.setText(QCoreApplication.translate("TrcGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.enable.setText(QCoreApplication.translate("TrcGenerator", u"\u0412\u043a\u043b\u044e\u0447\u0451\u043d", None))
        self.remove.setText(QCoreApplication.translate("TrcGenerator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.levelLabel.setText(QCoreApplication.translate("TrcGenerator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.modFreqLabel.setText(QCoreApplication.translate("TrcGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u0438", None))
        self.f420.setText(QCoreApplication.translate("TrcGenerator", u"420 \u0413\u0446", None))
        self.f480.setText(QCoreApplication.translate("TrcGenerator", u"480 \u0413\u0446", None))
        self.f565.setText(QCoreApplication.translate("TrcGenerator", u"565 \u0413\u0446", None))
        self.f720.setText(QCoreApplication.translate("TrcGenerator", u"720 \u0413\u0446", None))
        self.f780.setText(QCoreApplication.translate("TrcGenerator", u"780 \u0413\u0446", None))
        self.mf12.setText(QCoreApplication.translate("TrcGenerator", u"12 \u0413\u0446", None))
        self.mf8.setText(QCoreApplication.translate("TrcGenerator", u"8 \u0413\u0446", None))
    # retranslateUi

