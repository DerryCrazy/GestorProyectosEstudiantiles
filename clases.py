class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"


class Tarea:
    def __init__(self, descripcion, fecha_limite, estado="pendiente", matricula_asignada=None):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.estado = estado
        self.matricula_asignada = matricula_asignada
        self.dependencias = []  # Tareas que deben completarse antes

    def agregar_dependencia(self, tarea_previa):
        if tarea_previa not in self.dependencias:
            self.dependencias.append(tarea_previa)

    def marcar_finalizada(self):
        if self.estado == "finalizada":
            print(f"Ya está finalizada: {self.descripcion}")
            return False
        for dep in self.dependencias:
            if dep.estado != "finalizada":
                print(f"NO SE PUEDE: '{self.descripcion}' depende de '{dep.descripcion}' (aún pendiente)")
                return False
        self.estado = "finalizada"
        print(f"Finalizada: {self.descripcion}")
        return True

    def __str__(self):
        asignado = f" → {self.matricula_asignada}" if self.matricula_asignada else ""
        deps = f" (Depende de: {', '.join([d.descripcion for d in self.dependencias])})" if self.dependencias else ""
        return f"[{self.estado}] {self.descripcion} | {self.fecha_limite}{asignado}{deps}"


class Proyecto:
    def __init__(self, nombre, estado="activo"):
        self.nombre = nombre
        self.estado = estado
        self.equipo = []
        self.lista_tareas = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.equipo:
            self.equipo.append(estudiante)

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["activo", "finalizado"]:
            self.estado = nuevo_estado

    def __str__(self):
        return f"{self.nombre} [{self.estado}] | Equipo: {len(self.equipo)} | Tareas: {len(self.lista_tareas)}"