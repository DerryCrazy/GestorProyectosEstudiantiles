from clases import Proyecto
import datos
#este archivo se va a usar para poner funciones relacionadas con los proyectos

def crear_proyecto():
    print("--- Crear proyecto ---")
    nombre = input("Nombre del proyecto: ")

    if datos.buscar_proyecto_por_nombre(nombre) is not None:
        print("Ya existe un proyecto con ese nombre.")
        return

    proyecto = Proyecto(nombre)