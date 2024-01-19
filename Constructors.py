# creation of constructor and adding attributes
# useage of __init__ and self in classes and object
class CarDesign:
    def __init__(self,model,brand):
        self.model=model #data attributes
        self.brand=brand #data attributes
        print("object is created")
    
car1=CarDesign('Fortuner','toyota')
print(car1.model)
print(car1.brand)
car2=CarDesign('Inova Crysta','toyota')
print(car2.model)
print(car2.brand)