from database import conexion
class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email 
        self.password = password

    def registrar(self):
        return self.nombre

    def identificar(self):
        return self.nombre