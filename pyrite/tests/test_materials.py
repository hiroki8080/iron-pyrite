import json
from materials import distinction
from motions import rotate_motion, rotate, move_motion, move
from core.pipeline import Pipeline

def main():
    # s = '[{"points": [[1,2]], "outer_closed": 1}]'
    # s = '{"input":[{"id":1,"points":[[205,251],[234,167]],"outer_closed":true}]}'
    # s = '{"input":[{"id":1,"points":[[121,145],[129,104]],"outer_closed":true},{"id":2,"points":[[295,356],[325,231]],"outer_closed":true}]}'
    # s = '{"input":[{"id":1,"points":[[109,157],[111,93],[46,119],[56,155]],"outer_closed":true},{"id":2,"points":[[218,366],[282,323],[285,301],[150,289],[158,315]],"outer_closed":true}]}'
    # s = '{"input":[{"id":1,"points":[[54,149],[297,273]],"outer_closed":false,"position":{"x":175,"y":175},"angle":0},{"id":2,"points":[[199,176],[270,136],[271,106],[239,73],[117,125],[126,174]],"outer_closed":true,"position":{"x":204,"y":292},"angle":13}]}'
    # s = '{"input":[{"id":1,"points":[[144,166],[179,114],[165,67],[71,79],[65,135],[87,156]],"outer_closed":true,"position":{"x":119,"y":161},"angle":49},{"id":2,"points":[[42,174],[336,267]],"outer_closed":false,"position":{"x":189,"y":189},"angle":0}]}'
    # s = '{"input":[{"id":1,"points":[[194,178],[233,138],[232,87],[195,42],[150,48],[113,81],[103,118],[124,159],[156,177]],"outer_closed":true,"position":{"x":167,"y":151},"angle":28},{"id":2,"points":[[39,187],[309,249]],"outer_closed":false,"position":{"x":174,"y":218},"angle":0}]}'
    s = '{"input":[{"id":1,"points":[[199,165],[238,139],[252,93],[107,52],[102,104],[147,161]],"outer_closed":true,"position":{"x":177,"y":529},"angle":7},{"id":2,"points":[[52,166],[362,219]],"outer_closed":false,"position":{"x":207,"y":192},"angle":0}]}'
    res = ''
    # for i in range(0, 5):
    #     if i == 0:
    #         res = test(s)
    #     else:
    #         res = test(res)

    test(s)

def test(s):
    match_list = distinction(json.loads(s)["input"])
    print(f"match_list = {match_list}")
    for material in match_list:
        print(f"material = {material}")
        if material.get_name() == "Circle":
            print(f"before position = {material.position}")
            rotate_motion.RotateMotion(material, None, rotate.Rotate()).execute()
            for neighbor in material.neighbors:
                if neighbor.get_name() == "Line":
                    print(f"neighbor = {neighbor}")
                    print(f"before position = {material.position}")
                    move_motion.MoveMotion(material, neighbor, move.Move()).execute()
                    print(f"update position = {material.position}")

    for material in match_list:
        if material.get_name() == "Circle":
            print(f"update position = {material.position}")

    new_pipeline = Pipeline()
    return new_pipeline.write(match_list)

if __name__ == "__main__":
    main()