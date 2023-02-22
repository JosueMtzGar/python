# Josue Martinez Garcia
# Este codigo lee tres numeros e imprime el mayor.

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))
numero4 = int(input("Ingresa el cuarto numero: "))

#encontrar el numero mas grande
nmasGrande = numero1

if numero2>nmasGrande:
    nmasGrande = numero2
if numero3>nmasGrande:
    nmasGrande = numero3
if numero4>nmasGrande:
    nmasGrande = numero4


#imprimir el resultado (Respetar el formato de salida)
print("El numero mas grande es:", nmasGrande)