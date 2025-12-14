import usuarios.usuario as modelo
class Acciones:

    def registro(self):
        print("\n Ok !! Vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Ingresa tu email?: ")
        password = input("¿Ingresa tu constraseña?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\n Correcto {registro[1].nombre} {registro[1].apellidos} te has registrado con el correo {registro[1].email}")
        else:
            print("\n No te has registrado correctamente")

    def login(self):
        print("Identifícate en el sistema...")

        email = input("¿Ingresa tu email?: ")
        password = input("¿Ingresa tu contraseña?: ")

        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()

        if login:
            print(f"Bienvenido {login[1]}, te registraste el {login[4]}")
            self.instruccion(login)
        else:
            print("Email o contraseña incorrectos")

    def instruccion(self, usuario):
        print("""
        Acione Disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (Eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")

        if accion == "crear":
            print("Vamos a crear")
            self.instruccion(usuario)

        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.instruccion(usuario)

        elif accion == "eliminar":
            print("Vamos a  eliminar")
            self.instruccion(usuario)

        elif accion == "salir":
            exit()
        return None
        
