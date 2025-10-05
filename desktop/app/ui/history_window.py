# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_w_HistoryWindow(object):
    def setupUi(self, w_HistoryWindow):
        if not w_HistoryWindow.objectName():
            w_HistoryWindow.setObjectName(u"w_HistoryWindow")
        w_HistoryWindow.resize(800, 600)
        w_HistoryWindow.setStyleSheet(u"background-color: rgb(26, 26, 29);")
        self.centralwidget = QWidget(w_HistoryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"background-color: rgb(59, 28, 50); border: none;")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_back = QPushButton(self.groupBox)
        self.pb_back.setObjectName(u"pb_back")
        font = QFont()
        font.setPointSize(18)
        self.pb_back.setFont(font)
        self.pb_back.setStyleSheet(u"background-color: rgb(106, 30, 85);\n"
"border: 2px solid rgb(166, 77, 121);\n"
"padding: 5 40;")

        self.gridLayout_2.addWidget(self.pb_back, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.scra_history = QScrollArea(self.groupBox)
        self.scra_history.setObjectName(u"scra_history")
        self.scra_history.setStyleSheet(u"border: 2px solid rgb(166, 77, 121);")
        self.scra_history.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 760, 511))
        self.scra_history.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scra_history, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        w_HistoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(w_HistoryWindow)

        QMetaObject.connectSlotsByName(w_HistoryWindow)
    # setupUi

    def retranslateUi(self, w_HistoryWindow):
        w_HistoryWindow.setWindowTitle(QCoreApplication.translate("w_HistoryWindow", u"Number Guess - History", None))
        self.groupBox.setTitle("")
        self.pb_back.setText(QCoreApplication.translate("w_HistoryWindow", u"back", None))
    # retranslateUi

