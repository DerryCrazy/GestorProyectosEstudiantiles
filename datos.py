import json
import os
from clases import Estudiante, Tarea, Proyecto
from ordenamiento import quicksort_tareas_por_fecha

estudiantes = []
proyectos = []
cola_pendientes = []  # Cola FIFO global


def cargar_datos():
    global estudiantes, proyectos, cola_pendientes
    estudiantes.clear()
    proyectos.clear()
    cola_pendientes.clear()

    # Cargar estudiantes
    if os.path.exists("estudiantes.json"):
        with open("estudiantes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            estudiantes.extend([Estudiante(d["nombre"], d["matricula"]) for d in data])

    # Cargar proyectos
    if os.path.exists("proyectos.json"):
        with open("proyectos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            est_dict = {e.matricula: e for e in estudiantes}
            for p_data in data:
                p = Proyecto(p_data["nombre"], p_data.get("estado", "activo"))
                # Equipo
                for mat in p_data.get("equipo", []):
                    if mat in est_dict:
                        p.agregar_estudiante(est_dict[mat])
                # Tareas
                tareas_temp = []
                for t_data in p_data.get("lista_tareas", []):
                    t = Tarea(
                        t_data["descripcion"],
                        t_data["fecha_limite"],
                        t_data.get("estado", "pendiente"),
                        t_data.get("matricula_asignada")
                    )
                    tareas_temp.append(t)
                p.lista_tareas = tareas_temp
                # Reconstruir dependencias
                deps = p_data.get("dependencias", [])
                for i in range(len(tareas_temp)):
                    if i < len(deps):
                        for idx in deps[i]:
                            if 0 <= idx < len(tareas_temp):
                                tareas_temp[i].agregar_dependencia(tareas_temp[idx])
                proyectos.append(p)

    # Reconstruir cola FIFO
    for p in proyectos:
        for t in p.lista_tareas:
            if t.estado == "pendiente":
                cola_pendientes.append(t)

def guardar_datos():
    # Guardar estudiantes
    with open("estudiantes.json", "w", encoding="utf-8") as f:
        json.dump([{"nombre": e.nombre, "matricula": e.matricula} for e in estudiantes], f, indent=4)

    # Guardar proyectos
    proyectos_data = []
    for p in proyectos:
        tareas_data = []
        for t in p.lista_tareas:
            tareas_data.append({
                "descripcion": t.descripcion,
                "fecha_limite": t.fecha_limite,
                "estado": t.estado,
                "matricula_asignada": t.matricula_asignada
            })
        # Dependencias como índices
        dependencias = []
        for t in p.lista_tareas:
            deps_idx = [p.lista_tareas.index(d) for d in t.dependencias if d in p.lista_tareas]
            dependencias.append(deps_idx)

        proyectos_data.append({
            "nombre": p.nombre,
            "estado": p.estado,
            "equipo": [e.matricula for e in p.equipo],
            "lista_tareas": tareas_data,
            "dependencias": dependencias
        })

    with open("proyectos.json", "w", encoding="utf-8") as f:
        json.dump(proyectos_data, f, indent=4)