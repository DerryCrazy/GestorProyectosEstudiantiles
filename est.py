# Importa el módulo 'datos', que contiene las listas globales (estudiantes) 
# y las funciones de manejo de archivos (guardar_datos).
import datos

# Funciones de gestión de Estudiantes

# Función para añadir un nuevo estudiante
def agregar():
    nombre = input("Nombre: ")
    mat = input("Matrícula: ").upper()
    # Validación: Comprueba si ya existe un estudiante con la misma matrícula
    if any(e.matricula == mat for e in datos.estudiantes):
        print("Matrícula ya existe")
        return
     # Crea un nuevo objeto Estudiante y lo añade a la lista global
    datos.estudiantes.append(datos.Estudiante(nombre, mat))
    # Guarda la lista actualizada en el archivo JSON
    datos.guardar_datos()
    print("Estudiante agregado")

# Función para mostrar la lista de todos los estudiantes
def listar():
    # Itera sobre la lista global de estudiantes, comenzando la enumeración en 1
    for i, e in enumerate(datos.estudiantes, 1):
         # Imprime el número de índice y la representación en string del objeto Estudiante
        print(f"{i}. {e}")

# Función para eliminar un estudiante de la lista
def eliminar():
    # Primero, muestra la lista para que el usuario pueda elegir qué eliminar
    listar()
    try:
        # Pide al usuario el número de índice del estudiante a eliminar
        n = int(input("Número a eliminar (0 cancelar): "))
        if n > 0:
             # Elimina el estudiante de la lista usando su índice (recordando que la lista es base 0)
            datos.estudiantes.pop(n-1)
            # Guarda la lista actualizada
            datos.guardar_datos()
    except:
        # Captura cualquier error (ej. entrada no numérica, índice fuera de rango) y lo ignora (pass)
        pass

# Función que despliega y maneja el menú principal para la gestión de estudiantes
def mostrar_menu_estudiantes():
    while True:
        print("\n--- ESTUDIANTES ---")
        print("1. Agregar | 2. Listar | 3. Eliminar | 4. Volver")
        op = input("→ ")
        # Llama a la función correspondiente según la opción seleccionada
        if op == "1": agregar()
        elif op == "2": listar()
        elif op == "3": eliminar()
        # Opción 4: Sale del bucle, regresando al menú principal superior
        elif op == "4": break
