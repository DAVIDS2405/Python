from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox
from views.login_main_window import Login_Window
from controllers.Admin_Window import MainWindowFrom
from controllers.Empleado_Window import EmpleadoWindow
from database import login_Msql


class LoginWindow(QtWidgets.QMainWindow, Login_Window):
    def __init__(self):
        super().__init__()
        self.Login_ui = Login_Window()
        self.Login_ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowStaysOnTopHint)

        self.Login_ui.pushButton.clicked.connect(lambda: self.login_Empleado(self.Login_ui.ingresar_usuario.text(), self.Login_ui.Ingresar_contrasenia.text(), EmpleadoWindow))
        self.Login_ui.pushButton.clicked.connect(lambda: self.Login_Admin(self.Login_ui.ingresar_usuario.text(), self.Login_ui.Ingresar_contrasenia.text(), MainWindowFrom))
        self.Login_ui.pushButton_2.clicked.connect(self.close)


    def login_Empleado(self, username, password,WindowToChange):
        if username and password:
            user = login_Msql.loginJDE_Empleado(username, password)
            if user: 
                
                self.hide()
                self.Login_ui = WindowToChange()
                self.Login_ui.show()
                msg_box1 = QMessageBox()
                msg_box1.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
                msg_box1.setWindowTitle("JDE")
                msg_box1.setText("Login Realizado")
                msg_box1.exec()
            
                


    def Login_Admin(self, username, password, WindowToChange):
        if username and password:
            user = login_Msql.loginJDE_Admin(username, password)
            if user:

                self.hide()
                self.Login_ui = WindowToChange()
                self.Login_ui.show()
                msg_box1 = QMessageBox()
                msg_box1.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
                msg_box1.setWindowTitle("JDE")
                msg_box1.setText("Login Realizado")
                msg_box1.exec()