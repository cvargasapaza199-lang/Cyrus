def responder(texto):
    texto = texto.strip().lower()

    if texto == "hola":
        return "Hola, Cristian. ¿Cómo puedo ayudarte?"

    elif texto == "quien eres" or texto == "¿quién eres?":
        return "Soy Cyrus, tu asistente personal."

    elif texto == "gracias":
        return "¡De nada! 😊"

    elif texto == "adios":
        return "Hasta luego. ¡Que tengas un buen día!"

    else:
        return "Todavía estoy aprendiendo."