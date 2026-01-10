from usuarios.acciones import Acciones
print("""
Acciones disponibles
      - registro
      - login
      - login_github
""")
accion = input("¿Que quieres hacer?: ")
realiza = Acciones()

if accion == "registro":
    realiza.registro()

if accion == "login":
    realiza.login()

elif accion == "login_github" or accion == "github":
    realiza.login_github()



