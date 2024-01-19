class Instructor:
    followers=0 #class object variable no need of self, i.e a default attribute such as gobal variable for each and every object
    
    def __init__(self,name,address): # creation of constuctor with attributes 
        #self determones the actual object i.e current object ex ins1 first,then ins2 as second
        self.name=name # self.name is an attrubute same as variable
        self.address=address
        
    # creation of methods self is mandary in classes and objects because it determines the actual object
    
    def display(self):
        print("hi")
    
    def display1(self):
        print("hiiiiiiiiiii")
        
    # we can pass arguments in the methods also and can have attributes in that methods
        
    def display2(self,subjectname):
        print(f"hi my name is {self.name} and I teach {subjectname}") # with subjectname name we dont use self because its not 
                                                                      # an attribute its just a parameter value swe are passing
                                                                      # attributes are nothing but variables and subjectname is not a variable    
        # if we use self with subjectname AttributeError: 'Instructor' object has no attribute 'subjectname'
        
    # modify the followers for each and every object
    
    def update_followers(self,follower_name):
        self.followers+=1   # here we are using self beacuse its an attribute ie class attribute so we need to use self to an object  
ins1=Instructor("Jenny","Delhi")
print(ins1.display())
# The output will be 
# hi
# None because every function should return some value but we are printing the value in the function only
#so if we use print() to print a function containing print function it will print None

ins1.display1()
# the output for ins1.display1() will be "hiiiiiiiiiii" there no display of none

ins1.display2("python")
# the output is hi my name is Jenny and I teach python
print(ins1.followers)
# the output will be 0
ins1.update_followers("payal")
print(ins1.followers)
# the output will be 1 after updating
ins2=Instructor('gowda','bengaluru')
print(ins2.followers)
# the output will be 0

 

  

