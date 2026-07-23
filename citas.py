from datetime import datetime, timedelta

def programar_cita(datos):
    print("\n--- PROGRAMAR CITA DE PRÁCTICA ---")
    
    doc_cliente = input("Documento del Cliente: ").strip()
    if doc_cliente not in datos["clientes"]:
        print(" Error: Cliente no encontrado. Regístrelo primero.")
        return
    cliente = datos["clientes"][doc_cliente]

    tipo_req = cliente["tipo_vehiculo"]
    instructores_compatibles = {
        doc: info for doc, info in datos["instructores"].items() 
        if info["especialidad"] == tipo_req
    }

    if not instructores_compatibles:
        print(f" Error: No hay instructores registrados para la especialidad de '{tipo_req}'.")
        return

    print(f"\n--- INSTRUCTORES DISPONIBLES ({tipo_req.upper()}) ---")
    for doc_i, info_i in instructores_compatibles.items():
        print(f" • Documento: {doc_i} | Nombre: {info_i['nombre']}")
    print("--------------------------------------------------")

    doc_inst = input("\nDocumento del Instructor: ").strip()
    if doc_inst not in datos["instructores"]:
        print(" Error: Instructor no encontrado.")
        return
    instructor = datos["instructores"][doc_inst]

    placa = input("Placa del Vehículo: ").strip().upper()
    if placa not in datos["vehiculos"]:
        print(" Error: Vehículo no encontrado.")
        return
    vehiculo = datos["vehiculos"][placa]

    if cliente["tipo_vehiculo"] != instructor["especialidad"] or cliente["tipo_vehiculo"] != vehiculo["tipo"]:
        print(" Error: El tipo de vehículo del cliente, la especialidad del instructor y el vehículo deben coincidir.")
        return

    fecha_str = input("Fecha (DD/MM/AAAA): ").strip()
    hora_str = input("Hora (HH:MM, formato 24h): ").strip()
    duracion_str = input("Duración en horas (Máximo 2): ").strip()

    try:
        duracion_hrs = int(duracion_str)
        if duracion_hrs <= 0 or duracion_hrs > 2:
            print(" Error: La duración permitida es de máximo 2 horas (1 o 2).")
            return

        inicio_nueva = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
        fin_nueva = inicio_nueva + timedelta(hours=duracion_hrs)
    except ValueError:
        print(" Error: Formato de fecha, hora o duración inválido.")
        return

    for cita in datos["citas"]:
        if cita.get("asistencia") == "Cancelado":
            continue

        try:
            inicio_existente = datetime.strptime(f"{cita['fecha']} {cita['hora']}", "%d/%m/%Y %H:%M")
            fin_existente = inicio_existente + timedelta(hours=int(cita["duracion"]))
        except ValueError:
            continue

        se_cruzan = (inicio_nueva < fin_existente) and (fin_nueva > inicio_existente)

        if se_cruzan:
            if cita["doc_instructor"] == doc_inst:
                print(f" Error: El instructor ya tiene una cita ocupada de {cita['hora']} a {fin_existente.strftime('%H:%M')}.")
                return
            if cita["placa_vehiculo"] == placa:
                print(f" Error: El vehículo ya está ocupado de {cita['hora']} a {fin_existente.strftime('%H:%M')}.")
                return

    nueva_cita = {
        "id_cita": len(datos["citas"]) + 1,
        "doc_cliente": doc_cliente,
        "doc_instructor": doc_inst,
        "placa_vehiculo": placa,
        "fecha": fecha_str,
        "hora": hora_str,
        "duracion": duracion_str,
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
    opcion = input("Seleccione una opción: ").strip()

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
        print(" Error: ID inválido.")
        return

    cita_encontrada = None
    for cita in datos["citas"]:
        if cita["id_cita"] == id_cita:
            cita_encontrada = cita
            break

    if not cita_encontrada:
        print(" Error: Cita no encontrada.")
        return

    asistencia = input("¿Asistió? (Si/No/Cancelado): ").strip().capitalize()
    if asistencia not in ["Si", "No", "Cancelado"]:
        print(" Error: Estado de asistencia no válido.")
        return

    observaciones = input("Ingrese las observaciones de la práctica: ").strip()
    
    cita_encontrada["asistencia"] = asistencia
    cita_encontrada["observaciones"] = observaciones
    print(" Asistencia y observaciones actualizadas correctamente.")

def consultar_historial_cliente(datos):
    print("\n--- HISTORIAL DE PRÁCTICAS POR CLIENTE ---")
    doc = input("Documento del cliente: ").strip()
    if doc not in datos["clientes"]:
        print(" Error: Cliente no registrado.")
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