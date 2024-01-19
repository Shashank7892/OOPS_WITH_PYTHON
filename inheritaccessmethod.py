# if we want the base class method statement as well as the new overridden statement use the super() function to access the method
#i.e

class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def work(self):
        super().work()
        print("I can code")

male1=Male()
male1.work()

#output 
# I can work
# I can code