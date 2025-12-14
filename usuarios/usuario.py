from database import conexion
import datetime
import hashlib


class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        password_hash = hashlib.sha256(
            self.password.encode('utf-8')
        ).hexdigest()

        sql = """
        INSERT INTO usuarios (nombre, apellidos, email, password, fecha)
        VALUES (?, ?, ?, ?, ?)
        """

        conn = conexion()
        cursor = conn.cursor()
        cursor.execute(sql, (
            self.nombre,
            self.apellidos,
            self.email,
            password_hash,
            fecha
        ))
        conn.commit()

        cursor.close()
        conn.close()

        return [1, self]

    def identificar(self):
        password_hash = hashlib.sha256(
            self.password.encode('utf-8')
        ).hexdigest()

        sql = """
        SELECT id, nombre, apellidos, email, fecha
        FROM usuarios
        WHERE email = ? AND password = ?
        """

        conn = conexion()
        cursor = conn.cursor()
        cursor.execute(sql, (self.email, password_hash))
        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        return usuario
