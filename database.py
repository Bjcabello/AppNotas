import pyodbc

def conexion():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-31DR6UE;'
        'DATABASE=DBNota;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    return conn
