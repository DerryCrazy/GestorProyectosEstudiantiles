# Importa el módulo 'datos', que contiene funciones esenciales como cargar_datos() y la gestión de datos globales
import datos
# Importa la función del menú de estudiantes desde el módulo 'est'
from est import mostrar_menu_estudiantes
# Importa la función del menú de proyectos desde el módulo 'proy'
from proy import mostrar_menu_proyectos
# Importa la función del menú de tareas desde el módulo 'homework' (o 'tareas')
from homework import mostrar_menu_tareas

# Función Principal de la Interfaz

# Define la función que muestra el menú principal y controla el flujo de la aplicación
def menu_principal():
    # Carga todos los datos persistentes (estudiantes, proyectos, tareas) desde los archivos JSON a la memoria
    datos.cargar_datos()
    print("GESTOR DE PROYECTOS ESTUDIANTILES - TEC VALLES")
    # Bucle principal que mantiene la aplicación ejecutándose hasta que el usuario decida salir
    while True:
        # Muestra las opciones principales
        print("\n" + "="*40)
        print("1. Gestión de Proyectos")
        print("2. Gestión de Estudiantes")
        print("3. Gestión de Tareas")
        print("4. Salir")
        print("="*40)
        opcion = input("→ ")
        # Evalúa la opción seleccionada por el usuario
        if opcion == "1":
            # Llama al menú de gestión de proyectos
            mostrar_menu_proyectos()
            pass  # Pasa al siguiente ciclo del bucle principal
        elif opcion == '2':
            print("Navegando a Gestión de Estudiantes...")
            # Llama al menú de gestión de estudiantes
            mostrar_menu_estudiantes()
            pass
        elif opcion == '3':
            print("Navegando a Gestión de Tareas...")
            # Llama al menú de gestión de tareas
            mostrar_menu_tareas()
            pass
        elif opcion == '4':
            print("Guardando datos y saliendo...")
            # Guardado final si no se hace en cada sub-menú
            # datos.guardar_datos() # Llamar a la función de guardar si existe
            # Sale del bucle 'while True', terminando la función
            break
        else:
            print("Opción inválida.")


