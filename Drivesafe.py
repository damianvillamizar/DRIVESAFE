import data_manager
import clientes
import citas

def menu_principal():
    # Carga inicial de persistencia
    datos = data_manager.cargar_datos()

    while True:
        print("\n========================================")
        print("     SISTEMA DE GESTIÓN DRIVESAFE       ")
        print("========================================")
        print("1. Registrar Cliente")
        print("2. Registrar Instructor")
        print("3. Registrar Vehículo")
        print("4. Programar Cita de Práctica")
        print("5. Consultar Citas Programadas")
        print("6. Registrar Asistencia y Observaciones")
        print("7. Consultar Historial de Cliente")
        print("8. Salir")
        print("========================================")
        
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            clientes.registrar_cliente(datos)
        elif opcion == "2":
            clientes.registrar_instructor(datos)
        elif opcion == "3":
            clientes.registrar_vehiculo(datos)
        elif opcion == "4":
            citas.programar_cita(datos)
        elif opcion == "5":
            citas.consultar_citas(datos)
        elif opcion == "6":
            citas.registrar_asistencia(datos)
        elif opcion == "7":
            citas.consultar_historial_cliente(datos)
        elif opcion == "8":
            print("\nGuardando datos y saliendo del sistema... ¡Buen viaje!")
            data_manager.guardar_datos(datos)
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")
        
        # Guardado preventivo tras cada operación exitosa
        data_manager.guardar_datos(datos)

if __name__ == "__main__":
    menu_principal()