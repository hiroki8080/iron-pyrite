from . import material
from . import circle
from . import line

MATERIALS = [circle.Circle(), line.Line()]

# TODO Moved after py2wasm supports classmethod
def distinction(material_info_list):
    material_instancese = []
    for material_info in material_info_list:
        if 'points' not in material_info:
            continue
        for material in MATERIALS:
            if material.match(material_info):
                material_instance = material.create(material_info)
                material_instancese.append(material_instance)
    for target in material_instancese:
        for material_instance in material_instancese:
            if target.id == material_instance.id:
                continue
            target.is_near(material_instance)
    return material_instancese