import subprocess


def ejecutar_comando(texto):
    texto = texto.lower()

    comandos = {
        "abrir calculadora": ("calc.exe", "Abriendo la calculadora..."),
        "abrir bloc de notas": ("notepad.exe", "Abriendo el Bloc de notas..."),
        "abrir explorador": ("explorer.exe", "Abriendo el Explorador de archivos...")
    }

    if texto in comandos:
        programa, mensaje = comandos[texto]
        subprocess.Popen(programa)
        return mensaje

    return None