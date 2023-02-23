from mysql import connector
from database.connection import create_connection
from PySide6 import QtCore
from PySide6.QtWidgets import QMessageBox
from fpdf import FPDF


def inser_huesped(data):
    conn = create_connection()
    sql = """INSERT INTO HUESPEDES(CIHSP,NOMHSP,APELLIHSP,EMAILHSP,TELFHSP) 
          VALUES(%s,%s,%s,%s,%s)
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at insert_Data_huesped Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def Update_totales():
    conn = create_connection()
    sql = """UPDATE DETALLE_PAGO
             SET TOTALPAGARPGO = (TOTALPGO + (IVAPGO * TOTALPGO) - ((TOTALPGO*DESCUENTOPGO)/100))
           """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at Update_totales Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
    
def verHabitaciones():
    #El ordenamiento al tener NUMHBT como string se ocupa la funcion length para que el ordenamiento funcione
    conn = create_connection()
    sql = """SELECT NUMHBT, TIPOHBT, ESTADOHBT, PISOHBT, DESCRHBT FROM HABITACIONES
            WHERE ESTADOHBT like 'NR'
            ORDER BY  length(NUMHBT)
          """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        Habitaciones = cur.fetchall()
        return Habitaciones
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error atverHabitaciones Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def CambiarDeNRaR(data):
    conn = create_connection()
    sql = """  UPDATE HABITACIONES SET  ESTADOHBT  = "R"
               WHERE NUMHBT = %s
          """
    try:
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at CambiarDeNRaR Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def insert_resv(data):

    conn = create_connection()
    sql = """INSERT INTO RESERVAS_HUESPEDES(CIHSP,FDESDERHS,FHASTARHS,NUM_HBT) 
          VALUES(%s,DATE_FORMAT(%s,'%Y-%m-%d'),DATE_FORMAT(%s,'%Y-%m-%d'),%s)
          """
        
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

    except connector.Error as err:
        print(f"Erro at insert_Data_reserva Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def verReservacion():
    conn = create_connection()
    sql = """SELECT DP.CODRHS,CIHSP,FDESDERHS,FHASTARHS,NUM_HBT FROM RESERVAS_HUESPEDES as RH, DETALLE_PAGO as DP
          WHERE RH.CODRHS = DP.CODRHS """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        reservas = cur.fetchall()
        return reservas
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at verReservacion Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def valorPagar(data):
    conn = create_connection()
    sql = """SELECT TOTALPAGARPGO FROM DETALLE_PAGO 
            WHERE CODPGO = %s
             """
    try:
        cur = conn.cursor()
        cur.execute(sql,data)
        reservas = cur.fetchone()
        print(reservas[0])
        return reservas[0]
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at valorPagar Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def insert_Det_Pago(data):
    
    try:
        
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("select * from RESERVAS_HUESPEDES order by CODRHS desc limit 1")
        reserva = cursor.fetchone()
        lista = list()
       

        sqlTwo = "INSERT INTO DETALLE_PAGO (CODRHS,CODPGO,TOTALPGO,DESCUENTOPGO,IVAPGO) VALUES (%s,%s, %s,%s,%s)"
        Values = (reserva[0], data[0], data[1], data[2], 0.12)
        
        cursor.execute(sqlTwo, Values)

        connection.commit()
        return True

    except connector.Error as err:
        print(f"Erro at insert_Data_Pago Funtion: {err.msg}")
        return False
    finally:
        cursor.close()
        connection.close()

def insert_Caf_Pago(data):
    conn = create_connection()
    sql = """INSERT INTO CABECERA_PAGOS(CODPGO,CIHSP,FCONSUPGO,FORMAPGO,RUCEMPRPGO) 
          VALUES(%s,%s,DATE_FORMAT(%s,'%Y-%m-%d'),%s,'1713927348123')
          
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
        
    except connector.Error as err:
        print(f"Error at insert_Caf_Pago Funtion: {err.msg}")
        msg_box2 = QMessageBox()
        msg_box2.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
        msg_box2.setWindowTitle("JDE")
        msg_box2.setText("El codigo que ingreso ya esta ocupado debe de ser uno mayor a " + str(codCambiar())+" "+"Conserver el campo de Cedula, Habitacion,Total a pagar, Descuento, Forma de pago y las Fechas")
        msg_box2.exec()
        return False
    finally:
        cur.close()
        conn.close()

def codCambiar():
    conn = create_connection()
    sql = """SELECT * FROM DETALLE_PAGO ORDER BY IDNUMPGO DESC limit 1
             """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        reservas = cur.fetchone()
        return reservas[2]
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at codCambiar Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def Buscar_Reserva(param):
    conn = create_connection()
    param = f"%{param}%"
    sql = """SELECT CODRHS,CIHSP,FDESDERHS,FHASTARHS,NUM_HBT FROM RESERVAS_HUESPEDES
             WHERE  CODRHS like %s
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, (param,))
        usuario = cur.fetchall()
        return usuario
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at Select_Parameter Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def Exportar_Pdf_reserva():
    conn = create_connection()
    sql = """SELECT IDNUMPGO,CODRHS,CODPGO,TOTALPGO,DESCUENTOPGO,IVAPGO,TOTALPAGARPGO FROM DETALLE_PAGO ORDER BY IDNUMPGO DESC limit 1
             """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        reservas = cur.fetchone()

        lista = list()
        for usu in reservas:
            lista.append(usu)

        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.add_page()
        pdf.set_font('Arial', 'B', 30)
        pdf.image('assets/iconos/2.png', x = 10, y=3, w=30,h=30)
        # titulo
        
        pdf.set_y(40)
        pdf.cell(w=0, h=15, txt='RESERVA', border=0, ln=1, align='C', fill=0)
        pdf.set_font('Arial', 'B', 12)
        pdf.set_y(5)
        pdf.set_x(150)
        pdf.cell(w=0, h=15, txt='Ruc: '+'1713927348123', border=0, ln=1, fill=0)
        pdf.set_y(10)
        pdf.set_x(150)
        pdf.cell(w=0, h=15, txt='Tel: '+'0990095964', border=0, ln=1, fill=0)
        pdf.ln(50)
        pdf.set_font('Arial', '', 12)

        # encabezado
        
        pdf.set_fill_color(r=213, g=219, b=219)
        pdf.cell(w=27, h=13, txt='Num de pago', border=1, align='C', fill=1)
        pdf.cell(w = 27, h = 13, txt = 'Reserva', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 27, h = 13, txt = 'Cod de pago', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 27, h = 13, txt = 'Total', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 27, h = 13, txt = 'Descuento', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 27, h = 13, txt = 'Iva', border = 1,align = 'C', fill = 1)
        pdf.multi_cell(w=27, h=13, txt='Total a pagar', border=1, align='C', fill=1)
        
         # filas
        
        for usua in lista:
            pdf.cell(w=27, h=9, txt=str(usua), border=1, align='C', fill=0)
           
            
        # pie de pagina
        
        pdf.output('Reserva.pdf')
        return reservas
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at codCambiar Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()