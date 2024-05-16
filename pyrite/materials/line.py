from core.material import Material

class Line(Material):

    def check_points(self, points):
        try:
            if (len(points) == 2 and len(points[0]) == 2 and len(points[1]) == 2 and
                int(points[0][0]) and int(points[0][1]) and
                int(points[1][0]) and int(points[1][1])):
                return True
        except:
            return False

    def is_outer_closed(self):
        return False

    def match(self, info):
        if info['is_outer_closed'] == self.is_outer_closed() and self.check_points(info['points']):
            return True
        return False

    def get_name(self):
        return 'Line'