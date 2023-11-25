from main import *
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title("OhMyTask")


def crear_tarea():
    titulo = simpledialog.askstring(
        "Crear Tarea", "Ingrese el título de la tarea:")
    print(titulo)


# Botones
btn_crear = tk.Button(root, text="Crear Tarea", command=crear_tarea)
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminarTarea)
btn_modificar = tk.Button(root, text="Modificar Tarea", command=modificarTarea)
btn_realizar = tk.Button(root, text="Realizar Tarea", command=realizarTarea)
btn_mostrar = tk.Button(root, text="Mostrar Tareas", command=mostrarTareas)
btn_salir = tk.Button(root, text="Salir", command=root.destroy)

# Posicionamiento de botones
btn_crear.pack()
btn_eliminar.pack()
btn_modificar.pack()
btn_realizar.pack()
btn_mostrar.pack()
btn_salir.pack()

root.mainloop()
