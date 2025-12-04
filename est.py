from clases import Estudiante
import datos

#este archivo se va a usar para colocar funciones relacionadas con los estudihambres

#metodo para registrar un estudiante
def registrar_estudiante():
    print("--- Registrar estudiante ---")
    nombre = input("Nombre: ")
    matricula = input("Matrícula: ")
    nuevo = Estudiante(nombre, matricula)
    datos.estudiantes.append(nuevo)
    print("Estudiante registrado correctamente.")