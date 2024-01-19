from abstractiondemo import Vehicle

class bike(Vehicle):
    def __init__(self,n):
        super().__init__(n)
        
    def start(self):
        print(f"the number of wheels for a bike {self.num_of_wheels}")
        print("bike starts with a kick")
    
class scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
        
    def start(self):
        print(f"the number of wheels for a scooty {self.num_of_wheels}")
        print("scooty starts with a self ignition")

class car(Vehicle):
    def __init__(self,n):
        super().__init__(n)
        
    def start(self):
        print(f"the number of wheels for a car {self.num_of_wheels}")
        print("car starts with a key")
    
    