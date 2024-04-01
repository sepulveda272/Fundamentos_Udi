maximo = 0.0
minimo = 1001.0
print("Por favor, ingrese 100 números entre 1.0 y 1000.0:")
for i in range(100):
    while True:
            num = float(input(f"Ingrese el número {i + 1} (entre 1.0 y 1000.0): "))
            if 1.0 <= num <= 1000.0:
                if num > maximo:
                    maximo = num
                if num < minimo:
                    minimo = num
                break
            else:
                print("El número debe estar entre 1.0 y 1000.0. Inténtelo de nuevo.")
print(f"El número mayor es: {maximo}")
print(f"El número menor es: {minimo}")