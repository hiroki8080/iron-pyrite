from materials import distinction
from motions import rotate_motion, rotate
from motions import move_motion, move

class Sandbox:

    def __init__(self, pipeline) -> None:
        self.pipeline = pipeline

    def play(self):
        match_list = distinction(self.pipeline.read()["input"])
        result = []
        for material in match_list:
            if material.get_name() == "Circle":
                print(f"!!!!match material={material}")
                material = rotate_motion.RotateMotion(material, None, rotate.Rotate()).execute()
                for neighbor in material.neighbors:
                    print(f"neighbor={neighbor}")
                    if neighbor.get_name() == "Line":
                        material = move_motion.MoveMotion(material, neighbor, move.Move()).execute()
                result.append(material)
            if material.get_name() == "Line":
                result.append(material)

        self.pipeline.write(result)
