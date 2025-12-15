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

        for nota in notas:
            print("\n******************")
            print(nota[2])
            print(nota[3])
            print("******************")

    def borrar(self, usuario):
        print(f"\nOkey {usuario[1]} {usuario[2]}!! Se eliminarán notas")

        titulo = input("Introduce el título de la nota a borrar: ")

        
        nota = Nota(usuario[0], titulo, "")
        eliminadas = nota.eliminar(titulo)

        if eliminadas >= 1:
            print(f"Hemos borrado la nota: {titulo}")
        else:
            print("No se ha borrado ninguna nota")
