#Josue Martinez Garcia
#Programa para verificar un incio de sesion con el ciclo while

usuario_correcto = "Usuario1"
contasena_correcta = "password123"
intentos = 0

usuario = input("Introduce usuario: ")
contrasena = input("Introducir contrasena: ")

if usuario != usuario_correcto:
    print("El usuario introducido no esta registrado.")
else:
    while contrasena != contasena_correcta:
        intentos +=1
        print("La contrasena introducida no es correcta.")
        contrasena = input("Introduce contrasena de nuevo: ")

    print(f"Bienvendio {usuario_correcto} solo te tomo {intentos+1} intentos el inciar sesion")