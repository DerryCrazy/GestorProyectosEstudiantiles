from clases import Estudiante, Tarea, Proyecto
import json
import os

# Estas listas son como el boceto de la base de datos
estudiantes = []       # lista de Estudiante
proyectos = []         # lista de Proyecto
todas_las_tareas = []  # lista de Tarea
cola_pendientes = []   # cola FIFO de tareas pendientes


def cargar_datos():
    global estudiantes, proyectos
    # Cargar estudiantes (ya funcionando)
    if os.path.exists("estudiantes.json"):
        with open("estudiantes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            estudiantes = [Estudiante(e["nombre"], e["matricula"]) for e in data]
    else:
        estudiantes = []

    # Cargar proyectos
    if os.path.exists("proyectos.json"):
        with open("proyectos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            estudiantes_dict = {e.matricula: e for e in estudiantes}  # Para resolver equipo
            proyectos = []
            for p_data in data:
                p = Proyecto(p_data["nombre"], p_data.get("estado", "activo"))
                # Equipo
                for mat in p_data.get("equipo", []):
                    if mat in estudiantes_dict:
                        p.agregar_estudiante(estudiantes_dict[mat])
                # Tareas
                for t_data in p_data.get("lista_tareas", []):
                    t = Tarea(
                        t_data["descripcion"],
                        t_data["fecha_limite"],
                        t_data.get("estado", "pendiente"),
                        t_data.get("matricula_asignada")
                    )
                    p.agregar_tarea(t)
                # Dependencias (reconstruir con índices)
                dependencias = p_data.get("dependencias", [])
                for i in range(len(p.lista_tareas)):
                    if i < len(dependencias):
                        for idx in dependencias[i]:
                            if 0 <= idx < len(p.lista_tareas):
                                p.lista_tareas[i].agregar_dependencia(p.lista_tareas[idx])
                proyectos.append(p)
    else:
        proyectos = []

def guardar_datos():
    # Guardar estudiantes (ya funcionando)
    data_est = [{"nombre": e.nombre, "matricula": e.matricula} for e in estudiantes]
    with open("estudiantes.json", "w", encoding="utf-8") as f:
        json.dump(data_est, f, indent=4)

    # Guardar proyectos
    data_proy = []
    for p in proyectos:
        tareas_data = [{
            "descripcion": t.descripcion,
            "fecha_limite": t.fecha_limite,
            "estado": t.estado,
            "matricula_asignada": t.matricula_asignada
        } for t in p.lista_tareas]
        dependencias = []
        for t in p.lista_tareas:
            deps_indices = [p.lista_tareas.index(dep) for dep in t.dependencias if dep in p.lista_tareas]
            dependencias.append(deps_indices)
        data_proy.append({
            "nombre": p.nombre,
            "estado": p.estado,
            "equipo": [e.matricula for e in p.equipo],
            "lista_tareas": tareas_data,
            "dependencias": dependencias
        })
    with open("proyectos.json", "w", encoding="utf-8") as f:
        json.dump(data_proy, f, indent=4)

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