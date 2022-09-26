# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KrlGeneratorOkWMUD.app'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_KrlGenerator(object):
    def setupUi(self, KrlGenerator):
        if not KrlGenerator.objectName():
            KrlGenerator.setObjectName(u"KrlGenerator")
        KrlGenerator.resize(754, 118)
        KrlGenerator.setMinimumSize(QSize(0, 0))
        KrlGenerator.setMaximumSize(QSize(16777215, 1000))
        self.verticalLayout = QVBoxLayout(KrlGenerator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QGroupBox(KrlGenerator)
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

        self.codeLabel = QLabel(self.root)
        self.codeLabel.setObjectName(u"codeLabel")

        self.gridLayout.addWidget(self.codeLabel, 4, 1, 1, 1)

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
        self.f475 = QRadioButton(self.freqFrame)
        self.f475.setObjectName(u"f475")
        self.f475.setChecked(True)

        self.gridLayout_4.addWidget(self.f475, 0, 0, 1, 1)

        self.f525 = QRadioButton(self.freqFrame)
        self.f525.setObjectName(u"f525")

        self.gridLayout_4.addWidget(self.f525, 0, 1, 1, 1)

        self.f575 = QRadioButton(self.freqFrame)
        self.f575.setObjectName(u"f575")

        self.gridLayout_4.addWidget(self.f575, 0, 2, 1, 1)

        self.f625 = QRadioButton(self.freqFrame)
        self.f625.setObjectName(u"f625")

        self.gridLayout_4.addWidget(self.f625, 0, 3, 1, 1)

        self.f675 = QRadioButton(self.freqFrame)
        self.f675.setObjectName(u"f675")

        self.gridLayout_4.addWidget(self.f675, 0, 4, 1, 1)

        self.f725 = QRadioButton(self.freqFrame)
        self.f725.setObjectName(u"f725")

        self.gridLayout_4.addWidget(self.f725, 1, 0, 1, 1)

        self.f775 = QRadioButton(self.freqFrame)
        self.f775.setObjectName(u"f775")

        self.gridLayout_4.addWidget(self.f775, 1, 1, 1, 1)

        self.f825 = QRadioButton(self.freqFrame)
        self.f825.setObjectName(u"f825")

        self.gridLayout_4.addWidget(self.f825, 1, 2, 1, 1)

        self.f875 = QRadioButton(self.freqFrame)
        self.f875.setObjectName(u"f875")

        self.gridLayout_4.addWidget(self.f875, 1, 3, 1, 1)

        self.f925 = QRadioButton(self.freqFrame)
        self.f925.setObjectName(u"f925")

        self.gridLayout_4.addWidget(self.f925, 1, 4, 1, 1)


        self.gridLayout.addWidget(self.freqFrame, 2, 2, 1, 2)

        self.codeList = QComboBox(self.root)
        self.codeList.setObjectName(u"codeList")

        self.gridLayout.addWidget(self.codeList, 4, 2, 1, 2)


        self.verticalLayout.addWidget(self.root, 0, Qt.AlignTop)


        self.retranslateUi(KrlGenerator)

        QMetaObject.connectSlotsByName(KrlGenerator)
    # setupUi

    def retranslateUi(self, KrlGenerator):
        KrlGenerator.setWindowTitle(QCoreApplication.translate("KrlGenerator", u"Form", None))
        self.root.setTitle(QCoreApplication.translate("KrlGenerator", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u041a\u0420\u041b", None))
        self.freqLabel.setText(QCoreApplication.translate("KrlGenerator", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.enable.setText(QCoreApplication.translate("KrlGenerator", u"\u0412\u043a\u043b\u044e\u0447\u0451\u043d", None))
        self.remove.setText(QCoreApplication.translate("KrlGenerator", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.levelLabel.setText(QCoreApplication.translate("KrlGenerator", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.codeLabel.setText(QCoreApplication.translate("KrlGenerator", u"\u041a\u043e\u0434\u043e\u0432\u0430\u044f \u043f\u043e\u0441\u044b\u043b\u043a\u0430", None))
        self.f475.setText(QCoreApplication.translate("KrlGenerator", u"475 \u0413\u0446", None))
        self.f525.setText(QCoreApplication.translate("KrlGenerator", u"525 \u0413\u0446", None))
        self.f575.setText(QCoreApplication.translate("KrlGenerator", u"575 \u0413\u0446", None))
        self.f625.setText(QCoreApplication.translate("KrlGenerator", u"625 \u0413\u0446", None))
        self.f675.setText(QCoreApplication.translate("KrlGenerator", u"675 \u0413\u0446", None))
        self.f725.setText(QCoreApplication.translate("KrlGenerator", u"725 \u0413\u0446", None))
        self.f775.setText(QCoreApplication.translate("KrlGenerator", u"775 \u0413\u0446", None))
        self.f825.setText(QCoreApplication.translate("KrlGenerator", u"825 \u0413\u0446", None))
        self.f875.setText(QCoreApplication.translate("KrlGenerator", u"875 \u0413\u0446", None))
        self.f925.setText(QCoreApplication.translate("KrlGenerator", u"925 \u0413\u0446", None))
    # retranslateUi

