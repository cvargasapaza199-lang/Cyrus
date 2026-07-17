def responder(texto):
    texto = texto.lower()

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

    else:
        return "Aún no sé responder eso, pero sigo aprendiendo."