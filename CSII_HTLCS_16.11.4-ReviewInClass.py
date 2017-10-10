### to review in class

#CSII
#10/5/17
#Sarah Friedman

#16.11 Exercises 4


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

    def get_line_to(self, pTwo): ### 
        xVal = pTwo.x - self.x
        yVal = pTwo.y - self.y
        m = yVal/xVal
        m = int(m)

        b = self.y - (m * self.x)
        b = int(b)

        return m, b

p = Point(4, 11)
q = Point(6, 15)
print(p.get_line_to(q))
