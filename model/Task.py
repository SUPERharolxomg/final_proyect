from model.BaseTask import BaseTask

class Task(BaseTask):
    def __init__(self, titulo, descripcion, fecha_limite, completada=False):
        super().__init__(titulo, descripcion)
        self.fecha_limite = fecha_limite
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self._titulo} - {self._descripcion} (Para: {self.fecha_limite}) Estado: {estado}"

    def to_dict(self):
        return {
            "titulo": self._titulo,
            "descripcion": self._descripcion,
            "fecha_limite": self.fecha_limite,
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data):
        return Task(data['titulo'], data['descripcion'], data['fecha_limite'], data['completada'])
