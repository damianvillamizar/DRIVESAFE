def registrar_cliente(datos):
    print("\n--- REGISTRO DE CLIENTE ---")
    doc = input("Documento de identidad (Único): ").strip()
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
    doc = input("Documento de identidad (Único): ").strip()
    if doc in datos["instructores"]:
        print(" Error: Ya existe un instructor con este documento.")
        return
    
    nombre = input("Nombre completo: ").strip()
    especialidad = input("Especialidad (moto/carro): ").strip().lower()
    
    # Validación corregida de 'especialidad'
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
    placa = input("Placa del vehículo (Única): ").strip().upper()
    if placa in datos["vehiculos"]:
        print(" Error: Ya existe un vehículo con esta placa.")
        return
    
    tipo = input("Tipo de vehículo (moto/carro): ").strip().lower()
    if tipo not in ["moto", "carro"]:
        print(" Tipo inválido. Debe ser 'moto' o 'carro'.")
        return
    
    datos["vehiculos"][placa] = {
        "tipo": tipo,
        "disponible": True
    }
    print(f" Vehículo con placa {placa} registrado con éxito.")