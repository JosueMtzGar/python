#Josue Martinez Garcia

""" Programa para verificar un incio de sesion 
con limites de intentos """

usuario_correcto = "Usuario1"
contasena_correcta = "password123"
intentos = 0

usuario = input("Introduce usuario: ")

if usuario != usuario_correcto:
    print("El usuario introducido no esta registrado.")
else:
    contrasena = input("Introducir contrasena: ")
    intentos = 1

    while contrasena != contasena_correcta:
        print("La contrasena introducida no es correcta.")
        contrasena = input("Introduce contrasena de nuevo: ")
        intentos += 1
        
        if intentos == 3 and contrasena != contasena_correcta:
            print("Se terminaron tus intentos, cuenta bloqueada.")
            break
    
    if contrasena == contasena_correcta:
        print(f"Bienvendio {usuario_correcto} solo te tomo {intentos} intentos el inciar sesion")