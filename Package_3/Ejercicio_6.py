num1 = int(input("ingrese el numero"))
contador=0
for i in range (1,num1):
    rta = num1 % i
    if rta == 0:
        contador += 1
if contador < 2:
    print("es primo")
else:
    print("no es primo")