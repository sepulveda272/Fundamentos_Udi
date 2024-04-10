original = input().upper()
sinEspacios = ""
for i in original:
    if i!=" ":
        sinEspacios += i
invertida = ""
for i in reversed(sinEspacios):
    invertida += i
if sinEspacios == invertida:
    print("PALINDROMA")
else:
    print("NO PALINDROMA")

    hipotenusa = int(input())
Ca2 = int(input())

ca2 = Ca2/100

ca1 = (hipotenusa**2)-(ca2**2)

Ca1 = ca1**0.5


print(round(Ca1,2))
Ca1 = str(ca1**0.5)
hola1 =(Ca1[:4])
hola = float(hola1)
print(hola)