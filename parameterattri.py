class Human:
    def __init__(self,num_hearts):
        self.eyes=2
        self.nose=1
        self.num_hearts=num_hearts
        
class Male(Human):
    def __init__(self,name,hearts):
        super().__init__(hearts)
        self.name=name

male=Male("ajay",'1234')
print(male.name) 
print(male.num_hearts)

# output: ajay