from . import motion
from . import immovable

class ImmovableMotion(motion.Motion):

    def execute(self) -> None:
        # return super().execute()
        self.action.execute(self.material)