#Q11. Design an abstract class Shape with an abstract method area. Implement Circle and Rectangle classes.
import abc
class Shape:
    @abc.abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print('area: ',self.r*self.r*22/7)
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print('area: ',self.l*self.b)
c=Circle(5.4)
c.area()