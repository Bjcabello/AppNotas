import usuarios.usuario as modelo
import notas.acciones
import getpass
import json

# Prefer requests if available, otherwise fall back to urllib
try:
    import requests
except ImportError:
    requests = None
    import urllib.request
    import urllib.error


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

    def login_github(self):
        """Log in using a GitHub Personal Access Token (PAT).

        This method prompts (masked) for a PAT, verifies it with the GitHub API,
        and, on success, creates a temporary user tuple compatible with the
        existing instruction flow.
        """
        print("\nLogin with GitHub\n")

        token = getpass.getpass("GitHub Personal Access Token: ")

        if not token or not token.strip():
            print("\nToken cannot be empty")
            return

        headers = {"Authorization": f"token {token}", "User-Agent": "AppNotas"}
        user_data = None

        if requests:
            try:
                resp = requests.get("https://api.github.com/user", headers=headers, timeout=10)
                if resp.status_code == 200:
                    user_data = resp.json()
                else:
                    print("\nInvalid token or GitHub API error")
                    return
            except requests.RequestException:
                print("\nNetwork error contacting GitHub")
                return
        else:
            req = urllib.request.Request("https://api.github.com/user", headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    user_data = json.load(resp)
            except urllib.error.HTTPError:
                print("\nInvalid token or GitHub API error")
                return
            except Exception:
                print("\nNetwork error contacting GitHub")
                return

        nombre = user_data.get("name") or user_data.get("login") or ""
        apellidos = ""
        email = user_data.get("email") or ""
        fecha = "GitHub"

        usuario = (user_data.get("id"), nombre, apellidos, email, fecha)
        print(f"\nBienvenido {nombre} ({user_data.get('login')})\n")
        self.instruccion(usuario)

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
            ejecuta.borrar(usuario )
            self.instruccion(usuario)

        elif accion == "salir":
            print(f"usuario {usuario[1]} {usuario[2]}, Cerro sesion")
            exit()

