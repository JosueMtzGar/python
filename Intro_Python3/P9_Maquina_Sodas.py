#Josue Martinez Garcia
#Maquina de sodas
costo_soda = 17
saldo = 0
moneda = 0

while saldo < costo_soda:
    #Mostrar monto adeuado
    print("Monto adeudado: ", costo_soda-saldo, sep="$")
    #Solicitar ingresar moneda
    moneda = int(input("Ingrese moneda: "))
    #Verificar validez de moneda
    if moneda == 1 or moneda == 2 or moneda == 5 or moneda == 10:
        saldo += moneda

#Salida del programa
print("Toma tu soda, tu cambio es: ", saldo-costo_soda, sep="$")