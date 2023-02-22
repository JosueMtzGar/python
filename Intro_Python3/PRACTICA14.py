#Josue Martinez Garcia

lista_productos = []
lista_cantidades = []
opcion = "a"

while opcion != "s":
    opcion = input("Introduce 'c' si deseas agregar un nuevo producto o 's' si deseas imprimir tu lista: ")
    if opcion == "c":
        lista_productos.append(input("Introduce nombre de producto: "))
        lista_cantidades.append(input("Introduce cantidad: "))
    elif opcion == "s":
        print("Tu lista es: ")
        print("Producto","Cantidad", sep= "     ")
        for i in range(len(lista_productos)):
                print(f"{lista_productos[i]:16} {lista_cantidades[i]}")