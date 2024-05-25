import math
from . import motion
from . import rotate


class MoveMotion(motion.Motion):

    def execute(self) -> None:
        # return super().execute()
        self.material = self.action.execute(self.material, self.neighbor)
        return self.material
