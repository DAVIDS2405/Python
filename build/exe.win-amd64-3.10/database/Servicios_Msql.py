from mysql import connector
from database.connection import create_connection
from PySide6 import QtCore
from PySide6.QtWidgets import QMessageBox

def Servicios(data):
    conn = create_connection()
    sql = """INSERT INTO SERVICIOS(CODSRV,NOMBRESRV,DESCRIPCIONSRV) 
          VALUES(%s,%s,%s)
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at insert_Data Funtion: {err.msg}")
        msg_box2 = QMessageBox()
        msg_box2.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
        msg_box2.setWindowTitle("JDE")
        msg_box2.setText("El id del servicio que ingreso ya esta ocupado debe de ser uno mayor a " + str(ServicioCod())+" "+"Conserve todos los campos")
        msg_box2.exec()
        return False
    finally:
        cur.close()
        conn.close()


def insert_Servicio(data):
    conn = create_connection()
    sql = """INSERT INTO RESGISTRO_SERVICIO(CIHSP,CODSRV,FECHARSRV,TOTALRSRV) 
          VALUES(%s,%s,DATE_FORMAT(%s,'%Y-%m-%d'),%s)
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at insert_Data Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def udatepago():
    conn = create_connection()
    sql = """UPDATE RESGISTRO_SERVICIO
             SET TOTALPSRV = (TOTALRSRV + (0.12 * TOTALRSRV))
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

def valorPagar(data):
    conn = create_connection()
    sql = """SELECT TOTALPSRV FROM RESGISTRO_SERVICIO
            WHERE CODSRV = %s
             """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        reservas = cur.fetchone()
        return reservas[0]
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at valorPagar Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()


def ServicioCod():
    conn = create_connection()
    sql = """SELECT * FROM SERVICIOS ORDER BY CODSRV DESC limit 1
             """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        reservas = cur.fetchone()
        return reservas[0]
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at ServicioCod Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()


