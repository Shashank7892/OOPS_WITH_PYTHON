class A:
    def display(self):
        print("this is from class A")

class B(A):
    def display(self):
        print("this is from class B")
        
class C(A):
    def display(self):
        print("this is from class C")

class D(B,C):
    def display(self):
        print("this is from class D")
        
D1=D()
D1.display()
print(D.mro())
