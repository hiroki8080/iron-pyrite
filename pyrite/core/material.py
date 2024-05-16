import os
import importlib
import inspect
from abc import ABCMeta, abstractmethod
from .motion import Motion

def load_materials():
    materials = []
    try:
        package_name = 'materials'
        materials_dir = os.listdir(package_name)
        skip_files = ['__init__.py']
        materials = []
        for file_name in materials_dir:
            if file_name.endswith('py') and file_name not in skip_files:
                module_name = os.path.splitext(file_name)[0]
                module_path = '.'.join([package_name, module_name])
                material_module = importlib.import_module(module_path)
                classes = inspect.getmembers(material_module, inspect.isclass)
                print(f"Load material : {classes[0]}")
                materials.append(classes[0][1]())
    except Exception as e:
        raise Exception(f'Failed to load material module. error = {e}')
    return materials

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
