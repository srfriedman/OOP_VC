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

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def reflect_x(self):
        reflection = (self.x,  - (self.y))
        return reflection
        ### remember to use a return statement here.
        ### remember, your class is Point. The methods that you make to manipulate the instances of the class Point are
        ###     created as functions within your class.

p = Point(3, 4)
q = Point(5, 12)
print("The reflection of", p, "is", p.reflect_x())
