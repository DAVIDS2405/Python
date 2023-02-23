from PySide6.QtWidgets import *
from PySide6 import QtWidgets,QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QLineEdit, QMessageBox
from views.Empleado_Window import Empleado_Window
from controllers.ver_habitaciones import Habitaciones_Window
from database import Empleados_Msql
from database import Servicios_Msql



class EmpleadoWindow(QtWidgets.QMainWindow, Empleado_Window):
    def __init__(self):
        super().__init__()
       
     
        
        self.Empleado_ui = Empleado_Window()
        self.Empleado_ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowStaysOnTopHint)
        
        self.Empleado_ui.Home_pushButton.clicked.connect(lambda: self.Empleado_ui.stackedWidget.setCurrentWidget(self.Empleado_ui.page_home))
        self.Empleado_ui.Ver_urs_pushButton.clicked.connect(lambda: self.Empleado_ui.stackedWidget.setCurrentWidget(self.Empleado_ui.page_Usu))
        self.Empleado_ui.Crear_urs_pushButton.clicked.connect(lambda: self.Empleado_ui.stackedWidget.setCurrentWidget(self.Empleado_ui.page_Creu))
        self.Empleado_ui.Reportes_pushButton.clicked.connect(lambda: self.Empleado_ui.stackedWidget.setCurrentWidget(self.Empleado_ui.Page_RA))

       
        self.Empleado_ui.Guardar_R.clicked.connect(self.add_Reserva)
        self.Empleado_ui.Guardar_R.clicked.connect(self.Pago)
        self.Empleado_ui.Cancelar_R.clicked.connect(self.clear_inputs)

        self.Empleado_ui.pushButton.clicked.connect(lambda: self.Mostrar_Habitacion(Habitaciones_Window))

        self.Empleado_ui.pushButton_4.clicked.connect(self.Servicio)

        self.Empleado_ui.Buscar_R.clicked.connect(self.buscar_Reservacion)
        self.Empleado_ui.Cedula_R.textChanged.connect(self.resotore_table)

        self.Empleado_ui.codigo_servicio.setValidator(QIntValidator())
        self.Empleado_ui.Valor_consumo.setValidator(QDoubleValidator(0,0,0))
        self.Empleado_ui.habitacion_1.setValidator(QIntValidator())
        self.Empleado_ui.Total_Apagar_R.setValidator(QDoubleValidator(0, 0,0))
        self.Empleado_ui.Total_Apagar_R_2.setValidator(QDoubleValidator(0, 0,0))
        self.Empleado_ui.pushButton_6.clicked.connect(self.Reserva)
        

        self.config_tableR()
        self.set_table_data()




    def add_Reserva(self):
        
        nombre = self.Empleado_ui.Ingreso_Nombre.text()
        apellido = self.Empleado_ui.Ingreso_Apellido.text()
        cedula = self.Empleado_ui.Ingreso_Cedula.text()
        cedula2 = self.Empleado_ui.Ingreso_Cedula.text()
        habitacion = int(self.Empleado_ui.habitacion_1.text())
        
        email = self.Empleado_ui.Ingreso_Email.text()
        telefono = self.Empleado_ui.lineEdit_2.text()
        diaingreso1 = self.Empleado_ui.Fecha_Inicio_R.date()
        dia = diaingreso1.toPython()
        diaingreso2 = self.Empleado_ui.Fecha_Fin_R.date()
        dia2 = diaingreso2.toPython()


        data = (cedula2, dia, dia2, habitacion)
        data2 = (cedula, nombre, apellido, email, telefono)
        
        
        if Empleados_Msql.inser_huesped(data2) and Empleados_Msql.insert_resv(data):
            self.set_table_data()

        else:
            Empleados_Msql.insert_resv(data)
            self.set_table_data()
          
        

    def clear_inputs(self):
        self.Empleado_ui.Ingreso_Nombre.clear()
        self.Empleado_ui.Ingreso_Apellido.clear()
        self.Empleado_ui.Ingreso_Email.clear()
        self.Empleado_ui.Ingreso_Cedula.clear()
        self.Empleado_ui.lineEdit_2.clear()
        self.Empleado_ui.habitacion_1.clear()
        self.Empleado_ui.Total_Apagar_R.clear()
        self.Empleado_ui.Total_Apagar_R_3.clear()
        self.Empleado_ui.Total_Apagar_R_2.clear()

    def config_tableR(self):
        colum_label = ("Codigo Reserva", "Cedula del cliente","Fecha de ingreso", "Fecha de Salida", "Habitacion")
        self.Empleado_ui.Tabla_Reservacion.setColumnCount(len(colum_label))
        self.Empleado_ui.Tabla_Reservacion.setHorizontalHeaderLabels(colum_label)
        self.Empleado_ui.Tabla_Reservacion.setColumnWidth(1, 170)
        self.Empleado_ui.Tabla_Reservacion.setColumnWidth(2, 170)
        self.Empleado_ui.Tabla_Reservacion.setColumnWidth(3, 170)

    def Tabla_Reservas_Ver(self,data):
        self.Empleado_ui.Tabla_Reservacion.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
           for(index_cell, cell) in enumerate(row):
               if (index_cell == -1):
                   self.Empleado_ui.Tabla_Reservacion.setCellWidget(index_row, index_cell,None)
               else:
                   self.Empleado_ui.Tabla_Reservacion.setItem(index_row,index_cell, QTableWidgetItem(str(cell)))

    def buscar_Reservacion(self):
        param = self.Empleado_ui.Cedula_R.text()
        if param != "":
            data = Empleados_Msql.Buscar_Reserva(param)
            self.Tabla_Reservas_Ver(data)

    def resotore_table(self):
        param = self.Empleado_ui.Cedula_R.text()
        if param == "":
            self.set_table_data()

    def set_table_data(self):
        data = Empleados_Msql.verReservacion()
        self.Tabla_Reservas_Ver(data)

    def Mostrar_Habitacion(self, WindowToChange):
        self.show()
        self.Venta_ui = WindowToChange()
        self.Venta_ui.show()

    def Servicio(self):

        
        Cod_Servicio = int(self.Empleado_ui.codigo_servicio.text())
        Cod_Servicio2 = int(self.Empleado_ui.codigo_servicio.text())
        Cod_Servicio3 = int(self.Empleado_ui.codigo_servicio.text())
        Descripcion_Servicio = self.Empleado_ui.Descripcion_Ser.text()
        Descripcion_Servicio2 = self.Empleado_ui.Descripcion_Ser.text()
        cedula1 = self.Empleado_ui.Ingreso_Cedula_Srv.text()
        diaingreso1 = self.Empleado_ui.Dia_Consumo.date()
        dia = diaingreso1.toPython()
        Pago = float(self.Empleado_ui.Valor_consumo.text())
   

        data = (Cod_Servicio, Descripcion_Servicio, Descripcion_Servicio2)
        data2 = (cedula1, Cod_Servicio2,  dia, Pago)
        data3 = [Cod_Servicio3]

        errors_count = 0

        if Cod_Servicio == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Codigo del servicio obligatorio")
            msg_box.exec()
            errors_count += 1
        if Descripcion_Servicio == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Descripcion obligatorio")
            msg_box.exec()
            errors_count += 1
        if cedula1 == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(
                QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Cedula obligatorio")
            msg_box.exec()
            errors_count += 1
        if Pago == "":
            msg_box = QMessageBox()
            msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Pago obligatorio")
            msg_box.exec()
            errors_count += 1
        
        if errors_count == 0:
            if Servicios_Msql.Servicios(data) and Servicios_Msql.insert_Servicio(data2) and Servicios_Msql.udatepago():
            
                msg_box = QMessageBox()
                msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
                msg_box.setWindowTitle("JDE")
                msg_box.setText("Servicio añadido")
                msg_box.exec()

                msg_box2 = QMessageBox()
                msg_box2.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
                msg_box2.setWindowTitle("JDE")
                msg_box2.setText("Valor a pagar" + " " + str(Servicios_Msql.valorPagar(data3)))
                msg_box2.exec()
                return True
        
        
    def Reserva(self):
       Empleados_Msql.Exportar_Pdf_reserva()
       msg_box = QMessageBox()
       msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
       msg_box.setWindowTitle("JDE")
       msg_box.setText("PDF de la reserva creado")
       msg_box.exec()

    def Pago(self):
        Total_Pagar = float(self.Empleado_ui.Total_Apagar_R.text())
        Codigo_Pago = self.Empleado_ui.Total_Apagar_R_3.text()
        Codigo_Pago2 = self.Empleado_ui.Total_Apagar_R_3.text()
        Codigo_Pago3 = self.Empleado_ui.Total_Apagar_R_3.text()
        Descuento = float(self.Empleado_ui.Total_Apagar_R_2.text())
        Forma_Pago = self.Empleado_ui.Forma_Pago_2.currentText()
        cedula = self.Empleado_ui.Ingreso_Cedula.text()
        diaingreso1 = self.Empleado_ui.Fecha_Inicio_R.date()
        dia = diaingreso1.toPython()
        
        habitacion2 = int(self.Empleado_ui.habitacion_1.text())
        data3 = [habitacion2]
        data1 = (Codigo_Pago, cedula, dia, Forma_Pago)
        data2 = (Codigo_Pago2, Total_Pagar, Descuento)
        data4 = [Codigo_Pago3]

        if Empleados_Msql.insert_Caf_Pago(data1) and Empleados_Msql.insert_Det_Pago(data2) and Empleados_Msql.CambiarDeNRaR(data3) and Empleados_Msql.Update_totales():
            msg_box = QMessageBox()
            msg_box.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
            msg_box.setWindowTitle("JDE")
            msg_box.setText("Reserva realizada revise el modulo de reservas")
            msg_box.exec()

            msg_box2 = QMessageBox()
            msg_box2.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
            msg_box2.setWindowTitle("JDE")
            msg_box2.setText("Valor a pagar" + " " + str(Empleados_Msql.valorPagar(data4)))
            msg_box2.exec()
            