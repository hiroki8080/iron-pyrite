import os
import importlib
import inspect
from abc import ABCMeta, abstractmethod
from motion import Motion

def distinction(materials, material_info_list):
    for material_info in material_info_list:
        if 'points' not in material_info:
            continue
        for material in materials:
            if material.match(material_info):
                print('Match material ' + material.get_name())


class Material(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    def load(self, position, size, dimension, motion: Motion) -> None:
        self.position = size
        self.size = size
        self.dimension = dimension
        self.motion = motion

    def movement(self):
        return self.motion.execute()

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
    def get_name(self, points):
        raise NotImplementedError
