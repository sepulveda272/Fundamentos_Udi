mayor = 0
menor = 1000
sentinela = True
while sentinela:
    num1 = int(input("ingrese un numero (terminar el programa ingrese el -99): "))
    if num1 == -99:
        print("el numero mayor es: ", mayor)
        print("el numero menor es: ", menor)
        sentinela = False
    elif num1 > mayor:
        mayor = num1
    elif num1 < menor:
        menor = num1