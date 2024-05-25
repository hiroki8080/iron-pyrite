from .action import Action
from enum import Enum


class Direction(Enum):
    TOP = 0,
    BOTTOM = 1,
    LEFT = 2,
    RIGHT = 3,
    TOP_RIGHT = 4,
    TOP_LEFT = 5,
    BOTTOM_RIGHT = 6,
    BOTTOM_LEFT = 7,

class Move(Action):

    def execute(self, material, neighbor=None):
        return self.calc_position(material, neighbor)

    def calc_position(self, material, neighbor):
        move_type = Direction.TOP
        x1 = neighbor.points[0][0]
        y1 = neighbor.points[0][1]
        x2 = neighbor.points[1][0]
        y2 = neighbor.points[1][1]

        mx = material.position["x"]
        my = material.position["y"]

        # print(f"x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}, mx = {mx}, my = {my}")

        if x1 == x2:
            if y1 < y2:
                move_type = Direction.BOTTOM
                material.position["y"]+=self.volume
            else:
                move_type = Direction.TOP
                material.position["y"]-=self.volume
        elif y1 == y2:
            if x1 < x2:
                move_type = Direction.RIGHT
                material.position["x"]+=self.volume
            else:
                move_type = Direction.LEFT
                material.position["x"]-=self.volume
        elif x1 < x2 and y1 < y2:
            move_type = Direction.BOTTOM_RIGHT
            calc_my = self.__calc(mx, my, mx+(x2-x1), my+(y2-y1), mx+self.volume)
            # print(f"calc_my={calc_my}")
            material.position["x"]+=self.volume
            material.position["y"]=calc_my
        elif x1 < x2 and y1 > y2:
            move_type = Direction.TOP_RIGHT
            calc_my = self.__calc(mx, my, mx+(x2-x1), my-(y1-y2), mx+self.volume)
            material.position["x"]+=self.volume
            material.position["y"]=calc_my
        elif x1 > x2 and y1 < y2:
            move_type = Direction.BOTTOM_LEFT
            calc_my = self.__calc(mx, my, mx-(x1-x2), my+(y2-y1), mx-self.volume)
            material.position["x"]-=self.volume
            material.position["y"]=calc_my
        elif x1 > x2 and y1 > y2:
            move_type = Direction.TOP_LEFT
            calc_my = self.__calc(mx, my, mx-(x1-x2), my-(y1-y2), mx-self.volume)
            material.position["x"]-=self.volume
            material.position["y"]=calc_my
        # print(f"move_type = {move_type}")
        return material

    def __calc(self, x1, y1, x2, y2, mx):
        # print(f"x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}, mx = {mx}")
        a = y2 - y1
        b = x1 - x2
        c = y1 * x2 - x1 * y2
        # print(f"a = {a}, b = {b}, c = {c}")
        #a * mx + b * my + c = 0
        my = ( a * mx + c ) / -b
        # print(f"res = {int(my)}")
        return int(my)
