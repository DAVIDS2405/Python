from PySide6 import QtWidgets,QtCore
from PySide6.QtWidgets import QTableWidgetItem, QHBoxLayout, QFrame, QMessageBox, QLabel
from views.Admin_Window import Admin_Window
from database import Admin_mysql
from views import components
from controllers.edit_user import EditWindowForm



class MainWindowFrom(QtWidgets.QMainWindow, Admin_Window):
    #Iniciacion de la pantalla del Admin del sistema de reservas
    def __init__(self):
        super().__init__()
        self.Admin_ui = Admin_Window()
        self.Admin_ui.setupUi(self)
        
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowStaysOnTopHint)
        
        #Pasamos a cada boton que pagina corresponde cada uno
        self.Admin_ui.Home_pushButton.clicked.connect(lambda: self.Admin_ui.stackedWidget.setCurrentWidget(self.Admin_ui.page_home))
        self.Admin_ui.Ver_urs_pushButton.clicked.connect(lambda: self.Admin_ui.stackedWidget.setCurrentWidget(self.Admin_ui.page_Usu))
        self.Admin_ui.Crear_urs_pushButton.clicked.connect(lambda: self.Admin_ui.stackedWidget.setCurrentWidget(self.Admin_ui.page_Creu))
        self.Admin_ui.Reserva_act_pushButton.clicked.connect(lambda: self.Admin_ui.stackedWidget.setCurrentWidget(self.Admin_ui.Page_RA))
        self.Admin_ui.Reporte_men_pushButton.clicked.connect(lambda: self.Admin_ui.stackedWidget.setCurrentWidget(self.Admin_ui.page_RM))

        self.Admin_ui.pushButton_2.clicked.connect(self.add_Usuario)
        self.Admin_ui.pushButton_5.clicked.connect(self.clear_inputs)
        
        self.Admin_ui.pushButton_3.clicked.connect(self.search)
        self.Admin_ui.lineEdit_7.returnPressed.connect(self.search)
        self.Admin_ui.lineEdit_7.textChanged.connect(self.resotore_table_data)

        self.Admin_ui.Buscar_H.clicked.connect(self.buscarReserva)
        self.Admin_ui.Ingreso_Cedul_H.returnPressed.connect(self.buscarReserva)
        self.Admin_ui.Ingreso_Cedul_H.textChanged.connect(self.restore_reservas)

        self.Admin_ui.Buscar_R.clicked.connect(self.BuscarReporte)
        self.Admin_ui.Buscar_R_2.clicked.connect(self.ExportarReporte)
        
        self.config_tableU()
        self.set_table_data()




    def add_Usuario(self):
        nombre = self.Admin_ui.lineEdit.text()
        apellido = self.Admin_ui.lineEdit_6.text()
        cedula = self.Admin_ui.lineEdit_2.text()
        email = self.Admin_ui.lineEdit_3.text()
        diaingreso = self.Admin_ui.dateEdit.date()
        dia=diaingreso.toPython()
        contrasenia = self.Admin_ui.lineEdit_5.text()
       
        adminroll = 1
        data = (apellido, cedula, email, adminroll, nombre, contrasenia,dia)
        
        errors_count = 0

        if nombre == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Nombre obligatorio")
            msg_box.exec()
            errors_count += 1
        if apellido == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Apellido obligatorio")
            msg_box.exec()
            errors_count += 1
        if cedula == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Cedula obligatorio")
            msg_box.exec()
            errors_count += 1

        if email == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Email obligatorio")
            msg_box.exec()
            errors_count += 1
        if contrasenia == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Contrasenia obligatorio")

            msg_box.exec()
            errors_count += 1

        if errors_count == 0:
            Admin_mysql.insert_usuario(data)
            msg_box = QMessageBox()
            msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Usuario Añadido")
            msg_box.exec()
            self.set_table_data()
            return True
 
    
    def open_edit_window(self, cedula_id):
        window = EditWindowForm(self, cedula_id)
        window.show()

    def set_current_text(self,text):
        text_id = self.Admin_ui.lineEdit_7.findText()
        self.Admin_ui.lineEdit_7.setCurrenIndex(text_id)

    def edit_user(self):
        button = self.sender()
        table = self.Admin_ui.Ussuarios_M_V

        if button:
            cedula_id = self.get_recipie_id_from_table(table,button)
            self.open_edit_window(cedula_id)

    def clear_inputs(self):
        self.Admin_ui.lineEdit.clear()
        self.Admin_ui.lineEdit_6.clear()
        self.Admin_ui.lineEdit_2.clear()
        self.Admin_ui.lineEdit_3.clear()
        self.Admin_ui.lineEdit_5.clear()
        self.Admin_ui.dateEdit.clear()

    def config_tableU(self):
        colum_label = ("Cedula", "Nombre", "Apellido","Email", "Fecha de Ingreso", "")
        colum_label2 = ("Codigo Reserva", "Cedula del cliente","Fecha de ingreso", "Fecha de Salida", "Habitacion")
        colum_label3 = ("Codigo Reserva", "Cedula del cliente", "Fecha de ingreso", "Fecha de Salida", "Habitacion", "Total a pagar")
        self.Admin_ui.Ussuarios_M_V.setColumnCount(len(colum_label))
        self.Admin_ui.Ussuarios_M_V.setHorizontalHeaderLabels(colum_label)
        self.Admin_ui.Ussuarios_M_V.setColumnWidth(3, 170)
        self.Admin_ui.Ussuarios_M_V.verticalHeader().setDefaultSectionSize(50)

        self.Admin_ui.Tabla_ReservacionesA.setColumnCount(len(colum_label2))
        self.Admin_ui.Tabla_ReservacionesA.setHorizontalHeaderLabels(colum_label2)
        self.Admin_ui.Tabla_ReservacionesA.setColumnWidth(3, 170)
        self.Admin_ui.Tabla_ReservacionesA.setColumnWidth(4, 170)

        self.Admin_ui.Tabla_Reporte_Mensual.setColumnCount(len(colum_label3))
        self.Admin_ui.Tabla_Reporte_Mensual.setHorizontalHeaderLabels(colum_label3)
        self.Admin_ui.Tabla_Reporte_Mensual.setColumnWidth(3, 170)
        self.Admin_ui.Tabla_Reporte_Mensual.setColumnWidth(4, 170)

    
    def VerUsuariosU(self,data):
        self.Admin_ui.Ussuarios_M_V.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
           for(index_cell, cell) in enumerate(row):
               if (index_cell == -1):
                   self.Admin_ui.Ussuarios_M_V.setCellWidget(index_row, index_cell,None)
               else:
                   self.Admin_ui.Ussuarios_M_V.setItem(index_row,index_cell, QTableWidgetItem(str(cell)))
           self.Admin_ui.Ussuarios_M_V.setCellWidget(index_row, 5, self.buil_action_buttons())

    def set_table_data(self):
        data = Admin_mysql.VerUsuarios()
        data2 = Admin_mysql.ReporteM()
        data3 = Admin_mysql.VerReservas()
        self.VerUsuariosU(data)
        self.Tabla_Reporte_Mensual(data2)
        self.Tabla_Reservas_Ver(data3)

    def delete_User(self):
        button = self.sender()
        table = self.Admin_ui.Ussuarios_M_V

        if button:
            cedula_id = self.get_recipie_id_from_table(table,button)
            if Admin_mysql.delete(cedula_id):
                msg_box = QMessageBox()
                msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
                msg_box.setWindowTitle("JDE")
                msg_box.setText("Usuario Eliminado")
                msg_box.exec()
                self.set_table_data()

    def buscarReserva(self):
        param = self.Admin_ui.Ingreso_Cedul_H.text()
        if param != "":
            data = Admin_mysql.Buscar_Reserva(param)
            self.Tabla_Reservas_Ver(data)

    def restore_reservas(self):
        param = self.Admin_ui.Ingreso_Cedul_H.text()
        if param == "":
            self.set_table_data()

    def BuscarReporte(self):
        diaFin = self.Admin_ui.Fecha_Inicip.date()
        dia1 =  diaFin.toPython()
        mes = dia1.strftime('%m')
        param = (mes)
        data = Admin_mysql.BusquedaFechas(param)
        self.Tabla_Reporte_Mensual(data)
        
    def ExportarReporte(self):
        diaFin = self.Admin_ui.Fecha_Inicip.date()
        dia1 = diaFin.toPython()
        mes = dia1.strftime('%m')
        param = (mes)
        Admin_mysql.BusquedaFechas_Exportar(param)
        msg_box = QMessageBox()
        msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
        msg_box.setWindowTitle("JDE")
        msg_box.setText("Reporte realizado")
        msg_box.exec()

    def search(self):
        param = self.Admin_ui.lineEdit_7.text()
        if param !="":
            data = Admin_mysql.select_by_parameter(param)
            self.VerUsuariosU(data)

    def resotore_table_data(self):
        param = self.Admin_ui.lineEdit_7.text()
        if param =="":
            self.set_table_data()

    def buil_action_buttons(self):
        view_edit = components.Button("edit","#17A2B8")
        view_delete = components.Button("delete", "#17A2B8")

        buttons_layout = QHBoxLayout() 
        buttons_layout.addWidget(view_edit)
        buttons_layout.addWidget(view_delete)


        buttons_frame = QFrame() 
        buttons_frame.setLayout(buttons_layout)

        view_edit.clicked.connect(self.edit_user)
        view_delete.clicked.connect(self.delete_User)

        return buttons_frame

    def get_recipie_id_from_table(self,table,button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index,0)
        user_id = table.model().data(cell_id_index)
        return user_id
       
    def Tabla_Reservas_Ver(self,data):
        self.Admin_ui.Tabla_ReservacionesA.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
           for(index_cell, cell) in enumerate(row):
               if (index_cell == -1):
                   self.Admin_ui.Tabla_ReservacionesA.setCellWidget(index_row, index_cell,None)
               else:
                   self.Admin_ui.Tabla_ReservacionesA.setItem(index_row,index_cell, QTableWidgetItem(str(cell)))
           
    def Tabla_Reporte_Mensual(self,data):
        self.Admin_ui.Tabla_Reporte_Mensual.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
           for(index_cell, cell) in enumerate(row):
               if (index_cell == -1):
                   self.Admin_ui.Tabla_Reporte_Mensual.setCellWidget(index_row, index_cell,None)
               else:
                   self.Admin_ui.Tabla_Reporte_Mensual.setItem(index_row,index_cell, QTableWidgetItem(str(cell)))
    