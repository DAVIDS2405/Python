# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import assets.iconos.iconos_rc

class Admin_Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(822, 562)
        MainWindow.setStyleSheet(u"#home QPushButton {\n"
"	padding-left: 15px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"#menu_widget QPushButton{\n"
"	text-align:left;\n"
"	border: None;\n"
"}\n"
"\n"
"#menu_widget QPushButtom:hover, #Usuarios:hover,#Reportes:hover,#home:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}\n"
"\n"
"#menu_widget QPushButtom:disable{\n"
"	background-color: rgb(222, 222, 222);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#Reportes QPushButtom{\n"
"	padding-left: 0px;\n"
"	padding-top:15px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"#Urs_menu_widget QPushButton,#rp_menu_widget QPushButton{\n"
"	padding-left: 40px;\n"
"	padding-top:5px;\n"
"	paddin-bottom:5px;\n"
"}\n"
"#Urs_menu_widget QPushButton:hover,#rp_menu_widget QPushButton:hover{\n"
"	background-color:rgb(151, 226, 243);\n"
"}\n"
"\n"
"#menu_widget{\n"
"	background-color: rgb(240, 239, 239);\n"
"	border: solid 1px rgb(0, 0, 0);	\n"
"}\n"
"\n"
"#stackedWidget {\n"
"	background-color:  rgb(221, 216, 217);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 821, 141))
        self.logo.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.logo_2 = QLabel(self.centralwidget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(320, 0, 161, 141))
        self.logo_2.setStyleSheet(u"background-color: rgb(0, 0, 0, 0);\n"
"border-image: url(:/imagen/Logo_Blanco.png);")
        self.logo_2.setPixmap(QPixmap(u":/iconos/Logo_Blanco.png"))
        self.logo_2.setScaledContents(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 140, 591, 421))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"border-image: url(:/iconos/fondo_gris.png);")
        self.stackedWidget.addWidget(self.page_home)
        self.page_Usu = QWidget()
        self.page_Usu.setObjectName(u"page_Usu")
        self.label_9 = QLabel(self.page_Usu)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 20, 301, 41))
        self.label_9.setMinimumSize(QSize(10, 10))
        self.label_9.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.label_15 = QLabel(self.page_Usu)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(260, 250, 71, 20))
        self.lineEdit_7 = QLineEdit(self.page_Usu)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(240, 270, 113, 20))
        self.pushButton_3 = QPushButton(self.page_Usu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(260, 300, 75, 23))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.Ussuarios_M_V = QTableWidget(self.page_Usu)
        self.Ussuarios_M_V.setObjectName(u"Ussuarios_M_V")
        self.Ussuarios_M_V.setGeometry(QRect(15, 60, 571, 181))
        self.stackedWidget.addWidget(self.page_Usu)
        self.page_Creu = QWidget()
        self.page_Creu.setObjectName(u"page_Creu")
        self.pushButton_2 = QPushButton(self.page_Creu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 380, 121, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.label = QLabel(self.page_Creu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 301, 41))
        self.label.setMinimumSize(QSize(10, 10))
        self.label.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.label_2 = QLabel(self.page_Creu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 100, 47, 13))
        self.label_3 = QLabel(self.page_Creu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 100, 47, 13))
        self.label_4 = QLabel(self.page_Creu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 160, 47, 13))
        self.label_5 = QLabel(self.page_Creu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 160, 91, 20))
        self.pushButton_5 = QPushButton(self.page_Creu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(300, 380, 121, 23))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.label_6 = QLabel(self.page_Creu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 210, 47, 13))
        self.label_8 = QLabel(self.page_Creu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 260, 61, 16))
        self.dateEdit = QDateEdit(self.page_Creu)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(310, 180, 110, 22))
        self.dateEdit.setTime(QTime(5, 0, 0))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(Qt.UTC)
        self.dateEdit.setDate(QDate(2022, 1, 1))
        self.lineEdit = QLineEdit(self.page_Creu)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 120, 121, 20))
        self.lineEdit_2 = QLineEdit(self.page_Creu)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 180, 121, 20))
        self.lineEdit_3 = QLineEdit(self.page_Creu)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 230, 301, 20))
        self.lineEdit_5 = QLineEdit(self.page_Creu)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(120, 280, 121, 20))
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.lineEdit_6 = QLineEdit(self.page_Creu)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(310, 120, 111, 20))
        self.stackedWidget.addWidget(self.page_Creu)
        self.Page_RA = QWidget()
        self.Page_RA.setObjectName(u"Page_RA")
        self.Resercaciones_Activas = QLabel(self.Page_RA)
        self.Resercaciones_Activas.setObjectName(u"Resercaciones_Activas")
        self.Resercaciones_Activas.setGeometry(QRect(80, 10, 441, 41))
        self.Resercaciones_Activas.setMinimumSize(QSize(10, 10))
        self.Resercaciones_Activas.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.habitacion = QLabel(self.Page_RA)
        self.habitacion.setObjectName(u"habitacion")
        self.habitacion.setGeometry(QRect(270, 260, 41, 16))
        self.Buscar_H = QPushButton(self.Page_RA)
        self.Buscar_H.setObjectName(u"Buscar_H")
        self.Buscar_H.setGeometry(QRect(250, 310, 75, 23))
        self.Buscar_H.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.Ingreso_Cedul_H = QLineEdit(self.Page_RA)
        self.Ingreso_Cedul_H.setObjectName(u"Ingreso_Cedul_H")
        self.Ingreso_Cedul_H.setGeometry(QRect(210, 280, 161, 20))
        self.Tabla_ReservacionesA = QTableWidget(self.Page_RA)
        self.Tabla_ReservacionesA.setObjectName(u"Tabla_ReservacionesA")
        self.Tabla_ReservacionesA.setGeometry(QRect(10, 50, 571, 192))
        self.stackedWidget.addWidget(self.Page_RA)
        self.page_RM = QWidget()
        self.page_RM.setObjectName(u"page_RM")
        self.Reporte_Mensual = QLabel(self.page_RM)
        self.Reporte_Mensual.setObjectName(u"Reporte_Mensual")
        self.Reporte_Mensual.setGeometry(QRect(90, 20, 441, 41))
        self.Reporte_Mensual.setMinimumSize(QSize(10, 10))
        self.Reporte_Mensual.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.Desde = QLabel(self.page_RM)
        self.Desde.setObjectName(u"Desde")
        self.Desde.setGeometry(QRect(260, 80, 71, 20))
        self.Fecha_Inicip = QDateEdit(self.page_RM)
        self.Fecha_Inicip.setObjectName(u"Fecha_Inicip")
        self.Fecha_Inicip.setGeometry(QRect(240, 110, 101, 22))
        self.Fecha_Inicip.setCurrentSection(QDateTimeEdit.DaySection)
        self.Fecha_Inicip.setDisplayFormat(u"dd/MM/yyyy")
        self.Fecha_Inicip.setCalendarPopup(True)
        self.Fecha_Inicip.setDate(QDate(2022, 1, 1))
        self.Buscar_R = QPushButton(self.page_RM)
        self.Buscar_R.setObjectName(u"Buscar_R")
        self.Buscar_R.setGeometry(QRect(260, 160, 61, 23))
        self.Buscar_R.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.Tabla_Reporte_Mensual = QTableWidget(self.page_RM)
        self.Tabla_Reporte_Mensual.setObjectName(u"Tabla_Reporte_Mensual")
        self.Tabla_Reporte_Mensual.setGeometry(QRect(20, 200, 561, 192))
        self.Buscar_R_2 = QPushButton(self.page_RM)
        self.Buscar_R_2.setObjectName(u"Buscar_R_2")
        self.Buscar_R_2.setGeometry(QRect(510, 170, 75, 23))
        self.Buscar_R_2.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.stackedWidget.addWidget(self.page_RM)
        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setGeometry(QRect(0, 140, 231, 421))
        self.verticalLayout_3 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.home = QWidget(self.menu_widget)
        self.home.setObjectName(u"home")
        self.horizontalLayout_2 = QHBoxLayout(self.home)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Home_pushButton = QPushButton(self.home)
        self.Home_pushButton.setObjectName(u"Home_pushButton")
        font = QFont()
        font.setPointSize(12)
        self.Home_pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/iconos/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_pushButton.setIcon(icon)
        self.Home_pushButton.setIconSize(QSize(20, 20))
        self.Home_pushButton.setCheckable(False)
        self.Home_pushButton.setChecked(False)
        self.Home_pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.Home_pushButton)


        self.verticalLayout_3.addWidget(self.home)

        self.Usuarios = QWidget(self.menu_widget)
        self.Usuarios.setObjectName(u"Usuarios")
        self.horizontalLayout_6 = QHBoxLayout(self.Usuarios)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 5, 15, 5)
        self.Icono_Usuario = QLabel(self.Usuarios)
        self.Icono_Usuario.setObjectName(u"Icono_Usuario")
        self.Icono_Usuario.setMinimumSize(QSize(20, 20))
        self.Icono_Usuario.setMaximumSize(QSize(20, 20))
        self.Icono_Usuario.setPixmap(QPixmap(u":/iconos/user.svg"))
        self.Icono_Usuario.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Icono_Usuario)

        self.Usuario_pushButton = QPushButton(self.Usuarios)
        self.Usuario_pushButton.setObjectName(u"Usuario_pushButton")
        self.Usuario_pushButton.setFont(font)
        self.Usuario_pushButton.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/iconos/arrow-29-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/iconos/arrow-208-32.ico", QSize(), QIcon.Normal, QIcon.On)
        self.Usuario_pushButton.setIcon(icon1)
        self.Usuario_pushButton.setCheckable(True)
        self.Usuario_pushButton.setFlat(True)

        self.horizontalLayout_6.addWidget(self.Usuario_pushButton)


        self.verticalLayout_3.addWidget(self.Usuarios)

        self.Urs_menu_widget = QWidget(self.menu_widget)
        self.Urs_menu_widget.setObjectName(u"Urs_menu_widget")
        self.verticalLayout = QVBoxLayout(self.Urs_menu_widget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Ver_urs_pushButton = QPushButton(self.Urs_menu_widget)
        self.Ver_urs_pushButton.setObjectName(u"Ver_urs_pushButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.Ver_urs_pushButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/iconos/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ver_urs_pushButton.setIcon(icon2)
        self.Ver_urs_pushButton.setIconSize(QSize(25, 20))
        self.Ver_urs_pushButton.setCheckable(False)

        self.verticalLayout.addWidget(self.Ver_urs_pushButton)

        self.Crear_urs_pushButton = QPushButton(self.Urs_menu_widget)
        self.Crear_urs_pushButton.setObjectName(u"Crear_urs_pushButton")
        self.Crear_urs_pushButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/iconos/agregar-usuario (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Crear_urs_pushButton.setIcon(icon3)
        self.Crear_urs_pushButton.setIconSize(QSize(25, 25))
        self.Crear_urs_pushButton.setCheckable(False)

        self.verticalLayout.addWidget(self.Crear_urs_pushButton)


        self.verticalLayout_3.addWidget(self.Urs_menu_widget)

        self.Reportes = QWidget(self.menu_widget)
        self.Reportes.setObjectName(u"Reportes")
        self.horizontalLayout_4 = QHBoxLayout(self.Reportes)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 5, 15, 5)
        self.Reportes_icono = QLabel(self.Reportes)
        self.Reportes_icono.setObjectName(u"Reportes_icono")
        self.Reportes_icono.setMinimumSize(QSize(20, 20))
        self.Reportes_icono.setMaximumSize(QSize(20, 20))
        self.Reportes_icono.setPixmap(QPixmap(u":/iconos/bar-chart.svg"))
        self.Reportes_icono.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Reportes_icono)

        self.Reportes_pushButton = QPushButton(self.Reportes)
        self.Reportes_pushButton.setObjectName(u"Reportes_pushButton")
        self.Reportes_pushButton.setFont(font)
        self.Reportes_pushButton.setLayoutDirection(Qt.RightToLeft)
        self.Reportes_pushButton.setIcon(icon1)
        self.Reportes_pushButton.setCheckable(True)
        self.Reportes_pushButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.Reportes_pushButton)


        self.verticalLayout_3.addWidget(self.Reportes)

        self.rp_menu_widget = QWidget(self.menu_widget)
        self.rp_menu_widget.setObjectName(u"rp_menu_widget")
        self.verticalLayout_2 = QVBoxLayout(self.rp_menu_widget)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Reserva_act_pushButton = QPushButton(self.rp_menu_widget)
        self.Reserva_act_pushButton.setObjectName(u"Reserva_act_pushButton")
        self.Reserva_act_pushButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"../iconos/reservacion-en-linea.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reserva_act_pushButton.setIcon(icon4)
        self.Reserva_act_pushButton.setIconSize(QSize(30, 30))
        self.Reserva_act_pushButton.setCheckable(False)

        self.verticalLayout_2.addWidget(self.Reserva_act_pushButton)

        self.Reporte_men_pushButton = QPushButton(self.rp_menu_widget)
        self.Reporte_men_pushButton.setObjectName(u"Reporte_men_pushButton")
        self.Reporte_men_pushButton.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"../iconos/analitica.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reporte_men_pushButton.setIcon(icon5)
        self.Reporte_men_pushButton.setIconSize(QSize(25, 25))
        self.Reporte_men_pushButton.setCheckable(False)

        self.verticalLayout_2.addWidget(self.Reporte_men_pushButton)


        self.verticalLayout_3.addWidget(self.rp_menu_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Reportes_pushButton.toggled.connect(self.rp_menu_widget.setVisible)
        self.Usuario_pushButton.toggled.connect(self.Urs_menu_widget.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.logo_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">USUARIOS\n"
"</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Buscar usuario", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese la C.I", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">CREAR USUARIO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C.I:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fecha de ingreso", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el nombre", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese la C.I", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresar el correo electronico", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese contrase\u00f1a", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el apellido", None))
        self.Resercaciones_Activas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">RESERVACIONES ACTIVAS</span></p></body></html>", None))
        self.habitacion.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.Buscar_H.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Ingreso_Cedul_H.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el codigo de la reserva", None))
        self.Reporte_Mensual.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">REPORTE MENSUAL</span></p></body></html>", None))
        self.Desde.setText(QCoreApplication.translate("MainWindow", u"Mes a buscar", None))
        self.Buscar_R.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Buscar_R_2.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.Home_pushButton.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.Icono_Usuario.setText("")
        self.Usuario_pushButton.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.Ver_urs_pushButton.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.Crear_urs_pushButton.setText(QCoreApplication.translate("MainWindow", u"Crear Usuarios", None))
        self.Reportes_icono.setText("")
        self.Reportes_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.Reserva_act_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reservaciones Activas", None))
        self.Reporte_men_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reportes Mensuales", None))
    # retranslateUi

