import datos

def crear_proyecto():
    nombre = input("Nombre del proyecto: ")
    if any(p.nombre.lower() == nombre.lower() for p in datos.proyectos):
        print("Ya existe")
        return
    p = datos.Proyecto(nombre)
    datos.proyectos.append(p)
    datos.guardar_datos()
    print("Proyecto creado")
    if input("¿Agregar tareas/estudiantes ahora? (s/n): ").lower() == "s":
        editar_proyecto(p)

def listar_proyectos():
    print("\n=== PROYECTOS ===")
    for i, p in enumerate(datos.proyectos, 1):
        print(f"{i}. {p}")
        for t in p.lista_tareas:
            print(f"   • {t}")
        print("-" * 40)

def editar_proyecto(p=None):
    if p is None:
        listar_proyectos()
        try:
            n = int(input("Número de proyecto: ")) - 1
            p = datos.proyectos[n]
        except:
            return

    while True:
        print(f"\nEditando: {p.nombre}")
        print("1. Agregar estudiante")
        print("2. Agregar tarea")
        print("3. Cambiar estado proyecto")
        print("4. Volver")
        op = input("→ ")
        if op == "1":
            mat = input("Matrícula: ").upper()
            est = next((e for e in datos.estudiantes if e.matricula == mat), None)
            if est and est not in p.equipo:
                p.agregar_estudiante(est)
                datos.guardar_datos()
        elif op == "2":
            desc = input("Descripción: ")
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            mat = input("Matrícula asignada (enter = none): ").upper() or None
            t = datos.Tarea(desc, fecha, matricula_asignada=mat)
            if p.lista_tareas:
                dep = input(f"¿Depende de tarea? (1-{len(p.lista_tareas)} o enter): ")
                if dep.isdigit():
                    idx = int(dep) - 1
                    if 0 <= idx < len(p.lista_tareas):
                        t.agregar_dependencia(p.lista_tareas[idx])
            p.agregar_tarea(t)
            if t.estado == "pendiente":
                datos.cola_pendientes.append(t)
            datos.guardar_datos()
        elif op == "3":
            p.cambiar_estado("finalizado" if p.estado == "activo" else "activo")
            datos.guardar_datos()
        elif op == "4":
            break

def mostrar_menu_proyectos():
    while True:
        print("\n--- PROYECTOS ---")
        print("1. Crear | 2. Listar | 3. Editar | 4. Volver")
        op = input("→ ")
        if op == "1": crear_proyecto()
        elif op == "2": listar_proyectos()
        elif op == "3": editar_proyecto()
        elif op == "4": break