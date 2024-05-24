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
        print("call...")
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
                material.position["y"]+=1
            else:
                move_type = Direction.TOP
                material.position["y"]-=1
        elif y1 == y2:
            if x1 < x2:
                move_type = Direction.RIGHT
                material.position["x"]+=1
            else:
                move_type = Direction.LEFT
                material.position["x"]-=1
        elif x1 < x2 and y1 < y2:
            move_type = Direction.BOTTOM_RIGHT
            calc_my = self.__calc(mx, my, mx+(x2-x1), my+(y2-y1), mx+1)
            # print(f"calc_my={calc_my}")
            material.position["x"]+=1
            material.position["y"]+=abs(calc_my)
        elif x1 < x2 and y1 > y2:
            move_type = Direction.TOP_RIGHT
            calc_my = self.__calc(mx, my, mx+(x2-x1), my-(y1-y2), mx+1)
            material.position["x"]+=1
            material.position["y"]-=abs(calc_my)
        elif x1 > x2 and y1 < y2:
            move_type = Direction.BOTTOM_LEFT
            calc_my = self.__calc(mx, my, mx-(x1-x2), my+(y2-y1), mx-1)
            material.position["x"]-=1
            material.position["y"]+=abs(calc_my)
        elif x1 > x2 and y1 > y2:
            move_type = Direction.TOP_LEFT
            calc_my = self.__calc(mx, my, mx-(x1-x2), my-(y1-y2), mx-1)
            material.position["x"]-=1
            material.position["y"]-=abs(calc_my)
        print(f"move_type = {move_type}")
        return material

    def __calc(self, x1, y1, x2, y2, mx):
        # print(f"x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}, mx = {mx}")
        a = y2 - y1
        b = x1 - x2
        c = y1 * x2 - x1 * y2
        # print(f"a = {a}, b = {b}, c = {c}")
        #a * mx - b * my - c = 0
        my = ( a * mx - c ) / b
        return int(my)

# 203,203
# 446,327

# a=124
# b=-243
# c=24157

# 124 * 204 - -243 * my - 24157 = 0

# 25296 + 243my - 24157 = 0
# 25296 - 24157 = - 243my
# 1139 = -243my
