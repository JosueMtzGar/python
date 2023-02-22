largo = int(input("Intoudcir largo: "))
ancho = int(input("Introducir ancho: "))

print("+","-"*ancho, "+")
print(("|" + " "*(ancho+2) + "|\n")*largo, end = "")
print("+","-"*ancho, "+")