# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)


import assets.iconos.iconos_rc


class Login_Window(object):
   
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Login")
        MainWindow.resize(472, 232)
        MainWindow.setStyleSheet(u"background-color: rgb(220, 217, 217);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.usuario = QLabel(self.centralwidget)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(60, 60, 61, 16))
        font = QFont()
        font.setPointSize(12)
        self.usuario.setFont(font)
        self.contrasenia = QLabel(self.centralwidget)
        self.contrasenia.setObjectName(u"contrasenia")
        self.contrasenia.setGeometry(QRect(40, 110, 91, 16))
        self.contrasenia.setFont(font)
        self.ingresar_usuario = QLineEdit(self.centralwidget)
        self.ingresar_usuario.setObjectName(u"ingresar_usuario")
        self.ingresar_usuario.setGeometry(QRect(140, 60, 181, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.ingresar_usuario.setFont(font1)
        self.ingresar_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Ingresar_contrasenia = QLineEdit(self.centralwidget)
        self.Ingresar_contrasenia.setObjectName(u"Ingresar_contrasenia")
        self.Ingresar_contrasenia.setGeometry(QRect(140, 110, 181, 20))
        self.Ingresar_contrasenia.setFont(font1)
        self.Ingresar_contrasenia.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Ingresar_contrasenia.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 160, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 160, 75, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(330, 40, 161, 141))
        self.logo.setStyleSheet(u"border-image: url(:/imagen/2.png);")
        self.logo.setPixmap(QPixmap(u":/iconos/2.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.contrasenia.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.ingresar_usuario.setText("")
        self.ingresar_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.Ingresar_contrasenia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.logo.setText("")
    # retranslateUi
