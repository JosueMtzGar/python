#Josue Martinez Garcia
#Programa para verificar un incio de sesion

usuario_correcto = "Usuario1"
contasena_correcta = "password123"

usuario = input("Introduce usuario: ")
contrasena = input("Introducir contrasena: ")

if usuario != usuario_correcto:
    print("El usuario introducido no esta registrado.")
else:
    if contrasena != contasena_correcta:
        print("La contrasena introducida no es correcta.")
    else:
        print("Bienvendio.")