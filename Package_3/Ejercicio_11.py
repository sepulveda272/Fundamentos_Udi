factorial = 1
numFac = int(input("ingrese el numero que quiere allar elfarctorial: "))

for i in range(1, numFac+1):
    factorial *= i
print(f"el factorual de {numFac} es: {factorial}")