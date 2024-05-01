# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(982, 878)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEditVideoIn = QLineEdit(self.groupBox_6)
        self.lineEditVideoIn.setObjectName(u"lineEditVideoIn")

        self.horizontalLayout_3.addWidget(self.lineEditVideoIn)

        self.toolButtonOpenFile = QToolButton(self.groupBox_6)
        self.toolButtonOpenFile.setObjectName(u"toolButtonOpenFile")

        self.horizontalLayout_3.addWidget(self.toolButtonOpenFile)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listViewVideosIn = QListView(self.groupBox_5)
        self.listViewVideosIn.setObjectName(u"listViewVideosIn")

        self.verticalLayout_7.addWidget(self.listViewVideosIn)

        self.pushButtonDeleteVideoIn = QPushButton(self.groupBox_5)
        self.pushButtonDeleteVideoIn.setObjectName(u"pushButtonDeleteVideoIn")

        self.verticalLayout_7.addWidget(self.pushButtonDeleteVideoIn)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widgetPreview = QWidget(self.groupBox_4)
        self.widgetPreview.setObjectName(u"widgetPreview")
        self.widgetPreview.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px")

        self.verticalLayout_2.addWidget(self.widgetPreview)

        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 200))
        self.groupBox.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_12 = QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.checkBoxEnableEdit = QCheckBox(self.groupBox)
        self.checkBoxEnableEdit.setObjectName(u"checkBoxEnableEdit")
        self.checkBoxEnableEdit.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_11.addWidget(self.checkBoxEnableEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 0))
        self.label_2.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_11.addWidget(self.label_2)

        self.spinBoxMinAudio = QSpinBox(self.groupBox)
        self.spinBoxMinAudio.setObjectName(u"spinBoxMinAudio")
        self.spinBoxMinAudio.setMaximumSize(QSize(100, 16777215))
        self.spinBoxMinAudio.setMaximum(100)

        self.verticalLayout_11.addWidget(self.spinBoxMinAudio)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_11.addWidget(self.label_3)

        self.spinBoxMinMotion = QSpinBox(self.groupBox)
        self.spinBoxMinMotion.setObjectName(u"spinBoxMinMotion")
        self.spinBoxMinMotion.setMaximumSize(QSize(100, 16777215))
        self.spinBoxMinMotion.setMaximum(100)

        self.verticalLayout_11.addWidget(self.spinBoxMinMotion)


        self.horizontalLayout_6.addLayout(self.verticalLayout_11)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEditStartentSegment = QLineEdit(self.groupBox_7)
        self.lineEditStartentSegment.setObjectName(u"lineEditStartentSegment")

        self.horizontalLayout_4.addWidget(self.lineEditStartentSegment)

        self.toolButtonStartSegment = QToolButton(self.groupBox_7)
        self.toolButtonStartSegment.setObjectName(u"toolButtonStartSegment")

        self.horizontalLayout_4.addWidget(self.toolButtonStartSegment)

        self.toolButtonEndSegment = QToolButton(self.groupBox_7)
        self.toolButtonEndSegment.setObjectName(u"toolButtonEndSegment")

        self.horizontalLayout_4.addWidget(self.toolButtonEndSegment)

        self.toolButtonaddSegment = QToolButton(self.groupBox_7)
        self.toolButtonaddSegment.setObjectName(u"toolButtonaddSegment")

        self.horizontalLayout_4.addWidget(self.toolButtonaddSegment)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.listViewSegments = QListView(self.groupBox_7)
        self.listViewSegments.setObjectName(u"listViewSegments")

        self.verticalLayout_8.addWidget(self.listViewSegments)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout_6.addWidget(self.groupBox_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBoxEnableVideoConv = QCheckBox(self.groupBox_2)
        self.checkBoxEnableVideoConv.setObjectName(u"checkBoxEnableVideoConv")

        self.horizontalLayout_7.addWidget(self.checkBoxEnableVideoConv)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)

        self.lineEditVideoCodec = QLineEdit(self.groupBox_2)
        self.lineEditVideoCodec.setObjectName(u"lineEditVideoCodec")

        self.verticalLayout_13.addWidget(self.lineEditVideoCodec)


        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_14.addWidget(self.label_6)

        self.spinBoxVideoCrf = QSpinBox(self.groupBox_2)
        self.spinBoxVideoCrf.setObjectName(u"spinBoxVideoCrf")
        self.spinBoxVideoCrf.setMinimumSize(QSize(100, 0))
        self.spinBoxVideoCrf.setMinimum(0)
        self.spinBoxVideoCrf.setMaximum(50)
        self.spinBoxVideoCrf.setValue(22)

        self.verticalLayout_14.addWidget(self.spinBoxVideoCrf)


        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_15.addWidget(self.label_7)

        self.spinBoxVideoFps = QSpinBox(self.groupBox_2)
        self.spinBoxVideoFps.setObjectName(u"spinBoxVideoFps")
        self.spinBoxVideoFps.setMinimumSize(QSize(100, 0))
        self.spinBoxVideoFps.setMinimum(0)
        self.spinBoxVideoFps.setValue(15)

        self.verticalLayout_15.addWidget(self.spinBoxVideoFps)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.checkBoxEnableAudioConv = QCheckBox(self.groupBox_3)
        self.checkBoxEnableAudioConv.setObjectName(u"checkBoxEnableAudioConv")

        self.horizontalLayout_8.addWidget(self.checkBoxEnableAudioConv)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_16.addWidget(self.label_8)

        self.lineEditAudioCodec = QLineEdit(self.groupBox_3)
        self.lineEditAudioCodec.setObjectName(u"lineEditAudioCodec")

        self.verticalLayout_16.addWidget(self.lineEditAudioCodec)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_17.addWidget(self.label_9)

        self.spinBoxAudioBitrate = QSpinBox(self.groupBox_3)
        self.spinBoxAudioBitrate.setObjectName(u"spinBoxAudioBitrate")
        self.spinBoxAudioBitrate.setMinimumSize(QSize(100, 0))
        self.spinBoxAudioBitrate.setMaximum(320)
        self.spinBoxAudioBitrate.setValue(128)

        self.verticalLayout_17.addWidget(self.spinBoxAudioBitrate)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_2.addWidget(self.groupBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 100))
        self.groupBox_8.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.plainTextEditCmds = QPlainTextEdit(self.groupBox_8)
        self.plainTextEditCmds.setObjectName(u"plainTextEditCmds")
        self.plainTextEditCmds.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.plainTextEditCmds)

        self.pushButtonProcess = QPushButton(self.groupBox_8)
        self.pushButtonProcess.setObjectName(u"pushButtonProcess")
        self.pushButtonProcess.setMinimumSize(QSize(0, 50))
        self.pushButtonProcess.setStyleSheet(u"padding: 10px")

        self.horizontalLayout_5.addWidget(self.pushButtonProcess)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_8)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 982, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEditVideoIn, self.toolButtonOpenFile)
        QWidget.setTabOrder(self.toolButtonOpenFile, self.listViewVideosIn)
        QWidget.setTabOrder(self.listViewVideosIn, self.pushButtonDeleteVideoIn)
        QWidget.setTabOrder(self.pushButtonDeleteVideoIn, self.checkBoxEnableEdit)
        QWidget.setTabOrder(self.checkBoxEnableEdit, self.spinBoxMinAudio)
        QWidget.setTabOrder(self.spinBoxMinAudio, self.spinBoxMinMotion)
        QWidget.setTabOrder(self.spinBoxMinMotion, self.lineEditStartentSegment)
        QWidget.setTabOrder(self.lineEditStartentSegment, self.toolButtonStartSegment)
        QWidget.setTabOrder(self.toolButtonStartSegment, self.toolButtonEndSegment)
        QWidget.setTabOrder(self.toolButtonEndSegment, self.toolButtonaddSegment)
        QWidget.setTabOrder(self.toolButtonaddSegment, self.listViewSegments)
        QWidget.setTabOrder(self.listViewSegments, self.checkBoxEnableVideoConv)
        QWidget.setTabOrder(self.checkBoxEnableVideoConv, self.lineEditVideoCodec)
        QWidget.setTabOrder(self.lineEditVideoCodec, self.spinBoxVideoCrf)
        QWidget.setTabOrder(self.spinBoxVideoCrf, self.spinBoxVideoFps)
        QWidget.setTabOrder(self.spinBoxVideoFps, self.checkBoxEnableAudioConv)
        QWidget.setTabOrder(self.checkBoxEnableAudioConv, self.lineEditAudioCodec)
        QWidget.setTabOrder(self.lineEditAudioCodec, self.spinBoxAudioBitrate)
        QWidget.setTabOrder(self.spinBoxAudioBitrate, self.plainTextEditCmds)
        QWidget.setTabOrder(self.plainTextEditCmds, self.pushButtonProcess)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MCB V\u00eddeo Auto Editor", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo de origem", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecione em arquivo", None))
        self.toolButtonOpenFile.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Arquivos de origem", None))
        self.pushButtonDeleteVideoIn.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Pr\u00e9-visualiza\u00e7\u00e3o do v\u00eddeo", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o autom\u00e1tica", None))
        self.checkBoxEnableEdit.setText(QCoreApplication.translate("MainWindow", u"Habilitar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u00edn. \u00e1udio (%):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u00edn. Movimento (%):", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Momentos exclusos", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio,Fim:", None))
        self.lineEditStartentSegment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1sec,10sec 20sec,30sec", None))
        self.toolButtonStartSegment.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.toolButtonEndSegment.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.toolButtonaddSegment.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
        self.checkBoxEnableVideoConv.setText(QCoreApplication.translate("MainWindow", u"Converte", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Codec:", None))
        self.lineEditVideoCodec.setText(QCoreApplication.translate("MainWindow", u"libx264", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CRF:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u00c1udio", None))
        self.checkBoxEnableAudioConv.setText(QCoreApplication.translate("MainWindow", u"Converte", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Codec:", None))
        self.lineEditAudioCodec.setText(QCoreApplication.translate("MainWindow", u"aac", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bitrate (k):", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Comandos finais", None))
        self.pushButtonProcess.setText(QCoreApplication.translate("MainWindow", u"Processar V\u00eddeo!", None))
    # retranslateUi

