from .action import Action

class Rotate(Action):

    def execute(self, material, neighbor=None):
        material.angle+=1
        return material
        # current.angle+=1
