from . import material

class Square(material.Material):

    def check_points(self, points):
        res = False
        try:
            if len(points) == 4:
                for point in points:
                    if len (point) == 2:
                        res = int(point[0]) and int(point[1])
        except:
            return res
        return res

    def is_outer_closed(self):
        return True

    def match(self, info):
        if info["outer_closed"] == self.is_outer_closed() and self.check_points(info["points"]):
            return True
        return False

    def get_name(self):
        return "Square"