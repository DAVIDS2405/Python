# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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

class Edit_Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Editar usuario")
        MainWindow.resize(436, 352)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 441, 101))
        self.logo.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 47, 13))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 140, 121, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 170, 47, 13))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(20, 190, 111, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 220, 47, 13))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 240, 301, 20))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 300, 75, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.logo_2 = QLabel(self.centralwidget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(160, 10, 121, 91))
        self.logo_2.setStyleSheet(u"background-color: rgb(0, 0, 0, 0);\n"
"border-image: url(:/imagen/Logo_Blanco.png);")
        self.logo_2.setPixmap(QPixmap(u":/iconos/Logo_Blanco.png"))
        self.logo_2.setScaledContents(True)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 300, 75, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Editar Usuario", None))
        self.logo.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el apellido", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresar el correo electronico", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.logo_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
    # retranslateUi

