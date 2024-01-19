class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def Showdetails(self):
        print(f" the university name is {self.uni_name}")
        
class Course(University):
    def __init__(self,course_name):
        self.course_name=course_name
    
    def Showdetails(self):
        super().Showdetails()
        print(f" the course name is {self.course_name}")

class Branch(University):
    def __init__(self,uni_name,branch_name):
        super().__init__(uni_name)
        self.branch_name=branch_name
    
    def Showdetails(self):
        super().Showdetails()
        print(f" the branch name is {self.branch_name}")
        
class Student(Course,Branch):
    def __init__(self,uni_name,course_name,branch_name,student_name):
        Course.__init__(self,course_name)
        Branch.__init__(self,uni_name,branch_name)
        self.student_name=student_name
        
    def Showdetails(self):
        Course.Showdetails(self)
        Branch.Showdetails(self)
        print(f" Student name is {self.student_name}")
        
class Faculty(Branch):
    def __init__(self,uni_name,branch_name,faculty_name):
        super().__init__(branch_name,uni_name)
        self.faculty_name=faculty_name
        
    def Showdetails(self):
        super().Showdetails()
        print(f" faculty name is {self.faculty_name}")
        
stu=Student("BIT","MCA","Computer Applications","Ajay")
print(Student.mro())
stu.Showdetails()

Ftu=Faculty("BIT","Computers","vijay")
Ftu.Showdetails()
