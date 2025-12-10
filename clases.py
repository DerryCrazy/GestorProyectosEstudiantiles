class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"


class Tarea:  # Básica por ahora, para proyectos de ejemplo
    def __init__(self, descripcion, fecha_limite, estado="pendiente", matricula_asignada=None):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.estado = estado
        self.matricula_asignada = matricula_asignada
        self.dependencias = []  # Para árbol futuro

    def agregar_dependencia(self, tarea_previa):
        if tarea_previa not in self.dependencias:
            self.dependencias.append(tarea_previa)

    def __str__(self):
        return f"[{self.estado}] {self.descripcion} (Fecha: {self.fecha_limite})"

class Proyecto:
    def __init__(self, nombre, estado="activo"):
        self.nombre = nombre
        self.estado = estado  # "activo" o "finalizado"
        self.equipo = []  # Lista de Estudiantes
        self.lista_tareas = []  # Lista de Tareas

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.equipo:
            self.equipo.append(estudiante)

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["activo", "finalizado"]:
            self.estado = nuevo_estado
            print(f"Proyecto '{self.nombre}' ahora está {nuevo_estado}.")
        else:
            print("Estado inválido.")

    def __str__(self):
        return f"{self.nombre} [{self.estado}] - Equipo: {len(self.equipo)} miembros, Tareas: {len(self.lista_tareas)}"