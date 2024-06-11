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