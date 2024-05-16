from motion import Motion
from rotate import Rotate

class RotateMotion(Motion):

    def __init__(self, rotate: Rotate) -> None:
        super().__init__()
        self.__rotate = rotate

    def execute(self) -> None:
        return super().execute()