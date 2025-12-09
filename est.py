from clases import Estudiante
import datos

#este archivo se va a usar para colocar funciones relacionadas con los estudihambres

#metodo para registrar un estudiante
def registrar_estudiante():
    print("--- Registrar estudiante ---")
    nombre = input("Nombre: ")
    matricula = input("Matrícula: ")
    
    # Verificar si la matrícula ya existe
    if datos.buscar_estudiante_por_matricula(matricula) is not None:
        print("Ya existe un estudiante con esa matrícula.")
        return

    nuevo = Estudiante(nombre, matricula)
    datos.estudiantes.append(nuevo)
    print(f"Estudiante '{nombre}' (Matrícula: {matricula}) registrado correctamente.")
    # datos.guardar_datos() # Llama a la función de guardar si está implementada


def listar_estudiantes():
    print("\n--- Listar Estudiantes ---")
    if not datos.estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for i, estudiante in enumerate(datos.estudiantes, start=1):
        print(f"{i}. {estudiante.nombre} (Matrícula: {estudiante.matricula})")

def buscar_estudiante():
    print("\n--- Buscar Estudiante ---")
    matricula_busqueda = input("Ingresa la matrícula del estudiante a buscar: ")
    estudiante = datos.buscar_estudiante_por_matricula(matricula_busqueda)

    if estudiante:
        print(f"Estudiante encontrado: {estudiante.nombre} (Matrícula: {estudiante.matricula})")
        # Opcional: Mostrar en qué proyectos está
        proyectos_del_estudiante = [p.nombre for p in datos.proyectos if estudiante in p.equipo]
        if proyectos_del_estudiante:
            print(f"  - Perteneciente a los proyectos: {', '.join(proyectos_del_estudiante)}")
        else:
            print("  - No está asignado a ningún proyecto.")
    else:
        print("Estudiante no encontrado.")
        