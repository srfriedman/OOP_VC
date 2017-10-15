import math


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        """ Create a new point at the given coordinates. """
        self.x = x
        self.y = y

    def distance(self, other_point):
        """ Calculate the distance between a point, self and another point. """
        xdiff = (self.x - other_point.x) ** 2
        ydiff = (self.y - other_point.y) ** 2
        distance = math.sqrt(xdiff + ydiff)
        return distance

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Line:
    def __init__(self, slope, y_intersect):
        # a line is defined by a slope and a y intersection
        self.slope = slope
        self.y_intersect = y_intersect

    def perpendicular(self, point):
        # we compute resulting slope and y intersect of the perpendicular
        slope = - 1 / self.slope
        y_intersect = point.y - slope * point.x
        return Line(slope, y_intersect)

    def intersect(self, other_line):
        # see wikipedia https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_the_equations_of_the_lines
        x = (other_line.y_intersect - self.y_intersect) / (self.slope - other_line.slope)
        y = (self.slope * other_line.y_intersect - other_line.slope * self.y_intersect) / (self.slope - other_line.slope)
        return Point(x, y)

    def __str__(self):
        return "slope=" + str(self.slope) + ", y_intersect=" + str(self.y_intersect)


class Segment:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def line(self):
        # we transform a segment into a line by deducting slope and y intersect from coordinates of origin and destination
        slope = (self.destination.y - self.origin.y) / (self.destination.x - self.origin.x)
        y_intercept = self.origin.y - slope * self.origin.x
        return Line(slope, y_intercept)

    def middle_point(self):
        return Point((self.destination.x + self.origin.x) / 2, (self.destination.y + self.origin.y) / 2)

    def bisect(self):
        return self.line().perpendicular(self.middle_point())


p1 = Point(1, 4)
p2 = Point(4, 1)
p3 = Point(-2, 1)

s1 = Segment(p1, p3)
s2 = Segment(p1, p2)

lp1 = s1.bisect()
lp2 = s2.bisect()

center = lp1.intersect(lp2)
radius = center.distance(p1)
print("radius = ", radius)
print("center is located at: ", center)
