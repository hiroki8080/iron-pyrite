import copy
import json
from abc import ABCMeta, abstractmethod


class Material(metaclass=ABCMeta):

    GRAVITY_RANGE = 50

    def __init__(self) -> None:
        self.id = 0
        self.points = []
        self.outer_closed = False
        self.position = {}
        self.size = 0
        self.angle = 0
        self.start = []
        self.neighbors = []

    @abstractmethod
    def check_points(self, points):
        raise NotImplementedError

    @abstractmethod
    def is_outer_closed(self):
        raise NotImplementedError

    @abstractmethod
    def match(self, points):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    def create(self, info):
        new_instance = copy.deepcopy(self)
        new_instance.id = info["id"]
        new_instance.points = info["points"]
        new_instance.outer_closed = info["outer_closed"]
        new_instance.position = info["position"] if "position" in info else new_instance.__calc_average() # center position
        new_instance.start = new_instance.position
        new_instance.size = new_instance.__calc_size()
        new_instance.angle = info.get("angle", 0)
        return new_instance


    def is_near(self, neighbor):
        diff_x = self.__calc_diff(neighbor, "x")
        diff_y = self.__calc_diff(neighbor, "y")
        if diff_x < self.GRAVITY_RANGE and diff_y < self.GRAVITY_RANGE:
            self.neighbors.append(neighbor)
            return True
        return False

    def __calc_diff(self, neighbor, direction):
        diff = 0
        if self.position[direction] > neighbor.position[direction]:
            diff = (self.position[direction] - (self.size /2)) - (neighbor.position[direction] + (self.size /2))
        else:
            diff = (neighbor.position[direction] - (self.size /2)) - (self.position[direction] + (self.size /2))
        return diff

    def __calc_average(self):
        size = len(self.points)
        x = 0
        y = 0
        for point in self.points:
            x = x + point[0]
            y = y + point[1]
        return {"x": int(x / size), "y": int(y / size)}

    def __calc_size(self):
        l_x = {x for x,y in self.points}
        l_y = {y for x,y in self.points}
        diff_x = max(l_x) - min(l_x)
        diff_y = max(l_y) - min(l_y)
        return diff_x if diff_x > diff_y else diff_y

    def __str__(self) -> str:
        obj_j = {
            "id": self.id,
            "points": self.points,
            "outer_closed": self.outer_closed,
            "position": self.position,
            "size": self.size,
            "angle": self.angle,
            "start": self.start,
            "type": self.get_name()
            }
        return json.dumps(obj_j)

