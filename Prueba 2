import tkinter as tk
from tkinter import ttk  # Para usar estilos más avanzados

# Función para salir de la aplicación
def salir():
    root.quit()

# Función para crear la pantalla de inicio
def pantalla_inicio():
    # Limpiamos el contenido de la ventana
    for widget in root.winfo_children():
        widget.destroy()

    # Establecemos el título
    titulo = tk.Label(root, text="Software de Votación", font=("Arial", 24, "bold"), pady=20)
    titulo.pack()

    # Crear los botones
    boton_nueva_votacion = ttk.Button(root, text="Generar Nueva Votación", width=30)
    boton_nueva_votacion.pack(pady=10)

    boton_consultar_resultados = ttk.Button(root, text="Consultar Resultados Previos", width=30)
    boton_consultar_resultados.pack(pady=10)

    boton_configuracion = ttk.Button(root, text="Configuración", width=30)
    boton_configuracion.pack(pady=10)

    boton_salir = ttk.Button(root, text="Salir", width=30, command=salir)
    boton_salir.pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Votación")
root.geometry("400x400")  # Tamaño de la ventana

# Iniciar la pantalla de inicio
pantalla_inicio()

# Iniciar el loop de la ventana
root.mainloop()
