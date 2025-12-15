import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nVamos a registrarte...\n")

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")
        password = input("Contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nCorrecto {registro[1].nombre}, registrado con {registro[1].email}")
        else:
            print("\nNo se pudo registrar")

    def login(self):
        print("\nLogin\n")

        email = input("Email: ")
        password = input("Contraseña: ")

        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()

        if login:
            print(f"\nBienvenido {login[1]} {login[2]}, registrado el {login[4]}")
            self.instruccion(login)
        else:
            print("\nEmail o contraseña incorrectos")

    def instruccion(self, usuario):
        print("""
            Acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Qué deseas hacer?: ")
        ejecuta= notas.acciones.Acciones()

        if accion == "crear":
            ejecuta.crear(usuario)
            self.instruccion(usuario)
        
        elif accion == "mostrar":
            ejecuta.mostrar(usuario)
            self.instruccion(usuario)

        elif accion == "eliminar":
            ejecuta.borrar(usuario)
            self.instruccion(usuario)

        elif accion == "salir":
            print(f"usuario {usuario[1]} {usuario[2]}, Cerro sesion")
            exit()

