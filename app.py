import sys
from PySide6 import QtWidgets
from controllers.login import LoginWindow
from controllers.Admin_Window import MainWindowFrom
from controllers.Empleado_Window import EmpleadoWindow
from controllers.ver_habitaciones import Habitaciones_Window

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    #habitacion = Habitaciones_Window()
    #habitacion.show()
    #window = MainWindowFrom()
    windowLogin = LoginWindow()
    windowEmpleado = EmpleadoWindow()
    windowEmpleado.show()
    windowLogin.show()
    #window.show()
    sys.exit(app.exec())
