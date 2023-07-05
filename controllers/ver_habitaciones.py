from PySide6.QtWidgets import  QTableWidgetItem
from PySide6 import QtWidgets,QtCore
from views.Habitacion_Window import Habitacion_Window
from database import Empleados_Msql


class Habitaciones_Window(QtWidgets.QMainWindow, Habitacion_Window):
    def __init__(self):
        super().__init__()
        self.Habitacion_ui = Habitacion_Window()
        self.Habitacion_ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowStaysOnTopHint)

        self.config_table()
        self.Tabla_Reservas_Ver()



    def config_table(self):
        colum_label = ("Numero de habitacion", "Tipo","Estado", "Piso","Descripcion")
        self.Habitacion_ui.tableWidget.setColumnCount(len(colum_label))
        self.Habitacion_ui.tableWidget.setHorizontalHeaderLabels(colum_label)
        self.Habitacion_ui.tableWidget.setColumnWidth(1, 170)
        self.Habitacion_ui.tableWidget.setColumnWidth(2, 170)
        self.Habitacion_ui.tableWidget.setColumnWidth(3, 170)

    def Tabla_Reservas_Ver(self):
        data = Empleados_Msql.verHabitaciones()
        self.Habitacion_ui.tableWidget.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
           for(index_cell, cell) in enumerate(row):
               if (index_cell == -1):
                   self.Habitacion_ui.tableWidget.setCellWidget(index_row, index_cell,None)
               else:
                   self.Habitacion_ui.tableWidget.setItem(index_row,index_cell, QTableWidgetItem(str(cell)))