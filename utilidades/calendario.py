import json

RUTA = "datos/calendario.json"

def listar_eventos():
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_eventos(eventos):
    with open(RUTA, "w", encoding="utf-8") as archivo:
        json.dump(eventos, archivo, indent=4, ensure_ascii=False)

def agregar_evento(fecha, descripcion):
    eventos = listar_eventos()

    eventos.append({
        "fecha": fecha,
        "descripcion": descripcion
    })

    guardar_eventos(eventos)

def buscar_eventos(fecha):
    eventos = listar_eventos()
    resultado = []

    for evento in eventos:
        if evento["fecha"] == fecha:
            resultado.append(evento)

    return resultado