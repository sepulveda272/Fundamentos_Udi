B=int(input("ingrese la base: "))
P=int(input("ingrese el exponente: "))
result=1
for i in range (1,P+1):
    result=result*B
print (result)