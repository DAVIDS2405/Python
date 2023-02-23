from PySide6.QtCore import Qt
from views.general_custom_ui import GeneralCustom
from PySide6 import QtWidgets
from views.Edit_Window import Edit_Window
from database import Admin_mysql


class EditWindowForm(QtWidgets.QMainWindow, Edit_Window):
    def __init__(self, parent=None,cedula_id=None,):
        self.cedula_id = cedula_id
        self.parent = parent

        super().__init__(parent)
        
        self.setupUi(self)
        self.ui = GeneralCustom(self)
        self.setWindowFlag(Qt.Window)

        self.fill_inputd()  
        self.pushButton_3.clicked.connect(self.update_user)

    def mousePressEvent(self,event):
        self.ui.mouse_press_event(event)

    def update_user(self):
        nombre = self.lineEdit.text()
        apellido = self.lineEdit_6.text()
        email = self.lineEdit_3.text()
        adminroll = 1
        data = (apellido, email, nombre)

        if Admin_mysql.update(self.cedula_id, data):
            print("Usuario Modificado")
            self.parent.set_table_data()
            self.close()

    def fill_inputd(self):
        data = Admin_mysql.Select_id(self.cedula_id)

        self.lineEdit.setText(data[3])
        self.lineEdit_6.setText(data[4])
        self.lineEdit_3.setText(data[5])

