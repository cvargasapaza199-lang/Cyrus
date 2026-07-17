import customtkinter as ctk

# Configuración de la apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear ventana
ventana = ctk.CTk()
ventana.title("Cyrus")
ventana.geometry("700x500")

# Título
titulo = ctk.CTkLabel(
    ventana,
    text="🤖 CYRUS",
    font=("Arial", 30, "bold")
)
titulo.pack(pady=20)

# Mensaje
mensaje = ctk.CTkLabel(
    ventana,
    text="Bienvenido. Soy Cyrus, tu asistente personal.",
    font=("Arial", 18)
)
mensaje.pack(pady=10)

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
    text="Enviar"
)
boton.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()