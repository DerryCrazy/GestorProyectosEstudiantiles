📘 Gestor de Proyectos Estudiantiles

Sistema en Python para administrar estudiantes y proyectos de manera sencilla, usando archivos JSON para almacenar la información.

📌 Descripción del Proyecto

Este sistema permite registrar estudiantes, gestionar proyectos, ordenarlos, consultarlos y administrarlos mediante un menú interactivo en consola.

Está desarrollado con Programación Orientada a Objetos (POO) e incluye módulos separados para estudiantes, proyectos, ordenamiento y menú principal.


---

📁 Estructura del Proyecto

GestorProyectosEstudiantiles/
│
├── main.py
├── menu.py
├── clases.py
├── datos.py
├── ordenamiento.py
├── est.py
├── proy.py
├── homework.py
│
├── estudiantes.json
└── proyectos.json

📄 Archivos importantes

main.py → punto de inicio del programa.

menu.py → contiene las opciones del menú.

clases.py → clases principales del sistema.

est.py / proy.py → gestión de estudiantes y proyectos.

datos.py → lectura y escritura de archivos JSON.

ordenamiento.py → funciones para ordenar registros.



---

🚀 Instructivo de Uso

🔧 Requisitos

Python 3.10 o superior

Archivos JSON incluidos en el proyecto (vienen listos)



---

▶️ Paso 1: Clonar el repositorio

En GitHub, presiona Code → HTTPS → Copy y en tu computadora usa:

git clone https://github.com/tu_usuario/gestor-proyectos.git

(O descarga el ZIP y extráelo).


---

▶️ Paso 2: Ejecutar el programa

Entra a la carpeta del proyecto:

cd GestorProyectosEstudiantiles-main

Ejecuta el programa:

python main.py


---

📋 Paso 3: Usar el menú del sistema

Cuando ejecutes main.py verás un menú como este:

===== MENÚ PRINCIPAL =====
1. Registrar estudiante
2. Consultar estudiantes
3. Registrar proyecto
4. Consultar proyectos
5. Ordenar registros
6. Guardar
7. Salir

✔️ 1. Registrar estudiante

Te pedirá nombre, matrícula, carrera, etc.
Se guarda automáticamente en estudiantes.json.


---

✔️ 2. Consultar estudiantes

Muestra la lista completa de estudiantes registrados.


---

✔️ 3. Registrar proyecto

Pide datos del proyecto (nombre, responsable, fecha, etc.)
Lo guarda en proyectos.json.


---

✔️ 4. Consultar proyectos

Muestra todos los proyectos registrados.


---

✔️ 5. Ordenar registros

Permite ordenar estudiantes o proyectos por criterios como:

nombre

matrícula

carrera

fecha

responsable


Se usan funciones de ordenamiento.py.


---

✔️ 6. Guardar

Actualiza los archivos JSON.


---

✔️ 7. Salir

Termina el programa de forma segura.


---

📚 Tecnologías utilizadas

Python

Programación Orientada a Objetos (POO)

Manejo de archivos JSON
