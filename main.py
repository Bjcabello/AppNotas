from usuarios.acciones import Acciones
print("""
Acciones disponibles
      - registro
      - login
""")
accion = input("¿Que quieres hacer?: ")
realiza = Acciones()

if accion == "registro":
    realiza.registro()

if accion == "login":
    realiza.login()
    


