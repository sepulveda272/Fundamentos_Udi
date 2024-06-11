num=int(input("ingrese la cantidad de personas que van a votar:"))
v1="michael"
v2="paula"
v3="eliana"
while True:
    mic=0
    pau=0
    eli=0
    blan=0
    for i in range (1,num+1):
        print(f"[10] {v1}, [11] {v2}, [12] {v3}, [13]voto en blanco")
        x=int(input("ingrese su voto: "))
        if x==10:
            mic=mic+1
        elif x==11:
            pau=pau+1
        elif x==12:
            eli=eli+1
        elif x==13:
            blan=blan+1 
    if mic>pau and mic>eli and mic>blan:
        print (f"ganador {v1}")
        break
    elif pau>mic and pau>eli and pau>blan:
        print (f"ganador {v2}")
        break

    elif eli>mic and eli>pau and eli>blan:
        print (f"ganador {v3}")
        break
    else:
        print ("hubo un empate, se debe repetir la votación")
        print ("ingrese el nombre de los nuevos votantes")
        v1=input()
        v2=input()
        v3=input()