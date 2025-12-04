from clases import Tarea
import datos
from ordenamiento import quicksort_tareas_por_fecha

#archivo para funciones relacionadas con las cochinas tareas

def crear_tarea():
    print("--- Crear tarea ---")
    nombre_proyecto = input("Nombre del proyecto al que pertenece la tarea: ")
    proyecto = datos.buscar_proyecto_por_nombre(nombre_proyecto)

    if proyecto is None:
        print("No existe un proyecto con ese nombre")
        return

    descripcion = input("Descripción de la tarea: ")
    fecha = input("Fecha límite (año-mes-dia): ")
    mat = input("Matrícula del estudiante asignado: ")

    tarea = Tarea(descripcion, fecha, mat)

    ''' Crear algo apra guardar la tarea en el proyecto y en una lista general
        y una lista de tareas pendientes
'''    
  
