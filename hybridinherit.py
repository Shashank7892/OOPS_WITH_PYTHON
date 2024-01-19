class Grandfather:
    def eat(self):
        print("Grand father eats slowly")
        
    def work(sself):
        print("i quit my job after my sons starts working")

class Father(Grandfather):
    def work(self):
        super().work()
        print("i started to work")
        
class Mother():
    def cook(self):
        print("i started perparing food")

class Son(Father,Mother):
    def study(self):
        print("my father and mother tell always me to study hard")
        
    def work(self):
        Father.work(self)
        print("i make my father proud by my work")
        
son_1=Son()
print(Son.mro())
son_1.eat()
son_1.work()
    