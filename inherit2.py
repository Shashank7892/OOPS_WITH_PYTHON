class Humman:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
# the derived class can have their own methods rather than the base class methods        
class Male(Humman): 
    def trips(self):
        print("go for night outs")
        
male1=Male()
male1.eat()
male1.work()
male1.trips()

#I can eat
#I can work
#go for night outs   
