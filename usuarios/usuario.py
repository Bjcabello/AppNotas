from database import conexion
import datetime

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email 
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()  

        sql = """
        INSERT INTO usuarios (nombre, apellidos, email, password, fecha)
        VALUES (?, ?, ?, ?, ?)
        """

        datos = (self.nombre, self.apellidos, self.email, self.password, fecha)

        connector = conexion()
        if connector is None:
            return [0, self]

        cursor = connector.cursor()
        cursor.execute(sql, datos)
        connector.commit()

        return [cursor.rowcount, self]


    def identificar(self):
        return self.nombre