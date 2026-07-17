def responder(texto):
    texto = texto.lower().strip()

    saludos = ["hola", "buenas", "buen día", "buenos días", "hey", "hi"]
    preguntas = ["quien eres", "quién eres", "tu nombre"]
    gracias = ["gracias", "muchas gracias", "te agradezco"]
    despedidas = ["adios", "adiós", "hasta luego", "nos vemos", "chao"]

    if texto in saludos:
        return "Hola, Cristian. ¿Cómo puedo ayudarte?"

    elif texto in preguntas:
        return "Soy Cyrus, tu asistente personal."

    elif texto in gracias:
        return "¡De nada! 😊"

    elif texto in despedidas:
        return "Hasta luego. ¡Que tengas un excelente día!"

    return "Todavía estoy aprendiendo. Muy pronto sabré responder eso."