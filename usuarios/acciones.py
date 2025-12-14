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
            print(f"\n Correcto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\n No te has registrado correctamente")
    def login(self):
        print("Identificate en el sistema...")

        try:
            email = input("¿Ingresa tu email?: ")
            password = input("¿Ingresa tu constraseña?: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[1]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema {login[5]}")
                self.instruccion(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login Incorrecto")

    def instruccion(self, usuario):
        return None
        
