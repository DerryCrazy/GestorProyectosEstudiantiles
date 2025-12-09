class Estudiante:
    def _init_(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula


class Tarea:
    def __init__(self, descripcion, fecha_limite, estado="pendiente", matricula_asignada=None):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite # Se asume formato comparable (e.g., "YYYY-MM-DD")
        self.estado = estado
        self.matricula_asignada = matricula_asignada
        # Atributo para dependencias (lista de objetos Tarea)
        self.dependencias = []
        # Atributo para tareas que dependen de esta (para construir el árbol)
        self.tareas_dependientes = []

    def agregar_dependencia(self, tarea_dependiente):
        """Agrega una tarea que DEBE completarse ANTES de esta."""
        if tarea_dependiente not in self.dependencias:
            self.dependencias.append(tarea_dependiente)
            tarea_dependiente.tareas_dependientes.append(self)

    def __repr__(self):
        return f"Tarea(desc='{self.descripcion}', fecha='{self.fecha_limite}', estado='{self.estado}', mat_asig='{self.matricula_asignada}')"


class Proyecto:
    def __init__(self, nombre, equipo=None):
        if equipo is None:
            equipo = []
        self.nombre = nombre
        self.equipo = equipo # Lista de objetos Estudiante
        self.lista_tareas = [] # Lista de objetos Tarea

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

    def __repr__(self):
         return f"Proyecto(nombre='{self.nombre}', equipo={len(self.equipo)} miembros, tareas={len(self.lista_tareas)})"
