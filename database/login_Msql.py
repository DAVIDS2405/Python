from mysql import connector
from database.connection import create_connection

def loginJDE_Empleado(user,password):
    conn = create_connection()
    sql="""SELECT CIEMP,PWDEMP,IDROL FROM EMPLEADOS_USUARIOS
            WHERE CIEMP like %s and PWDEMP like %s and IDROL = 1"""
    try:
        cur = conn.cursor(True)
        cur.execute(sql,(user,password))
        LoginUser = cur.fetchone()
        return LoginUser
    except connector.Error as err:
        print(f"Erro at Lofin Funtion: {err.msg}")

        return False
    finally:
        cur.close()
        conn.close()


def loginJDE_Admin(user, password):
    conn = create_connection()
    sql = """SELECT CIEMP,PWDEMP,IDROL FROM EMPLEADOS_USUARIOS
            WHERE CIEMP like %s and PWDEMP like %s and IDROL = 0"""
    try:
        cur = conn.cursor(True)
        cur.execute(sql, (user, password,))
        LoginUser = cur.fetchone()
        return LoginUser
    except connector.Error as err:
        print(f"Erro at Lofin Funtion: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()