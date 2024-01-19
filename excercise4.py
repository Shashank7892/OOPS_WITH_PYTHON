class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showdetails(self):
        print(f"Hi my name is {self.name}, my age is {self.age}..")
        
class Student(Person):
    def __init__(self,name,age,occupation):
        super().__init__(name,age)
        self.occupation=occupation
        
    def showdetails(self):
        super().showdetails()
        print(f"I am a {self.occupation}")
        
class Teacher(Person):
    def __init__(self,name,age,occupation):
        super().__init__(name,age)
        self.occupation=occupation
        
    def showdetails(self):
        super().showdetails()
        print(f"I am a {self.occupation}")

stu=Student("ajay",23,"student")
stu.showdetails()
teach=Teacher("Madhu",46,"Professor")
teach.showdetails()