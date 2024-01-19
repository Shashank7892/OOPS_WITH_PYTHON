class Rectangle:
    
    def __init__(self,width,length):
        Rectangle.width=width
        Rectangle.length=length
        
    def area(self):
        return Rectangle.width*Rectangle.length
    
R1=Rectangle(20,30)
print(f"the area of a rectangle is {R1.area()}")