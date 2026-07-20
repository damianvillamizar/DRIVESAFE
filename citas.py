from datetime import datetime

def programar_cita(datos):
    print("\n--- PROGRAMAR CITA DE PRÁCTICA ---")
    
    doc_cliente = input("Documento del Cliente: ").strip()
    if doc_cliente not in datos["clientes"]:
        print(" Cliente no encontrado. Regístrelo primero.")
        return
    cliente = datos["clientes"][doc_cliente]

    doc_inst = input("Documento del Instructor: ").strip()
    if doc_inst not in datos["instructores"]:
        print(" Instructor no encontrado.")
        return
    instructor = datos["instructores"][doc_inst]

    placa = input("Placa del Vehículo: ").strip().upper()
    if placa not in datos["vehiculos"]:
        print(" Vehículo no encontrado.")
        return
    vehiculo = datos["vehiculos"][placa]

    if cliente["tipo_vehiculo"] != instructor["especialidad"] or cliente["tipo_vehiculo"] != vehiculo["tipo"]:
        print(" Conflicto: El tipo de vehículo del cliente, la especialidad del instructor y el vehículo deben coincidir.")
        return

    fecha_str = input("Fecha (DD/MM/AAAA): ").strip()
    hora_str = input("Hora (HH:MM, formato 24h): ").strip()
    try:
        datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
    except ValueError:
        print(" Formato de fecha u hora inválido.")
        return

    duracion = input("Duración en horas (Ej: 1 o 2): ").strip()

    for cita in datos["citas"]:
        if cita["fecha"] == fecha_str and cita["hora"] == hora_str:
            if cita["doc_instructor"] == doc_inst:
                print(" El instructor ya tiene una cita programada a esa hora.")
                return
            if cita["placa_vehiculo"] == placa:
                print(" El vehículo ya está asignado a otra cita a esa hora.")
                return

    nueva_cita = {
        "id_cita": len(datos["citas"]) + 1,
        "doc_cliente": doc_cliente,
        "doc_instructor": doc_inst,
        "placa_vehiculo": placa,
        "fecha": fecha_str,
        "hora": hora_str,
        "duracion": duracion,
        "asistencia": "Pendiente",
        "observaciones": ""
    }
    
    datos["citas"].append(nueva_cita)
    print(f" Cita programada con éxito. ID de Cita: {nueva_cita['id_cita']}")

def consultar_citas(datos):
    print("\n--- CONSULTAR CITAS ---")
    print("1. Ver todas las citas")
    print("2. Filtrar por Cliente")
    print("3. Filtrar por Fecha")
    opcion = input("Seleccione una opción: ")

    citas_filtradas = datos["citas"]

    if opcion == "2":
        doc = input("Documento del cliente: ").strip()
        citas_filtradas = [c for c in datos["citas"] if c["doc_cliente"] == doc]
    elif opcion == "3":
        fecha = input("Fecha (DD/MM/AAAA): ").strip()
        citas_filtradas = [c for c in datos["citas"] if c["fecha"] == fecha]

    if not citas_filtradas:
        print("No se encontraron citas con los criterios especificados.")
        return

    for c in citas_filtradas:
        print(f"\nID: {c['id_cita']} | Fecha: {c['fecha']} {c['hora']} ({c['duracion']}h)")
        print(f"Cliente: {datos['clientes'][c['doc_cliente']]['nombre']} | Instructor: {datos['instructores'][c['doc_instructor']]['nombre']}")
        print(f"Vehículo: {c['placa_vehiculo']} | Asistencia: {c['asistencia']}")
        if c['observaciones']:
            print(f"Observaciones: {c['observaciones']}")

def registrar_asistencia(datos):
    print("\n--- REGISTRAR ASISTENCIA Y OBSERVACIONES ---")
    try:
        id_cita = int(input("Ingrese el ID de la cita: "))
    except ValueError:
        print(" ID inválido.")
        return

    cita_encontrada = None
    for cita in datos["citas"]:
        if cita["id_cita"] == id_cita:
            cita_encontrada = cita
            break

    if not cita_encontrada:
        print(" Cita no encontrada.")
        return

    asistencia = input("¿Asistió? (Si/No/Cancelado): ").strip().capitalize()
    if asistencia not in ["Si", "No", "Cancelado"]:
        print(" Estado de asistencia no válido.")
        return

    observaciones = input("Ingrese las observaciones de la práctica: ").strip()
    
    cita_encontrada["asistencia"] = asistencia
    cita_encontrada["observaciones"] = observaciones
    print(" Asistencia y observaciones actualizadas correctamente.")

def consultar_historial_cliente(datos):
    print("\n--- HISTORIAL DE PRÁCTICAS POR CLIENTE ---")
    doc = input("Documento del cliente: ").strip()
    if doc not in datos["clientes"]:
        print(" Cliente no registrado.")
        return

    print(f"\nHistorial de: {datos['clientes'][doc]['nombre']}")
    historial = [c for c in datos["citas"] if c["doc_cliente"] == doc]

    if not historial:
        print("El cliente no registra ninguna cita en el sistema.")
        return

    for c in historial:
        print(f"- [{c['fecha']} {c['hora']}] Vehículo: {c['placa_vehiculo']} | Estado: {c['asistencia']}")
        if c['observaciones']:
            print(f"  Obs: {c['observaciones']}")