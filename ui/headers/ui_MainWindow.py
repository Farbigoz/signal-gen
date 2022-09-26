# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowzwEujc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 611)
        self.menuLoad = QAction(MainWindow)
        self.menuLoad.setObjectName(u"menuLoad")
        self.menuSave = QAction(MainWindow)
        self.menuSave.setObjectName(u"menuSave")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.actionempty = QAction(MainWindow)
        self.actionempty.setObjectName(u"actionempty")
        self.actionempty.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QFrame(self.centralwidget)
        self.root.setObjectName(u"root")
        self.root.setFrameShape(QFrame.StyledPanel)
        self.root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.root)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.outputDevice = QComboBox(self.root)
        self.outputDevice.setObjectName(u"outputDevice")

        self.verticalLayout_4.addWidget(self.outputDevice)

        self.line = QFrame(self.root)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 10))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.splitter = QSplitter(self.root)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setFrameShadow(QFrame.Plain)
        self.splitter.setLineWidth(1)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(False)
        self.signalViewer = QGroupBox(self.splitter)
        self.signalViewer.setObjectName(u"signalViewer")
        self.signalViewer.setMinimumSize(QSize(0, 200))
        self.verticalLayout_3 = QVBoxLayout(self.signalViewer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.signalViewer)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addGeneratorFrame = QFrame(self.frame)
        self.addGeneratorFrame.setObjectName(u"addGeneratorFrame")
        self.addGeneratorFrame.setFrameShape(QFrame.StyledPanel)
        self.addGeneratorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.addGeneratorFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addGenerator = QPushButton(self.addGeneratorFrame)
        self.addGenerator.setObjectName(u"addGenerator")

        self.horizontalLayout.addWidget(self.addGenerator)

        self.generatorList = QComboBox(self.addGeneratorFrame)
        self.generatorList.setObjectName(u"generatorList")

        self.horizontalLayout.addWidget(self.generatorList)


        self.verticalLayout_2.addWidget(self.addGeneratorFrame)

        self.generatorsScrollArea = QScrollArea(self.frame)
        self.generatorsScrollArea.setObjectName(u"generatorsScrollArea")
        self.generatorsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.generatorsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 794, 318))
        self.generatorsScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.generatorsScrollArea)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.splitter.addWidget(self.frame)

        self.verticalLayout_4.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.root)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menuLoad)
        self.menu.addAction(self.menuSave)
        self.menu.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuLoad.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.menuSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.actionempty.setText(QCoreApplication.translate("MainWindow", u"empty", None))
        self.signalViewer.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.addGenerator.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435", None))
    # retranslateUi

