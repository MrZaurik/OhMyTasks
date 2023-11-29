import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk

class OhMyTasks():
    """
    Clase principal de la aplicación
    """
    def __init__ (self, root): # El argumento self funciona como un constructor
        # -----------------------------------------------------------------------
        # Defino nuestro root (Programa principal)
        # Atributos principales
        self.root = root
        self.root.title("OhMyTasks") # Titulo de la ventana
        self.root.resizable(0, 0)     # Tamaño estático
        self.root.configure(background="#EEF5FF") # Color de fondo
        # Variables bandera
        self.listaSeleccionada_listbox = tk.StringVar()
        self.listaSeleccionada_otros = tk.StringVar()

        # Asignación de valores
        self.listaSeleccionada_listbox.set("Tareas Pendientes")
        self.listaSeleccionada_otros.set("Tareas Pendientes") # Constante
        # -----------------------------------------------------------------------
        # DISEÑO INTERFAZ

        style = ttk.Style()
        style.configure("TButton", background="#EEF5FF")

        # Botones
        self.botonCrear = ttk.Button(root, text="Crear", command=self.CrearTarea)
        self.botonEditar = tk.Button(root, text="Modificar", command=self.EditarTarea)
        self.botonBorrar = tk.Button(root, text="Eliminar", command=self.BorrarTarea)
        self.botonSwitch = tk.Button(root, text="Cambiar Lista", command=self.CambioLista)

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

    #--------------------------------------------------------------------------------
    # MÉTODOS
    def CambioLista(self):
        listaSeleccionadaActual = self.listaSeleccionada_listbox.get()
        if listaSeleccionadaActual == "Tareas Pendientes":
            indice = self.tareasPendientes.curselection()
            if indice:
                tituloTarea = self.tareasPendientes.get(indice)
                self.tareasPendientes.delete(indice)
                self.tareasRealizadas.insert(tk.END, tituloTarea)
        else:
            indice = self.tareasRealizadas.curselection()
            if indice:
                tituloTarea = self.tareasRealizadas.get(indice)
                self.tareasRealizadas.delete(indice)
                self.tareasPendientes.insert(tk.END, tituloTarea)

        self.listaSeleccionada_listbox.set("Tareas Pendientes" if listaSeleccionadaActual == "Tareas Realizadas" else "Tareas Realizadas")

    def CrearTarea(self):
        titulo = simpledialog.askstring("Crear Tarea", "Ingrese el título de la tarea")
        if titulo:
            listaSeleccionadaActual = self.listaSeleccionada_otros.get()
            if listaSeleccionadaActual == "Tareas Pendientes":
                self.tareasPendientes.insert(tk.END, titulo)

    def EditarTarea(self):
        listaSeleccionadaActual = self.listaSeleccionada_otros.get()
        if listaSeleccionadaActual == "Tareas Pendientes":
            indice = self.tareasPendientes.curselection()
            titulo = self.tareasPendientes.get(indice)
            nuevoTitulo = simpledialog.askstring("Editar Tarea", "Ingrese el nuevo título de la tarea", initialvalue=titulo)

            if titulo and nuevoTitulo:
                self.tareasPendientes.delete(indice)
                self.tareasPendientes.insert(indice, nuevoTitulo)

    def BorrarTarea(self):
        listaSeleccionadaActual = self.listaSeleccionada_otros.get()
        if listaSeleccionadaActual == "Tareas Pendientes":
            indice = self.tareasPendientes.curselection()
            self.tareasPendientes.delete(indice)



def main():
    root = tk.Tk()
    app = OhMyTasks(root)
    root.mainloop()

main()





