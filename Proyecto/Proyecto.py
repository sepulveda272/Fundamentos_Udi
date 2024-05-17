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

                                                                                        if imc < 18.5:
                                                                                            categoria = "Bajo peso"
                                                                                            print(categoria)
                                                                                        elif 18.5 <= imc < 25:
                                                                                            categoria = "Normal"
                                                                                            print(categoria)
                                                                                        elif 25 <= imc < 30:
                                                                                            categoria = "Sobrepeso"
                                                                                            print(categoria)
                                                                                        else:
                                                                                            categoria = "Obesidad"
                                                                                            print(categoria)

                                                                                        nuevo_paciente = {
                                                                                            "cedula": cedula,
                                                                                            "nombre": nombre,
                                                                                            "genero": genero,
                                                                                            "edad": edad,
                                                                                            "altura": [altura],
                                                                                            "peso": [peso],
                                                                                            "IMC": [imc],
                                                                                            "visita": visitas,
                                                                                            "categoria": [categoria]
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
                        senti = True
                        while senti:
                            try:
                                edit = int(input("Ingrese la cedula del paciente que desea editar: "))
                                edit_true = False
                                for paciente in pacientes["pacientes"]:
                                    if paciente["cedula"] == edit:
                                        hola = paciente
                                        edit_true = True
                                if edit_true == True:
                                    for k, v in hola.items():
                                        print(f"{k}: {v}")

                                    while senti:
                                        editarDato = input("¿Qué campo desea cambiar? (nombre, genero, edad, altura, peso): ").lower()
                                        if editarDato not in hola:
                                            print("Campo inválido. Por favor, seleccione un campo válido.")
                                            continue
                                        
                                        nuevoDato = input(f"Ingrese el nuevo valor para {editarDato}: ")

                                        if editarDato in ["edad", "altura", "peso"]:
                                            try:
                                                nuevoDato = int(nuevoDato)
                                                if editarDato == "edad" and nuevoDato < 1:
                                                    print("La edad no puede ser negativa. Inténtelo de nuevo.")
                                                    continue
                                                if editarDato == "altura" and nuevoDato < 60:
                                                    print("Ingrese una altura coherente. Inténtelo de nuevo.")
                                                    continue
                                                if editarDato == "peso" and nuevoDato < 1:
                                                    print("Ingrese un peso coherente. Inténtelo de nuevo.")
                                                    continue
                                            except ValueError:
                                                print("Por favor, ingrese un valor numérico válido.")
                                                continue
                                        
                                        hola[editarDato] = nuevoDato
                                        
                                        # para poder editar el peso o altura y me actualize el valor del imc
                                        
                                        """ if editarDato in ["peso", "altura"]:
                                            peso = hola.get("peso", 0)
                                            altura = hola.get("altura", 0)
                                            if peso > 0 or altura > 0:
                                                imc = peso / ((altura / 100) ** 2)
                                                hola["imc"] = imc """

                                        with open("Proyecto/pacientes.json", "w") as file:
                                            json.dump(pacientes, file)

                                        print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                        senti= False
                                else:
                                    print("No existe ese paciente que busca")
                            except ValueError:
                                print("Ingrese lo que le pide")
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