import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk

class OhMyTasks:
    """
    Clase principal de la aplicación
    """
    def __init__(self, root): # El argumento self funciona como un constructor
        # -----------------------------------------------------------------------
        # Defino nuestro root (Programa principal)
        # Atributos principales
        self.root = root
        self.root.title("OhMyTasks") # Titulo de la ventana
        self.root.resizable(0, 0)     # Tamaño estático
        self.root.configure(background="#EEF5FF") # Color de fondo
        
        # Variable bandera
        self.listaSeleccionada_listbox = tk.StringVar()
        # Asignación de valores
        self.listaSeleccionada_listbox.set("Tareas Pendientes")
        # -----------------------------------------------------------------------
        # DISEÑO INTERFAZ

        style = ttk.Style()
        style.configure("TButton", background="#EEF5FF", padding=10)
        style.configure(style="TLabel", background="#EEF5FF")

        # OhMyTasks!
        self.tituloApp = ttk.Label(root, text="OhMyTasks", foreground="#A25772", padding=20, font=("Helvetica", 20,"bold", "italic"))
        # Botones
        self.botonCrear = ttk.Button(root, text="Crear", command=self.CrearTarea)
        self.botonEditar = ttk.Button(root, text="Modificar", command=self.EditarTarea)
        self.botonBorrar = ttk.Button(root, text="Eliminar", command=self.BorrarTarea)
        self.botonSwitch = ttk.Button(root, text="Cambiar Lista", command=self.CambioLista)

        # Listbox (Listas)
        # Titulos
        self.tituloTareasPendientes = ttk.Label(root, text="Tareas Pendientes", padding=15, font=("Helvetica", 10, "bold"))
        self.tituloTareasRealizadas = ttk.Label(root, text="Tareas Realizadas", padding=15, font=("Helvetica", 10, "bold"))
        # Listbox
        self.tareasPendientes = tk.Listbox(root, selectmode=tk.SINGLE, background="#9EB8D9", foreground="white",
                                           selectbackground="#7C93C3", selectforeground="white", font=("Helvetica", 10))
        self.tareasRealizadas = tk.Listbox(root, selectmode=tk.SINGLE, background="#9EB8D9", foreground="white",
                                           selectbackground="#7C93C3", selectforeground="white", font=("Helvetica", 10))
        # Espacio en blanco
        self.espacioBlanco = ttk.Label(root, text="", padding=10, font=("Helvetica", 8))
        #------------------------------------------------------------------------

        # POSICIONAMIENTO
        self.tituloApp.grid(row=0, column=1)
        self.botonCrear.grid(row=1, column=0)
        self.botonEditar.grid(row=1, column=1)
        self.botonBorrar.grid(row=1, column=2)
        self.tituloTareasPendientes.grid(row=2, column=0)
        self.tituloTareasRealizadas.grid(row=2, column=2)
        self.tareasPendientes.grid(row=3, column=0)
        self.botonSwitch.grid(row=3, column=1)
        self.tareasRealizadas.grid(row=3, column=2)
        self.espacioBlanco.grid(row=4, column=1)

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
            self.tareasPendientes.insert(tk.END, titulo)

    def EditarTarea(self):
        indice = self.tareasPendientes.curselection()
        titulo = self.tareasPendientes.get(indice)
        nuevoTitulo = simpledialog.askstring("Editar Tarea", "Ingrese el nuevo título de la tarea", initialvalue=titulo)

        if titulo and nuevoTitulo:
            self.tareasPendientes.delete(indice)
            self.tareasPendientes.insert(indice, nuevoTitulo)

    def BorrarTarea(self):
        indice = self.tareasPendientes.curselection()
        self.tareasPendientes.delete(indice)



# Main
def main():
    root = tk.Tk()
    OhMyTasks(root)
    root.mainloop()
main()





