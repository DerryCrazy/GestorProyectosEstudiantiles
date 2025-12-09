import datos
from homework import crear_tarea, listar_tareas_ordenadas, buscar_tareas, marcar_tarea_como_finalizada
# Importar funciones de gestión de proyectos y estudiantes aquí también
# from gestion_proyectos import crear_proyecto, ...
# from gestion_estudiantes import crear_estudiante, ...

def mostrar_menu():
    print("\n--- Gestor de Proyectos Estudiantiles ---")
    print("1. Gestionar Proyectos")
    print("2. Gestionar Estudiantes")
    print("3. Gestionar Tareas")
    print("4. Salir")

def submenu_tareas():
    print("\n--- Gestión de Tareas ---")
    print("1. Crear Tarea")
    print("2. Listar Tareas (ordenadas por fecha)")
    print("3. Buscar Tareas")
    print("4. Marcar Tarea como Finalizada")
    print("5. Volver al Menú Principal")
    opcion = input("Selecciona una opción (1-5): ")
    return opcion

def menu_principal():
    # datos.cargar_datos() # Llamar a la función de cargar si existe
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            print("Navegando a Gestión de Proyectos...")
            # Llamar a funciones de gestion_proyectos.py
            pass
        elif opcion == '2':
            print("Navegando a Gestión de Estudiantes...")
            # Llamar a funciones de gestion_estudiantes.py
            pass
        elif opcion == '3':
            while True:
                sub_opcion = submenu_tareas()
                if sub_opcion == '1':
                    crear_tarea()
                elif sub_opcion == '2':
                    listar_tareas_ordenadas()
                elif sub_opcion == '3':
                    buscar_tareas()
                elif sub_opcion == '4':
                    marcar_tarea_como_finalizada()
                elif sub_opcion == '5':
                    break
                else:
                    print("Opción inválida.")
        elif opcion == '4':
            print("Guardando datos y saliendo...")
            # datos.guardar_datos() # Llamar a la función de guardar si existe
            break
        else:
            print("Opción inválida.")