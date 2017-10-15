import math

class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def __repr__(self):
        return self.__str__()

    def midpoint(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def distance_from_point(self, a):
        xdiff = (self.x - a.x) ** 2
        ydiff = (self.y - a.y) ** 2
        distance = (xdiff + ydiff) ** .5
        return distance

    def slope_yintercept(self, a): ###
        xVal = a.x - self.x
        yVal = a.y - self.y
        m = yVal/xVal
        b = (self.y - (m * self.x))
        return m, b



def radius(a, b, c):
    A = a.distance_from_point(b)
    B = a.distance_from_point(c)
    C = b.distance_from_point(c)
    s = (A + B + C) * 0.5
    Area = math.sqrt(s * (s - A) * (s - B) * (s - C))
    radius = (A * B * C) / (4 * Area)
    return radius


def center(a, b, c):
    slope1, yintercept1 = a.slope_yintercept(b)
    slope2, yintercept2 = a.slope_yintercept(c)
    midpoint1 = a.midpoint(b)
    midpoint2 = a.midpoint(c)
    slope_1_perpendicular = -1 / slope1
    slope_2_perpendicular = -1 / slope2
    b1 = midpoint1.y - (slope_1_perpendicular * midpoint1.x)
    b2 = midpoint2.y - (slope_2_perpendicular * midpoint2.x)
    center_x = (((slope1 * slope2) * (b.y - c.y)) + (slope2 * ( b.x + a.x)) - (slope1 * (a.x + c.x)))/ (2 * (slope2 - slope1))
    center_y = (slope_1_perpendicular * (center_x - ((a.x + b.x) / 2 ))) + ((a.y + b.y) / 2)
    center = Point(center_x, center_y)
    return center

def main():
    p = Point(1, 4)
    q = Point(4, 1)
    r = Point(-2, 1)

    print(p)
    print(p.midpoint(q))
    print(radius(p, q, r))
    print(center(p, q, r))

main()

