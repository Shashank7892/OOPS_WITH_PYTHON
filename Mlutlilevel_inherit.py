class Human:
    can_breath=True
    def __init__(self,num_heart):
        self.nose=1
        self.eyes=2
        self.num_heart=num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can done and dust")
        
class Male(Human):
    def __init__(self,name):
        self.name=name
    def work(self):
        print("i can work")

class Boy(Male):
    def __init__(self,lang,name,heart):
        Human.__init__(self,heart)
        super().__init__(name)
        self.lang=lang
    def work(self):
        super().work()
        Human.work(self)
        print("i can also work")
    
    def task(self):
        print("I can perform tasks")
        
    def display(self):
        print(f"hi my name is {self.name} and i work on language {self.lang} also my heart rate is {self.num_heart} bpm")
        
boy_1=Boy('python','ajay','234')
boy_1.eat()
boy_1.work()
boy_1.task()
print(Boy.mro())
boy_1.work()
print(boy_1.nose)
print(boy_1.eyes)
print(boy_1.num_heart)
print(boy_1.name)
print(boy_1.lang)
boy_1.display()
print(boy_1.can_breath)