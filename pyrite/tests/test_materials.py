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
    # s = '{"input":[{"id":1,"points":[[199,165],[238,139],[252,93],[107,52],[102,104],[147,161]],"outer_closed":true,"position":{"x":177,"y":529},"angle":7},{"id":2,"points":[[52,166],[362,219]],"outer_closed":false,"position":{"x":207,"y":192},"angle":0}]}'
    # s = '{"input":[{"id":1,"points":[[279,169],[27,301]],"outer_closed":false,"position":{"x":153,"y":235},"angle":0},{"id":2,"points":[[59,87],[77,87],[85,67],[80,42],[25,42]],"outer_closed":true,"position":{"x":65,"y":65},"angle":14},{"id":3,"points":[[170,156],[166,92],[98,80],[54,130],[52,175],[86,207],[134,212],[173,176]],"outer_closed":true,"position":{"x":115,"y":427},"angle":14}]}'
    # s = '{"input":[{"id":3,"points":[[170,156],[166,92],[98,80],[54,130],[52,175],[86,207],[134,212],[173,176]],"outer_closed":true,"angle":14}]}'
    # s = '{"input":[{"id":1,"points":[[233,142],[272,32],[213,15],[155,67],[162,99],[188,120]],"outer_closed":true,"angle":12},{"id":2,"points":[[320,127],[65,249]],"outer_closed":false,"angle":0}]}'
    # s = '{"input":[{"id":1,"points":[[290,141],[299,50],[265,40],[215,98],[228,118]],"outer_closed":true,"angle":8},{"id":2,"points":[[360,139],[73,243]],"outer_closed":false,"angle":0}]}'
    s = '{"input":[{"id":1,"points":[[252,141],[292,82],[281,64],[235,52],[185,83],[185,110],[200,127]],"outer_closed":true,"angle":10},{"id":2,"points":[[332,127],[22,275]],"outer_closed":false,"angle":0}]}'
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
                    print(f"[neighbor]before position = {material.position}")
                    move_motion.MoveMotion(material, neighbor, move.Move()).execute()
                    print(f"[neighbor]update position = {material.position}")

    new_pipeline = Pipeline()
    return new_pipeline.write(match_list)

if __name__ == "__main__":
    main()