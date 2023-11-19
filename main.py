"""
Bienvenidos al proyecto OhMyTask, este es el archivo fuente apartir del cual se ejecuta el programa.
Este proyecto viene a ser una propuesta de software para la gestión efectiva de tareas.
Programadores: - Juan Guillermo Saurith Moreno
               - William Alcides Trillos Sarmiento
               - Sebastian David Bohorquez Ponce
Asignatura: Programación I
Docente: Juan Pablo Hoyos Sanchez, PhD
Institución: Universidad Nacional de Colombia
"""

import gc

TAREAS = []  # lista de tareas pendientes
TAREAS_HECHAS = []  # lista de tareas realizadas

# funciones a utilizar


def crearTarea() -> list:
    """ Función que crea una tarea y la agrega a la lista de tareas """

    # Registro de los datos de la tarea
    titulo = input("Ingrese el titulo de la tarea: ")

    # Comprobamos la entrada del usuario
    if titulo == '':  # Si el usuario no ingresa nada
        while titulo == '':  # Mientras el usuario no ingrese nada
            print("El título no puede estar vacío")
            titulo = input("Ingrese el titulo de la tarea: ")

    descripcion = input("Ingrese la descripcion de la tarea: ") # Característica opcional
    fecha = input("Ingrese la fecha de la tarea: ")  # Característica opcional
    # Característica opcional
    prioridad = input("Ingrese la prioridad de la tarea: ")

    # Asignamos cada argumento a una casilla de la lista
    tareaCreada = [titulo, descripcion, fecha, prioridad]
    print("Tarea creada exitosamente")
    return tareaCreada  # Devolvemos el array con los datos de la tarea creada


def eliminarTarea(listaTareas: list, tarea: str) -> list:
    """ Función que elimina una tarea de la lista de tareas """
    if tarea in listaTareas:
        listaTareas.remove(tarea)  # Eliminamos la tarea de la lista de tareas
        print(f'Tarea "{tarea}" eliminada exitosamente')
    else:
        print("Tarea no encontrada")
    return listaTareas  # Devolvemos la lista de tareas actualizada


def modificarTarea(listaTareas: list, tarea: str) -> list:
    """
    Función que modifica una tarea de la lista de tareas.

    Parameters:
        listaTareas (list): La lista de tareas.
        tarea (list): La tarea a modificar.

    Returns:
        list: La lista de tareas actualizada.
    """
    if tarea in listaTareas:
        # Solicitamos los nuevos datos de la tarea a actualizar
        print("Ingrese los nuevos datos de la tarea (Deje en blanco si desea mantener lo que tenía antes)")
        tituloNuevo = input("Ingrese el nuevo título de la tarea: ")
        if tituloNuevo == '':  # Si el usuario no ingresa nada
            while tituloNuevo == '':
                print("El título no puede estar vacío")
                tituloNuevo = input("Ingrese el nuevo título de la tarea: ")
        
        descripcionNueva = input("Ingrese la nueva descripción de la tarea: ")
        fechaNueva = input("Ingrese la nueva fecha de la tarea: ")
        prioridadNueva = input("Ingrese la nueva prioridad de la tarea: ")

        # Actualizamos los datos de la tarea
        if tituloNuevo:
            tarea[0] = tituloNuevo
            print("Título actualizado exitosamente")
        if descripcionNueva:
            tarea[1] = descripcionNueva
            print("Descripción actualizada exitosamente")
        if fechaNueva:
            tarea[2] = fechaNueva
            print("Fecha actualizada exitosamente")
        if prioridadNueva:
            tarea[3] = prioridadNueva
            print("Prioridad actualizada exitosamente")

        print("Tarea actualizada exitosamente")
    else:
        print("Tarea no encontrada")

    return listaTareas


def realizarTarea(listaTareas: list, tarea: str) -> list:
    """ Función que marca una tarea como realizada """
    # Almacena la tarea en la variable TAREAS_HECHAS
    if tarea in listaTareas:
        # Agregamos la tarea a la lista de tareas realizadas
        TAREAS_HECHAS.append(tarea)
        print(f'Tarea "{tarea[0]}" marcada como realizada')

        # Eliminamos la tarea de la lista de tareas pendientes
        eliminarTarea(listaTareas, tarea)


def mostrarTareas(listaTareas: list, Selector: int = 0) -> list:
    """ Función que muestra las tareas pendientes y realizadas """
    if Selector == 0:
        # Muestra las tareas pendientes en forma de lista
        print("Tareas pendientes: ")
        # Comprobamos si hay tareas pendientes
        if len(listaTareas) == 0:
            print("No hay tareas pendientes")
        # Si hay tareas pendientes, las mostramos
        else:
            for tarea in listaTareas:
                print(f'● {tarea[0]}')
            return 0
    else:
        # Muestra las tareas realizadas en forma de lista
        print("Tareas realizadas: ")
        # Comprobamos si hay tareas realizadas
        if len(listaTareas) == 0:
            print("No hay tareas realizadas")
        # Si hay tareas realizadas, las mostramos
        else:
            for tarea in listaTareas:
                print(f'● {tarea[0]}')
            return 0

# -------------------------------- Ejecución del programa --------------------------------------------
# De momento estamos trabajando en la consola, pero más adelante se implementará una interfaz gráfica


# Menú principal
print("Bienvenido a OhMyTask")

# Bucle principal
try:  # Manejo de excepciones
    while True:
        print("¿Qué desea hacer?")
        print("1. Crear tarea")
        print("2. Eliminar tarea")
        print("3. Modificar tarea")
        print("4. Marcar tarea como realizada")
        print("5. Mostrar tareas pendientes")
        print("6. Salir")
        opcion = input("Ingrese la opción que desea realizar: ")

        # Creación de la tarea
        if opcion == '1':
            # Agregamos la tarea en forma de array a la lista de tareas
            TAREAS.append(crearTarea())

        # Eliminación de la tarea
        elif opcion == '2':
            # Mostramos las tareas para que el usuario pueda elegir cual eliminar
            mostrarTareas(TAREAS)
            tareaEliminar = input(
                "Ingrese el titulo de la tarea que desea eliminar: ")
            for tarea in TAREAS:
                if tarea[0] == tareaEliminar:
                    eliminarTarea(TAREAS, tarea)  # Eliminamos la tarea
                else:
                    print("Tarea no encontrada")

        # Modificación de la tarea
        elif opcion == '3':
            mostrarTareas(TAREAS)
            tareaModificar = input(
                "Ingrese el titulo de la tarea que desea modificar: ")
            for tarea in TAREAS:
                if tarea[0] == tareaModificar:
                    modificarTarea(TAREAS, tarea)
                else:
                    print("Tarea no encontrada")

        # Marcar tarea como realizada
        elif opcion == '4':
            mostrarTareas(TAREAS)
            tareaRealizada = input(
                "Ingrese el titulo de la tarea que desea marcar como realizada: ")
            for tarea in TAREAS:
                if tarea[0] == tareaRealizada:
                    realizarTarea(TAREAS, tarea)
                else:
                    print("Tarea no encontrada")

        elif opcion == '5':
            mostrarTareas(TAREAS)
            mostrarTareas(TAREAS_HECHAS, 1)

        elif opcion == '6':
            gc.collect()  # Liberamos la memoria
            break

        else:
            print("Opción no válida")

except KeyboardInterrupt:
    print("\nPrograma finalizado")
    gc.collect()  # Liberamos la memoria

except TypeError:
    print("Error de tipo de dato")
