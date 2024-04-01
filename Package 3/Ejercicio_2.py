num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

if (num1 > num2):
    maximo = num1
else:
    maximo = num2

while maximo % num1 != 0 or maximo % num2 != 0:
    maximo += 1

print("El mínimo común múltiplo de", num1, "y", num2, "es:", maximo)    