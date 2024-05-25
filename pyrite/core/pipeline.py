import json
import sys

class Pipeline:

    def read(self):

        #{
        # "input": [
        #    "id": 1,
        #    {"points": [[0, 1], [2, 3]], "outer_closed": 1},
        #    {"points": [[4, 5], [6, 7]], "outer_closed": 0},
        #    ]
        #}
        read_str = sys.stdin.readline().rstrip()
        return json.loads(read_str)

    def write(self, material_list):
        output_str = '{"output":['
        materials_str = ''
        for material in material_list:
            materials_str += str(material)
            materials_str += ","
        output_str += materials_str[:-1] + "]}"
        print(output_str)
        return output_str
