print("""
Acciones disponibles
      - registro
      - login

""")
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    print("Ok !! Vamos a registrarte en el sistema...")
    nombre = input("¿Cual es tu nombre?: ")
    apellidos = input("¿Cuales son tus apellidos?: ")
    email = input("¿Ingresa tu email?: ")
    password = input("¿Ingresa tu constraseña?: ")


if accion == "login":
    print("Identificate en el sistema...")
    email = input("¿Ingresa tu email?: ")
    password = input("¿Ingresa tu constraseña?: ")
