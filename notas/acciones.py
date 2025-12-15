from notas.nota import Nota 

class Acciones:
    
    def crear(self, usuario):
        print(f"Ok {usuario[1]} {usuario[2]}!! Vamos a crear una nota: ")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce la descripcion de tu nota: ")

        nota = Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nSe ha guardado correctamente la nota: {nota.titulo}")
        
        else:
            print(f"\nNo se guardo la nota {usuario[1]}")

    def mostrar(self, usuario):
        print(f"Ok {usuario[1]} !! Listado notas: ")

        nota = Nota(usuario[0])
        notas = nota.listar()

        print(notas)