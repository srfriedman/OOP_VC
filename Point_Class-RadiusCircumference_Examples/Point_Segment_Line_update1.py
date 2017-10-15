import math


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        """ Create a new point at the given coordinates. """

        self.x = x
        self.y = y

    def distance(self, other_point):
        """ Calculate the distance between a point, self, and another point. """

        x_diff_square = (self.x - other_point.x) ** 2
        y_diff_square = (self.y - other_point.y) ** 2
        distance = math.sqrt(x_diff_square + y_diff_square)
        return distance

    def __str__(self):
        """ When a programmer changes the meaning of a special method we say that we override the method.
        Note also that the str type converter function uses whatever __str__ method we provide."""

        return "x=" + str(self.x) + ", y=" + str(self.y)

    def __repr__(self):
        """ Similar to overwrite of existing method for str type conversion. This allows the overwrite to be read and
         executed inside of a tuple. """

        return self.__str__()


class Line:
    """ Line class for an object, line, defined by its slope and y-intercept. """

    def __init__(self, slope, y_intercept):
        """ A line is defined by a slope and a y-intercept. """

        self.slope = slope
        self.y_intercept = y_intercept

    def perpendicular(self, point):
        """ Computes resulting slope and y intersect of the perpendicular. """

        slope = - 1 / self.slope
        y_intercept = point.y - slope * point.x
        return Line(slope, y_intercept)

    def intersect(self, other_line):
        """ Finds the intersection of two non-vertical lines.
        see wikipedia: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_the_equations_of_the_lines

        Given the equations of two lines, the x and y coordinates of the point of intersection of two non-vertical lines
        can easily be found using the following substitutions and rearrangements:

        Suppose that two lines have the equations y = a * x + c and y = b * x + d where a and b are the slopes of the
        lines and where c and d are the y-intercepts of the lines.

        At the point where the two lines intersect (if they do), both y coordinates will be the same, hence the following equality:
        a * x + c = b * x + d .

        We can rearrange this expression in order to extract the value of x, a * x − b * x = d − c, and so,
        x = (d − c) / (a − b).

        To find the y coordinate, all we need to do is substitute the value of x into either one of the two line equations, for example, into the first:
        y = a * ((d − c) / (a − b)) + c.

        Hence, the point of intersection is P ( (d − c) / (a − b) , a * ((d − c) / (a − b)) + c.

        Note if a = b then the two lines are parallel. If c ≠ d as well, the lines are different and there is no
        intersection, otherwise the two lines are identical."""

        x = (other_line.y_intercept - self.y_intercept) / (self.slope - other_line.slope)
        y = self.slope * x + self.y_intercept
        return Point(x, y)

    def __str__(self):
        """ When a programmer changes the meaning of a special method we say that we override the method.
        Note also that the str type converter function uses whatever __str__ method we provide."""

        return "slope=" + str(self.slope) + ", y_intercept=" + str(self.y_intercept)


class Segment:
    """ Segment class for a line segment object, defined by two points. """

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def length(self):
        """ Using delegation we use the distance method from the Point class to establish a length method to determine
        the length of a segment from within the segment class. """

        return self.point_a.distance(self.point_b)

    def line(self):
        """ Transforms a segment into a line. """

        slope = (self.point_b.y - self.point_a.y) / (self.point_b.x - self.point_a.x)
        y_intercept = self.point_a.y - slope * self.point_a.x
        return Line(slope, y_intercept)

    def midpoint(self):
        """ Calculates the midpoint on a line segment. """

        return Point((self.point_b.x + self.point_a.x) / 2, (self.point_b.y + self.point_a.y) / 2)

    def bisect(self):
        """ Creates a line bisecting the original segment at the midpoint. """

        return self.line().perpendicular(self.midpoint())


def main():
    p1 = Point(1, 4)
    p2 = Point(4, 1)
    p3 = Point(-2, 1)

    s1 = Segment(p1, p3)
    s2 = Segment(p1, p2)

    lp1 = s1.bisect()
    lp2 = s2.bisect()

    center = lp1.intersect(lp2)
    # See "Equation of a Circle from 3 Points (2 dimensions)"
    # by http://paulbourke.net/geometry/circlesphere/

    radius = center.distance(p1)
    print("radius = ", radius, "\n" "center is located at: ", center)


main()
