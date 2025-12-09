from clases import Proyecto, Estudiante
import datos
#este archivo se va a usar para poner funciones relacionadas con los proyectos

def crear_proyecto():
    print("--- Crear proyecto ---")
    nombre = input("Nombre del proyecto: ")

    if datos.buscar_proyecto_por_nombre(nombre) is not None:
        print("Ya existe un proyecto con ese nombre.")
        return

    proyecto = Proyecto(nombre)
    datos.proyectos.append(proyecto) # Agrega a la lista de proyectos
    print("Proyecto '{nombre}' creado exitosamente.")
    
def listar_proyectos():
        print("\n--- Listar Proyectos ---")
        if not datos.proyectos:
             print("No hay proyectos registrados.")
             return
        
        for i, proyecto in enumerate(datos.proyectos, start=1):
            print(f"{i}. {proyecto.nombre} - Miembros: {len(proyecto.equipo)} - Tareas: {len(proyecto.lista_tareas)}")

def buscar_proyecto():
    print("\n--- Buscar Proyecto ---")
    nombre_busqueda = input("Ingresa el nombre del proyecto a buscar: ")
    proyecto = datos.buscar_proyecto_por_nombre(nombre_busqueda)

    if proyecto:
        print(f"Proyecto encontrado: {proyecto.nombre}")
        print(f"  - Miembros: {len(proyecto.equipo)}")
        for est in proyecto.equipo:
            print(f"    * {est.nombre} (Matrícula: {est.matricula})")
        print(f"  - Tareas ({len(proyecto.lista_tareas)}):")
        for tarea in proyecto.lista_tareas:
            print(f"    * {tarea.descripcion} [{tarea.estado}] (Fecha: {tarea.fecha_limite})")
    else:
        print("Proyecto no encontrado.")


def asignar_estudiante_a_proyecto():
    print("\n--- Asignar Estudiante a Proyecto ---")
    nombre_proyecto = input("Nombre del proyecto: ")
    proyecto = datos.buscar_proyecto_por_nombre(nombre_proyecto)
    
    if not proyecto:
        print("Proyecto no encontrado.")
        return

    matricula_estudiante = input("Matrícula del estudiante a asignar: ")
    estudiante = datos.buscar_estudiante_por_matricula(matricula_estudiante)
    if not estudiante:
        print("Estudiante no encontrado.")
        return
    if estudiante in proyecto.equipo:
        print(f"El estudiante {estudiante.nombre} ya está en el equipo del proyecto '{nombre_proyecto}'.")
    else:
        proyecto.equipo.append(estudiante)
        print(f"Estudiante {estudiante.nombre} asignado al proyecto '{nombre_proyecto}'.")
        # datos.guardar_datos() # Llama a la función de guardar si está implementada

