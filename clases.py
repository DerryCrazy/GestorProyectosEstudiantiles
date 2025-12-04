class Estudiante:
    def _init_(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula


class Tarea:
    def _init_(self, descripcion, fecha_limite, estudiante_matricula=None):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite  # formato: "YYYY-MM-DD"
        self.estudiante_matricula = estudiante_matricula
        self.estado = "pendiente"  # pendiente o completada


class Proyecto:
    def _init_(self, nombre):
        self.nombre = nombre
        self.equipo = []   # lista de matrículas de estudiantes
        self.tareas = []   # lista de objetos Tarea