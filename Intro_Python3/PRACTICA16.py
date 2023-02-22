""" Josue Martinez Garcia """
import random as r

dias = []
""" round(r.uniform(0,40),2) <- Numeros aleatorios para probar el codigo"""

for i in range(5):
    temperatura_hora = []
    for j in range(4):
        temperatura_hora.append(float(input(f"Ingrese temperatura: ")))
    dias.append(temperatura_hora)

print("Las temperaturas registradas son: ")
for i in dias:
    print(i)

""" Calculo de temperatura promedio al mediodia """
suma = 0
for i in dias:
    suma += i[2]
promedio = suma/len(dias)
print("Temperatura promedio al mediodia: ", round(promedio,2))


""" Se encuentra la temperatura mas alta de todas las registradas """
temperatura_maxima = dias[0][0]
for i in dias:
    for j in temperatura_hora:
        if j > temperatura_maxima:
            temperatura_maxima = j
print("La temperatura mas alta fue: ", round(temperatura_maxima,2))