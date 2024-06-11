
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
if num2 < num1:
    menor = num2
else:
    menor = num1

for i in range(1, menor + 1):
    if num1 % i == 0 and num2 % i == 0:
        MCD = i
print("El maximo comun divisor de", num1, " y " ,num2 ,"es: ", MCD)