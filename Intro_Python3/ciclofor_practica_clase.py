num = int(input("Introduzca un número para calcular el factorial: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"El factorial es {factorial}")