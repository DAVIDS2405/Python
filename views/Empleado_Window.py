# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Empleado.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import assets.iconos.iconos_rc

class Empleado_Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 632)
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, -10, 821, 141))
        self.logo.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setGeometry(QRect(0, 130, 231, 501))
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
        self.Icono_Usuario.setPixmap(QPixmap(u":/iconos/reservacion-en-linea (1).png"))
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
        self.Ver_urs_pushButton.setFont(font)
        self.Ver_urs_pushButton.setIconSize(QSize(25, 20))
        self.Ver_urs_pushButton.setCheckable(False)

        self.verticalLayout.addWidget(self.Ver_urs_pushButton)

        self.Crear_urs_pushButton = QPushButton(self.Urs_menu_widget)
        self.Crear_urs_pushButton.setObjectName(u"Crear_urs_pushButton")
        self.Crear_urs_pushButton.setMinimumSize(QSize(10, 10))
        self.Crear_urs_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.Crear_urs_pushButton.setSizeIncrement(QSize(10, 10))
        self.Crear_urs_pushButton.setBaseSize(QSize(10, 10))
        self.Crear_urs_pushButton.setFont(font)
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
        self.Reportes_icono.setMinimumSize(QSize(25, 25))
        self.Reportes_icono.setMaximumSize(QSize(20, 20))
        self.Reportes_icono.setPixmap(QPixmap(u":/iconos/servicio-al-cliente.png"))
        self.Reportes_icono.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.Reportes_icono)

        self.Reportes_pushButton = QPushButton(self.Reportes)
        self.Reportes_pushButton.setObjectName(u"Reportes_pushButton")
        self.Reportes_pushButton.setFont(font)
        self.Reportes_pushButton.setLayoutDirection(Qt.RightToLeft)
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

        self.verticalLayout_3.addWidget(self.rp_menu_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 130, 591, 531))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"image: url(:/iconos/fondo_gris.png);")
        self.stackedWidget.addWidget(self.page_home)
        self.page_Usu = QWidget()
        self.page_Usu.setObjectName(u"page_Usu")
        self.Reservaciones = QLabel(self.page_Usu)
        self.Reservaciones.setObjectName(u"Reservaciones")
        self.Reservaciones.setGeometry(QRect(170, 20, 301, 41))
        self.Reservaciones.setMinimumSize(QSize(10, 10))
        self.Reservaciones.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.Busqueda_Reser = QLabel(self.page_Usu)
        self.Busqueda_Reser.setObjectName(u"Busqueda_Reser")
        self.Busqueda_Reser.setGeometry(QRect(250, 270, 101, 20))
        self.Cedula_R = QLineEdit(self.page_Usu)
        self.Cedula_R.setObjectName(u"Cedula_R")
        self.Cedula_R.setGeometry(QRect(230, 300, 141, 20))
        self.Buscar_R = QPushButton(self.page_Usu)
        self.Buscar_R.setObjectName(u"Buscar_R")
        self.Buscar_R.setGeometry(QRect(260, 330, 75, 23))
        self.Buscar_R.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.Tabla_Reservacion = QTableWidget(self.page_Usu)
        self.Tabla_Reservacion.setObjectName(u"Tabla_Reservacion")
        self.Tabla_Reservacion.setGeometry(QRect(10, 60, 571, 192))
        self.stackedWidget.addWidget(self.page_Usu)
        self.page_Creu = QWidget()
        self.page_Creu.setObjectName(u"page_Creu")
        self.Nueva_Reservacion = QLabel(self.page_Creu)
        self.Nueva_Reservacion.setObjectName(u"Nueva_Reservacion")
        self.Nueva_Reservacion.setGeometry(QRect(100, 20, 391, 41))
        self.Nueva_Reservacion.setMinimumSize(QSize(10, 10))
        self.Nueva_Reservacion.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.Nombre = QLabel(self.page_Creu)
        self.Nombre.setObjectName(u"Nombre")
        self.Nombre.setGeometry(QRect(10, 100, 47, 13))
        self.Apellido = QLabel(self.page_Creu)
        self.Apellido.setObjectName(u"Apellido")
        self.Apellido.setGeometry(QRect(330, 100, 47, 13))
        self.Cedula_R_2 = QLabel(self.page_Creu)
        self.Cedula_R_2.setObjectName(u"Cedula_R_2")
        self.Cedula_R_2.setGeometry(QRect(330, 150, 47, 13))
        self.Fech_inicio_R = QLabel(self.page_Creu)
        self.Fech_inicio_R.setObjectName(u"Fech_inicio_R")
        self.Fech_inicio_R.setGeometry(QRect(10, 230, 101, 20))
        self.Email = QLabel(self.page_Creu)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(10, 150, 47, 13))
        self.Habitaciones_Disponibles = QLabel(self.page_Creu)
        self.Habitaciones_Disponibles.setObjectName(u"Habitaciones_Disponibles")
        self.Habitaciones_Disponibles.setGeometry(QRect(330, 250, 131, 16))
        self.Pago = QLabel(self.page_Creu)
        self.Pago.setObjectName(u"Pago")
        self.Pago.setGeometry(QRect(160, 340, 71, 20))
        self.Fecha_Inicio_R = QDateEdit(self.page_Creu)
        self.Fecha_Inicio_R.setObjectName(u"Fecha_Inicio_R")
        self.Fecha_Inicio_R.setGeometry(QRect(10, 260, 110, 22))
        self.Fecha_Inicio_R.setCalendarPopup(True)
        self.Fecha_Inicio_R.setTimeSpec(Qt.LocalTime)
        self.Fecha_Inicio_R.setDate(QDate(2022, 1, 1))
        self.Ingreso_Nombre = QLineEdit(self.page_Creu)
        self.Ingreso_Nombre.setObjectName(u"Ingreso_Nombre")
        self.Ingreso_Nombre.setGeometry(QRect(10, 120, 231, 20))
        self.Ingreso_Cedula = QLineEdit(self.page_Creu)
        self.Ingreso_Cedula.setObjectName(u"Ingreso_Cedula")
        self.Ingreso_Cedula.setGeometry(QRect(330, 170, 201, 20))
        self.Ingreso_Email = QLineEdit(self.page_Creu)
        self.Ingreso_Email.setObjectName(u"Ingreso_Email")
        self.Ingreso_Email.setGeometry(QRect(10, 170, 231, 20))
        self.Total_Apagar_R = QLineEdit(self.page_Creu)
        self.Total_Apagar_R.setObjectName(u"Total_Apagar_R")
        self.Total_Apagar_R.setGeometry(QRect(270, 340, 121, 20))
        self.Ingreso_Apellido = QLineEdit(self.page_Creu)
        self.Ingreso_Apellido.setObjectName(u"Ingreso_Apellido")
        self.Ingreso_Apellido.setGeometry(QRect(330, 120, 201, 20))
        self.logo_3 = QLabel(self.page_Creu)
        self.logo_3.setObjectName(u"logo_3")
        self.logo_3.setGeometry(QRect(0, 60, 591, 31))
        self.logo_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Reservacion_Hasta = QLabel(self.page_Creu)
        self.Reservacion_Hasta.setObjectName(u"Reservacion_Hasta")
        self.Reservacion_Hasta.setGeometry(QRect(190, 230, 101, 20))
        self.Fecha_Fin_R = QDateEdit(self.page_Creu)
        self.Fecha_Fin_R.setObjectName(u"Fecha_Fin_R")
        self.Fecha_Fin_R.setGeometry(QRect(190, 260, 110, 22))
        self.Fecha_Fin_R.setCalendarPopup(True)
        self.Fecha_Fin_R.setTimeSpec(Qt.LocalTime)
        self.Fecha_Fin_R.setDate(QDate(2022, 1, 1))
        self.logo_4 = QLabel(self.page_Creu)
        self.logo_4.setObjectName(u"logo_4")
        self.logo_4.setGeometry(QRect(0, 300, 591, 31))
        self.logo_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Forma_Pago = QLabel(self.page_Creu)
        self.Forma_Pago.setObjectName(u"Forma_Pago")
        self.Forma_Pago.setGeometry(QRect(160, 430, 81, 20))
        self.Forma_Pago_2 = QComboBox(self.page_Creu)
        self.Forma_Pago_2.addItem("")
        self.Forma_Pago_2.addItem("")
        self.Forma_Pago_2.addItem("")
        self.Forma_Pago_2.addItem("")
        self.Forma_Pago_2.setObjectName(u"Forma_Pago_2")
        self.Forma_Pago_2.setGeometry(QRect(270, 430, 121, 22))
        self.label_22 = QLabel(self.page_Creu)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(190, 63, 191, 20))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Informacion_Pago = QLabel(self.page_Creu)
        self.Informacion_Pago.setObjectName(u"Informacion_Pago")
        self.Informacion_Pago.setGeometry(QRect(210, 303, 151, 20))
        self.Informacion_Pago.setFont(font)
        self.Informacion_Pago.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.habitacion_1 = QLineEdit(self.page_Creu)
        self.habitacion_1.setObjectName(u"habitacion_1")
        self.habitacion_1.setGeometry(QRect(330, 270, 113, 20))
        self.pushButton = QPushButton(self.page_Creu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 270, 75, 23))
        self.Cedula_R_3 = QLabel(self.page_Creu)
        self.Cedula_R_3.setObjectName(u"Cedula_R_3")
        self.Cedula_R_3.setGeometry(QRect(330, 200, 47, 13))
        self.lineEdit_2 = QLineEdit(self.page_Creu)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(330, 220, 201, 20))
        self.Total_Apagar_R_2 = QLineEdit(self.page_Creu)
        self.Total_Apagar_R_2.setObjectName(u"Total_Apagar_R_2")
        self.Total_Apagar_R_2.setGeometry(QRect(270, 400, 121, 20))
        self.Pago_2 = QLabel(self.page_Creu)
        self.Pago_2.setObjectName(u"Pago_2")
        self.Pago_2.setGeometry(QRect(160, 400, 71, 20))
        self.Total_Apagar_R_3 = QLineEdit(self.page_Creu)
        self.Total_Apagar_R_3.setObjectName(u"Total_Apagar_R_3")
        self.Total_Apagar_R_3.setGeometry(QRect(270, 370, 121, 20))
        self.Pago_3 = QLabel(self.page_Creu)
        self.Pago_3.setObjectName(u"Pago_3")
        self.Pago_3.setGeometry(QRect(160, 370, 81, 20))
        self.Guardar_R = QPushButton(self.page_Creu)
        self.Guardar_R.setObjectName(u"Guardar_R")
        self.Guardar_R.setGeometry(QRect(150, 470, 121, 23))
        self.Guardar_R.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.Cancelar_R = QPushButton(self.page_Creu)
        self.Cancelar_R.setObjectName(u"Cancelar_R")
        self.Cancelar_R.setGeometry(QRect(290, 470, 121, 23))
        self.Cancelar_R.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.pushButton_6 = QPushButton(self.page_Creu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(490, 470, 75, 23))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.stackedWidget.addWidget(self.page_Creu)
        self.Page_RA = QWidget()
        self.Page_RA.setObjectName(u"Page_RA")
        self.Servicios = QLabel(self.Page_RA)
        self.Servicios.setObjectName(u"Servicios")
        self.Servicios.setGeometry(QRect(80, 10, 441, 41))
        self.Servicios.setMinimumSize(QSize(10, 10))
        self.Servicios.setStyleSheet(u"font: 25 8pt \"Perpetua Titling MT\";")
        self.pushButton_4 = QPushButton(self.Page_RA)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(500, 470, 75, 23))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgba(28, 114, 147, 100);\n"
"selection-background-color: rgb(151, 226, 243);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(151, 226, 243);\n"
"}")
        self.Descripcion_Ser = QLineEdit(self.Page_RA)
        self.Descripcion_Ser.setObjectName(u"Descripcion_Ser")
        self.Descripcion_Ser.setGeometry(QRect(240, 130, 141, 20))
        self.Codigo_Servicio = QLabel(self.Page_RA)
        self.Codigo_Servicio.setObjectName(u"Codigo_Servicio")
        self.Codigo_Servicio.setGeometry(QRect(260, 60, 101, 16))
        self.logo_5 = QLabel(self.Page_RA)
        self.logo_5.setObjectName(u"logo_5")
        self.logo_5.setGeometry(QRect(0, 160, 591, 31))
        self.logo_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Descripcion = QLabel(self.Page_RA)
        self.Descripcion.setObjectName(u"Descripcion")
        self.Descripcion.setGeometry(QRect(280, 110, 61, 16))
        self.Cedula_Ser = QLabel(self.Page_RA)
        self.Cedula_Ser.setObjectName(u"Cedula_Ser")
        self.Cedula_Ser.setGeometry(QRect(90, 210, 81, 20))
        self.Fecha_Consumo = QLabel(self.Page_RA)
        self.Fecha_Consumo.setObjectName(u"Fecha_Consumo")
        self.Fecha_Consumo.setGeometry(QRect(90, 240, 101, 20))
        self.Total_consumido = QLabel(self.Page_RA)
        self.Total_consumido.setObjectName(u"Total_consumido")
        self.Total_consumido.setGeometry(QRect(90, 270, 81, 20))
        self.Ingreso_Cedula_Srv = QLineEdit(self.Page_RA)
        self.Ingreso_Cedula_Srv.setObjectName(u"Ingreso_Cedula_Srv")
        self.Ingreso_Cedula_Srv.setGeometry(QRect(190, 210, 151, 20))
        self.codigo_servicio = QLineEdit(self.Page_RA)
        self.codigo_servicio.setObjectName(u"codigo_servicio")
        self.codigo_servicio.setGeometry(QRect(240, 80, 141, 20))
        self.Valor_consumo = QLineEdit(self.Page_RA)
        self.Valor_consumo.setObjectName(u"Valor_consumo")
        self.Valor_consumo.setGeometry(QRect(190, 270, 151, 20))
        self.label_29 = QLabel(self.Page_RA)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(220, 164, 151, 20))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Dia_Consumo = QDateEdit(self.Page_RA)
        self.Dia_Consumo.setObjectName(u"Dia_Consumo")
        self.Dia_Consumo.setGeometry(QRect(190, 240, 110, 22))
        self.Dia_Consumo.setCalendarPopup(True)
        self.Dia_Consumo.setTimeSpec(Qt.LocalTime)
        self.Dia_Consumo.setDate(QDate(2022, 1, 1))
        self.stackedWidget.addWidget(self.Page_RA)
        self.logo_2 = QLabel(self.centralwidget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(340, 0, 161, 121))
        self.logo_2.setStyleSheet(u"background-color: rgb(0, 0, 0, 0);\n"
"border-image: url(:/imagen/Logo_Blanco.png);")
        self.logo_2.setPixmap(QPixmap(u":/iconos/Logo_Blanco.png"))
        self.logo_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Usuario_pushButton.toggled.connect(self.Urs_menu_widget.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.logo.setText("")
        self.Home_pushButton.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.Icono_Usuario.setText("")
        self.Usuario_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reservaciones", None))
        self.Ver_urs_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reservaciones", None))
        self.Crear_urs_pushButton.setText(QCoreApplication.translate("MainWindow", u"Nueva Reservaci\u00f3n", None))
        self.Reportes_icono.setText("")
        self.Reportes_pushButton.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.Reservaciones.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">RESERVACIONES\n"
"</span></p></body></html>", None))
        self.Busqueda_Reser.setText(QCoreApplication.translate("MainWindow", u"Buscar Reservaci\u00f3n", None))
        self.Cedula_R.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el cod de la reserva", None))
        self.Buscar_R.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Nueva_Reservacion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">NUEVA RESERVACI\u00d3N</span></p></body></html>", None))
        self.Nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.Apellido.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.Cedula_R_2.setText(QCoreApplication.translate("MainWindow", u"C.I:", None))
        self.Fech_inicio_R.setText(QCoreApplication.translate("MainWindow", u"Reservaci\u00f3n desde:", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Habitaciones_Disponibles.setText(QCoreApplication.translate("MainWindow", u"Habitaciones disponibles:", None))
        self.Pago.setText(QCoreApplication.translate("MainWindow", u"Total a pagar:", None))
        self.Ingreso_Nombre.setInputMask("")
        self.Ingreso_Nombre.setText("")
        self.Ingreso_Nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el nombre del cliente", None))
        self.Ingreso_Cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese la C.I del cliente", None))
        self.Ingreso_Email.setText("")
        self.Ingreso_Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresar el correo electronico del cliente", None))
        self.Total_Apagar_R.setText("")
        self.Total_Apagar_R.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: 102.2", None))
        self.Ingreso_Apellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el apellido", None))
        self.logo_3.setText("")
        self.Reservacion_Hasta.setText(QCoreApplication.translate("MainWindow", u"Reservaci\u00f3n hasta:", None))
        self.logo_4.setText("")
        self.Forma_Pago.setText(QCoreApplication.translate("MainWindow", u"Forma de pago:", None))
        self.Forma_Pago_2.setItemText(0, "")
        self.Forma_Pago_2.setItemText(1, QCoreApplication.translate("MainWindow", u"EF", None))
        self.Forma_Pago_2.setItemText(2, QCoreApplication.translate("MainWindow", u"DP", None))
        self.Forma_Pago_2.setItemText(3, QCoreApplication.translate("MainWindow", u"TF", None))

        self.Forma_Pago_2.setCurrentText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n de la Reserva", None))
        self.Informacion_Pago.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del Pago", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Cedula_R_3.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefono del huesped", None))
        self.Total_Apagar_R_2.setText("")
        self.Total_Apagar_R_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: 10", None))
        self.Pago_2.setText(QCoreApplication.translate("MainWindow", u"Descuento", None))
        self.Total_Apagar_R_3.setText("")
        self.Total_Apagar_R_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: P1", None))
        self.Pago_3.setText(QCoreApplication.translate("MainWindow", u"Codigo de pago:", None))
        self.Guardar_R.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.Cancelar_R.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.Servicios.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">SERVICIOS</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.Descripcion_Ser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese una descripcion", None))
        self.Codigo_Servicio.setText(QCoreApplication.translate("MainWindow", u"Codigo del servicio:", None))
        self.logo_5.setText("")
        self.Descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.Cedula_Ser.setText(QCoreApplication.translate("MainWindow", u"C.I del Huesped", None))
        self.Fecha_Consumo.setText(QCoreApplication.translate("MainWindow", u"Fecha del Consumo", None))
        self.Total_consumido.setText(QCoreApplication.translate("MainWindow", u"Total consumido", None))
        self.Ingreso_Cedula_Srv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el numero de cedula", None))
        self.codigo_servicio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: SR00001", None))
        self.Valor_consumo.setPlaceholderText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Datos del Consumo", None))
        self.logo_2.setText("")
    # retranslateUi

