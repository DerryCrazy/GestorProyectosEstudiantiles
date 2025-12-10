import datos

def agregar():
    nombre = input("Nombre: ")
    mat = input("Matrícula: ").upper()
    if any(e.matricula == mat for e in datos.estudiantes):
        print("Matrícula ya existe")
        return
    datos.estudiantes.append(datos.Estudiante(nombre, mat))
    datos.guardar_datos()
    print("Estudiante agregado")

def listar():
    for i, e in enumerate(datos.estudiantes, 1):
        print(f"{i}. {e}")

def eliminar():
    listar()
    try:
        n = int(input("Número a eliminar (0 cancelar): "))
        if n > 0:
            datos.estudiantes.pop(n-1)
            datos.guardar_datos()
    except:
        pass

def mostrar_menu_estudiantes():
    while True:
        print("\n--- ESTUDIANTES ---")
        print("1. Agregar | 2. Listar | 3. Eliminar | 4. Volver")
        op = input("→ ")
        if op == "1": agregar()
        elif op == "2": listar()
        elif op == "3": eliminar()
        elif op == "4": break