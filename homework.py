# Importa el módulo 'datos', que contiene las listas globales (proyectos, cola_pendientes) 
# y la función de ordenamiento Quicksort
import datos

# Funciones de Análisis y Gestión de Tareas

# Función que muestra todas las tareas de todos los proyectos ordenadas por fecha límite usando Quicksort
def panel_quicksort():
    # Crea una lista plana que contiene todas las tareas de todos los proyectos
    todas = [t for p in datos.proyectos for t in p.lista_tareas]
    if not todas:
        print("No hay tareas.")
        return
    
    # Crea una COPIA de la lista de tareas para que el ordenamiento no altere el estado original 
    # de las tareas dentro de los objetos Proyecto
    tareas_copia = todas.copy()
    
    print("\n=== TAREAS ORDENADAS POR FECHA LÍMITE ===")
    # Llama a la función Quicksort para ordenar la lista de tareas_copia.
    # El ordenamiento se realiza in-place (directamente en la lista).
    datos.quicksort_tareas_por_fecha(tareas_copia, 0, len(tareas_copia)-1)
    
    for t in tareas_copia:
        print(t)
        # Se podría insertar  aquí si fuera relevante para el usuario entender cómo funciona el algoritmo.

# Función que permite buscar tareas basándose en diferentes criterios
def buscar():
    print("\n1. Descripción | 2. Fecha | 3. Estado | 4. Estudiante")
    op = input("→ ")
    term = input("Buscar: ").lower()
    # Itera sobre todas las tareas en todos los proyectos
    for p in datos.proyectos:
        for t in p.lista_tareas:
            # Lógica de búsqueda: Evalúa el criterio seleccionado (op) y si el término (term) 
            # se encuentra en el atributo correspondiente.
            if ((op == "1" and term in t.descripcion.lower()) or
                (op == "2" and term == t.fecha_limite.lower()) or
                (op == "3" and term == t.estado.lower()) or
                 # Se asegura de que haya una matrícula asignada antes de intentar buscar en ella (op == "4")
                (op == "4" and t.matricula_asignada and term in t.matricula_asignada.lower())):
                print(f"[Proyecto: {p.nombre}] {t}")

# Función para gestionar la cola de tareas pendientes (implementación FIFO)
def cola_fifo():
    print("\n=== COLA PENDIENTES (FIFO) ===")
    if not datos.cola_pendientes:
        print("No hay pendientes")
        return
    # Muestra las tareas en la cola, donde la tarea con el índice 1 es la que entró primero (FIFO)
    for i, t in enumerate(datos.cola_pendientes, 1):
        print(f"{i}. {t}")
    # Opción para completar la tarea que está al frente de la cola (índice 0)
    if input("¿Completar la primera? (s/n): ").lower() == "s":
        # Intenta marcar la tarea como finalizada (la tarea verifica sus propias dependencias)
        if datos.cola_pendientes[0].marcar_finalizada():
            # Si se finaliza con éxito, se remueve de la cola (pop(0) = primer elemento), simulando el 'dequeue'
            datos.cola_pendientes.pop(0)
            # Guarda los cambios en la base de datos
            datos.guardar_datos()
            # Se podría insertar  para ilustrar el concepto de cola.

# Función para visualizar las dependencias de tareas como un árbol (o grafo acíclico dirigido, DAG)
def arbol_dependencias():
    print("Seleccione un proyecto para ver su árbol de dependencias:")
    if not datos.proyectos:
        return
    # Permite al usuario seleccionar un proyecto
    for i, p in enumerate(datos.proyectos, 1):
        print(f"{i}. {p.nombre}")
    n = int(input("Proyecto: ")) - 1
    if 0 <= n < len(datos.proyectos):
        p = datos.proyectos[n]
        print(f"\nÁrbol de {p.nombre}:")
        visitados = set()# Conjunto para evitar bucles infinitos en caso de dependencias circulares (aunque no deberían existir)
         # Función recursiva auxiliar para imprimir la estructura de árbol/grafo
        def imprimir(t, indent=""):
            # Evita procesar tareas ya visitadas
            if t in visitados: return
            visitados.add(t)
            print(f"{indent}└→ {t}")
            # Llamada recursiva: Procesa las tareas que dependen de la tarea actual (sus dependencias)
            for dep in t.dependencias:
                imprimir(dep, indent + "   ")
        # Itera sobre todas las tareas del proyecto para asegurar que se impriman incluso las que no tienen dependencias
        for t in p.lista_tareas:
            if t not in visitados:
                imprimir(t)
                # Se podría insertar  para visualizar la relación de dependencias.
    print("Quieres editar la dependencia?")
    if input("s/n: ").lower() == "s":
        desc=input("Nombre de la tarea a editar:")
        for t in p.lista_tareas:
            if t.descripcion.lower() == desc.lower():
                print("1. Cambiar dependencia")
                print("2. Eliminar dependencia")
                op=input("→ ")
                desc_dep=input("Descripción de la tarea dependencia: ")
                for t_dep in p.lista_tareas:
                    if t_dep.descripcion.lower() == desc_dep.lower():
                        if op == "1":
                            t.agregar_dependencia(t_dep)
                            print(f"Dependencia '{t_dep.descripcion}' agregada a '{t.descripcion}'")
                        elif op == "2":
                            t.eliminar_dependencia(t_dep)
                            print(f"Dependencia '{t_dep.descripcion}' eliminada de '{t.descripcion}'")
                        datos.guardar_datos()
                        return
                print("Tarea dependencia no encontrada.")
                return

# Función para marcar una tarea como finalizada buscando por su descripción
def marcar_finalizada():
    desc = input("Descripción exacta: ")
    # Itera sobre todas las tareas para encontrar la que coincide con la descripción
    for p in datos.proyectos:
        for t in p.lista_tareas:
            if t.descripcion.lower() == desc.lower():
                 # Llama al método de la Tarea, que verifica si se cumplen las dependencias
                if t.marcar_finalizada():
                    # Si la tarea estaba en la cola de pendientes, se remueve
                    if t in datos.cola_pendientes:
                        datos.cola_pendientes.remove(t)
                    datos.guardar_datos()
                return  # Termina la función tan pronto como se encuentra la tarea
    print("No encontrada")

# Función que despliega y maneja el menú principal para la gestión y análisis de tareas
def mostrar_menu_tareas():
    while True:
        print("\n" + "="*40)
        print("         GESTIÓN DE TAREAS")
        print("="*40)
        # Opciones de menú que reflejan las funciones de análisis y estructura de datos
        print("1. Panel ordenado (Quicksort)")
        print("2. Buscar tareas")
        print("3. Cola pendientes (FIFO)")
        print("4. Árbol de dependencias")
        print("5. Marcar tarea finalizada")
        print("6. Volver")
        op = input("→ ")
        if op == "1": panel_quicksort()
        elif op == "2": buscar()
        elif op == "3": cola_fifo()
        elif op == "4": arbol_dependencias()
        elif op == "5": marcar_finalizada()
        elif op == "6": break
