"""_summary_

Constructors in python
Is a special type of  method used to initialize object of a class
Constructor is  executed automatically when an object is created
main purpose of constructor is to declare  and initialize  instance variables
"""

class Student:
    def __init__(self,name,percentage):
        self.name  = name        #instance variable
        self.percentage = percentage
        
        
    def show(self):
            print("Name is:", self.name, "and percentage is:", self.percentage)
            
#object of a class 
stud = Student("Jessa",80)
stud.show()