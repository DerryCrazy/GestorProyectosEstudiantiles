# Definicion de Clase Estudiante
class Estudiante:
     # Constructor: Inicializa un estudiante con su nombre y matrícula.
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

     # Representación en string: Muestra el nombre y la matrícula al imprimir el objeto.
    def __str__(self):
        return f"{self.nombre} ({self.matricula})"


# Definicion de Clase Tarea
class Tarea:
    # Constructor: Inicializa la descripción, fecha límite, estado (defecto: "pendiente") y asignación
    def __init__(self, descripcion, fecha_limite, estado="pendiente", matricula_asignada=None):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.estado = estado
        self.matricula_asignada = matricula_asignada
         # Lista para almacenar otras Tareas que deben completarse primero (dependencias)
        self.dependencias = []  # Tareas que deben completarse antes

     # Método clave: Agrega un requisito previo (otra Tarea) que debe completarse
    def agregar_dependencia(self, tarea_previa):
        if tarea_previa not in self.dependencias:
            self.dependencias.append(tarea_previa)

     # Método clave: Intenta marcar la tarea como finalizada
    def marcar_finalizada(self):
        # Evita finalizar tareas ya finalizadas.
        if self.estado == "finalizada":
            print(f"Ya está finalizada: {self.descripcion}")
            return False
         # Comprueba las dependencias: Itera y verifica que todas las tareas dependientes estén "finalizadas".
        for dep in self.dependencias:
            if dep.estado != "finalizada":
                # Si hay una pendiente, bloquea la finalización.
                print(f"NO SE PUEDE: '{self.descripcion}' depende de '{dep.descripcion}' (aún pendiente)")
                return False
        # Si no hay dependencias pendientes, cambia el estado.
        self.estado = "finalizada"
        print(f"Finalizada: {self.descripcion}")
        return True

    # Representación en string: Muestra el estado, la descripción y las dependencias.
    def __str__(self):
        asignado = f" → {self.matricula_asignada}" if self.matricula_asignada else ""
        deps = f" (Depende de: {', '.join([d.descripcion for d in self.dependencias])})" if self.dependencias else ""
        return f"[{self.estado}] {self.descripcion} | {self.fecha_limite}{asignado}{deps}"


# Definicion de Clase Proyecto
class Proyecto:
    # Constructor: Inicializa el nombre, estado (defecto: "activo"), equipo (lista de Estudiantes) y tareas
    def __init__(self, nombre, estado="activo"):
        self.nombre = nombre
        self.estado = estado
        self.equipo = []  # Lista de Estudiantes
        self.lista_tareas = []  # Lista de Tareas

    # Método para añadir un objeto Estudiante al equipo
    def agregar_estudiante(self, estudiante):
        if estudiante not in self.equipo:
            self.equipo.append(estudiante)

    # Método para añadir un objeto Tarea al proyecto
    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)

     # Representación en string: Resume el nombre, estado, equipo y número de tareas
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["activo", "finalizado"]:
            self.estado = nuevo_estado

    def __str__(self):
        return f"{self.nombre} [{self.estado}] | Equipo: {len(self.equipo)} | Tareas: {len(self.lista_tareas)}"
