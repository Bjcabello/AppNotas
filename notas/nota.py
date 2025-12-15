from database import conexion

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self. usuario_id = usuario_id
        self.titulo = titulo
        self.decripcion = descripcion

    def guardar(self):

        connect = conexion()
        cursor = connect.cursor()
        sql = "INSERT INTO notas VALUES(null, ?, ?, ?, NOW())"
        nota = (self.usuario_id, self.titulo, self.decripcion)

        cursor.execute(sql, nota)
        cursor.commit()

        return[cursor.rowcount, self]

        