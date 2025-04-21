from model.ListTask import ListTask
from model.Task import Task
from model.exception import IndexInvalid, TipeTaskInvalid
from view.view import Vista

class Controller:
    def __init__(self):
        self.tareas = ListTask()
        self.vista = Vista()

    def agregar_tarea(self, titulo, descripcion, fecha_limite):
        try:
            tarea = Task(titulo, descripcion, fecha_limite)
            self.tareas.agregar(tarea)
            self.vista.mostrar_mensaje("Tarea agregada correctamente.")
        except TipeTaskInvalid as e:
            self.vista.mostrar_mensaje(f"Error: {e}")

    def eliminar_tarea(self, indice):
        try:
            self.tareas.eliminar(indice)
            self.vista.mostrar_mensaje("Tarea eliminada.")
        except IndexInvalid as e:
            self.vista.mostrar_mensaje(f"Error: {e}")

    def completar_tarea(self, indice):
        try:
            self.tareas.completar(indice)
            self.vista.mostrar_mensaje("Tarea completada.")
        except IndexInvalid as e:
            self.vista.mostrar_mensaje(f"Error: {e}")

    def mostrar_tareas(self):
        self.vista.mostrar_tareas(self.tareas.obtener_todas())
