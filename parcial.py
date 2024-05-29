import json
from datetime import datetime

with open("Pacientes.json", "r") as file:
    pacientes = json.load(file)

""" while True:
    usuario=input("ingrese el usuario")
    contraseña=input("ingrese la contraseña")
    if usuario == "Nikoll" and contraseña == "123456":
        break
    else:
        print("chao") """

while True:
    try:
        print ("Buenos dias que decea hacer: \n 1.pacientes \n 2.deportes \n 3.enfermedades \n 4.alimentos \n 0. salir")
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
                                edit_true = False
                                for paciente in pacientes["pacientes"]:
                                    if paciente["cedula"] == edit:
                                        hola = paciente
                                        edit_true = True
                                if edit_true:
                                    for k, v in hola.items():
                                        print(f"{k}: {v}")
                                    while sen:
                                        editarDato = input("¿Qué campo desea cambiar? (nombre, genero, edad, altura, peso): ").lower()
                                        if editarDato not in hola:
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
                                                
                                                if len(hola[editarDato]) > 0:
                                                    hola[editarDato][-1] = nuevoDato
                                                else:
                                                    hola[editarDato].append(nuevoDato)
                            
                                                altura = hola["altura"][-1]
                                                peso = hola["peso"][-1]
                                                imc = peso / (altura**2) * 10000
                                                imc = round(imc, 1)
                                                if len(hola["imc"]) > 0:
                                                    hola["imc"][-1] = imc
                                                else:
                                                    hola["imc"].append(imc)
                            
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
                                            if nuevoPeso >= 1 and nuevoPeso <= 595:
                                                print("Ingrese un peso coherente. Inténtelo de nuevo.")
                                                continue

                                            nuevaAltura = int(input("Ingrese la nueva altura del paciente (centímetros): "))
                                            if nuevaAltura >= 60 and nuevaAltura<=260:
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
                        print("eliminar registro")
                    elif opPaciente ==5:
                        print ("mostrar recomendaciones")
                    elif opPaciente==6:
                        print ("mortrar registro de pacientes")
                    elif opPaciente==7:
                        print("listado de pacientes")
                    elif opPaciente==8:
                        print ("volver")
                        break
                    else:
                        print("ingrese opcion correcta")
                except ValueError:
                    print ("ingrese opcion correcta")
        elif o==2:
            print("deportes") 
        elif o==3:
            print("enfermedades")
        elif o==4:
            print ("alimentos")
        elif o==0:
            print ("SALIR")
            break
        else:
            print ("ingrese opcion correcta")
    except ValueError:
        print("ingrese opcion correcta")
        
