import re

def registrar_cliente(datos):
    print("\n--- REGISTRO DE CLIENTE ---")
    
    while True:
        doc = input("Documento de identidad (Único, solo números entre 6 y 12 dígitos): ").strip()
        if not doc.isdigit():
            print(" Error: El documento debe contener únicamente números.")
        elif not (6 <= len(doc) <= 12):
            print(" Error: El documento debe tener entre 6 y 12 caracteres.")
        else:
            break

    if doc in datos["clientes"]:
        print(" Error: Ya existe un cliente registrado con este documento.")
        return
    
    nombre = input("Nombre completo: ").strip()
    tipo_vehiculo = input("Tipo de vehículo de interés (moto/carro): ").strip().lower()
    if tipo_vehiculo not in ["moto", "carro"]:
        print(" Tipo de vehículo inválido. Debe ser 'moto' o 'carro'.")
        return

    datos["clientes"][doc] = {
        "nombre": nombre,
        "tipo_vehiculo": tipo_vehiculo
    }
    print(f" Cliente {nombre} registrado con éxito.")

def registrar_instructor(datos):
    print("\n--- REGISTRO DE INSTRUCTOR ---")
    
    while True:
        doc = input("Documento de identidad (Único, solo números entre 6 y 12 dígitos): ").strip()
        if not doc.isdigit():
            print(" Error: El documento debe contener únicamente números.")
        elif not (6 <= len(doc) <= 12):
            print(" Error: El documento debe tener entre 6 y 12 caracteres.")
        else:
            break

    if doc in datos["instructores"]:
        print(" Error: Ya existe un instructor con este documento.")
        return
    
    nombre = input("Nombre completo: ").strip()
    especialidad = input("Especialidad (moto/carro): ").strip().lower()
    
    if especialidad not in ["moto", "carro"]:
        print(" Especialidad inválida. Debe ser 'moto' o 'carro'.")
        return

    datos["instructores"][doc] = {
        "nombre": nombre,
        "especialidad": especialidad
    }
    print(f" Instructor {nombre} registrado con éxito.")

def registrar_vehiculo(datos):
    print("\n--- REGISTRO DE VEHÍCULO ---")
    
    # Patrón: Exactamente 3 letras mayúsculas seguidas de 3 números
    patron_placa = r"^[A-Z]{3}[0-9]{3}$"
    
    while True:
        placa = input("Placa del vehículo (Ejemplo: HAX189): ").strip().upper()
        
        if not re.match(patron_placa, placa):
            print(" Error: Formato de placa inválido. Debe tener 3 letras seguidas de 3 números (Ej: HAX189).")
        elif placa in datos["vehiculos"]:
            print(" Error: Ya existe un vehículo registrado con esta placa.")
            return
        else:
            break
    
    tipo = input("Tipo de vehículo (moto/carro): ").strip().lower()
    if tipo not in ["moto", "carro"]:
        print(" Tipo inválido. Debe ser 'moto' o 'carro'.")
        return
    
    datos["vehiculos"][placa] = {
        "tipo": tipo,
        "disponible": True
    }
    print(f" Vehículo con placa {placa} registrado con éxito.")