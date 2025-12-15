from database import conexion

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        conn = conexion()
        cursor = conn.cursor()

        sql = """
        INSERT INTO notas (usuario_id, titulo, descripcion, fecha)
        VALUES (?, ?, ?, GETDATE())
        """

        datos = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, datos)
        conn.commit()

        resultado = [cursor.rowcount, self]

        cursor.close()
        conn.close()

        return resultado
