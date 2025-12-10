import datos

def crear_proyecto():
    print("\n--- Crear Proyecto ---")
    nombre = input("Nombre del proyecto: ").strip()

    # Verificar si existe
    for p in datos.proyectos:
        if p.nombre.lower() == nombre.lower():
            print("¡Error! Proyecto con ese nombre ya existe.")
            return

    nuevo = datos.Proyecto(nombre)
    datos.proyectos.append(nuevo)
    datos.guardar_datos()
    print(f"Proyecto '{nombre}' creado correctamente como activo.")

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
        print("4. Volver al menú principal")
        print("="*35)

        op = input("Elige una opción: ")
        if op == "1":
            crear_proyecto()
        elif op == "2":
            listar_proyectos()
        elif op == "3":
            cambiar_estado_proyecto()
        elif op == "4":
            datos.guardar_datos()  # Guarda al salir
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida.")