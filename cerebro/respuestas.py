def responder(texto):
    texto = texto.lower().strip()

    saludos = ["hola", "buenas", "buen día", "buenos días", "hey", "hi"]
    preguntas = ["quien eres", "quién eres", "tu nombre"]
    gracias = ["gracias", "muchas gracias", "te agradezco"]
    despedidas = ["adios", "adiós", "hasta luego", "nos vemos", "chao"]

    for saludo in saludos:
        if saludo in texto:
            return "Hola, Cristian. ¿Cómo puedo ayudarte?"
    for pregunta in preguntas:
        if pregunta in texto:
            return "Soy Cyrus, tu asistente personal."
    for palabra in gracias:
        if palabra in texto:
            return "¡De nada!"
    for despedida in despedidas:
        if despedida in texto:
            return "Hasta luego. ¡Que tengas un excelente día!"
    return "Todavía estoy aprendiendo. Muy pronto sabré responder eso."
        