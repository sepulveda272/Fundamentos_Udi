import json

with open("Proyecto/inicio.json", "r") as file:
    inicio = json.load(file)

with open("Proyecto/pacientes.json", "r") as file:
    pacientes = json.load(file)

sentinela = True

""" while True:
    usuario = input("ingrese el usuario: ")
    password = input("ingrese el password: ")

    if usuario  == inicio["cuenta"][0]["usuario"] and password == inicio["cuenta"][0]["password"]:
        print("INGRESO EXITOSO")
        break
    else:
        print("Usuario o password incorrecto: ") """

while True:
    print("Buenos dias que decea hacer: \n 1.Paciente  \n 0.salir")
    try:
        op = int(input("Ingrese su opción: "))
        if op == 1:
            while True:
                print("Que decea realizar: \n 1.Registrar nuevo Paciente \n 2.Editar Info de un paciente \n 3.Registar nuevos valores de una paciente ya existentes \n 4.Volver al menu anterios")
                try:
                    menuPacientes = int(input("Ingrese su opción: "))
                    if menuPacientes == 1:
                        while sentinela:
                            try:
                                cedula = int(input("ingrese la identificacion del paciente: "))
                                cedula_existente = False
                                for paciente in pacientes["pacientes"]:
                                    if paciente["cedula"] == cedula:
                                        cedula_existente = True
                                        break
                                if cedula_existente == False:
                                    while sentinela:
                                        nombre = input("ingrese el nombre del paciente: ")
                                        if nombre.strip() and all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
                                            while sentinela:
                                                genero = input("ingrese el genero del paciente (H) Hombre o (M) Mujer: ").upper()
                                                if genero == "H" or genero == "M":
                                                    while sentinela:
                                                        try:
                                                            edad = int(input("ingrese el edad del paciente: "))
                                                            if edad >= 1:
                                                                while sentinela:
                                                                    try:   
                                                                        altura = int(input("Ingrese su altura (centimetros): "))
                                                                        if altura >= 60:
                                                                            while sentinela:
                                                                                try:
                                                                                    peso = int(input("Ingrese su peso (kilogramos): "))
                                                                                    if peso >= 1:
                                                                                        if genero == "H":
                                                                                            genero = "Hombre"
                                                                                        elif genero == "M":
                                                                                            genero = "Mujer"
                                                                                        else:
                                                                                            print("no se que poner")
                                                                                        
                                                                                        imc = peso / (altura**2)
                                                                                        imc = imc * 10000
                                                                                        imc = round(imc,1)

                                                                                        visitas = 1
                                                                                        nuevo_paciente = {
                                                                                            "cedula": cedula,
                                                                                            "nombre": nombre,
                                                                                            "genero": genero,
                                                                                            "edad": edad,
                                                                                            "altura": altura,
                                                                                            "peso": peso,
                                                                                            "IMC": imc,
                                                                                            "visita": visitas
                                                                                        }
                                                                                        pacientes["pacientes"].append(nuevo_paciente)
                                                                                        with open("Proyecto/pacientes.json", "w") as file:
                                                                                            json.dump(pacientes, file)
                                                                                        print("Gracias por su informacion")
                                                                                        sentinela = False
                                                                                    else:
                                                                                        print("ingrese un peso coerente")
                                                                                except ValueError:
                                                                                    print("Por favor, ingrese solo números.")
                                                                        else:
                                                                            print("ingrese una altura coerente")
                                                                    except ValueError:
                                                                        print("Por favor, ingrese lo que le pide.")
                                                            else:
                                                                print("la edad no puedo ser negativa")
                                                        except ValueError:
                                                            print("Por favor, ingrese lo que le pide.")
                                                    break
                                                else:
                                                    print("Por favor, ingrese una de las opciones que se muestra. ")
                                        else:
                                            print("Por favor, no deje este campo vacio.")
                                else:
                                   print("La cédula ingresada ya está registrada. Inténtelo de nuevo.")
                            except ValueError:
                                print("Por favor, ingrese lo que le pide.")
                    elif menuPacientes == 2:
                        
                        print("hola")
                    elif menuPacientes == 3:
                        
                        print("hola")
                    elif menuPacientes == 4:
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
                except ValueError:
                    print("Por favor, ingrese solo números.")
        elif op == 0:
            print("Hasta luego, vuelva pronto")
            break
        else:
            print("Opción no válida. Por favor, ingrese 0 o 1.")
    except ValueError:
        print("Por favor, ingrese solo números.")