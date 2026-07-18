from memoria.memoria import guardar_dato, obtener_dato, guardar_historial
from datetime import datetime
def responder(texto):
    texto = texto.lower().strip()

    # Saludos
    if "hola" in texto:
        return "Hola, Cristian. ¿Cómo puedo ayudarte?"

    elif "buenos dias" in texto or "buen día" in texto:
        return "¡Buenos días! Espero que tengas un excelente día."

    elif "buenas tardes" in texto:
        return "¡Buenas tardes! ¿En qué puedo ayudarte?"

    elif "buenas noches" in texto:
        return "¡Buenas noches! ¿Cómo estuvo tu día?"

    elif "quien eres" in texto or "quién eres" in texto:
        return "Soy Cyrus, tu asistente personal."

    elif "gracias" in texto:
        return "¡De nada! 😊"

    elif "adios" in texto or "adiós" in texto or "hasta luego" in texto:
        return "Hasta luego. ¡Que tengas un excelente día!"

    # Recordar el nombre
    elif texto.startswith("mi nombre es "):
        nombre = texto.replace("mi nombre es ", "").strip()
        guardar_dato("nombre", nombre)
        return f"Mucho gusto, {nombre}. Recordaré tu nombre."

    # Recordar el color favorito
    elif texto.startswith("mi color favorito es "):
        color = texto.replace("mi color favorito es ", "").strip()
        guardar_dato("color_favorito", color)
        return f"Entendido. Recordaré que tu color favorito es {color}."

    # Recuperar el nombre
    elif "cual es mi nombre" in texto or "cuál es mi nombre" in texto:
        nombre = obtener_dato("nombre")
        if nombre:
            return f"Tu nombre es {nombre}."
        else:
            return "Todavía no me has dicho tu nombre."

    # Recuperar el color favorito
    elif "cual es mi color favorito" in texto or "cuál es mi color favorito" in texto:
        color = obtener_dato("color_favorito")
        if color:
            return f"Tu color favorito es {color}."
        else:
            return "Todavía no sé cuál es tu color favorito."

    # Hora actual
    elif "que hora es" in texto or "qué hora es" in texto:
        hora = datetime.now().strftime("%H:%M")
        return f"La hora actual es {hora}."

    # Fecha actual
    elif "que fecha es hoy" in texto or "qué fecha es hoy" in texto:
        fecha = datetime.now().strftime("%d/%m/%Y")
        return f"La fecha de hoy es {fecha}."

    else:
        return "Aún no sé responder eso, pero sigo aprendiendo."