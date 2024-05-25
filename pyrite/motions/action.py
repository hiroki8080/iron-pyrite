from abc import ABCMeta, abstractmethod

class Action(metaclass=ABCMeta):

    volume = 5

    @abstractmethod
    def execute(self, material, neighbor=None):
        pass
