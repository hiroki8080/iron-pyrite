import sys
import json
from material import distinction
from circle import Circle
from line import Line

MATERIALS = [Circle(), Line()]


def main():

    material_info_list_str = sys.stdin.readline().rstrip() # by wasm
    material_info_list = json.loads(material_info_list_str)
    distinction(MATERIALS, material_info_list)

    # # Test(Circle)
    # material_info_list_str = '[{"points": [1,2], "is_outer_closed": 1}]'
    # material_info_list = json.loads(material_info_list_str)
    # distinction(MATERIALS, material_info_list)

    # # Test(Line)
    # material_info_list_str = '[{"points": [[1,2], [2,4]], "is_outer_closed": 0}]'
    # material_info_list = json.loads(material_info_list_str)
    # distinction(MATERIALS, material_info_list)


if __name__ == "__main__":
    main()