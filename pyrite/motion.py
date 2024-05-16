from abc import ABCMeta, abstractmethod

class Motion(metaclass=ABCMeta):

    @abstractmethod
    def execute(self) -> None:
        pass
