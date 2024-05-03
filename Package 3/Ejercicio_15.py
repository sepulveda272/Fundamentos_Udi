frase=str(input("ingrese una frase: "))
a=e=i=o=u=0
for j in frase:
    if j=="a":
        a+=1
    elif j=="e":
        e+=1
    elif j=="i":
        i+=1
    elif j=="o":
        o+=1
    elif j=="u":
        u+=1
print ("la a se encuentra:", a)
print ("la e se encuentra:", e)
print ("la i se encuentra:", i)
print ("la o se encuentra:", o)
print ("la u se encuentra:", u)

