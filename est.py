import datos

def agregar_estudiante():
    print("\n--- Agregar Estudiante ---")
    nombre = input("Nombre completo: ").strip()
    matricula = input("Matrícula: ").strip().upper()

    # Validar que no exista la matrícula
    for e in datos.estudiantes:
        if e.matricula == matricula:
            print("¡Error! Esa matrícula ya existe.")
            return

    nuevo = datos.Estudiante(nombre, matricula)
    datos.estudiantes.append(nuevo)
    datos.guardar_estudiantes()
    print(f"Estudiante {nombre} ({matricula}) agregado correctamente.")

def listar_estudiantes():
    print("\n--- Lista de Estudiantes ---")
    if not datos.estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for i, e in enumerate(datos.estudiantes, 1):
        print(f"{i}. {e}")

def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")
    if not datos.estudiantes:
        print("No hay estudiantes para eliminar.")
        return

    listar_estudiantes()
    try:
        num = int(input("\nNúmero del estudiante a eliminar (0 para cancelar): "))
        if num == 0:
            return
        if 1 <= num <= len(datos.estudiantes):
            eliminado = datos.estudiantes.pop(num - 1)
            datos.guardar_estudiantes()
            print(f"Estudiante {eliminado.nombre} eliminado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
            print("Por favor ingresa un número válido.")

def mostrar_menu_estudiantes():
    datos.cargar_estudiantes()  # Carga al entrar
    while True:
        print("\n" + "="*35)
        print("     GESTIÓN DE ESTUDIANTES")
        print("="*35)
        print("1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Volver al menú principal")
        print("="*35)

        op = input("Elige una opción: ")
        if op == "1":
            agregar_estudiante()
        elif op == "2":
            listar_estudiantes()
        elif op == "3":
            eliminar_estudiante()
        elif op == "4":
            datos.guardar_estudiantes()  # Guarda al salir
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida.")

def buscar_estudiante_por_matricula(matricula):
    for e in datos.estudiantes:
        if e.matricula == matricula:
            return e
    return None