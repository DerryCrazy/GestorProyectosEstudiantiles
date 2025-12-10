import datos
from est import mostrar_menu_estudiantes
from proy import mostrar_menu_proyectos
from homework import mostrar_menu_tareas
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
            print("Navegando a Gestión de Tareas...")
            mostrar_menu_tareas()
            pass
        elif opcion == '4':
            print("Guardando datos y saliendo...")
            # datos.guardar_datos() # Llamar a la función de guardar si existe
            break
        else:
            print("Opción inválida.")


