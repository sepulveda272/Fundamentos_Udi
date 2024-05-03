import math
x=int(input("ingrese un numero: "))
if x<=1 or x>12:
    print ("error, no hay probabilidad")
else:
    combix=0
    for dado1 in range (1,7):
        for dado2 in range (1,7):
            combi=dado1*dado2
            if dado1+dado2==x:
                combix+=1
    probabi=math.floor (combix/combi*100)/100
    pro=combix/combi*100
    pro=math.floor (pro*100)/100
    print (probabi)
    print (pro,"%")