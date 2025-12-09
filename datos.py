from clases import Estudiante, Tarea, Proyecto
import json
import os

# Estas listas son como el boceto de la base de datos
estudiantes = []       # lista de Estudiante
proyectos = []         # lista de Proyecto
todas_las_tareas = []  # lista de Tarea
cola_pendientes = []   # cola FIFO de tareas pendientes


def cargar_estudiantes():
    global estudiantes
    if os.path.exists("estudiantes.json"):
        with open("estudiantes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            estudiantes = [Estudiante(e["nombre"], e["matricula"]) for e in data]
    else:
        estudiantes = []

def guardar_estudiantes():
    data = [{"nombre": e.nombre, "matricula": e.matricula} for e in estudiantes]
    with open("estudiantes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

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