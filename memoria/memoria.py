import json
RUTA_MEMORIA = "datos/memoria.json"
def cargar_memoria():
    try:
        with open(RUTA_MEMORIA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return {}
def guardar_memoria(memoria):
    with open(RUTA_MEMORIA, "w", encoding="utf-8") as archivo:
        json.dump(memoria, archivo, indent=4, ensure_ascii=False)
def guardar_dato(clave, valor):
    memoria = cargar_memoria()
    memoria[clave] = valor
    guardar_memoria(memoria)

def obtener_dato(clave):
    memoria = cargar_memoria()
    return memoria.get(clave, None)
def guardar_historial(usuario, respuesta):
    memoria = cargar_memoria()

    if "historial" not in memoria:
        memoria["historial"] = []

    memoria["historial"].append({
        "usuario": usuario,
        "cyrus": respuesta
    })

    guardar_memoria(memoria)

def obtener_historial():
    memoria = cargar_memoria()
    return memoria.get("historial", [])
def guardar_historial(usuario, respuesta):
    memoria = cargar_memoria()

    if "historial" not in memoria:
        memoria["historial"] = []

    memoria["historial"].append({
        "usuario": usuario,
        "cyrus": respuesta
    })

    guardar_memoria(memoria)


def obtener_historial():
    memoria = cargar_memoria()
    return memoria.get("historial", [])