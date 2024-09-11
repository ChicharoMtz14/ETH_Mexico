import tkinter as tk
from tkinter import simpledialog, messagebox

# Función para iniciar la votación
def iniciar_votacion():
    nombre_votacion = simpledialog.askstring("Nombre de la Votación", "¿Cuál es el nombre de tu votación?")
    descripcion_votacion = simpledialog.askstring("Descripción de la Votación", "Agrega una descripción de la votación")
    
    # Opciones para el tipo de votación
    tipos_votacion = ["Empresarial", "Consulta Popular", "Política", "Otro"]
    
    tipo_votacion = simpledialog.askstring("Tipo de Votación", f"Elige un tipo de votación: {', '.join(tipos_votacion)}")

    # Opciones de votación
    opciones = []
    num_opciones = simpledialog.askinteger("Opciones", "¿Cuántas opciones tendrá la votación?")
    for i in range(num_opciones):
        opcion = simpledialog.askstring("Opción de Voto", f"Ingrese el nombre de la opción {i+1}:")
        opciones.append(opcion)
    
    # Cantidad de votantes
    num_votantes = simpledialog.askinteger("Cantidad de Votantes", "¿Cuántas personas participarán en la votación?")
    
    # Guardamos los datos de la votación
    votacion = {
        'nombre': nombre_votacion,
        'descripcion': descripcion_votacion,
        'tipo': tipo_votacion,
        'opciones': opciones,
        'num_votantes': num_votantes,
        'votos': {opcion: 0 for opcion in opciones}  # Inicializamos los votos en 0
    }
    
    # Función para registrar votos
    registrar_votos(votacion)

# Función para registrar los votos
def registrar_votos(votacion):
    messagebox.showinfo("Inicio de Votación", f"La votación '{votacion['nombre']}' ha comenzado.")
    
    for i in range(votacion['num_votantes']):
        voto = simpledialog.askstring("Votación", f"Votante {i+1}, elige una opción: {', '.join(votacion['opciones'])}")
        if voto in votacion['opciones']:
            votacion['votos'][voto] += 1
        else:
            messagebox.showerror("Error", "Opción inválida. Intenta de nuevo.")
            i -= 1  # Reintentar si hay error

    # Mostramos los resultados finales
    mostrar_resultados(votacion)

# Función para mostrar los resultados de la votación
def mostrar_resultados(votacion):
    resultados = "\n".join([f"{opcion}: {votos} votos" for opcion, votos in votacion['votos'].items()])
    messagebox.showinfo("Resultados Finales", f"Resultados de la votación '{votacion['nombre']}':\n\n{resultados}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Votación")

# Botón para iniciar la votación
boton_iniciar = tk.Button(root, text="Iniciar Votación", command=iniciar_votacion)
boton_iniciar.pack(pady=20)

# Iniciar el loop de la ventana
root.mainloop()