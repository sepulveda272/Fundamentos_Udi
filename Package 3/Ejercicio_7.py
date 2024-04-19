menor = 1000
mayor = 0
producto = 1
suma = 0
for i in range (1,7):
    num1 = float(input("ingrese el numero: "))
    suma = suma + num1
    producto = producto * num1
    if num1 > mayor:
        mayor = num1
    elif num1 < menor :
        menor = num1
rango = mayor - menor
media = suma/6
print(producto)
print(suma)
print(rango)
print(media)