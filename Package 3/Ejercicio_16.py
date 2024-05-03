num=(input("ingrese un numero: "))
reverse=""
for i in reversed(num):
    reverse+=i
if num==reverse:
    print ("es capicua")
else:
    print ("no es capicua")