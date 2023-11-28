import tkinter as tk
from tkinter import simpledialog

class OhMyTasks():
    def __init__ (self, root): # El argumento self funciona como un constructor
        # -----------------------------------------------------------------------
        # Defino nuestro root (Programa principal)
        # Atributos principales
        self.root = root
        self.root.title = "OhMyTasks" # Titulo de la ventana
        self.root.resizable(0, 0)     # Tamaño estático

        # Variables bandera
        self.listaSeleccionada_listbox = tk.StringVar()
        self.listaSeleccionada_otros = tk.StringVar()

        # Asignación de valores
        self.listaSeleccionada_listbox.set("Tareas Pendientes")
        self.listaSeleccionada_otros.set("Tareas Pendientes") # Constante
        # -----------------------------------------------------------------------

        # DISEÑO INTERFAZ
        # Botones
        self.botonCrear = tk.Button(root, text="Crear", comand="")
        self.botonEditar = tk.Button(root, text="Crear", comand="")
        self.botonBorrar = tk.Button(root, text="Crear", comand="")
        self.botonSwitch = tk.Button(root, text="Crear", comand="")

        # Listbox (Listas)
        # Titulos
        self.tituloTareasPendientes = tk.Label(root, text="Tareas Pendientes")
        self.tituloTareasRealizadas = tk.Label(root, text="Tareas Realizadas")
        # Listbox
        self.tareasPendientes = tk.Listbox(root, selectmode=tk.SINGLE)
        self.tareasRealizadas = tk.Listbox(root, selectmode=tk.SINGLE)
        
        #------------------------------------------------------------------------

        # POSICIONAMIENTO
        """
        El diseño que se está trabajando es un grid 3x3
        |Boton Crear (0, 0)| |Boton Editar (0, 1)| |Boton Eliminar (0, 2)|
        |LabelTareas (1, 0)| |          -        | |  LabelTareas (1,2)  |
        |Listbox Pen (2, 0)| |Boton Switch (2, 1)| |Listbox Realiz (2, 2)|
        """

        self.botonCrear.grid(row=0, column=0)
        self.botonEditar.grid(row=0, column=1)
        self.botonBorrar.grid(row=0, column=2)
        self.tituloTareasPendientes.grid(row=1, column=0)
        self.tituloTareasRealizadas.grid(row=1, column=2)
        self.tareasPendientes.grid(row=2, column=0)
        self.botonSwitch.grid(row=2, column=1)
        self.tareasRealizadas.grid(row=2, column=2)

def main():
    

