from . import motion
from . import rotate

class RotateMotion(motion.Motion):

    def execute(self) -> None:
        # return super().execute()
        self.material = self.action.execute(self.material)
        return self.material