from database import conexion

class Nota:
    def __init__(self, usuario_id, titulo = "", descripcion =""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        

        sql = """
        INSERT INTO notas (usuario_id, titulo, descripcion, fecha)
        VALUES (?, ?, ?, GETDATE())
        """

        datos = (self.usuario_id, self.titulo, self.descripcion)
        conn = conexion()
        cursor = conn.cursor() 

        cursor.execute(sql, datos)
        conn.commit()

        resultado = [cursor.rowcount, self]

        cursor.close()
        conn.close()

        return resultado
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        conn = conexion()
        cursor = conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self, titulo):
        sql = """
        DELETE FROM notas
        WHERE usuario_id = ?
        AND titulo LIKE ?
        """

        datos = (self.usuario_id, f"%{titulo}%")

        conn = conexion()
        cursor = conn.cursor()

        cursor.execute(sql, datos)
        conn.commit()

        resultado = cursor.rowcount

        cursor.close()
        conn.close()

        return resultado

