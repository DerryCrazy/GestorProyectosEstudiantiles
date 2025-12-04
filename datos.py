from clases import Estudiante, Tarea, Proyecto

# Estas listas son como el boceto de la base de datos
estudiantes = []       # lista de Estudiante
proyectos = []         # lista de Proyecto
todas_las_tareas = []  # lista de Tarea
cola_pendientes = []   # cola FIFO de tareas pendientes


def buscar_estudiante_por_matricula(matricula):
    for e in estudiantes:
        if e.matricula == matricula:
            return e
    return None


def buscar_proyecto_por_nombre(nombre):
    for p in proyectos:
        if p.nombre == nombre:
            return p
    return None