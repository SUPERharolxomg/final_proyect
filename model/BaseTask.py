from model.ITask import ITask

class BaseTask(ITask):
    def __init__(self, titulo, descripcion):
        self._titulo = titulo
        self._descripcion = descripcion

    def get_titulo(self):
        return self._titulo

    def get_descripcion(self):
        return self._descripcion

    def marcar_completada(self):
        pass

    def __str__(self):
        return f"{self._titulo} - {self._descripcion}"
