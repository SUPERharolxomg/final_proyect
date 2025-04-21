import json
import os
from model.Task import Task
from model.exception import IndexInvalid,TipeTaskInvalid

class ListTask:
    def __init__(self):
        self._archivo = "tareas.json"
        self._tareas = self.cargar()

    def agregar(self, tarea):
        if isinstance(tarea, Task):
            self._tareas.append(tarea)
            self.guardar()
        else:
            raise TipeTaskInvalid("Solo se pueden agregar objetos de tipo Tarea.")

    def eliminar(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)
            self.guardar()
        else:
            raise IndexInvalid("Índice fuera de rango.")

    def completar(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].marcar_completada()
            self.guardar()
        else:
            raise IndexInvalid("Índice fuera de rango.")

    def obtener_todas(self):
        return self._tareas

    def guardar(self):
        with open(self._archivo, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self._tareas], f, indent=4, ensure_ascii=False)

    def cargar(self):
        if not os.path.exists(self._archivo):
            return []
        with open(self._archivo, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
            except json.JSONDecodeError:
                return []
