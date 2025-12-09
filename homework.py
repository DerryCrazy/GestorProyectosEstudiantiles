from clases import Tarea
import datos
import ordenamiento
from datetime import datetime

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

    mat = input("Matrícula del estudiante asignado (dejar vacío si no se asigna): ")
    estudiante_asignado = None
    if mat:
        estudiante_asignado = datos.buscar_estudiante_por_matricula(mat)
        if estudiante_asignado is None:
            print("No existe un estudiante con esa matrícula. La tarea no se asignará.")
            mat = None # No asignar si no existe

    tarea = Tarea(descripcion, fecha, matricula_asignada=mat)
    proyecto.agregar_tarea(tarea)
    datos.todas_las_tareas.append(tarea) # Añadir a la lista general
    
    # Agrega a la cola FIFO de pendientes si su estado es 'pendiente'
    if tarea.estado == "pendiente":
        datos.cola_pendientes.append(tarea)

    #datos.guardar_datos() # Llamar a la función de guardar si existe
    print(f"Tarea '{descripcion}' creada y asignada al proyecto '{nombre_proyecto}'.")


def listar_tareas_ordenadas():
    print("\n--- Listar Tareas Ordenadas por Fecha ---")
    
    if not datos.todas_las_tareas:
        print("No hay tareas registradas.")
        return
    
    # Crear copia para no alterar la lista original al ordenarla
    tareas_a_mostrar = datos.todas_las_tareas.copy()
    # Llamar a quicksort recursivo
    ordenamiento.quicksort_tareas_por_fecha(tareas_a_mostrar, 0, len(tareas_a_mostrar) - 1)
    
    print("\nTareas ordenadas por fecha límite:")
    for i, tarea in enumerate(tareas_a_mostrar, start=1):
        print(f"{i}. [{tarea.estado}] {tarea.descripcion} | Proyecto: {next((p.nombre for p in datos.proyectos if tarea in p.lista_tareas), 'Desconocido')} | Fecha: {tarea.fecha_limite} | Asignada a: {tarea.matricula_asignada or 'Nadie'}")


def buscar_tareas():
    print("\n--- Buscar Tareas ---")
    print("Buscar por: 1) Descripción, 2) Fecha, 3) Estado, 4) Estudiante")
    opcion = input("Selecciona una opción (1-4): ")

    resultados = []
    if opcion == '1':
        descripcion_busqueda = input("Ingresa la descripción a buscar: ").lower()
        for tarea in datos.todas_las_tareas:
            if descripcion_busqueda in tarea.descripcion.lower():
                resultados.append(tarea)
    elif opcion == '2':
        fecha_busqueda = input("Ingresa la fecha límite a buscar (YYYY-MM-DD): ")
        for tarea in datos.todas_las_tareas:
            if tarea.fecha_limite == fecha_busqueda:
                resultados.append(tarea)
    elif opcion == '3':
        estado_busqueda = input("Ingresa el estado a buscar (pendiente, en progreso, finalizada): ").lower()
        for tarea in datos.todas_las_tareas:
            if tarea.estado.lower() == estado_busqueda:
                resultados.append(tarea)
    elif opcion == '4':
        mat_busqueda = input("Ingresa la matrícula del estudiante: ")
        for tarea in datos.todas_las_tareas:
            if tarea.matricula_asignada == mat_busqueda:
                resultados.append(tarea)
    else:
        print("Opción inválida.")
        return

    if not resultados:
        print("No se encontraron tareas con esos criterios.")
    else:
        print("\nResultados de la búsqueda:")
        for tarea in resultados:
            print(f"- {tarea}")


def marcar_tarea_como_finalizada():
    print("\n--- Marcar Tarea como Finalizada ---")
    listar_tareas_ordenadas() # Mostrar tareas para elegir
    if not datos.todas_las_tareas:
        return
    try:
        indice = int(input("Ingrese el número de la tarea a finalizar: ")) - 1
        # Usamos la lista ordenada generada en listar_tareas_ordenadas
        tareas_ordenadas = datos.todas_las_tareas.copy()
        ordenamiento.quicksort_tareas_por_fecha(tareas_ordenadas, 0, len(tareas_ordenadas) - 1)

        if 0 <= indice < len(tareas_ordenadas):
            tarea_a_finalizar = tareas_ordenadas[indice]
            
            # Verificar dependencias
            if tarea_a_finalizar.dependencias:
                dependencias_incompletas = [dep for dep in tarea_a_finalizar.dependencias if dep.estado != 'finalizada']
                if dependencias_incompletas:
                    print(f"\nNo se puede finalizar '{tarea_a_finalizar.descripcion}' porque las siguientes tareas dependientes no están finalizadas:")
                    for dep in dependencias_incompletas:
                        print(f" - {dep.descripcion}")
                    return
                
            tarea_a_finalizar.estado = "finalizada"
            
            # Opcional: Sacarla de la cola de pendientes si estaba allí
            # Esto es O(n) para cada operación de búsqueda y eliminación en la lista
            if tarea_a_finalizar in datos.cola_pendientes:
                 datos.cola_pendientes.remove(tarea_a_finalizar) # Dequeue (si está en la cola)
            
            print(f"Tarea '{tarea_a_finalizar.descripcion}' marcada como finalizada.")
            # datos.guardar_datos() # Llamar a la función de guardar si existe
        else:
            print("Número de tarea inválido.")
    except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
