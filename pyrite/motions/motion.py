from abc import ABCMeta, abstractmethod
from .action import Action

class Motion(metaclass=ABCMeta):

    def __init__(self, material, neighbor, action: Action) -> None:
        self.material = material
        self.neighbor = neighbor
        self.action = action

    @abstractmethod
    def execute(self) -> None:
        pass
