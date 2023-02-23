from mysql import connector
from database.connection import create_connection
from fpdf import FPDF


def ReporteM():
    conn = create_connection()
    sql = """SELECT DP.CODRHS,CIHSP,FDESDERHS,FHASTARHS,NUM_HBT,TOTALPAGARPGO FROM RESERVAS_HUESPEDES as RH, DETALLE_PAGO as DP
          WHERE RH.CODRHS = DP.CODRHS
          """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        reservas = cur.fetchall()
        
        return reservas
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at Select Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def BusquedaFechas(param):
    conn = create_connection()
    param = f"{param}"
    sql = """SELECT DP.CODRHS,CIHSP,FDESDERHS,FHASTARHS,NUM_HBT,TOTALPAGARPGO FROM RESERVAS_HUESPEDES as RH, DETALLE_PAGO as DP
             WHERE RH.CODRHS = DP.CODRHS and  MONTH(FDESDERHS) = %s
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

def BusquedaFechas_Exportar(param):
    conn = create_connection()
    param = f"{param}"
    sql = """SELECT DP.CODRHS,CIHSP,FDESDERHS,FHASTARHS,NUM_HBT,TOTALPAGARPGO FROM RESERVAS_HUESPEDES as RH, DETALLE_PAGO as DP
             WHERE RH.CODRHS = DP.CODRHS and  MONTH(FDESDERHS) = %s
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, (param,))
        usuario = cur.fetchall()
        
        lista = list()
        for usu in usuario:
            lista.append(usu)

        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.add_page()
        pdf.set_font('Arial', 'B', 30)
        
        pdf.image('assets/iconos/2.png', x = 10, y=3, w=30,h=30)
        # titulo
        pdf.set_y(40)
        pdf.cell(w=0, h=15, txt='REPORTE', border=0, ln=1, align='C', fill=0)
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
        pdf.cell(w=20, h=13, txt='Reserva', border=1, align='C', fill=1)
        pdf.cell(w = 35, h = 13, txt = 'Cedula', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 35, h = 13, txt = 'Fecha Inicio', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 35, h = 13, txt = 'Fecha Fin', border = 1,align = 'C', fill = 1)
        pdf.cell(w = 30, h = 13, txt = 'Habitacion', border = 1,align = 'C', fill = 1)
        pdf.multi_cell(w=30, h=13, txt='Pago', border=1, align='C', fill=1)
        
         # filas
        for usua in lista:
            pdf.cell(w = 20, h = 9, txt = str(usua[0]), border = 1,align = 'C', fill = 0)
            pdf.cell(w = 35, h = 9, txt = str(usua[1]), border = 1,align = 'C', fill = 0)
            pdf.cell(w = 35, h = 9, txt = str(usua[2]), border = 1,align = 'C', fill = 0)
            pdf.cell(w = 35, h = 9, txt = str(usua[3]), border = 1,align = 'C', fill = 0)
            pdf.cell(w = 30, h = 9, txt = str(usua[4]), border = 1,align = 'C', fill = 0)
            pdf.multi_cell(w = 30, h = 9, txt = str(usua[5]), border = 1,align = 'C', fill = 0)
        # pie de pagina

        pdf.output('Reporte.pdf')
        return usuario
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at Select_Parameter Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def VerReservas():
    conn = create_connection()
    sql = """SELECT DP.CODRHS,CIHSP,FDESDERHS,FHASTARHS,NUM_HBT FROM RESERVAS_HUESPEDES as RH, DETALLE_PAGO as DP
          WHERE RH.CODRHS = DP.CODRHS"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        reservas = cur.fetchall()
        return reservas
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at Select Funtion: {err.msg}")
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

def insert_usuario(data):
    conn = create_connection()
    sql = """INSERT INTO EMPLEADOS_USUARIOS (APELLIEMP,CIEMP,EMAILEMP,IDROL,NOMEMP,PWDEMP,EMPING ) 
          VALUES(%s,%s,%s,%s,%s,%s,DATE_FORMAT(%s,'%Y-%m-%d'))
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

def VerUsuarios():
    conn = create_connection()
    sql = """SELECT CIEMP,NOMEMP,APELLIEMP,EMAILEMP,EMPING FROM EMPLEADOS_USUARIOS"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        usuarios = cur.fetchall()
        return usuarios
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at Select Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def Select_id(_id):
    conn = create_connection()
    sql = f"""SELECT * FROM EMPLEADOS_USUARIOS WHERE CIEMP = {_id}"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        usuario = cur.fetchone()
        return usuario
    #presentacion de un prin en caso de un error
    except connector.Error as err:
        print(f"Error at Select_id Funtion: {err.msg}")
        return False
    finally:
        #cerramos el cursor y la conexion con la base
        cur.close()
        conn.close()

def update(_id,data):
    conn = create_connection()
    sql = f"""UPDATE EMPLEADOS_USUARIOS SET 
                                            APELLIEMP = %s,
                                            EMAILEMP = %s,
                                            NOMEMP = %s
          WHERE CIEMP = {_id}
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at update_recipe Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_parameter(param):
    conn = create_connection()
    param = f"%{param}%"
    sql = """SELECT CIEMP,NOMEMP,APELLIEMP,EMAILEMP,EMPING FROM EMPLEADOS_USUARIOS
             WHERE  CIEMP LIKE %s 
            """
    try:
        cur = conn.cursor()
        cur.execute(sql,(param,))
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

def delete(_id):
    conn = create_connection()
    sql = f"""DELETE FROM EMPLEADOS_USUARIOS
          WHERE CIEMP = {_id}
          """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Erro at update_recipe Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
