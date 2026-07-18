from memoria.memoria import guardar_dato, obtener_dato, guardar_historial
from datetime import datetime
from utilidades.comandos import ejecutar_comando
from utilidades.tareas import (agregar_tarea, listar_tareas, completar_tarea, eliminar_tarea, buscar_tareas, contar_tareas)
from utilidades.calendario import (agregar_evento, listar_eventos, buscar_eventos)
def responder(texto):
    texto = texto.lower().strip()
    print (f"Texto recibido: {texto}")
    comando = ejecutar_comando(texto)
    if comando:
        return comando

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

    # Agregar tarea
    elif texto.startswith("agregar tarea:"):
        tarea = texto.replace("agregar tarea:", "").strip()
        agregar_tarea(tarea)
        return f"✅ Tarea '{tarea}' agregada correctamente."
    
    elif texto.startswith("completar tarea"):
        try:
            numero = int(texto.replace("completar tarea", "").strip())
            if completar_tarea(numero):
                return f"✅ Tarea {numero} completada."
            else:
                return "Ese número de tarea no existe."
        except ValueError:
            return "Debes escribir un número. Ejemplo: completar tarea 2"
    elif texto.startswith("eliminar tarea"):
        try:
            numero = int(texto.replace("eliminar tarea", "").strip())

            tarea = eliminar_tarea(numero)

            if tarea:
                return f"🗑️ Se eliminó la tarea: {tarea}"

            return "Ese número de tarea no existe."

        except ValueError:
            return "Debes escribir un número. Ejemplo: eliminar tarea 2"
        
    elif texto.startswith("buscar tarea"):
        palabra = texto.replace("buscar tarea", "").strip()

        resultado = buscar_tareas(palabra)

        if resultado:
            return "🔎 Encontré estas tareas:\n\n" + "\n".join(resultado)

        return "No encontré ninguna tarea con ese nombre."

    elif "cuantas tareas tengo" in texto or "cuántas tareas tengo" in texto:
        cantidad = contar_tareas()
        if cantidad == 0:
            return "No tienes tareas registradas."

        elif cantidad == 1:
            return "Tienes 1 tarea registrada."

        else:
            return f"Tienes {cantidad} tareas registradas."

    elif texto.startswith("agregar " \
    "evento:"):
        datos = texto.replace("agregar evento:", "").strip()
        try:
            fecha, descripcion = datos.split(" ", 1)
            agregar_evento(fecha, descripcion)
            return f"📅 Evento agregado para el {fecha}: {descripcion}"
        except ValueError:
            return "Formato incorrecto. Ejemplo: Agregar evento: 20/07/2026 -"  " Examen de Álgebra"
        
    elif "mostrar eventos" in texto:
        eventos = listar_eventos()

        if not eventos:
            return "No tienes eventos registrados."

        respuesta = "📅 Tus eventos:\n\n"
        for i, evento in enumerate(eventos, start=1):
            respuesta += f"{i}. {evento['fecha']} - {evento['descripcion']}\n"
        return respuesta
    elif texto.startswith("eventos del"):
        fecha = texto.replace("eventos del", "").strip()
        eventos = buscar_eventos(fecha)

        if not eventos:
            return f"No hay eventos registrados para el {fecha}."

        respuesta = f"📅 Eventos del {fecha}:\n\n"
        for i, evento in enumerate(eventos, start=1):
            respuesta += f"{i}. {evento['descripcion']}\n"
        return respuesta
    
    # Mostrar tareas
    elif "mostrar tareas" in texto:
        tareas = listar_tareas()
        if not tareas:
            return "No tienes tareas registradas."

        respuesta = "📋 Tus tareas:\n"

        for i, tarea in enumerate(tareas, start=1):
            respuesta += f"{i}. {tarea}\n"

        return respuesta
    