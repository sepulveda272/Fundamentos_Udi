cant = int(input("ingrese la cantidad de numeros que va a ingresar: "))
string = ""
for i in range(1, cant + 1):
    num = int(input("ingrese un numero: "))
    if num != 0:
        numeros = str(num)
        string = string + " " + numeros
print(string)
