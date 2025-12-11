# Importa la librería 'json' para manejar la serialización/deserialización de datos
import json
# Importa la librería 'os' para interactuar con el sistema operativo (ej. verificar la existencia de archivos)
import os
# Importa las clases personalizadas definidas en 'clases.py'
from clases import Estudiante, Tarea, Proyecto
# Importa la función de ordenamiento Quicksort para tareas
from ordenamiento import quicksort_tareas_por_fecha

# Listas globales que almacenarán los objetos de datos en memoria
estudiantes = []
proyectos = []
# Cola global que gestiona las tareas pendientes, siguiendo el principio FIFO (First-In, First-Out)
cola_pendientes = []  # Cola FIFO global

# Función principal para cargar los datos desde archivos JSON al iniciar el programa
def cargar_datos():
    # Declara las variables como globales para poder modificarlas dentro de la función
    global estudiantes, proyectos, cola_pendientes
    # Limpia las listas globales para evitar duplicación al recargar
    estudiantes.clear()
    proyectos.clear()
    cola_pendientes.clear()

    # Cargar estudiantes
    # Verifica si el archivo de estudiantes existe
    if os.path.exists("estudiantes.json"):
        # Abre y lee el archivo JSON.
        with open("estudiantes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            # Crea objetos Estudiante a partir de los datos cargados y los añade a la lista global
            estudiantes.extend([Estudiante(d["nombre"], d["matricula"]) for d in data])

    # Cargar proyectos
    # Verifica si el archivo de proyectos existe
    if os.path.exists("proyectos.json"):
        # Abre y lee el archivo JSON
        with open("proyectos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
             # Crea un diccionario de estudiantes (matricula -> objeto Estudiante) para búsquedas rápidas
            est_dict = {e.matricula: e for e in estudiantes}
            # Itera sobre los datos de cada proyecto
            for p_data in data:
                # Crea el objeto Proyecto
                p = Proyecto(p_data["nombre"], p_data.get("estado", "activo"))
                # Reconstruye el equipo de estudiantes (usando las matrículas guardadas)
                for mat in p_data.get("equipo", []):
                    if mat in est_dict:
                        p.agregar_estudiante(est_dict[mat])
                # Reconstruye las Tareas
                tareas_temp = []
                for t_data in p_data.get("lista_tareas", []):
                    # Crea el objeto Tarea con sus atributos
                    t = Tarea(
                        t_data["descripcion"],
                        t_data["fecha_limite"],
                        t_data.get("estado", "pendiente"),
                        t_data.get("matricula_asignada")
                    )
                    tareas_temp.append(t)
                # Asigna la lista de tareas al proyecto
                p.lista_tareas = tareas_temp
                # Reconstruir dependencias
                # Las dependencias se guardaron como índices
                deps = p_data.get("dependencias", [])
                # Itera sobre cada tarea
                for i in range(len(tareas_temp)):
                    if i < len(deps):
                        # Itera sobre los índices de las dependencias para esta tarea 'i'
                        for idx in deps[i]:
                            # Verifica que el índice sea válido
                            if 0 <= idx < len(tareas_temp):
                                # Usa el índice para obtener el objeto Tarea dependiente y añadirlo
                                tareas_temp[i].agregar_dependencia(tareas_temp[idx])
                proyectos.append(p)

    # Reconstruir cola FIFO (cola_pendientes)
    # Itera sobre todas las tareas de todos los proyectos
    for p in proyectos:
        for t in p.lista_tareas:
            # Si una tarea está pendiente, se añade a la cola global
            if t.estado == "pendiente":
                cola_pendientes.append(t)

# Función principal para guardar los datos de memoria en archivos JSON
def guardar_datos():
    # Guardar estudiantes
    # Abre el archivo para escritura ('w')
    with open("estudiantes.json", "w", encoding="utf-8") as f:
         # Serializa (convierte a JSON) la lista de estudiantes, guardando solo nombre y matrícula
        json.dump([{"nombre": e.nombre, "matricula": e.matricula} for e in estudiantes], f, indent=4)

    # Guardar proyectos
    proyectos_data = []
    for p in proyectos:
        tareas_data = []
        # Prepara la data de las tareas para la serialización
        for t in p.lista_tareas:
            tareas_data.append({
                "descripcion": t.descripcion,
                "fecha_limite": t.fecha_limite,
                "estado": t.estado,
                "matricula_asignada": t.matricula_asignada
            })
        # Dependencias como índices
        # Calcula y guarda las dependencias como índices (más fácil de guardar que referencias a objetos)
        dependencias = []
        for t in p.lista_tareas:
             # Obtiene el índice de cada tarea dependiente dentro de la lista 'p.lista_tareas'
            deps_idx = [p.lista_tareas.index(d) for d in t.dependencias if d in p.lista_tareas]
            dependencias.append(deps_idx)

        # Prepara la data del proyecto (incluye la lista de tareas y las dependencias separadas por índice)
        proyectos_data.append({
            "nombre": p.nombre,
            "estado": p.estado,
             # Guarda solo las matrículas de los miembros del equipo
            "equipo": [e.matricula for e in p.equipo],
            "lista_tareas": tareas_data,
            "dependencias": dependencias
        })

    # Guarda la lista final de proyectos serializada
    with open("proyectos.json", "w", encoding="utf-8") as f:
        json.dump(proyectos_data, f, indent=4)
