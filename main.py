import customtkinter as ctk
from cerebro.respuestas import responder
import json 

with open("datos/config.json", "r", encoding="utf-8") as archivo:
    config = json.load(archivo)

# Configuración de la apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear ventana
ventana = ctk.CTk()
ventana.title(config["nombre"])
ventana.geometry("700x500")

# Función para responder
def enviar_mensaje():
    texto = entrada.get().strip()

    if texto == "":
        return
    chat.configure(state="normal")
    chat.insert("end", f"👤 Tú: {texto}\n")
    respuesta = responder(texto)
    chat.insert("end", f"🤖 {config['nombre']}: {respuesta}\n\n")
    chat.configure(state="disabled")
    entrada.delete(0, "end")
    
# Título
titulo = ctk.CTkLabel(
    ventana,
    text=f"🤖 {config['nombre'].upper()}",
    font=("Arial", 30, "bold")
)
titulo.pack(pady=20)

# Mensaje
mensaje = ctk.CTkLabel(
    ventana,
    text=f"Bienvenido. Soy {config['nombre']}, tu asistente personal.",
    font=("Arial", 18)
)
mensaje.pack(pady=10)

# Historial del chat
chat = ctk.CTkTextbox(
    ventana,
    width=600,
    height=220,
    font=("Arial", 15)
)
chat.pack(pady=10)

chat.insert("end", f"🤖 {config['nombre']}: Hola, soy {config['nombre']}. ¿En qué puedo ayudarte?\n\n")
chat.configure(state="disabled")

# Respuesta de Cyrus
respuesta = ctk.CTkLabel(
    ventana,
    text="",
    font=("Arial", 18),
    wraplength=600
)
respuesta.pack(pady=10)
# Caja de texto
entrada = ctk.CTkEntry(
    ventana,
    width=400,
    placeholder_text="Escribe un mensaje..."
)
entrada.pack(pady=20)

# Botón
boton = ctk.CTkButton(
    ventana,
    text="Enviar",
    command=enviar_mensaje
)
boton.pack(pady=10)
ventana.bind("<Return>", lambda 
event: enviar_mensaje())

# Ejecutar ventana
ventana.mainloop()