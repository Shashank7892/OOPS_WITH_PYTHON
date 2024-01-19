class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Showdetails(self):
        print(f" Hi my name is {self.name} and my age is {self.age}....")

class Male(Human):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location
        
    def Showdetails(self):
        super().Showdetails()
        print(f" I live in {self.location}")
        
class Female(Human):
    def __init__(self, name, age,can_cook):
        super().__init__(name, age)
        self.can_cook=can_cook
    
    def Showdetails(self):
        super().Showdetails()
        print(f" Can cook : {self.can_cook}")
        

fem=Female("anitha",'23',True)
fem.Showdetails()
mal=Male("ajay",'25',"bangalore")
mal.Showdetails()