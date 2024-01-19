class Human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class Male:
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")
    
class Boy(Human,Male):
    def work(self):
        Human.work(self)
        Male.work(self)
        print("i can work and code")

boy_1=Boy()
boy_1.eat()
boy_1.flirt()
boy_1.work()
print(Boy.mro())

# output
# i can eat
# i can flirt
# i can work
