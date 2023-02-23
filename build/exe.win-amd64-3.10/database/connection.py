from mysql import connector


config = {
    'user': '252095',
    'password': 'jhoanasistemas',
    'host': 'mysql-jhoanaaucancela.alwaysdata.net',
    'database': 'jhoanaaucancela_hoteljde'
}

def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}" )
    return conn

