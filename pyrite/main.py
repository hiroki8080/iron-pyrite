import sys
import json
from core.material import load_materials, distinction


def main():
    materials = load_materials()

    # material_info_list_str = sys.stdin.readline().rstrip() # by wasm

    # Test(Circle)
    material_info_list_str = '[{"points": [1,2], "is_outer_closed": 1}]'
    material_info_list = json.loads(material_info_list_str)
    print(len(material_info_list[0]["points"]))
    print(material_info_list[0]["points"][0])
    print(material_info_list[0]["points"][1])
    distinction(materials, material_info_list)

    # Test(Line)
    material_info_list_str = '[{"points": [[1,2], [2,4]], "is_outer_closed": 0}]'
    material_info_list = json.loads(material_info_list_str)
    print(len(material_info_list[0]["points"]))
    print(len(material_info_list[0]["points"][0]))
    print(len(material_info_list[0]["points"][1]))
    distinction(materials, material_info_list)


if __name__ == "__main__":
    main()