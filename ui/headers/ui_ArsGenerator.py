# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArsGeneratordGDIHI.app'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ArsGenerator(object):
    def setupUi(self, ArsGenerator):
        if not ArsGenerator.objectName():
            ArsGenerator.setObjectName(u"ArsGenerator")
        ArsGenerator.resize(754, 129)
        ArsGenerator.setMinimumSize(QSize(0, 0))
        ArsGenerator.setMaximumSize(QSize(16777215, 1000))
        self.verticalLayout = QVBoxLayout(ArsGenerator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QGroupBox(ArsGenerator)
        self.root.setObjectName(u"root")
        self.root.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.root)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.freqLabel_1 = QLabel(self.root)
        self.freqLabel_1.setObjectName(u"freqLabel_1")

        self.gridLayout.addWidget(self.freqLabel_1, 3, 1, 1, 1)

        self.enable = QCheckBox(self.root)
        self.enable.setObjectName(u"enable")
        self.enable.setMinimumSize(QSize(70, 0))
        self.enable.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.enable, 0, 4, 1, 1)

        self.freqFrame_1 = QFrame(self.root)
        self.freqFrame_1.setObjectName(u"freqFrame_1")
        self.freqFrame_1.setFrameShape(QFrame.StyledPanel)
        self.freqFrame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.freqFrame_1)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.f125_1 = QRadioButton(self.freqFrame_1)
        self.f125_1.setObjectName(u"f125_1")

        self.gridLayout_4.addWidget(self.f125_1, 0, 1, 1, 1)

        self.f175_1 = QRadioButton(self.freqFrame_1)
        self.f175_1.setObjectName(u"f175_1")

        self.gridLayout_4.addWidget(self.f175_1, 0, 2, 1, 1)

        self.f75_1 = QRadioButton(self.freqFrame_1)
        self.f75_1.setObjectName(u"f75_1")
        self.f75_1.setChecked(True)

        self.gridLayout_4.addWidget(self.f75_1, 0, 0, 1, 1)

        self.f225_1 = QRadioButton(self.freqFrame_1)
        self.f225_1.setObjectName(u"f225_1")

        self.gridLayout_4.addWidget(self.f225_1, 0, 3, 1, 1)

        self.f275_1 = QRadioButton(self.freqFrame_1)
        self.f275_1.setObjectName(u"f275_1")

        self.gridLayout_4.addWidget(self.f275_1, 0, 4, 1, 1)

        self.f325_1 = QRadioButton(self.freqFrame_1)
        self.f325_1.setObjectName(u"f325_1")

        self.gridLayout_4.addWidget(self.f325_1, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.freqFrame_1, 3, 2, 1, 2)

        self.remove = QPushButton(self.root)
        self.remove.setObjectName(u"remove")
        self.remove.setMinimumSize(QSize(70, 0))
        self.remove.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.remove, 6, 4, 1, 1)

        self.levelLabel_1 = QLabel(self.root)
        self.levelLabel_1.setObjectName(u"levelLabel_1")
        self.levelLabel_1.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.levelLabel_1, 0, 1, 1, 1)

        self.freqLabel_2 = QLabel(self.root)
        self.freqLabel_2.setObjectName(u"freqLabel_2")

        self.gridLayout.addWidget(self.freqLabel_2, 6, 1, 1, 1)

        self.levelSlider_1 = QSlider(self.root)
        self.levelSlider_1.setObjectName(u"levelSlider_1")
        self.levelSlider_1.setMinimumSize(QSize(100, 0))
        self.levelSlider_1.setMaximum(100)
        self.levelSlider_1.setPageStep(1)
        self.levelSlider_1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.levelSlider_1, 0, 2, 1, 1)

        self.levelSpin_1 = QSpinBox(self.root)
        self.levelSpin_1.setObjectName(u"levelSpin_1")
        self.levelSpin_1.setMinimumSize(QSize(80, 0))
        self.levelSpin_1.setMaximumSize(QSize(16777215, 16777215))
        self.levelSpin_1.setMaximum(100)
        self.levelSpin_1.setSingleStep(1)

        self.gridLayout.addWidget(self.levelSpin_1, 0, 3, 1, 1)

        self.freqFrame_2 = QFrame(self.root)
        self.freqFrame_2.setObjectName(u"freqFrame_2")
        self.freqFrame_2.setFrameShape(QFrame.StyledPanel)
        self.freqFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.freqFrame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.f75_2 = QRadioButton(self.freqFrame_2)
        self.f75_2.setObjectName(u"f75_2")
        self.f75_2.setChecked(True)

        self.gridLayout_3.addWidget(self.f75_2, 0, 0, 1, 1)

        self.f125_2 = QRadioButton(self.freqFrame_2)
        self.f125_2.setObjectName(u"f125_2")

        self.gridLayout_3.addWidget(self.f125_2, 0, 1, 1, 1)

        self.f175_2 = QRadioButton(self.freqFrame_2)
        self.f175_2.setObjectName(u"f175_2")

        self.gridLayout_3.addWidget(self.f175_2, 0, 2, 1, 1)

        self.f225_2 = QRadioButton(self.freqFrame_2)
        self.f225_2.setObjectName(u"f225_2")

        self.gridLayout_3.addWidget(self.f225_2, 0, 3, 1, 1)

        self.f275_2 = QRadioButton(self.freqFrame_2)
        self.f275_2.setObjectName(u"f275_2")

        self.gridLayout_3.addWidget(self.f275_2, 0, 4, 1, 1)

        self.f325_2 = QRadioButton(self.freqFrame_2)
        self.f325_2.setObjectName(u"f325_2")

        self.gridLayout_3.addWidget(self.f325_2, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.freqFrame_2, 6, 2, 1, 2)

        self.levelLabel_2 = QLabel(self.root)
        self.levelLabel_2.setObjectName(u"levelLabel_2")

        self.gridLayout.addWidget(self.levelLabel_2, 5, 1, 1, 1)

        self.levelSlider_2 = QSlider(self.root)
        self.levelSlider_2.setObjectName(u"levelSlider_2")
        self.levelSlider_2.setMaximum(100)
        self.levelSlider_2.setPageStep(1)
        self.levelSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.levelSlider_2, 5, 2, 1, 1)

        self.levelSpin_2 = QSpinBox(self.root)
        self.levelSpin_2.setObjectName(u"levelSpin_2")
        self.levelSpin_2.setMaximum(100)

        self.gridLayout.addWidget(self.levelSpin_2, 5, 3, 1, 1)


        self.verticalLayout.addWidget(self.root, 0, Qt.AlignTop)


        self.retranslateUi(ArsGenerator)

        QMetaObject.connectSlotsByName(ArsGenerator)
    # setupUi

    def retranslateUi(self, ArsGenerator):
        ArsGenerator.setWindowTitle(QCoreApplication.translate("ArsGenerator", u"Form", None))
        self.root.setTitle(QCoreApplication.translate("ArsGenerator", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0410\u0420\u0421", None))
        self.freqLabel_1.setText(QCoreApplication.translate("ArsGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 1", None))
        self.enable.setText(QCoreApplication.translate("ArsGenerator", u"\u0412\u043a\u043b\u044e\u0447\u0451\u043d", None))
        self.f125_1.setText(QCoreApplication.translate("ArsGenerator", u"125 \u0413\u0446", None))
        self.f175_1.setText(QCoreApplication.translate("ArsGenerator", u"175 \u0413\u0446", None))
        self.f75_1.setText(QCoreApplication.translate("ArsGenerator", u"75 \u0413\u0446", None))
        self.f225_1.setText(QCoreApplication.translate("ArsGenerator", u"225 \u0413\u0446", None))
        self.f275_1.setText(QCoreApplication.translate("ArsGenerator", u"275 \u0413\u0446", None))
        self.f325_1.setText(QCoreApplication.translate("ArsGenerator", u"325 \u0413\u0446", None))
        self.remove.setText(QCoreApplication.translate("ArsGenerator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.levelLabel_1.setText(QCoreApplication.translate("ArsGenerator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c 1", None))
        self.freqLabel_2.setText(QCoreApplication.translate("ArsGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 2", None))
        self.f75_2.setText(QCoreApplication.translate("ArsGenerator", u"75 \u0413\u0446", None))
        self.f125_2.setText(QCoreApplication.translate("ArsGenerator", u"125 \u0413\u0446", None))
        self.f175_2.setText(QCoreApplication.translate("ArsGenerator", u"175 \u0413\u0446", None))
        self.f225_2.setText(QCoreApplication.translate("ArsGenerator", u"225 \u0413\u0446", None))
        self.f275_2.setText(QCoreApplication.translate("ArsGenerator", u"275 \u0413\u0446", None))
        self.f325_2.setText(QCoreApplication.translate("ArsGenerator", u"325 \u0413\u0446", None))
        self.levelLabel_2.setText(QCoreApplication.translate("ArsGenerator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c 2", None))
    # retranslateUi

