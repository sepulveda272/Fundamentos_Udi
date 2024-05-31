# LIBRERIA

import json  
from datetime import datetime

# DICCIONARIOS

with open("Pacientes.json", "r") as file:
    pacientes = json.load(file)
    
with open("Deportes.json", "r") as file:
    deportes = json.load(file)
    
with open("Alimentaciones.json", "r") as file:
    alimentaciones = json.load(file)

# FUNCIONES

# 1. SIN PARAMETROS Y SIN RETORNAR
# 2. CON PARAMETROS Y SIN RETORNAR
# 3. SIN PARAMETROS Y CON RETORNAR
# 4. COM PARAMETROS Y CON RETORNAR

def mostrar_registros(paciente):
    print("Registros actuales:")
    for i in range(len(paciente["altura"])):
        print(f"{i + 1}: Altura: {paciente['altura'][i]}, Peso: {paciente['peso'][i]}, IMC: {paciente['imc'][i]}, Categoría: {paciente['categoria'][i]}, Fecha: {paciente['fecha'][i]}.")

def eliminar_registro(paciente, indice):
    if len(paciente["altura"]) > 1:
        paciente["altura"].pop(indice)
        paciente["peso"].pop(indice)
        paciente["imc"].pop(indice)
        paciente["categoria"].pop(indice)
        paciente["fecha"].pop(indice)
        return True
    else:
        print("No se puede eliminar el último registro. ")
        return False

def buscar_paciente(pacientes, cedula):
    for paciente in pacientes["pacientes"]:
        if paciente["cedula"] == cedula:
            return paciente
    return None

# AUTENTICACION

""" while True:
    usuario=input("ingrese el usuario")
    contraseña=input("ingrese la contraseña")
    if usuario == "Nikoll" and contraseña == "123456":
        break
    else:
        print("chao") """

while True:
    try:
        print ("Buenos dias que decea hacer: \n 1.pacientes \n 2.deportes \n 3.alimentos \n 0. salir")
        o= int(input("Ingrese una opcion: "))
        if o==1:
            while True:
                try:
                    print("Que desea realizar: \n 1.Registrar Paciente \n 2.Editar Paciente \n 3.Registar nueva visita \n 4.Eliminar registros\n 5.Mostrar recomendaciones para un paciente \n 6.Mostrar registros de un paciente \n 7.Listado de pacientes \n 8.Volver al menu anterios")
                    opPaciente = int(input("ingrese una opcion: "))
                    if opPaciente == 1:
                        while True:
                            try:
                                cedula = int(input("Ingrese la identificación del paciente: "))
                                if cedula >= 1:
                                    cedula = str(cedula)
                                    if len(cedula) >= 8 and len(cedula) <= 10:
                                        cedula = int(cedula)
                                        cedula_existente = any(paciente["cedula"] == cedula for paciente in pacientes["pacientes"])
                                        if cedula_existente:
                                            print("La cédula ya existe")
                                        else:
                                            break
                                    else:
                                        print("chao")
                                else:
                                    print("nada de negativos pa")
                            except ValueError:
                                print("ingrese opcion correcta")
                        while True:
                            nombre = input("nombre")
                            if nombre and all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
                                break
                            else:
                                print("nose")
                        while True:
                            try:
                                edad=int(input("edad"))
                                if edad>=0 and edad<=150:
                                    print(edad)
                                    break
                                else:
                                    print("ingrese una edad valida")
                            except ValueError:
                                print("hagalo de nuevo pa")

                        while True:
                            genero= input("Ingrese el género del paciente (H) Hombre o (M) Mujer: ").upper()
                            if genero == "H":
                                genero = "Hombre"
                                break
                            elif genero == "M":
                                genero = "Mujer"
                                break
                            else:
                                print("ESCOJA")

                        while True:
                            try:
                                altura = int(input("Ingrese su altura (centímetros): "))
                                if altura >= 60 and altura<=260:
                                    break
                                else:
                                    print("Por favor, ingrese una altura válida (mayor o igual a 60 cm).")
                            except ValueError:
                                print("Por favor, ingrese un número válido para la altura.")

                        while True:
                            try:
                                peso = int(input("Ingrese su peso (kilogramos): "))
                                if peso >= 1 and peso <= 595:
                                    break
                                else:
                                    print("Por favor, ingrese un peso válido (mayor o igual a 1 kg).")
                            except ValueError:
                                print("Por favor, ingrese un número válido para el peso.")
                                
                        imc = round(peso / (altura ** 2) * 10000, 1)
                        visitas = 1
                        
                        if edad < 2:
                            categoria = "Sin categoria"
                            print("El IMC para niños menores de 2 años no se calcula de la misma manera.")
                            print("Por favor, consulte a un profesional de la salud.")
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
                        
                        nuevo = {
                            "cedula": cedula,
                            "nombre": nombre,
                            "edad": edad,
                            "genero": genero,
                            "altura": [altura],
                            "peso": [peso],
                            "imc": [imc],
                            "categoria": [categoria],
                            "visitas": visitas,
                            "fecha": [fecha_hora_registro]
                        }
                        pacientes["pacientes"].append(nuevo)
                        with open("Pacientes.json", "w") as file:
                            json.dump(pacientes, file)
                        print("gracias")
                    elif opPaciente == 2:
                        sen = True
                        while sen:
                            try:
                                edit = int(input("Ingrese la cedula del paciente que desea editar: "))
                                paciente_encontrado = buscar_paciente(pacientes, edit)
                                if paciente_encontrado:
                                    for k, v in paciente_encontrado.items():
                                        print(f"{k}: {v}")
                                    while sen:
                                        editarDato = input("¿Qué campo desea cambiar? (nombre, genero, edad, altura, peso): ").lower()
                                        if editarDato not in paciente_encontrado:
                                            print("Campo inválido. Por favor, seleccione un campo válido.")
                                        else:
                                            nuevoDato = input(f"Ingrese el nuevo valor para {editarDato}: ")

                                            if editarDato == "nombre":
                                                if not nuevoDato.replace(" ", "").isalpha():
                                                    print("El nombre solo puede contener letras y espacios. Inténtelo de nuevo.")
                                                    continue

                                            if editarDato in ["edad", "altura", "peso"]:
                                                if not nuevoDato.isdigit():
                                                    print("Por favor, ingrese solo números.")
                                                    continue
                                                nuevoDato = int(nuevoDato)
                                                if editarDato == "edad":
                                                    if not 1 <= nuevoDato <= 150:
                                                        print("La edad debe estar entre 1 y 150 años. Inténtelo de nuevo.")
                                                        continue
                                                elif editarDato == "altura":
                                                    if not 60 <= nuevoDato <= 260:
                                                        print("La altura debe estar entre 60 y 260 cm. Inténtelo de nuevo.")
                                                        continue
                                                elif editarDato == "peso":
                                                    if not 2 <= nuevoDato <= 595:
                                                        print("El peso debe estar entre 2 y 595 kg. Inténtelo de nuevo.")
                                                        continue
                                                
                                            if editarDato in ["altura", "peso"]:
                                                
                                                if len(paciente_encontrado[editarDato]) > 0:
                                                    paciente_encontrado[editarDato][-1] = nuevoDato
                                                else:
                                                    paciente_encontrado[editarDato].append(nuevoDato)
                            
                                                altura = paciente_encontrado["altura"][-1]
                                                peso = paciente_encontrado["peso"][-1]
                                                imc = peso / (altura**2) * 10000
                                                imc = round(imc, 1)
                                                if len(paciente_encontrado["imc"]) > 0:
                                                    paciente_encontrado["imc"][-1] = imc
                                                else:
                                                    paciente_encontrado["imc"].append(imc)
                            
                                                edad = paciente_encontrado["edad"]

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
                            
                                                if len(paciente_encontrado["categoria"]) > 0:
                                                    paciente_encontrado["categoria"][-1] = categoria
                                                else:
                                                    paciente_encontrado["categoria"].append(categoria)
                                            else:
                                                paciente_encontrado[editarDato] = nuevoDato
                            
                                            with open("Pacientes.json", "w") as file:
                                                json.dump(pacientes, file)
                            
                                            print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                            sen = False
                                else:
                                        print("No existe ese paciente que busca")    
                            except ValueError:
                                print("ingrese de nuevo.")
                    elif opPaciente==3:
                        senti = True
                        while senti:
                            try:
                                edit = int(input("Ingrese la cédula del paciente que desea registrar la nueva visita: "))
                                nuevoRegistro = buscar_paciente(pacientes, edit)

                                if nuevoRegistro:
                                    print("Paciente encontrado:")
                                    for k, v in nuevoRegistro.items():
                                        print(f"{k}: {v}")

                                    while senti:
                                        try:
                                            nuevoPeso = int(input("Ingrese el nuevo peso del paciente (kilogramos): "))
                                            if nuevoPeso < 2 or nuevoPeso > 595:
                                                print("Ingrese un peso entre 2 y 595 kg. Inténtelo de nuevo.")
                                                continue

                                            nuevaAltura = int(input("Ingrese la nueva altura del paciente (centímetros): "))
                                            if nuevaAltura < 60 or nuevaAltura > 260:
                                                print("Ingrese una altura entre 60 y 260 cm. Inténtelo de nuevo.")
                                                continue

                                            if not isinstance(nuevoRegistro["altura"], list):
                                                nuevoRegistro["altura"] = [nuevoRegistro["altura"]]

                                            if not isinstance(nuevoRegistro["peso"], list):
                                                nuevoRegistro["peso"] = [nuevoRegistro["peso"]]

                                            nuevoRegistro["altura"].append(nuevaAltura)
                                            nuevoRegistro["peso"].append(nuevoPeso)

                                            imc = nuevoPeso / (nuevaAltura ** 2) * 10000
                                            imc = round(imc, 1)

                                            if not isinstance(nuevoRegistro["imc"], list):
                                                nuevoRegistro["imc"] = [nuevoRegistro["imc"]]
                                            nuevoRegistro["imc"].append(imc)

                                            edad = nuevoRegistro["edad"]

                                            if edad < 2:
                                                print("El IMC para niños menores de 2 años no se calcula de la misma manera.")
                                                print("Por favor, consulte a un profesional de la salud.")
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

                                            with open("Pacientes.json", "w") as file:
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
                    elif opPaciente==4:
                        senti = True
                        while senti:
                            try:
                                cedula = int(input("Ingrese la cédula del paciente cuyos registros desea eliminar: "))
                                paciente = buscar_paciente(pacientes, cedula)
                                
                                if paciente:
                                    while senti:
                                        mostrar_registros(paciente)
                                        try:
                                            seleccion = int(input("Ingrese el número del registro que desea eliminar (0 para salir): "))
                                            if seleccion == 0:
                                                senti = False
                                            elif 1 <= seleccion <= len(paciente["altura"]):
                                                if eliminar_registro(paciente, seleccion - 1):
                                                    with open("Pacientes.json", "w") as file:
                                                        json.dump(pacientes, file, indent=4)
                                                    print("Registro eliminado exitosamente.")
                                                else:
                                                    print("Error al eliminar el registro.")
                                            else:
                                                print("Selección no válida.")
                                        except ValueError:
                                            print("Por favor, ingrese un número válido.")
                                else:
                                    print("Paciente no encontrado.")
                            except ValueError:
                                print("Por favor, ingrese una cédula válida.")
                    elif opPaciente ==5:
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
                    elif opPaciente==6:
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
                    elif opPaciente==7:
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
                            imc = paciente["imc"][-1]
                            categoria = paciente["categoria"][-1]
                            fecha = paciente["fecha"][-1]
                            
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<30}".format(
                                cedula, nombre, genero, edad, altura, peso, imc, categoria, fecha))
                            print("-" * 120)
                    elif opPaciente==8:
                        break
                    else:
                        print("ingrese opcion correcta")
                except ValueError:
                    print ("ingrese opcion correcta")
        elif o==2:
            while True:
                print("Qué desea realizar: \n 1.Registrar nuevo Deporte \n 2.Editar Información de un Deporte \n 3.Eliminar Deporte \n 4.Mostrar los Deportes registrados \n 5.Volver al menú anterior")
                try:
                    menuDeportes = int(input("Ingrese una opción: "))
                    
                    if menuDeportes == 1:
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
                        with open("Deportes.json", "w") as file:
                            json.dump(deportes, file, indent=4)

                        print("Gracias por su información")
                        break

                    elif menuDeportes == 2:
                        while True:
                            print("Deportes disponibles:")
                            for deporte in deportes["deportes"]:
                                print(deporte["nombre"])

                            editDeport = input("Ingrese el nombre del deporte que va a editar: ").lower().strip()
                            edit_true = False
                            for deporte in deportes["deportes"]:
                                if deporte["nombre"].lower() == editDeport:
                                    edit_true = True
                                    break

                            if edit_true:
                                for k, v in deporte.items():
                                    print(f"{k}: {v}")

                                while True:
                                    editarDato = input("¿Qué campo desea cambiar? (nombre, frecuencia, categoria, edad_min, edad_max): ").lower().strip()
                                    if editarDato not in deporte:
                                        print("Campo inválido. Por favor, seleccione un campo válido.")
                                        continue
                                    
                                    if editarDato == "categoria":
                                        while True:
                                            nuevoDato = input("Ingrese el nuevo valor para categoría (Bajo peso, Normal, Sobrepeso, Obesidad): ").capitalize().strip()
                                            if nuevoDato in ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]:
                                                break
                                            else:
                                                print("Categoría inválida. Por favor, ingrese una de las opciones válidas.")
                                    elif editarDato in ["edad_min", "edad_max"]:
                                        while True:
                                            try:
                                                nuevoDato = int(input(f"Ingrese el nuevo valor para {editarDato}: ").strip())
                                                if 1 <= nuevoDato <= 150:
                                                    break
                                                else:
                                                    print("Edad inválida. Por favor, ingrese un valor entre 1 y 150.")
                                            except ValueError:
                                                print("Entrada inválida. Por favor, ingrese un número.")
                                    else:
                                        nuevoDato = input(f"Ingrese el nuevo valor para {editarDato}: ").strip()

                                    deporte[editarDato] = nuevoDato

                                    with open("Deportes.json", "w") as file:
                                        json.dump(deportes, file, indent=4)
                                    
                                    print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                    break
                            else:
                                print("No existe el deporte que busca.")
                            break

                    elif menuDeportes == 3:
                        while True:
                            print("Deportes disponibles:")
                            for deporte in deportes["deportes"]:
                                print(deporte["nombre"])

                            deleteDeport = input("Ingrese el nombre del deporte que desea eliminar (o 'salir' para terminar): ").lower().strip()
                            
                            if deleteDeport == "salir":
                                break

                            delete_true = False

                            for deporte in deportes["deportes"]:
                                if deporte["nombre"].lower() == deleteDeport:
                                    deportes["deportes"].remove(deporte)
                                    delete_true = True
                                    break

                            if delete_true:
                                with open("Deportes.json", "w") as file:
                                    json.dump(deportes, file, indent=4)

                                print(f"El deporte '{deleteDeport}' ha sido eliminado.")
                            else:
                                print("No existe el deporte que busca.")
                            break
                    elif menuDeportes == 4:
                        print("+----+-------------+--------------------+-------------+")
                        print("| ID |   Nombre    |     Frecuencia     |  Categoria  |")
                        print("+----+-------------+--------------------+-------------+")

                        for i, deporte in enumerate(deportes["deportes"]):
                            nombre = deporte["nombre"]
                            frecuencia = deporte["frecuencia"]
                            categoria = deporte["categoria"]
                            print(f"| {i:2} | {nombre:11} | {frecuencia:18} | {categoria:11} |")

                        print("+----+-------------+--------------------+-------------+")
                        
                    elif menuDeportes == 5:
                        break
                    
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
                    
                except ValueError:
                    print("Ingrese solo números.")
        elif o==3:
            while True:
                print("Qué desea realizar: \n 1.Registrar nueva Alimentación \n 2.Editar Información de una Alimentación \n 3.Eliminar Alimentación \n 4.Mostrar las Alimentaciones registradas \n 5.Volver al menú anterior")
                try:
                    menuAlimentacion = int(input("Ingrese una opción: "))
                    
                    if menuAlimentacion == 1:
                        while True:
                            alimento = input("Ingrese la categoría del alimento (Granos, Verduras, Frutas, Lácteos, Proteínas): ")
                            if alimento in ["Granos", "Verduras", "Frutas", "Lácteos", "Proteínas"]:
                                frecuencia = input("Ingrese la frecuencia que debe comer esa clase de alimento: ")
                                while True:
                                    categoria = input("Ingrese la categoría que lo tiene que hacer (Bajo peso, Normal, Sobrepeso, Obesidad): ")
                                    if categoria in ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]:
                                        nuevaAlimentacion = {
                                            "alimento": alimento,
                                            "frecuencia": frecuencia,
                                            "categoria": categoria
                                        }
                                        alimentaciones["alimentaciones"].append(nuevaAlimentacion)
                                        with open("Alimentaciones.json", "w") as file:
                                            json.dump(alimentaciones, file, indent=4)
                                        print("Gracias por su información.")
                                        break
                                    else:
                                        print("Categoría inválida. Por favor, ingrese una de las opciones válidas.")
                                break
                            else:
                                print("Categoría de alimento inválida. Por favor, ingrese una opción válida.")
                                
                    elif menuAlimentacion == 2:
                        while True:
                            print("Alimentaciones disponibles:")
                            for alimentacion in alimentaciones["alimentaciones"]:
                                print(alimentacion["alimento"])

                            editAlimento = input("Ingrese el nombre del alimento que va a editar: ")
                            edit_true = False
                            for alimentacion in alimentaciones["alimentaciones"]:
                                if alimentacion["alimento"].lower() == editAlimento.lower():
                                    edit_true = True
                                    break

                            if edit_true:
                                for k, v in alimentacion.items():
                                    print(f"{k}: {v}")

                                while True:
                                    editarDato = input("¿Qué campo desea cambiar? (alimento, frecuencia, categoria): ").lower()
                                    if editarDato not in alimentacion:
                                        print("Campo inválido. Por favor, seleccione un campo válido.")
                                        continue

                                    if editarDato == "categoria":
                                        while True:
                                            nuevoDato = input("Ingrese el nuevo valor para categoría (Bajo peso, Normal, Sobrepeso, Obesidad): ").capitalize()
                                            if nuevoDato in ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]:
                                                break
                                            else:
                                                print("Categoría inválida. Por favor, ingrese una de las opciones válidas.")
                                    else:
                                        nuevoDato = input(f"Ingrese el nuevo valor para {editarDato}: ")

                                    alimentacion[editarDato] = nuevoDato

                                    with open("Alimentaciones.json", "w") as file:
                                        json.dump(alimentaciones, file, indent=4)

                                    print(f"El campo {editarDato} ha sido actualizado a {nuevoDato}.")
                                    break
                                break
                            else:
                                print("No existe el alimento que busca.")
                                
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
                                with open("Alimentaciones.json", "w") as file:
                                    json.dump(alimentaciones, file, indent=4)

                                print(f"El alimento '{deleteAlimenta}' ha sido eliminado.")
                            else:
                                print("No existe el alimento que busca.")
                                
                    elif menuAlimentacion == 4:
                        print("+----+-------------+--------------------+-------------+")
                        print("| ID |   Alimento  |     Frecuencia     |  Categoria  |")
                        print("+----+-------------+--------------------+-------------+")

                        for i, alimentacion in enumerate(alimentaciones["alimentaciones"]):
                            alimento = alimentacion["alimento"]
                            frecuencia = alimentacion["frecuencia"]
                            categoria = alimentacion["categoria"]
                            print(f"| {i:2} | {alimento:11} | {frecuencia:18} | {categoria:11} |")

                        print("+----+-------------+--------------------+-------------+")
                        
                    elif menuAlimentacion == 5:
                        break
                        
                    else:
                        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
                        
                except ValueError:
                    print("Ingrese solo números.")
        elif o==0:
            print ("SALIR")
            break
        else:
            print ("ingrese opcion correcta")
    except ValueError:
        print("ingrese opcion correcta")