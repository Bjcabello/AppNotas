import pyodbc

def conexion():
    try:
        connector = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-31DR6UE;'
            'DATABASE=DBNota;'
            'Trusted_Connection=yes;'
            'TrustServerCertificate=yes;'
        )
        print("Conexión exitosa a SQL Server")
        return connector
    except pyodbc.Error as e:
        print("Error al conectar a SQL Server")
        print(e)
        return None
