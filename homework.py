import datos

def panel_quicksort():
    todas = [t for p in datos.proyectos for t in p.lista_tareas]
    if not todas:
        print("No hay tareas.")
        return
    
    # Hacemos una COPIA para no modificar el orden original en los proyectos
    tareas_copia = todas.copy()
    
    print("\n=== TAREAS ORDENADAS POR FECHA LÍMITE ===")
    datos.quicksort_tareas_por_fecha(tareas_copia, 0, len(tareas_copia)-1)
    
    for t in tareas_copia:
        print(t)

def buscar():
    print("\n1. Descripción | 2. Fecha | 3. Estado | 4. Estudiante")
    op = input("→ ")
    term = input("Buscar: ").lower()
    for p in datos.proyectos:
        for t in p.lista_tareas:
            if ((op == "1" and term in t.descripcion.lower()) or
                (op == "2" and term == t.fecha_limite.lower()) or
                (op == "3" and term == t.estado.lower()) or
                (op == "4" and t.matricula_asignada and term in t.matricula_asignada.lower())):
                print(f"[Proyecto: {p.nombre}] {t}")

def cola_fifo():
    print("\n=== COLA PENDIENTES (FIFO) ===")
    if not datos.cola_pendientes:
        print("No hay pendientes")
        return
    for i, t in enumerate(datos.cola_pendientes, 1):
        print(f"{i}. {t}")
    if input("¿Completar la primera? (s/n): ").lower() == "s":
        if datos.cola_pendientes[0].marcar_finalizada():
            datos.cola_pendientes.pop(0)
            datos.guardar_datos()

def arbol_dependencias():
    if not datos.proyectos:
        return
    for i, p in enumerate(datos.proyectos, 1):
        print(f"{i}. {p.nombre}")
    n = int(input("Proyecto: ")) - 1
    if 0 <= n < len(datos.proyectos):
        p = datos.proyectos[n]
        print(f"\nÁrbol de {p.nombre}:")
        visitados = set()
        def imprimir(t, indent=""):
            if t in visitados: return
            visitados.add(t)
            print(f"{indent}└→ {t}")
            for dep in t.dependencias:
                imprimir(dep, indent + "   ")
        for t in p.lista_tareas:
            if t not in visitados:
                imprimir(t)

def marcar_finalizada():
    desc = input("Descripción exacta: ")
    for p in datos.proyectos:
        for t in p.lista_tareas:
            if t.descripcion.lower() == desc.lower():
                if t.marcar_finalizada():
                    if t in datos.cola_pendientes:
                        datos.cola_pendientes.remove(t)
                    datos.guardar_datos()
                return
    print("No encontrada")

def mostrar_menu_tareas():
    while True:
        print("\n" + "="*40)
        print("         GESTIÓN DE TAREAS")
        print("="*40)
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