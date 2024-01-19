from abc import ABC,abstractmethod

class Vehicle:
    def __init__(self,n):
        self.num_of_wheels=n
        
    @abstractmethod
    def start(self):
        pass
