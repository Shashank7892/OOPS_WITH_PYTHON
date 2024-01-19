class Human:
    def __init__(self):
        self.eyes=2
        self.nose=1
        
class Male(Human):
    def __init__(self):   
        super().__init__()     #############
        self.hands=2
        
male=Male()
print(male.eyes)    

# print(male.eyes)
#           ^^^^^^^^^
# AttributeError: 'Male' object has no attribute 'eyes' we cannot access the base class attributes because of __init___ in child class
# if we want to access the base class attributes we need to use super() in __init__() of child class

print(male.nose)
print(male.hands)
# output
# 2
# 1
# 2