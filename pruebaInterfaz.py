import tkinter as tk
from datetime import datetime as dt

window = tk.Tk()
window.title("Gestor de Tareas")
# window.geometry("400x500")
window.resizable(False, False)


tareas = []
contador = 1

# Funciones
def nuevaTarea():
    global contador
    tarea = entradaTarea.get()
    tareas.append([f'{contador}. {tarea}', dt.now()])
    contador += 1
    entradaTarea.delete(0, tk.END)
    actualizarTareas()

def actualizarTareas():
    task_list.delete(0, tk.END)
    for tarea in tareas:
        task_list.insert(tk.END, f'{tarea[0]} at {tarea[1]}')

def completarTarea():
    seleccion = task_list.curselection()
    tareasHechas.insert(tk.END, tareas[seleccion[0]])
    tareas.pop(seleccion[0])
    actualizarTareas()

def eliminarTarea():
    seleccion = task_list.curselection()
    tareas.pop(seleccion[0])
    actualizarTareas()

# Elementos gráficos
titulo = tk.Label(window, text="Gestor de Tareas", font=("Helvetica", 20), bg="#F5F5F5")
titulo.pack(pady=20)

task_label = tk.Label(window, text="Digite la tarea:", font=("Helvetica", 12), bg="#F5F5F5")
task_label.pack()

entradaTarea = tk.Entry(window, font=("Helvetica", 12), width=30)
entradaTarea.pack(pady=10)

add_button = tk.Button(window, text="Añadir Tarea", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=nuevaTarea)
add_button.pack(pady=10)

eliminar_button = tk.Button(window, text="Eliminar Tarea", font=("Helvetica", 12), bg="#F44336", fg="white", command=eliminarTarea)
eliminar_button.pack(pady=10)

completar_button = tk.Button(window, text="Completar Tarea", font=("Helvetica", 12), bg="#2196F3", fg="white", command=completarTarea)
completar_button.pack(pady=10)

task_list = tk.Listbox(window, font=("Arial", 12), width=40, height=10)
task_list.pack(pady=10)

mensaje = tk.Label(window, text="Tareas realizadas:", font=("Helvetica", 12), bg="#F5F5F5")
mensaje.pack(pady=10)

tareasHechas = tk.Listbox(window, font=("Arial", 12), width=40, height=5)
tareasHechas.pack(pady=10)

task_list.config(font=("Helvetica", 12))
tareasHechas.config(font=("Helvetica", 12))
window.mainloop()