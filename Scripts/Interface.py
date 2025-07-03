# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1073, 606)
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionA_Propos = QAction(MainWindow)
        self.actionA_Propos.setObjectName(u"actionA_Propos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 29, 491, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.qrcode_image = QLabel(self.verticalLayoutWidget)
        self.qrcode_image.setObjectName(u"qrcode_image")
        self.qrcode_image.setStyleSheet(u"border-color: rgb(192, 28, 40);")
        self.qrcode_image.setFrameShape(QFrame.Shape.Box)
        self.qrcode_image.setFrameShadow(QFrame.Shadow.Sunken)
        self.qrcode_image.setLineWidth(5)
        self.qrcode_image.setMidLineWidth(0)
        self.qrcode_image.setScaledContents(False)
        self.qrcode_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.qrcode_image)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 10, 91, 17))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.information = QTextEdit(self.frame_2)
        self.information.setObjectName(u"information")
        self.information.setGeometry(QRect(10, 10, 501, 321))
        self.information.setFrameShape(QFrame.Shape.StyledPanel)
        self.information.setFrameShadow(QFrame.Shadow.Sunken)
        self.information.setLineWidth(1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 340, 51, 21))
        self.change_size = QComboBox(self.frame_2)
        self.change_size.setObjectName(u"change_size")
        self.change_size.setGeometry(QRect(70, 340, 141, 25))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 370, 141, 17))
        self.path = QLineEdit(self.frame_2)
        self.path.setObjectName(u"path")
        self.path.setEnabled(False)
        self.path.setGeometry(QRect(10, 400, 401, 25))
        self.path_button = QPushButton(self.frame_2)
        self.path_button.setObjectName(u"path_button")
        self.path_button.setGeometry(QRect(420, 400, 89, 25))
        self.save = QPushButton(self.frame_2)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(140, 470, 181, 41))
        self.save.setStyleSheet(u"")

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1073, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuFichier.addAction(self.actionQuitter)
        self.menuhelp.addAction(self.actionA_Propos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rateur Qrcode", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionA_Propos.setText(QCoreApplication.translate("MainWindow", u"A Propos", None))
        self.qrcode_image.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">280X290</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Taille : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enregistrer dans :", None))
        self.path_button.setText(QCoreApplication.translate("MainWindow", u"Parcourir", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help!", None))
    # retranslateUi

