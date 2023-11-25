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
    """
    Crea una nueva tarea y la agrega a la lista de tareas pendientes.

    Returns:
        list: Lista que representa la tarea creada con los siguientes elementos:
            - Título de la tarea.
            - Descripción de la tarea (puede ser vacía).
            - Fecha de la tarea (puede ser vacía).
            - Prioridad de la tarea.
    """

    while True:
        try:
            # Registro de los datos de la tarea
            titulo = input("Ingrese el titulo de la tarea: ")

            # Lanzar una excepción si el título está vacío
            if not titulo:
                raise ValueError("El título no puede estar vacío")

            # Característica opcional
            descripcion = input("Ingrese la descripcion de la tarea: ")
            fecha = input("Ingrese la fecha de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea: ")

            # Asignamos cada argumento a una casilla de la lista
            tareaCreada = [titulo, descripcion, fecha, prioridad]
            print("Tarea creada exitosamente")
            return tareaCreada  # Devolvemos el array con los datos de la tarea creada

        except ValueError as ve:
            print(f"Error: {ve}")


def eliminarTarea(listaTareas: list, tarea: str) -> None:
    """
    Elimina una tarea específica de la lista de tareas pendientes.

    Args:
        listaTareas (list): Lista de tareas pendientes.
        tarea (str): Título de la tarea que se desea eliminar.

    Returns:
        None
    """
    for i in range(len(listaTareas)):
        if listaTareas[i][0] == tarea:
            del listaTareas[i]
            print("Tarea eliminada exitosamente")
            break
        else:
            print("Tarea no encontrada")


def modificarTarea(listaTareas: list, nombreTarea: str) -> None:
    """
    Modifica los detalles de una tarea específica en la lista de tareas pendientes.

    Args:
        listaTareas (list): Lista de tareas pendientes.
        nombreTarea (str): Título de la tarea que se desea modificar.

    Returns:
        None
    """
    for tarea in listaTareas:
        if tarea[0] == nombreTarea:
            print(
                "Ingrese los nuevos datos de la tarea (Deje en blanco si desea mantener lo que tenía antes)")
            tituloNuevo = input("Ingrese el nuevo título de la tarea: ")
            if tituloNuevo == '':
                pass
            else:
                tarea[0] = tituloNuevo
                print("Título actualizado exitosamente")

            descripcionNueva = input(
                "Ingrese la nueva descripción de la tarea: ")
            if descripcionNueva == '':
                pass
            else:
                tarea[1] = descripcionNueva
                print("Descripción actualizada exitosamente")

            fechaNueva = input("Ingrese la nueva fecha de la tarea: ")
            if fechaNueva == '':
                pass
            else:
                tarea[2] = fechaNueva
                print("Fecha actualizada exitosamente")

            prioridadNueva = input("Ingrese la nueva prioridad de la tarea: ")
            if prioridadNueva == '':
                pass
            else:
                tarea[3] = prioridadNueva
                print("Prioridad actualizada exitosamente")

            print("Tarea actualizada exitosamente")
            break

        else:
            print("Tarea no encontrada")


def realizarTarea(listaTareas: list, tarea: str) -> None:
    """
    Marca una tarea específica como realizada y la traslada a la lista de tareas completadas.

    Args:
        listaTareas (list): Lista de tareas pendientes.
        tarea (str): Título de la tarea que se desea marcar como realizada.

    Returns:
        None
    """
    for i in range(len(listaTareas)):
        if listaTareas[i][0] == tarea:
            TAREAS_HECHAS.append(listaTareas[i])
            del listaTareas[i]
            print("Tarea marcada como realizada exitosamente")
            break
        else:
            print("Tarea no encontrada")


def mostrarTareas(listaTareas: list, Selector: int = 0) -> None:
    """
    Muestra las tareas pendientes o realizadas en la consola.

    Args:
        listaTareas (list): Lista de tareas pendientes o realizadas.
        Selector (int): Valor que determina si se deben mostrar tareas pendientes (0) o realizadas (1).
            Valor predeterminado es 0.

    Returns:
        None
    """

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

# -------------------------------- Ejecución del programa --------------------------------------------
# De momento estamos trabajando en la consola, pero más adelante se implementará una interfaz gráfica


def main():
    """Función principal del programa."""
    print("Bienvenido a OhMyTask")

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Crear tarea")
        print("2. Eliminar tarea")
        print("3. Modificar tarea")
        print("4. Marcar tarea como realizada")
        print("5. Mostrar tareas pendientes")
        print("6. Mostrar tareas realizadas")
        print("7. Visualizar elementos de la tarea")
        print("q. Salir")

        opcion = input(
            "Ingrese la opción que desea realizar (o 'q' para salir): ")

        if opcion == '1':
            TAREAS.append(crearTarea())
        elif opcion in ['2', '3', '4', '7']:    # Opciones que requieren tareas creadas
            if not TAREAS:
                print("No hay tareas creadas.")
            else:
                if opcion == '2':
                    mostrarTareas(TAREAS)
                    tarea_eliminar = input(
                        "Ingrese el título de la tarea que desea eliminar: ")
                    eliminarTarea(TAREAS, tarea_eliminar)
                elif opcion == '3':
                    mostrarTareas(TAREAS)
                    tarea_modificar = input(
                        "Ingrese el título de la tarea que desea modificar: ")
                    modificarTarea(TAREAS, tarea_modificar)
                elif opcion == '4':
                    mostrarTareas(TAREAS)
                    tarea_realizar = input(
                        "Ingrese el título de la tarea que desea marcar como realizada: ")
                    realizarTarea(TAREAS, tarea_realizar)
                elif opcion == '7':  # Visualizar elementos de la tarea
                    mostrarTareas(TAREAS)
                    tarea_visualizar = input(
                        "Ingrese el título de la tarea que desea visualizar: ")
                    for tarea in TAREAS:
                        if tarea[0] == tarea_visualizar:
                            print(
                                f'Título: {tarea[0]}\nDescripción: {tarea[1]}\nFecha: {tarea[2]}\nPrioridad: {tarea[3]}')
                            break
                        else:
                            print("Tarea no encontrada")

        elif opcion == '5':
            mostrarTareas(TAREAS)
        elif opcion == '6':
            mostrarTareas(TAREAS_HECHAS, 1)
        elif opcion.lower() == 'q':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    print("\nPrograma finalizado")
    for task in TAREAS:
        print(task)
    gc.collect()


if __name__ == "__main__":
    main()
