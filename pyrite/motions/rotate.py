from .action import Action

class Rotate(Action):

    def execute(self, material, neighbor=None):
        material.angle+=self.volume
        return material
        # current.angle+=1
