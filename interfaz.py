import tkinter as tk
from tkinter import simpledialog

class OhMyTasks:
    def __init__(self, root):
        self.root = root
        self.root.title("OhMyTask")

        # Variables
        self.current_switch_listbox = tk.StringVar()
        self.current_listbox_operations = tk.StringVar()
        self.current_switch_listbox.set("Tareas Pendientes")
        self.current_listbox_operations.set("Tareas Pendientes")

        # Botones superiores
        self.create_button = tk.Button(root, text="Crear", command=self.create_task)
        self.delete_button = tk.Button(root, text="Eliminar", command=self.delete_task)
        self.modify_button = tk.Button(root, text="Modificar", command=self.modify_task)
        self.switch_button = tk.Button(root, text="Cambiar Lista", command=self.switch_listbox)

        # Listas
        self.pending_tasks_label = tk.Label(root, text="Tareas Pendientes")
        self.completed_tasks_label = tk.Label(root, text="Tareas Realizadas")

        self.pending_tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.completed_tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE)

        # Posicionar elementos
        self.create_button.grid(row=0, column=0)
        self.delete_button.grid(row=0, column=1)
        self.modify_button.grid(row=0, column=2)
        self.switch_button.grid(row=2, column=1)

        self.pending_tasks_label.grid(row=1, column=0)
        self.completed_tasks_label.grid(row=1, column=2)

        self.pending_tasks_listbox.grid(row=2, column=0)
        self.completed_tasks_listbox.grid(row=2, column=2)

    def switch_listbox(self):
        current_switch_listbox = self.current_switch_listbox.get()
        current_listbox_operations = self.current_listbox_operations.get()

        if current_switch_listbox == "Tareas Pendientes":
            selected_index = self.pending_tasks_listbox.curselection()
            if selected_index:
                task_title = self.pending_tasks_listbox.get(selected_index)
                self.pending_tasks_listbox.delete(selected_index)
                self.completed_tasks_listbox.insert(tk.END, task_title)
        else:
            selected_index = self.completed_tasks_listbox.curselection()
            if selected_index:
                task_title = self.completed_tasks_listbox.get(selected_index)
                self.completed_tasks_listbox.delete(selected_index)
                self.pending_tasks_listbox.insert(tk.END, task_title)

        self.current_switch_listbox.set("Tareas Pendientes" if current_switch_listbox == "Tareas Realizadas" else "Tareas Realizadas")

    def create_task(self):
        title = simpledialog.askstring("Crear Tarea", "Ingrese el título de la tarea:")

        if title:
            current_listbox_operations = self.current_listbox_operations.get()

            if current_listbox_operations == "Tareas Pendientes":
                self.pending_tasks_listbox.insert(tk.END, title)
            else:
                self.completed_tasks_listbox.insert(tk.END, title)

    def delete_task(self):
        current_listbox_operations = self.current_listbox_operations.get()
        selected_index = None

        if current_listbox_operations == "Tareas Pendientes":
            selected_index = self.pending_tasks_listbox.curselection()
            self.pending_tasks_listbox.delete(selected_index)
        elif current_listbox_operations == "Tareas Realizadas":
            selected_index = self.completed_tasks_listbox.curselection()
            self.completed_tasks_listbox.delete(selected_index)

    def modify_task(self):
        current_listbox_operations = self.current_listbox_operations.get()

        if current_listbox_operations == "Tareas Pendientes":
            selected_index = self.pending_tasks_listbox.curselection()
            title = self.pending_tasks_listbox.get(selected_index)
        elif current_listbox_operations == "Tareas Realizadas":
            selected_index = self.completed_tasks_listbox.curselection()
            title = self.completed_tasks_listbox.get(selected_index)

        new_title = simpledialog.askstring("Modificar Tarea", "Ingrese el nuevo título de la tarea:", initialvalue=title)

        if title and new_title:
            if current_listbox_operations == "Tareas Pendientes":
                self.pending_tasks_listbox.delete(selected_index)
                self.pending_tasks_listbox.insert(tk.END, new_title)
            elif current_listbox_operations == "Tareas Realizadas":
                self.completed_tasks_listbox.delete(selected_index)
                self.completed_tasks_listbox.insert(tk.END, new_title)

if __name__ == "__main__":
    root = tk.Tk()
    app = OhMyTasks(root)
    root.mainloop()

