# DRIVESAFE

## Descripción

DriveSafe es una aplicación desarrollada en Python para gestionar de manera organizada las prácticas de conducción de motocicletas y automóviles.

El sistema permite registrar clientes, instructores y vehículos, programar citas de práctica, controlar la asistencia y consultar el historial de prácticas. Toda la información se almacena localmente mediante archivos JSON, sin utilizar una base de datos.

## Objetivo

Digitalizar y organizar la gestión de citas de prácticas de conducción, evitando confusiones relacionadas con horarios, instructores, clientes y vehículos disponibles.

## Funcionalidades

* Registrar y consultar clientes.
* Validar que el documento de cada cliente sea único.
* Registrar instructores con especialidad en moto o carro.
* Registrar vehículos con tipo, placa y disponibilidad.
* Programar citas de práctica.
* Validar la disponibilidad de instructores y vehículos.
* Consultar citas programadas.
* Filtrar citas por cliente o fecha.
* Registrar asistencia a las prácticas.
* Agregar observaciones sobre cada práctica.
* Consultar el historial de prácticas de un cliente.
* Guardar y cargar información mediante archivos JSON.

## Tecnologías utilizadas

* Python 3
* JSON para la persistencia de datos
* Consola como interfaz de usuario


## Requisitos

Para ejecutar el proyecto necesitas:

* Python 3.8 o superior.
* Un editor de código como Visual Studio Code (opcional).

## Funcionamiento

Al iniciar la aplicación, se muestra un menú principal desde el cual el usuario puede acceder a las diferentes funcionalidades del sistema:


===== DRIVESAFE =====

("========================================")
("     SISTEMA DE GESTIÓN DRIVESAFE       ")
("========================================")
("1. Registrar Cliente")
("2. Registrar Instructor")
("3. Registrar Vehículo")
("4. Programar Cita de Práctica")
("5. Consultar Citas Programadas")
("6. Registrar Asistencia y Observaciones")
("7. Consultar Historial de Cliente")
("8. Salir")
("========================================")


El sistema valida los datos ingresados y evita problemas como:

* Documentos de clientes duplicados.
* Placas de vehículos repetidas.
* Fechas inválidas.
* Citas en horarios ocupados.
* Asignación de vehículos o instructores no disponibles.
* Citas con vehículos o instructores de una especialidad incorrecta.

## Persistencia de datos

La información se guarda en archivos locales en formato JSON. Esto permite que los datos permanezcan almacenados incluso después de cerrar el programa.

Ejemplo de un cliente:

{
    "nombre": "Juan Pérez",
    "documento": "123456789",
    "tipo_vehiculo": "moto"
}

## Validaciones principales

El sistema realiza validaciones básicas para garantizar el correcto funcionamiento:

* El documento del cliente debe ser único.
* La placa del vehículo debe ser única.
* El tipo de vehículo debe ser `moto` o `carro`.
* La especialidad del instructor debe coincidir con el tipo de vehículo.
* No se pueden programar citas en horarios ocupados.
* Las fechas y horas deben tener un formato válido.
* Solo se puede registrar asistencia en citas existentes.

## Autores

Proyecto académico desarrollado para la gestión de prácticas de conducción de la academia DriveSafe.

## Licencia

Este proyecto fue desarrollado con fines académicos.