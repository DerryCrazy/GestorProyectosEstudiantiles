import datos
from est import mostrar_menu_estudiantes
from proy import mostrar_menu_proyectos
from homework import mostrar_menu_tareas, submenu_tareas, crear_tarea, listar_tareas_ordenadas, buscar_tareas, marcar_tarea_como_finalizada

def menu_principal():
    datos.cargar_datos()
    print("GESTOR DE PROYECTOS ESTUDIANTILES - TEC VALLES")
    while True:
        print("\n" + "="*40)
        print("1. Gestión de Proyectos")
        print("2. Gestión de Estudiantes")
        print("3. Gestión de Tareas")
        print("4. Salir")
        print("="*40)
        opcion = input("→ ")
        if opcion == "1":
            mostrar_menu_proyectos()
            pass
        elif opcion == '2':
            print("Navegando a Gestión de Estudiantes...")
            mostrar_menu_estudiantes()
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


