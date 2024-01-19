class Human:
    def __init__(self,num_heart):
        self.eyes=2
        self.nose=1
        self.num_heart=num_heart
        
class Male:
    def __init__(self,name):
        self.name=name
        
class Boy(Human,Male):
    def __init__(self,name,heart,lang):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.lang=lang
    
    def display(self):
        print(f"hi my name is {self.name} and I work on the language{self.lang} , my heart rate is {self.num_heart} bpm")

boy1=Boy("ajay","234","python")
print(boy1.eyes)
print(boy1.name)
print(boy1.num_heart)
print(boy1.lang)
boy1.display()