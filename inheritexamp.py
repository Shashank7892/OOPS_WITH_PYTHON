class Human:
    def eat(self):
        print("I can eat")
    
    def work(self):
        print("I can work")

class Male(Human):
    pass

male_1=Male()
male_1.eat()
male_1.work()    #output I can eat 
                        #I can work inheriting methods of base class in derived class
                        