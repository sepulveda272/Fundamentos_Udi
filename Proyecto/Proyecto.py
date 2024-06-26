import json
from datetime import datetime

with open("Proyecto/inicio.json", "r") as file:
    inicio = json.load(file)

with open("Proyecto/pacientes.json", "r") as file:
    pacientes = json.load(file)

with open("Proyecto/deportes.json", "r") as file:
    deportes = json.load(file)

with open("Proyecto/alimentaciones.json", "r") as file:
    alimentaciones = json.load(file)

sentinela = True


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def mostrar_registros(paciente):
    print("Registros actuales:")
    for i in range(len(paciente["altura"])):
        print(f"{i + 1}: Altura: {paciente['altura'][i]}, Peso: {paciente['peso'][i]}, IMC: {paciente['IMC'][i]}, Categoría: {paciente['categoria'][i]}, Fecha: {paciente['fecha'][i]}.")

def eliminar_registro(paciente, indice):
    if len(paciente["altura"]) > 1:
        paciente["altura"].pop(indice)
        paciente["peso"].pop(indice)
        paciente["IMC"].pop(indice)
        paciente["categoria"].pop(indice)
        paciente["fecha"].pop(indice)
        return True
    else:
        print(f"{RED}No se puede eliminar el último registro. {RESET}")
        return False

def aplicar_color(categoria, texto):
    if categoria == "Bajo peso":
        return f"\033[91m{texto}\033[0m"
    elif categoria == "Normal":
        return f"\033[92m{texto}\033[0m"
    elif categoria == "Sobrepeso":
        return f"\033[93m{texto}\033[0m"
    elif categoria == "Obesidad":
        return f"\033[95m{texto}\033[0m"
    else:
        return texto
                            
""" print(f"{GREEN}Buenos dias profesor y compañeros de clase. {RESET}")
while True:
    usuario = input(f"{BLUE}ingrese el usuario: {RESET}")
    password = input(f"{BLUE}ingrese el password: {RESET}")

    if usuario  == inicio["cuenta"][0]["usuario"] and password == inicio["cuenta"][0]["password"]:
        print(f"{GREEN}INGRESO EXITOSO. {RESET}")
        break
    else:
        print(f"{RED}Usuario o password incorrecto: {RESET}") """

while True:
    try:
        print("Buenos dias que decea hacer: \n 1.Paciente \n 2.Deportes \n 3.Alimentacion \n 0.salir")
        op = int(input(f"{BLUE}Ingrese su opción: {RESET}"))
        if op == 1:
            while True:
                try:
                    print("Que decea realizar: \n 1.Registrar nuevo Paciente \n 2.Editar Info de un paciente \n 3.Registar nuevos valores de una paciente ya existentes \n 4.Eliminar registros de un paciente \n 5.Mostrar recomendaciones para un paciente \n 6.Mostrar registros de un paciente \n 7.Listado de pacientes \n 8.Volver al menu anterios")
                    menuPacientes = int(input(f"{BLUE}Ingrese su opción: {RESET}"))
                    if menuPacientes == 1:            
                        while True:
                            try:
                                cedula = int(input(f"{BLUE}Ingrese la identificación del paciente: {RESET}"))
                                if cedula >= 1:
                                    cedula = str(cedula)
                                    if len(cedula) >= 8 and len(cedula) <= 10:
                                        cedula = int(cedula)
                                        cedula_existente = any(paciente["cedula"] == cedula for paciente in pacientes["pacientes"])
                                        if cedula_existente:
                                            print(f"{RED}La cédula ingresada ya está registrada. Inténtelo de nuevo.{RESET}")
                                        else:
                                            break
                                    else:
                                        print(f"{RED}La cédula ingresada tiene que tener de 8 a 10 numeros{RESET}")
                                else:
                                    print(f"{RED}La cédula no puede ser negativa.{RESET}")
                            except ValueError:
                                print(f"{RED}ingrese opcion correcta.{RESET}")
                                        
                        while True:
                            nombre = input(f"{BLUE}Ingrese el nombre del paciente: {RESET}").strip()
                            if nombre and all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
                                break
                            else:
                                print(f"{RED}Por favor, ingrese un nombre válido sin dejar el campo vacío.{RESET}")

                        while True:
                            genero = input(f"{BLUE}Ingrese el género del paciente (H) Hombre o (M) Mujer: {RESET}").upper().strip()
                            if genero in ["H", "M"]:
                                genero = "Hombre" if genero == "H" else "Mujer"
                                break
                            else:
                                print(f"{RED}Por favor, ingrese una de las opciones que se muestra (H o M).{RESET}")

                        while True:
                            try:
                                edad = int(input(f"{BLUE}Ingrese la edad del paciente: {RESET}"))
                                if 1 <= edad < 150:
                                    break
                                else:
                                    print(f"{RED}Por favor, ingrese una edad válida entre 1 y 149.{RESET}")
                            except ValueError:
                                print(f"{RED}Por favor, ingrese un número válido para la edad.{RESET}")

                        while True:
                            try:
                                altura = int(input(f"{BLUE}Ingrese su altura (centímetros): {RESET}"))
                                if altura >= 60:
                                    break
                                else:
                                    print(f"{RED}Por favor, ingrese una altura válida (mayor o igual a 60 cm).{RESET}")
                            except ValueError:
                                print(f"{RED}Por favor, ingrese un número válido para la altura.{RESET}")

                        while True:
                            try:
                                peso = int(input(f"{BLUE}Ingrese su peso (kilogramos): {RESET}"))
                                if peso >= 1:
                                    break
                                else:
                                    print(f"{RED}Por favor, ingrese un peso válido (mayor o igual a 1 kg).{RESET}")
                            except ValueError:
                                print(f"{RED}Por favor, ingrese un número válido para el peso.{RESET}")

                        imc = round(peso / (altura ** 2) * 10000, 1)
                        visitas = 1

                        if edad < 2:
                            categoria = "Sin categoria"
                            print(f"{RED}El IMC para niños menores de 2 años no se calcula de la misma manera.{RESET}")
                            print(f"{RED}Por favor, consulte a un profesional de la salud.{RESET}")
                            imc = "No tiene ya que es menor a dos años"
                        elif 2 <= edad < 6:
                            if imc < 14:
                                categoria = "Bajo peso"
                            elif 14 <= imc < 18:
                                categoria = "Normal"
                            elif 18 <= imc < 21:
                                categoria = "Sobrepeso"
                            else:
                                categoria = "Obesidad"
                        elif 6 <= edad < 11:
                            if imc < 13:
                                categoria = "Bajo peso"
                            elif 13 <= imc < 18:
                                categoria = "Normal"
                            elif 18 <= imc < 21:
                                categoria = "Sobrepeso"
                            else:
                                categoria = "Obesidad"
                        elif 11 <= edad < 18:
                            if imc < 15:
                                categoria = "Bajo peso"
                            elif 15 <= imc < 20:
                                categoria = "Normal"
                            elif 20 <= imc < 25:
                                categoria = "Sobrepeso"
                            else:
                                categoria = "Obesidad"
                        else:
                            if imc < 18.5:
                                categoria = "Bajo peso"
                            elif 18.5 <= imc < 25:
                                categoria = "Normal"
                            elif 25 <= imc < 30:
                                categoria = "Sobrepeso"
                            else:
                                categoria = "Obesidad"

                        print(f"IMC: {imc}")
                        print(f"Categoría: {categoria}")

                        fecha_hora_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        nuevo_paciente = {
                            "cedula": cedula,
                            "nombre": nombre,
                            "genero": genero,
                            "edad": edad,
                            "altura": [altura],
                            "peso": [peso],
                            "IMC": [imc],
                            "visitas": visitas,
                            "categoria": [categoria],
                            "fecha": [fecha_hora_registro]
                        }

                        pacientes["pacientes"].append(nuevo_paciente)
                        with open("Proyecto/pacientes.json", "w") as file:
                            json.dump(pacientes, file)

                        print(f"{GREEN}Gracias por su información. {RESET}")
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
                                        
                                            
                        
                                        if editarDato in ["edad", "altura", "peso"]:
                                            try:
                                                nuevoDato = int(nuevoDato)
                                                if editarDato == "edad" and 150 > nuevoDato > 1:
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
                                            
                                            if len(hola[editarDato]) > 0:
                                                hola[editarDato][-1] = nuevoDato
                                            else:
                                                hola[editarDato].append(nuevoDato)
                        
                                            altura = hola["altura"][-1]
                                            peso = hola["peso"][-1]
                                            imc = peso / (altura**2) * 10000
                                            imc = round(imc, 1)
                                            if len(hola["IMC"]) > 0:
                                                hola["IMC"][-1] = imc
                                            else:
                                                hola["IMC"].append(imc)
                        
                                            edad = hola["edad"]

                                            if edad < 2:
                                                print("El IMC para niños menores de 2 años no se calcula de la misma manera.")
                                                print("Por favor, consulte a un profesional de la salud.")
                                                categoria = "Sin categoría"
                                            if 2 <= edad < 6:
                                                if imc < 14:
                                                    categoria = "Bajo peso"
                                                elif 14 <= imc < 18:
                                                    categoria = "Normal"
                                                elif 18 <= imc < 21:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"
                                            elif 6 <= edad < 11:
                                                if imc < 13:
                                                    categoria = "Bajo peso"
                                                elif 13 <= imc < 18:
                                                    categoria = "Normal"
                                                elif 18 <= imc < 21:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"
                                            elif 18 > edad >= 11:
                                                if imc < 15:
                                                    categoria = "Bajo peso"
                                                elif 15 <= imc < 20:
                                                    categoria = "Normal"
                                                elif 20 <= imc < 25:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"
                                            elif edad >= 18:
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
                                            hola[editarDato] = nuevoDato
                        
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
                                                print(f"{RED}Ingrese un peso coherente. Inténtelo de nuevo.{RESET}")
                                                continue

                                            nuevaAltura = int(input("Ingrese la nueva altura del paciente (centímetros): "))
                                            if nuevaAltura < 60:
                                                print(f"{RED}Ingrese una altura coherente. Inténtelo de nuevo.{RESET}")
                                                continue

                                            if not isinstance(nuevoRegistro["altura"], list):
                                                nuevoRegistro["altura"] = [nuevoRegistro["altura"]]
                                            if nuevaAltura < nuevoRegistro["altura"][-1]:
                                                print(f"{RED}La nueva altura no puede ser menor que la última altura registrada ({nuevoRegistro['altura'][-1]} cm). Inténtelo de nuevo.{RESET}")
                                                continue

                                            if not isinstance(nuevoRegistro["peso"], list):
                                                nuevoRegistro["peso"] = [nuevoRegistro["peso"]]

                                            nuevoRegistro["altura"].append(nuevaAltura)
                                            nuevoRegistro["peso"].append(nuevoPeso)

                                            imc = nuevoPeso / (nuevaAltura ** 2) * 10000
                                            imc = round(imc, 1)

                                            if not isinstance(nuevoRegistro["IMC"], list):
                                                nuevoRegistro["IMC"] = [nuevoRegistro["IMC"]]
                                            nuevoRegistro["IMC"].append(imc)

                                            edad = nuevoRegistro["edad"]

                                            if edad < 2:
                                                print(f"{RED}El IMC para niños menores de 2 años no se calcula de la misma manera.{RESET}")
                                                print(f"{RED}Por favor, consulte a un profesional de la salud.{RESET}")
                                                categoria = "Sin categoría"
                                            elif 2 <= edad < 6:
                                                if imc < 14:
                                                    categoria = "Bajo peso"
                                                elif 14 <= imc < 18:
                                                    categoria = "Normal"
                                                elif 18 <= imc < 21:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"
                                            elif 6 <= edad < 11:
                                                if imc < 13:
                                                    categoria = "Bajo peso"
                                                elif 13 <= imc < 18:
                                                    categoria = "Normal"
                                                elif 18 <= imc < 21:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"
                                            elif 11 <= edad < 18:
                                                if imc < 15:
                                                    categoria = "Bajo peso"
                                                elif 15 <= imc < 20:
                                                    categoria = "Normal"
                                                elif 20 <= imc < 25:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"
                                            else:
                                                if imc < 18.5:
                                                    categoria = "Bajo peso"
                                                elif 18.5 <= imc < 25:
                                                    categoria = "Normal"
                                                elif 25 <= imc < 30:
                                                    categoria = "Sobrepeso"
                                                else:
                                                    categoria = "Obesidad"

                                            fecha_hora_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                                            if not isinstance(nuevoRegistro["categoria"], list):
                                                nuevoRegistro["categoria"] = [nuevoRegistro["categoria"]]
                                            nuevoRegistro["categoria"].append(categoria)

                                            if not isinstance(nuevoRegistro["fecha"], list):
                                                nuevoRegistro["fecha"] = [nuevoRegistro["fecha"]]
                                            nuevoRegistro["fecha"].append(fecha_hora_registro)

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
                                            print(f"{RED}Por favor, ingrese un valor numérico válido.{RESET}")
                                            continue
                                else:
                                    print(f"{RED}No existe ese paciente que busca.{RESET}")
                            except ValueError:
                                print(f"{RED}Por favor, ingrese un número válido.{RESET}")
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
                    elif menuPacientes == 5:
                        while True:
                            try:
                                cedulaPaciente = int(input("Ingrese la cédula del paciente para mostrar recomendaciones (o '0' para terminar): "))
                                if cedulaPaciente == 0:
                                    break
                                for paciente in pacientes["pacientes"]:
                                    if paciente["cedula"] == cedulaPaciente:
                                        
                                        categoriaPaciente = paciente["categoria"][-1] 
                                        edadPaciente = paciente["edad"]
                                        
                                        deportesCategoriaEdad = [deporte for deporte in deportes["deportes"] if deporte["categoria"] == categoriaPaciente and deporte["edad_min"] <= edadPaciente <= deporte["edad_max"]]
                                        
                                        alimentacionCategoria = [alimentacion for alimentacion in alimentaciones["alimentaciones"] if alimentacion["categoria"] == categoriaPaciente]
                                        
                                        if deportesCategoriaEdad and not alimentacionCategoria:
                                            print("{:<15} {:<15} {:<15}".format("Paciente", "Deporte", "Frecuencia"))
                                            print("-" * 45)
                                            for deporte in deportesCategoriaEdad:
                                                print("{:<15} {:<15} {:<15}".format(paciente['nombre'], deporte['nombre'], deporte['frecuencia']))
                                                
                                        elif alimentacionCategoria and not deportesCategoriaEdad:
                                            print("{:<15} {:<15} {:<15}".format("Paciente", "Alimento", "Frecuencia"))
                                            print("-" * 45)
                                            for alimentacion in alimentacionCategoria:
                                                print("{:<15} {:<15} {:<15}".format(paciente['nombre'], alimentacion['alimento'], alimentacion['frecuencia']))
                                                
                                        elif deportesCategoriaEdad and alimentacionCategoria:
                                            print("{:<15} {:<15} {:<15}".format("Paciente", "Deporte", "Frecuencia"))
                                            print("-" * 45)
                                            for deporte in deportesCategoriaEdad:
                                                print("{:<15} {:<15} {:<15}".format(paciente['nombre'], deporte['nombre'], deporte['frecuencia']))
                                            print("")
                                            print("{:<15} {:<15} {:<15}".format("Paciente","Alimento", "Frecuencia"))
                                            print("-" * 45)
                                            for alimentacion in alimentacionCategoria:
                                                print("{:<15} {:<15} {:<15}".format(paciente['nombre'], alimentacion['alimento'], alimentacion['frecuencia']))
                                                    
                                        else:
                                            print(f"El paciente {paciente['nombre']} con categoría {categoriaPaciente} no tiene recomendaciones registradas para esa categoría y edad.")        
                            except ValueError:
                                print("No deje el campo vacío")
                    elif menuPacientes == 6:
                        senti = True
                        while senti:
                            try:
                                print("Cédulas registradas con su respectivo nombre del paciente:")
                                print("{:<15} {:<30}".format("Cédula", "Nombre"))
                                print("-" * 45)
                                for paciente in pacientes["pacientes"]:
                                    print("{:<15} {:<30}".format(paciente["cedula"], paciente["nombre"]))
                                    print("-" * 45)

                                cedula = int(input("Ingrese la cédula del paciente cuyos registros desea ver (0 para salir): "))
                                if cedula == 0:
                                    break
                                else:
                                    paciente_encontrado = False
                                    for paciente in pacientes["pacientes"]:
                                        if paciente["cedula"] == cedula:
                                            paciente_encontrado = True
                                            while senti:
                                                mostrar_registros(paciente)
                                                break
                                    if not paciente_encontrado:
                                        print("Paciente no encontrado.")
                            except ValueError:
                                print("Por favor, ingrese una cédula válida.")
                    elif menuPacientes == 7:
                        print("Listado de pacientes")
                        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<30}".format(
                            "Cédula", "Nombre", "Género", "Edad", "Altura", "Peso", "IMC", "Categoría"))
                        print("-" * 120)

                        for paciente in pacientes["pacientes"]:
                            cedula = paciente["cedula"]
                            nombre = paciente["nombre"]
                            genero = paciente["genero"]
                            edad = paciente["edad"]
                            altura = paciente["altura"][-1]
                            peso = paciente["peso"][-1]
                            imc = paciente["IMC"][-1]
                            categoria = paciente["categoria"][-1]
                            fecha = paciente["fecha"][-1]
                            
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<30}".format(
                                cedula, nombre, genero, edad, altura, peso, imc, categoria, fecha))
                            print("-" * 120)
                    elif menuPacientes == 8:
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 8.")
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
                            while True:
                                nombre = input("Ingrese el nombre del deporte: ").lower().strip()
                                if nombre and all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
                                    break
                                else:
                                    print("Por favor, ingrese un nombre válido sin dejar el campo vacío.")
                                    
                            while True:
                                frecuencia = input("Ingrese la frecuencia que debe realizar: ").strip()
                                if frecuencia:
                                    break
                                else:
                                    print("Por favor, no deje este campo vacío.")
                                    
                            while True:
                                try:
                                    edad_min = int(input("Ingrese la edad mínima recomendada para este deporte: ").strip())
                                    if 1 <= edad_min <= 150:
                                        break
                                    else:
                                        print("Por favor, ingrese una edad válida entre 1 y 150.")
                                except ValueError:
                                    print("Por favor, ingrese un número válido para la edad mínima.")

                            while True:
                                try:
                                    edad_max = int(input("Ingrese la edad máxima recomendada para este deporte: ").strip())
                                    if 1 <= edad_max <= 150 and edad_max >= edad_min:
                                        break
                                    else:
                                        print("Por favor, ingrese una edad válida entre 1 y 150 que sea mayor o igual a la edad mínima.")
                                except ValueError:
                                    print("Por favor, ingrese un número válido para la edad máxima.")
                                    
                            while True:
                                categoria = input("Ingrese la categoría que lo tiene que hacer (Bajo peso, Normal, Sobrepeso, Obesidad): ").capitalize().strip()
                                if categoria in ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]:
                                    break
                                else:
                                    print("Por favor, ingrese una categoría válida (Bajo peso, Normal, Sobrepeso, Obesidad).")

                            nuevoDeporte = {
                                "nombre": nombre,
                                "frecuencia": frecuencia,
                                "edad_min": edad_min,
                                "edad_max": edad_max,
                                "categoria": categoria
                            }

                            deportes["deportes"].append(nuevoDeporte)
                            with open("Proyecto/deportes.json", "w") as file:
                                json.dump(deportes, file)

                            print("Gracias por su información")
                            sentin = False
                    elif menuDeportes == 2:
                        senti = True
                        while senti:
                            print("Deportes disponibles:")
                            for deporte in deportes["deportes"]:
                                print(deporte["nombre"])

                            editDeport = input("Ingrese el nombre del deporte que va a editar: ")
                            edit_true = False
                            for deporte in deportes["deportes"]:
                                if deporte["nombre"] == editDeport:
                                    hola = deporte
                                    edit_true = True
                            if edit_true:
                                for k, v in hola.items():
                                    print(f"{k}: {v}")
                                    
                                while senti:
                                    editarDato = input("¿Qué campo desea cambiar? (nombre, frecuencia, categoria, edad_min, edad_max): ").lower()
                                    if editarDato not in hola:
                                        print("Campo inválido. Por favor, seleccione un campo válido.")
                                        continue
                                    
                                    if editarDato in ["categoria"]:
                                        while True:
                                            nuevoDato = input("Ingrese el nuevo valor para categoria (Bajo peso, Normal, Sobrepeso, Obesidad): ").capitalize()
                                            if nuevoDato in ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]:
                                                break
                                            else:
                                                print("Categoría inválida. Por favor, ingrese una de las opciones válidas.")
                                    elif editarDato in ["edad_min", "edad_max"]:
                                        while True:
                                            try:
                                                nuevoDato = int(input(f"Ingrese el nuevo valor para {editarDato}: "))
                                                if 1 <= nuevoDato <= 150:
                                                    break
                                                else:
                                                    print("Edad inválida. Por favor, ingrese un valor entre 1 y 150.")
                                            except ValueError:
                                                print("Entrada inválida. Por favor, ingrese un número.")
                                    else:
                                        nuevoDato = input(f"Ingrese el nuevo valor para {editarDato}: ")

                                    hola[editarDato] = nuevoDato

                                    with open("Proyecto/deportes.json", "w") as file:
                                        json.dump(deportes, file)
                                    
                                    print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                    senti = False
                            else:
                                print("No existe el deporte que busca")
                    elif menuDeportes == 3:
                        while True:
                            print("Deportes disponibles:")
                            for deporte in deportes["deportes"]:
                                print(deporte["nombre"])

                            deleteDeport = input("Ingrese el nombre del deporte que desea eliminar (o 'salir' para terminar): ")
                            
                            if deleteDeport.lower() == "salir":
                                break

                            delete_true = False

                            for deporte in deportes["deportes"]:
                                if deporte["nombre"].lower() == deleteDeport.lower():
                                    deportes["deportes"].remove(deporte)
                                    delete_true = True
                                    break

                            if delete_true:
                                with open("Proyecto/deportes.json", "w") as file:
                                    json.dump(deportes, file, indent=4)

                                print(f"El deporte '{deleteDeport}' ha sido eliminado.")
                            else:
                                print("No existe el deporte que busca.")
                            print("eliminar")
                    elif menuDeportes == 4:

                        # Crear y mostrar la tabla
                        print("+----+-------------+--------------------+-------------+")
                        print("| ID |   Nombre    |     Frecuencia     |  Categoria  |")
                        print("+----+-------------+--------------------+-------------+")

                        for i, deporte in enumerate(deportes["deportes"]):
                            nombre = aplicar_color(deporte["categoria"], deporte["nombre"])
                            frecuencia = aplicar_color(deporte["categoria"], deporte["frecuencia"])
                            categoria = aplicar_color(deporte["categoria"], deporte["categoria"])
                            print(f"| {i:2} | {nombre:20} | {frecuencia:27} | {categoria:20} |")

                        print("+----+-------------+--------------------+-------------+")
                    elif menuDeportes == 5:
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
                except ValueError:
                    print("Ingrese solo numeros")
        elif op == 3:
            sentin = True
            while True:
                print("Que decea realizar: \n 1.Registrar nueva Alimentacion \n 2.Editar Info de un Alimentacion \n 3.Eliminar Alimentacion \n 4.Mostrar los Alimentacion registrados \n 5.Volver al menu anterios")
                try:
                    menuAlimentacion = int(input("Ingrese una opcion: "))
                    if menuAlimentacion == 1:
                        while sentin:
                            alimento = input("ingrese la categoria del alimento (Granos, Verduras, Frutas, Lacteos, Proteinas): ")
                            if alimento == "Granos" or alimento == "Verduras" or alimento == "Frutas" or alimento == "Lacteos" or alimento == "Proteinas":
                                while sentin:
                                    frecuencia = input("ingrese la frecuencia que debe comer esa clase de alimento: ")
                                    while sentin:
                                        try:
                                            categoria = input("ingrese la categiria que lo tiene que hacer (Bajo peso, Normal, Sobrepeso, Obesidad): ")
                                            if categoria == "Bajo peso" or categoria == "Normal" or categoria == "Sobrepeso" or categoria == "Obesidad":
                                                nuevaAlimentacion = {
                                                    "alimento": alimento,
                                                    "frecuencia": frecuencia,
                                                    "categoria": categoria
                                                }
                                                alimentaciones["alimentaciones"].append(nuevaAlimentacion)
                                                with open("Proyecto/alimentaciones.json", "w") as file:
                                                    json.dump(alimentaciones, file)
                                                print("Gracias por su informacion")
                                                sentin = False
                                            else:
                                                print("Por favor, ingrese lo que le pide.")
                                        except ValueError:
                                            print("Por favor, ingrese lo que le pide.")
                                    break
                            else:
                                print("Por favor, ingrese lo que le pide.")
                    elif menuAlimentacion == 2:
                        senti = True
                        while senti:
                            print("Alimentacion disponibles:")
                            for alimentacion in alimentaciones["alimentaciones"]:
                                print(alimentacion["alimento"])

                            editAlimento = input("Ingrese el nombre del alimento que va a editar: ")
                            edit_true = False
                            for alimentacion in alimentaciones["alimentaciones"]:
                                if alimentacion["alimento"] == editAlimento:
                                        hola = alimentacion
                                        edit_true = True
                            if edit_true:
                                    for k, v in hola.items():
                                        print(f"{k}: {v}")
                                        
                                    while senti:
                                        editarDato = input("¿Qué campo desea cambiar? (alimento, frecuencia, categoria): ").lower()
                                        if editarDato not in hola:
                                            print("Campo inválido. Por favor, seleccione un campo válido.")
                                            continue
                                        
                                        if editarDato in ["categoria"]:
                                            while True:
                                                nuevoDato = input("Ingrese el nuevo valor para categoria (Bajo peso, Normal, Sobrepeso, Obesidad): ").capitalize()
                                                if nuevoDato in ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]:
                                                    break
                                                else:
                                                    print("Categoría inválida. Por favor, ingrese una de las opciones válidas.")
                                        else:
                                            nuevoDato = input(f"Ingrese el nuevo valor para {editarDato}: ")

                                        hola[editarDato] = nuevoDato
                        
                                        with open("Proyecto/alimentaciones.json", "w") as file:
                                            json.dump(alimentaciones, file)
                        
                                        print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                        senti = False
                            else:
                                print("No existe el alimento que busca")
                    elif menuAlimentacion == 3:
                        while True:
                            print("Alimentos disponibles:")
                            for alimentacion in alimentaciones["alimentaciones"]:
                                print(alimentacion["alimento"])

                            deleteAlimenta = input("Ingrese el nombre del alimento que desea eliminar (o 'salir' para terminar): ")
                            
                            if deleteAlimenta.lower() == "salir":
                                break

                            delete_true = False

                            for alimentacion in alimentaciones["alimentaciones"]:
                                if alimentacion["alimento"].lower() == deleteAlimenta.lower():
                                    alimentaciones["alimentaciones"].remove(alimentacion)
                                    delete_true = True
                                    break

                            if delete_true:
                                with open("Proyecto/alimentaciones.json", "w") as file:
                                    json.dump(alimentaciones, file, indent=4)

                                print(f"El deporte '{deleteAlimenta}' ha sido eliminado.")
                            else:
                                print("No existe el alimento que busca.")
                            print("eliminar")
                    elif menuAlimentacion == 4:
                        # Crear y mostrar la tabla
                        print("+----+-------------+--------------------+-------------+")
                        print("| ID |   Alimento  |     Frecuencia     |  Categoria  |")
                        print("+----+-------------+--------------------+-------------+")

                        for i, alimentacion in enumerate(alimentaciones["alimentaciones"]):
                            alimento = aplicar_color(alimentacion["categoria"], alimentacion["alimento"])
                            frecuencia = aplicar_color(alimentacion["categoria"], alimentacion["frecuencia"])
                            categoria = aplicar_color(alimentacion["categoria"], alimentacion["categoria"])
                            print(f"| {i:2} | {alimento:20} | {frecuencia:27} | {categoria:20} |")

                        print("+----+-------------+--------------------+-------------+")
                    elif menuAlimentacion == 5:
                        break
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
                except ValueError:
                    print("Ingrese solo numeros")
        elif op == 0:
            print("\n¡Estos fueron los creadores del programa! Muchas gracias por su atención.")
            print("+----+-------------+----------------+")
            print(f"{GREEN}SEPULVEDA ROJAS JUAN DAVID{RESET}")
            print(f"{GREEN}AREVALO GUERRERO ANGEL GIOVANNY{RESET}")
            print("+----+-------------+----------------+")
            print(f"{YELLOW}CARREÑO BARAJAS CRISTIAN CAMILO{RESET}")

            # Mensaje de agradecimiento y mención a los creadores
            break
        else:
            print("Opción no válida. Por favor, ingrese 0 o 4.")
    except ValueError:
        print("Por favor, ingrese solo números.")