import json

with open("Proyecto/inicio.json", "r") as file:
    inicio = json.load(file)

with open("Proyecto/pacientes.json", "r") as file:
    pacientes = json.load(file)

with open("Proyecto/deportes.json", "r") as file:
    deportes = json.load(file)

sentinela = True

# Función para mostrar los registros de un paciente
def mostrar_registros(paciente):
    print("Registros actuales:")
    for i in range(len(paciente["altura"])):
        print(f"{i + 1}: Altura: {paciente['altura'][i]}, Peso: {paciente['peso'][i]}, IMC: {paciente['IMC'][i]}, Categoría: {paciente['categoria'][i]}")

# Función para eliminar un registro específico de un paciente
def eliminar_registro(paciente, indice):
    if len(paciente["altura"]) > 1:
        paciente["altura"].pop(indice)
        paciente["peso"].pop(indice)
        paciente["IMC"].pop(indice)
        paciente["categoria"].pop(indice)
        return True
    else:
        print("\033[91mNo se puede eliminar el último registro.\033[0m")
        return False

""" while True:
    usuario = input("ingrese el usuario: ")
    password = input("ingrese el password: ")

    if usuario  == inicio["cuenta"][0]["usuario"] and password == inicio["cuenta"][0]["password"]:
        print("INGRESO EXITOSO")
        break
    else:
        print("\033[91mUsuario o password incorrecto: \033[0m") """

while True:
    print("Buenos dias que decea hacer: \n 1.Paciente \n 2.Deportes \n 3.Alimentacion \n 4.Enfermedades \n 0.salir")
    try:
        op = int(input("Ingrese su opción: "))
        if op == 1:
            while True:
                print("Que decea realizar: \n 1.Registrar nuevo Paciente \n 2.Editar Info de un paciente \n 3.Registar nuevos valores de una paciente ya existentes \n 4.Eliminar registros de un paciente \n 5.Mostrar recomendaciones para un paciente \n 6.Volver al menu anterios")
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
                                                                                            "visitas": visitas,
                                                                                            "categoria": [categoria]
                                                                                        }
                                                                                        pacientes["pacientes"].append(nuevo_paciente)
                                                                                        with open("Proyecto/pacientes.json", "w") as file:
                                                                                            json.dump(pacientes, file)
                                                                                        print("Gracias por su informacion")
                                                                                        sentinela = False
                                                                                    else:
                                                                                        print("\033[91mingrese un peso coerente\033[0m")
                                                                                        print("")
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
                                if edit_true:
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
                                            
                                        if editarDato in ["altura", "peso"]:
                                            # Reemplazar el último valor de la lista con el nuevo dato
                                            if len(hola[editarDato]) > 0:
                                                hola[editarDato][-1] = nuevoDato
                                            else:
                                                hola[editarDato].append(nuevoDato)
                        
                                            # Calcular el nuevo IMC y reemplazar el último valor en la lista de IMC
                                            altura = hola["altura"][-1]
                                            peso = hola["peso"][-1]
                                            imc = peso / (altura**2) * 10000
                                            imc = round(imc, 1)
                                            if len(hola["IMC"]) > 0:
                                                hola["IMC"][-1] = imc
                                            else:
                                                hola["IMC"].append(imc)
                        
                                            # Determinar la nueva categoría y reemplazar el último valor en la lista de categorías
                                            if imc < 18.5:
                                                categoria = "Bajo peso"
                                            elif 18.5 <= imc < 25:
                                                categoria = "Normal"
                                            elif 25 <= imc < 30:
                                                categoria = "Sobrepeso"
                                            else:
                                                categoria = "Obesidad"
                        
                                            if len(hola["categoria"]) > 0:
                                                hola["categoria"][-1] = categoria
                                            else:
                                                hola["categoria"].append(categoria)
                                        else:
                                            hola[editarDato] = nuevoDato  # Para los otros campos no listados
                        
                                        with open("Proyecto/pacientes.json", "w") as file:
                                            json.dump(pacientes, file)
                        
                                        print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                        senti = False
                                else:
                                    print("No existe ese paciente que busca")
                            except ValueError:
                                print("Ingrese lo que le pide")
                    elif menuPacientes == 3:
                        senti = True
                        while senti:
                            try:
                                edit = int(input("Ingrese la cédula del paciente que desea actualizar: "))
                                edit_true = False
                                for paciente in pacientes["pacientes"]:
                                    if paciente["cedula"] == edit:
                                        nuevoRegistro = paciente
                                        edit_true = True
                                        break
                                    
                                if edit_true:
                                    print("Paciente encontrado:")
                                    for k, v in nuevoRegistro.items():
                                        print(f"{k}: {v}")
                    
                                    while senti:
                                        try:
                                            nuevoPeso = int(input("Ingrese el nuevo peso del paciente (kilogramos): "))
                                            if nuevoPeso < 1:
                                                print("Ingrese un peso coherente. Inténtelo de nuevo.")
                                                continue
                                            
                                            nuevaAltura = int(input("Ingrese la nueva altura del paciente (centímetros): "))
                                            if nuevaAltura < 60:
                                                print("Ingrese una altura coherente. Inténtelo de nuevo.")
                                                continue
                                            
                                            if not isinstance(nuevoRegistro["altura"], list):
                                                nuevoRegistro["altura"] = [nuevoRegistro["altura"]]
                                            if not isinstance(nuevoRegistro["peso"], list):
                                                nuevoRegistro["peso"] = [nuevoRegistro["peso"]]
                    
                                            nuevoRegistro["altura"].append(nuevaAltura)
                                            nuevoRegistro["peso"].append(nuevoPeso)
                    
                                            imc = nuevoPeso / (nuevaAltura ** 2) * 10000
                                            imc = round(imc, 1)
                    
                                            if not isinstance(nuevoRegistro["IMC"], list):
                                                nuevoRegistro["IMC"] = [nuevoRegistro["IMC"]]
                                            nuevoRegistro["IMC"].append(imc)
                    
                                            if imc < 18.5:
                                                categoria = "Bajo peso"
                                            elif 18.5 <= imc < 25:
                                                categoria = "Normal"
                                            elif 25 <= imc < 30:
                                                categoria = "Sobrepeso"
                                            else:
                                                categoria = "Obesidad"
                    
                                            if not isinstance(nuevoRegistro["categoria"], list):
                                                nuevoRegistro["categoria"] = [nuevoRegistro["categoria"]]
                                            nuevoRegistro["categoria"].append(categoria)
                                            
                                            # Incrementar el número de visitas
                                            if "visitas" not in nuevoRegistro:
                                                nuevoRegistro["visitas"] = 1
                                            else:
                                                nuevoRegistro["visitas"] += 1
                        
                                            print(f"El nuevo IMC es {imc} y la nueva categoría es {categoria}.")
                                            print(f"Visitas actualizadas: {nuevoRegistro['visitas']}")
                    
                                            with open("Proyecto/pacientes.json", "w") as file:
                                                json.dump(pacientes, file, indent=4)
                    
                                            print("Los nuevos valores han sido registrados exitosamente.")
                                            senti = False
                                        
                                        except ValueError:
                                            print("Por favor, ingrese un valor numérico válido.")
                                            continue
                                else:
                                    print("No existe ese paciente que busca.")
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                    elif menuPacientes == 4:
                        senti = True
                        while senti:
                            try:
                                cedula = int(input("Ingrese la cédula del paciente cuyos registros desea eliminar: "))
                                paciente_encontrado = False
                                for paciente in pacientes["pacientes"]:
                                    if paciente["cedula"] == cedula:
                                        paciente_encontrado = True
                                        while senti:
                                            mostrar_registros(paciente)
                                            try:
                                                seleccion = int(input("Ingrese el número del registro que desea eliminar (0 para salir): "))
                                                if seleccion == 0:
                                                    senti = False
                                                if 1 <= seleccion <= len(paciente["altura"]):
                                                    if eliminar_registro(paciente, seleccion - 1):
                                                        with open("Proyecto/pacientes.json", "w") as file:
                                                            json.dump(pacientes, file, indent=4)
                                                        print("Registro eliminado exitosamente.")
                                                    else:
                                                        print(" ")
                                                else:
                                                    print("Selección no válida.")
                                            except ValueError:
                                                print("Por favor, ingrese un número válido.")
                                        break
                                if not paciente_encontrado:
                                    print("Paciente no encontrado.")
                            except ValueError:
                                print("Por favor, ingrese una cédula válida.")
                            print("en proceso")

                        # me falta mirar unas cosas

                    elif menuPacientes == 5:
                        print("en proceso")
                    elif menuPacientes == 6:
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
                except ValueError:
                    print("Por favor, ingrese solo números.")
        elif op == 2:
            sentin = True
            while True:
                print("Que decea realizar: \n 1.Registrar nuevo Deporte \n 2.Editar Info de un Deporte \n 3.Eliminar Deportes \n 4.Mostrar los Deportes registrados \n 5.Volver al menu anterios")
                try:
                    menuDeportes = int(input("Ingrese una opcion: "))
                    if menuDeportes == 1:
                        while sentin:
                            
                            print("hola")
                    elif menuDeportes == 5:
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
                except ValueError:
                    print("Ingrese solo numeros")
        elif op == 0:
            print("Hasta luego, vuelva pronto")
            break
        else:
            print("Opción no válida. Por favor, ingrese 0 o 4.")
    except ValueError:
        print("Por favor, ingrese solo números.")