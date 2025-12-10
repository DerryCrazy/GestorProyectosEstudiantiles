import datos
from est import buscar_estudiante_por_matricula  # Si no tienes, agrega en est.py: def buscar_estudiante_por_matricula(mat): ... como antes

def crear_proyecto():
    print("\n--- Crear Proyecto ---")
    nombre = input("Nombre del proyecto: ").strip()
    if any(p.nombre.lower() == nombre.lower() for p in datos.proyectos):
        print("❌ Proyecto ya existe.")
        return

    nuevo = datos.Proyecto(nombre)
    datos.proyectos.append(nuevo)
    print(f"✅ Proyecto '{nombre}' creado como activo.")

    # Flujo opcional: ¿agregar tasks/estudiantes ahora?
    if input("¿Quieres agregar estudiantes o tareas ahora? (s/n): ").lower() == 's':
        editar_proyecto(nuevo)  # Llama directo al editor
    datos.guardar_datos()

def agregar_estudiante_a_proyecto(proyecto):
    print("\n--- Agregar Estudiante a Proyecto ---")
    listar_estudiantes_disponibles(proyecto)  # Función helper abajo
    mat = input("Matrícula del estudiante: ").strip().upper()
    estudiante = buscar_estudiante_por_matricula(mat)
    if estudiante and estudiante not in proyecto.equipo:
        proyecto.agregar_estudiante(estudiante)
        print(f"✅ {estudiante} agregado a '{proyecto.nombre}'.")
    else:
        print("❌ Estudiante no encontrado o ya en equipo.")

def agregar_tarea_a_proyecto(proyecto):
    print(f"\n--- Agregar Tarea a '{proyecto.nombre}' ---")
    desc = input("Descripción: ").strip()
    fecha = input("Fecha límite (YYYY-MM-DD): ").strip()
    mat_asignada = input("Matrícula asignada (o Enter para none): ").strip().upper() or None
    if mat_asignada:
        est = buscar_estudiante_por_matricula(mat_asignada)
        if not est:
            print("❌ Estudiante no encontrado. Tarea sin asignar.")
            mat_asignada = None

    # Dependencia opcional (simple: ¿depende de tarea existente?)
    nueva_tarea = datos.Tarea(desc, fecha, matricula_asignada=mat_asignada)
    if proyecto.lista_tareas:
        dep_num = input(f"¿Depende de tarea existente? (número 1-{len(proyecto.lista_tareas)}, o Enter para none): ")
        if dep_num.isdigit():
            idx = int(dep_num) - 1
            if 0 <= idx < len(proyecto.lista_tareas):
                nueva_tarea.agregar_dependencia(proyecto.lista_tareas[idx])
                print(f"✅ Dependencia agregada: depende de '{proyecto.lista_tareas[idx].descripcion}'.")

    proyecto.agregar_tarea(nueva_tarea)
    print(f"✅ Tarea '{desc}' agregada.")
    datos.guardar_datos()

def listar_estudiantes_disponibles(proyecto):
    print("Estudiantes disponibles (no en equipo):")
    disponibles = [e for e in datos.estudiantes if e not in proyecto.equipo]
    for i, e in enumerate(disponibles, 1):
        print(f"{i}. {e}")

def editar_proyecto(proyecto_especifico=None):
    if not datos.proyectos:
        print("❌ No hay proyectos.")
        return
    if proyecto_especifico is None:
        listar_proyectos()  # Tu función actual
        try:
            num = int(input("Número del proyecto a editar: ")) - 1
            proyecto_especifico = datos.proyectos[num]
        except:
            print("❌ Número inválido.")
            return

    while True:
        print(f"\n--- Editando '{proyecto_especifico.nombre}' ---")
        print("1. Agregar estudiante")
        print("2. Agregar tarea")
        print("3. Ver detalles (equipo + tareas)")
        print("4. Salir")
        op = input("Opción: ")
        if op == "1":
            agregar_estudiante_a_proyecto(proyecto_especifico)
        elif op == "2":
            agregar_tarea_a_proyecto(proyecto_especifico)
        elif op == "3":
            print(f"Equipo: {[str(e) for e in proyecto_especifico.equipo]}")
            print("Tareas:")
            for t in proyecto_especifico.lista_tareas:
                print(f"  - {t}")
        elif op == "4":
            break

def listar_proyectos():
    print("\n" + "="*50)
    print("          LISTA DE PROYECTOS")
    print("="*50)
    
    if not datos.proyectos:
        print("No hay proyectos registrados aún.")
        print("="*50)
        return

    for i, p in enumerate(datos.proyectos, 1):
        estado_icon = "Activo" if p.estado == "activo" else "Finalizado"
        print(f"{i}. {p.nombre} [{estado_icon}]")
        print(f"    Equipo: {len(p.equipo)} estudiante(s) | Tareas: {len(p.lista_tareas)}")
        
        if p.lista_tareas:
            print("    Tareas:")
            for j, tarea in enumerate(p.lista_tareas, 1):
                asignado = f" → {datos.buscar_estudiante_por_matricula(tarea.matricula_asignada).nombre}" if tarea.matricula_asignada else ""
                depende = ""
                if tarea.dependencias:
                    # Mostrar de qué tarea(s) depende
                    nombres_deps = [dep.descripcion for dep in tarea.dependencias]
                    depende = f" (depende de: {', '.join(nombres_deps)})"
                print(f"       • [{tarea.estado}] {tarea.descripcion} → {tarea.fecha_limite}{asignado}{depende}")
        else:
            print("    → Sin tareas aún")
        print("-" * 50)

def cambiar_estado_proyecto():
    print("\n--- Cambiar Estado de Proyecto ---")
    if not datos.proyectos:
        print("No hay proyectos.")
        return

    listar_proyectos()
    try:
        num = int(input("\nNúmero del proyecto (0 para cancelar): "))
        if num == 0:
            return
        if 1 <= num <= len(datos.proyectos):
            p = datos.proyectos[num - 1]
            nuevo = "finalizado" if p.estado == "activo" else "activo"
            p.cambiar_estado(nuevo)
            datos.guardar_datos()
        else:
            print("Número inválido.")
    except ValueError:
        print("Ingresa un número válido.")

def mostrar_menu_proyectos():
    datos.cargar_datos()  # Carga al entrar
    while True:
        print("\n" + "="*35)
        print("     GESTIÓN DE PROYECTOS")
        print("="*35)
        print("1. Crear proyecto")
        print("2. Listar proyectos")
        print("3. Cambiar estado (activo/finalizado)")
        print("4. Editar proyecto (agregar estudiantes/tareas)")
        print("5. Volver al menú principal")
        print("="*35)

        op = input("Elige una opción: ")
        if op == "1":
            crear_proyecto()
        elif op == "2":
            listar_proyectos()
        elif op == "3":
            cambiar_estado_proyecto()
        elif op == "4":
            editar_proyecto()
        elif op == "5":
            datos.guardar_datos()  # Guarda al salir
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida.")