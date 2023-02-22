#Joue Martinez Garcia

usuarios = []
passwords = []
opcion = 1
encontrado = False
indice_encontrado = 0

while opcion:

    print("Digite el numero de la opcion que desea realizar ")
    opcion = int(input("1. Nueva cuenta\n2. Ver datos guardados\n0. Salir\n"))

    if opcion == 1:
        usuario = input("Nombre de usuario: ")
        for i in range(len(usuarios)):
            encontrado = usuarios[i] == usuario
            if encontrado:
                indice_encontrado = i
                break
        
        if encontrado:
            print("Usuario ya registrado!")
            print("Desea cambiar la contrasena?: ")
            opcion2 = int(input("1. Si\n0. No\n"))
            if opcion2:
                nueva_contrasena = input("Nueva contrasena: ")
                passwords[indice_encontrado] = nueva_contrasena
        else:
            usuarios.append(usuario)
            passwords.append(input("Contrasena: "))

    elif opcion == 2:
        print("Usuario,Contrasena")
        for i in range(len(usuarios)):
            print(f"{usuarios[i]}, {passwords[i]}")