# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(800, 600)
        w_MainWindow.setStyleSheet(u"background-color: rgb(26, 26, 29);")
        self.actionHistory = QAction(w_MainWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.centralwidget = QWidget(w_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(59, 28, 50); border-radius: 20px;")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 2, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 2, 1)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_new_game = QPushButton(self.frame)
        self.pb_new_game.setObjectName(u"pb_new_game")
        font1 = QFont()
        font1.setPointSize(16)
        self.pb_new_game.setFont(font1)
        self.pb_new_game.setStyleSheet(u"background-color: rgb(106, 30, 85);")

        self.gridLayout_3.addWidget(self.pb_new_game, 9, 1, 1, 1)

        self.le_user_guess = QLineEdit(self.frame)
        self.le_user_guess.setObjectName(u"le_user_guess")
        font2 = QFont()
        font2.setPointSize(23)
        self.le_user_guess.setFont(font2)
        self.le_user_guess.setStyleSheet(u"background-color: rgb(94, 92, 100); color: #a9a9a9; border-color: rgb(166, 77, 121);")
        self.le_user_guess.setMaxLength(2)
        self.le_user_guess.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.le_user_guess, 5, 0, 1, 2)

        self.lb_tries_remaining = QLabel(self.frame)
        self.lb_tries_remaining.setObjectName(u"lb_tries_remaining")

        self.gridLayout_3.addWidget(self.lb_tries_remaining, 7, 0, 1, 1)

        self.pb_guess = QPushButton(self.frame)
        self.pb_guess.setObjectName(u"pb_guess")
        self.pb_guess.setFont(font1)
        self.pb_guess.setStyleSheet(u"background-color: rgb(106, 30, 85);")

        self.gridLayout_3.addWidget(self.pb_guess, 9, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: #a9a9a9;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setUnderline(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: #a9a9a9;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 8, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 4, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        w_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        w_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        w_MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionHistory)
        self.menuMenu.addSeparator()

        self.retranslateUi(w_MainWindow)

        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Number Guess", None))
        self.actionHistory.setText(QCoreApplication.translate("w_MainWindow", u"History", None))
        self.groupBox.setTitle("")
        self.pb_new_game.setText(QCoreApplication.translate("w_MainWindow", u"New Game", None))
        self.le_user_guess.setPlaceholderText(QCoreApplication.translate("w_MainWindow", u"Enter Guess Here...", None))
        self.lb_tries_remaining.setText(QCoreApplication.translate("w_MainWindow", u"Tries: 0", None))
        self.pb_guess.setText(QCoreApplication.translate("w_MainWindow", u"Guess", None))
        self.label.setText(QCoreApplication.translate("w_MainWindow", u"Guess A Number Between 1 and 20", None))
        self.label_2.setText(QCoreApplication.translate("w_MainWindow", u"Number Guess", None))
        self.menuMenu.setTitle(QCoreApplication.translate("w_MainWindow", u"Menu", None))
    # retranslateUi

