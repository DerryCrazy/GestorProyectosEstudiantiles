# Importa el módulo 'datos' que contiene las listas globales (proyectos, estudiantes) 
# y las funciones de las clases (Proyecto, Tarea) y de manejo de archivos (guardar_datos)
import datos

# Funciones de Gestión de Proyectos

# Permite crear un nuevo proyecto
def crear_proyecto():
    nombre = input("Nombre del proyecto: ")
    # Validación: Verifica si ya existe un proyecto con el mismo nombre (sin importar mayúsculas/minúsculas)
    if any(p.nombre.lower() == nombre.lower() for p in datos.proyectos):
        print("Ya existe")
        return
    # Crea una nueva instancia de Proyecto
    p = datos.Proyecto(nombre)
    # Añade el nuevo proyecto a la lista global
    datos.proyectos.append(p)
     # Guarda los datos actualizados en el archivo JSON
    datos.guardar_datos()
    print("Proyecto creado")
    # Ofrece la opción de pasar directamente a la edición del proyecto recién creado
    if input("¿Agregar tareas/estudiantes ahora? (s/n): ").lower() == "s":
        editar_proyecto(p)

# Muestra la lista completa de proyectos junto con sus tareas internas
def listar_proyectos():
    print("\n=== PROYECTOS ===")
    # Itera sobre la lista global de proyectos
    for i, p in enumerate(datos.proyectos, 1):
         # Muestra el resumen del proyecto
        print(f"{i}. {p}")
        # Muestra cada tarea asociada al proyecto (sub-listado)
        for t in p.lista_tareas:
            print(f"   • {t}")
        print("-" * 40)

# Permite modificar un proyecto existente (agregar miembros, tareas o cambiar estado)
def editar_proyecto(p=None):
    # Si no se pasa un proyecto (p es None), pide al usuario que seleccione uno de la lista
    if p is None:
        listar_proyectos()
        try:
            n = int(input("Número de proyecto: ")) - 1
            p = datos.proyectos[n]
        except:
            return  # Regresa si la entrada es inválida o el índice es incorrecto

    # Bucle del menú de edición para el proyecto seleccionado
    while True:
        print(f"\nEditando: {p.nombre}")
        print("1. Agregar estudiante")
        print("2. Agregar tarea")
        print("3. Cambiar estado proyecto")
        print("4. Volver")
        op = input("→ ")
        # Opción 1: Agregar Estudiante al Equipo
        if op == "1":
            mat = input("Matrícula: ").upper()
            # Busca un objeto Estudiante existente por matrícula usando 'next' (optimización de búsqueda)
            est = next((e for e in datos.estudiantes if e.matricula == mat), None)
            # Si el estudiante existe y no está ya en el equipo, lo agrega
            if est and est not in p.equipo:
                p.agregar_estudiante(est)
                datos.guardar_datos()
        # Opción 2: Agregar Tarea
        elif op == "2":
            desc = input("Descripción: ")
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            mat = input("Matrícula asignada (enter = none): ").upper() or None
            # Crea el objeto Tarea
            t = datos.Tarea(desc, fecha, matricula_asignada=mat)
            # Gestión de dependencias (opcional)
            if p.lista_tareas:
                dep = input(f"¿Depende de tarea? (1-{len(p.lista_tareas)} o enter): ")
                if dep.isdigit():
                    idx = int(dep) - 1
                    # Valida el índice ingresado
                    if 0 <= idx < len(p.lista_tareas):
                        # Asigna la tarea existente como dependencia de la nueva tarea (t)
                        t.agregar_dependencia(p.lista_tareas[idx])
             # Añade la tarea a la lista del proyecto
            p.agregar_tarea(t)
            # Si la tarea está pendiente, la añade a la cola global FIFO
            if t.estado == "pendiente":
                datos.cola_pendientes.append(t)
            datos.guardar_datos()
         # Opción 3: Cambiar Estado (Activo <-> Finalizado)
        elif op == "3":
            # Cambia el estado del proyecto de forma alterna y guarda
            p.cambiar_estado("finalizado" if p.estado == "activo" else "activo")
            datos.guardar_datos()
        # Opción 4: Volver
        elif op == "4":
            break

# Función que despliega y maneja el menú de gestión de Proyectos
def mostrar_menu_proyectos():
    while True:
        print("\n--- PROYECTOS ---")
        print("1. Crear | 2. Listar | 3. Editar | 4. Volver")
        op = input("→ ")
        if op == "1": crear_proyecto()
        elif op == "2": listar_proyectos()
        elif op == "3": editar_proyecto()
        elif op == "4": break
