from usuarios import acciones
print("""
Acciones disponibles
      - registro
      - login
""")
accion = input("¿Que quieres hacer?: ")
realiza = acciones.Acciones()

if accion == "registro":
    realiza.registro()

if accion == "login":
    realiza.login()
    


