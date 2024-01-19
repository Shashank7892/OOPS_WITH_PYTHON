class Human:
    def eat(self):
        print("i can eat")
    
    def work(self):
        print("i can work")
        
#Override base class method with derived class method i.e redefine the method as the way we want with same method name   
class Male(Human):
    def work(self):
        print("I can code")
        
male_1=Male()
male_1.eat()
male_1.work()

#output i can eat
#       I can code # when we create the object of male class it will access method of derived class(Male) not the base class(Human)