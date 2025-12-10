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
        op = input("→ ")
        if op == "1":
            mostrar_menu_proyectos()
        elif op == "2":
            mostrar_menu_estudiantes()
        elif op == "3":
            mostrar_menu_tareas()
        elif op == "4":
            datos.guardar_datos()
            print("¡Adiós!")
            break