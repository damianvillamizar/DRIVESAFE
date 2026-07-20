import json
import os

DATA_FILE = "drivesafe_data.json"

def cargar_datos():
    """Carga los datos desde el archivo JSON. Si no existe, inicializa la estructura."""
    if not os.path.exists(DATA_FILE): 
        return {
            "clientes": {},
            "instructores": {},
            "vehiculos": {},
            "citas": []
        }
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error al leer la base de datos. Se iniciará con datos vacíos.")
        return {"clientes": {}, "instructores": {}, "vehiculos": {}, "citas": []}

def guardar_datos(datos):
    """Guarda el diccionario de datos en el archivo JSON."""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")