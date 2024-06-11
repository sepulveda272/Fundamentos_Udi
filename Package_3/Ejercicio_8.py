tamaño = int(input("ingrese el rango de numero que desea sumar"))
sumaPar = 0
sumaImpar = 0

for impar in range(1,tamaño+1,2):
    sumaImpar = sumaImpar + impar
print("La suma de los impares hasta", tamaño ," es: ",sumaImpar)

for par in range(0,tamaño+1,2):
    sumaPar = sumaPar + par
print("La suma de los pares hasta", tamaño ," es: ",sumaPar)