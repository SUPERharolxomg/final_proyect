from abc import ABC, abstractmethod

class ITask(ABC):
    @abstractmethod
    def marcar_completada(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
