# Josue Martinez Garcia
# Este programa calcula la hora de dinalizacion de una
# tarea, dada una hora de inicio y la duracion de la tarea

#Obtener datos de entrada (Respetar el orden en que se solicitan)
inicial_horas = int(input("Introduzca la hora de inicio: "))
inicial_minutos = int(input("Introdusca los minutos de inicio: "))
duracion = int(input("Introduzca la duracion en minutos: " ))

# Calcular hora de finalizacion

final_hora = (inicial_horas + (inicial_minutos + duracion)//60)%24
final_minutos = (inicial_minutos + duracion%60)%60

# Mostrar resultado (Respetar el siguiente formato de salida)
print("La hora final de la tarea es: ", final_hora, ":", final_minutos, sep="")