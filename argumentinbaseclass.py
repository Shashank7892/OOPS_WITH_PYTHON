# if we have the arguments in base class and has to be accessed in derived class 

class Human:
    def __init__(self,humanheart):
        self.humanheart=humanheart
        
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
        
    def display(self):
        print(f"hi my name is {self.name} and my heartrate is {self.humanheart} bpm")
        
male=Male("ajay",'234')
print(male.name)
print(male.humanheart)
male.display()

# we need to pass the value from child class argument and with super () through it we can have base class arguments
# output:
# ajay
# 234

#hi my name is ajay and my heartrate is 234 bpm