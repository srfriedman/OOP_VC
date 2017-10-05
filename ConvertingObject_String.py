class Point:
    """ Point class for representing and manipulating x,y coordinates. """

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
        """ When a programmer changes the meaning of a special method we say that we override the method.
        Note also that the str type converter function uses whatever __str__ method we provide."""

        return "x=" + str(self.x) + ", y=" + str(self.y)

p = Point(7, 6)
print(p)
