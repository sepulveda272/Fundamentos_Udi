
m = int(input("ingrese el primer numero: "))
n = int(input("ingrese el segundo numero: "))
x = int(input("ingrese el espaciado entre valores >= 3: "))

rta = "".rjust(x)

for i in range (m,n+1,1):
    rta = rta.rjust(x) + str(i).rjust(x)
print(rta)
for i in range (1,11,1):
    rta= str(i).rjust(x)
    for j in range (m,n+1):
        rta = rta.rjust(x) + str(j*i).rjust(x)
    print(rta)