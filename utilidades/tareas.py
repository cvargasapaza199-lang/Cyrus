import json

RUTA = "datos/tareas.json"

def cargar_tareas():
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_tareas(lista):
    with open(RUTA, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)

def agregar_tarea(tarea):
    tareas = cargar_tareas()

    tareas.append({
        "texto": tarea,
        "completada": False
    })
    guardar_tareas(tareas)

def listar_tareas():
    tareas = cargar_tareas()

    resultado = []

    for tarea in tareas:
        estado = "✅" if tarea["completada"] else "❌"
        resultado.append(f"{estado} {tarea['texto']}")
    return resultado
def completar_tarea(numero):
    tareas = cargar_tareas()

    if 1 <= numero <= len(tareas):
        tareas[numero - 1]["completada"] = True
        guardar_tareas(tareas)
        return True
    return False
def eliminar_tarea(numero):
    tareas = cargar_tareas()

    if 1 <= numero <= len(tareas):
        tarea = tareas.pop(numero - 1)
        guardar_tareas(tareas)
        return tarea["texto"]

    return None
def buscar_tareas(palabra):
    tareas = cargar_tareas()
    resultado = []

    for i, tarea in enumerate(tareas, start=1):
        if palabra.lower() in tarea["texto"].lower():
            estado = "✅" if tarea["completada"] else "❌"
            resultado.append(f"{i}. {estado} {tarea['texto']}")

    return resultado
def contar_tareas():
    tareas = cargar_tareas()
    return len(tareas)
