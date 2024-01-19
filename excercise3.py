import math
class Shape:
    pie=math.pi
    def area(self):
        pass
    def areaperimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return self.pie*(self.radius**2)
    
    def areaperimeter(self):
        return 2*self.pie*self.radius
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return (self.side**2)
    
    def areaperimeter(self):
        return 4*self.side
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        return (self.length*self.width)
    
    def areaperimeter(self):
        return 2*(self.width + self.length)
    
class Triangle(Shape):
    def __init__(self,h,b,s1,s2,s3):
        self.h=h
        self.b=b
        self.s1=s1
        self.s2=s2
        self.s3=s3
        
    def area(self):
        return (self.h * self.b)/2
    
    def areaperimeter(self):
        return self.s1+self.s2+self.s3
    
cir=Circle(5)
print(cir.area())
print(cir.areaperimeter())
sq=Square(5)
print(sq.area())
print(sq.areaperimeter())
rec=Rectangle(5,3)
print(rec.area())
print(rec.areaperimeter())
tri=Triangle(10,6,3,4,5)
print(tri.area())
print(tri.areaperimeter())