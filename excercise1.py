import math
class Circle:
    pie=math.pi
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        area=self.pie*(self.radius**2)
        return area
    
    def circumference(self):
        circum=2*self.pie*self.radius
        return circum
    
c1=Circle(10)
print(c1.area())
print(c1.circumference())

    
        