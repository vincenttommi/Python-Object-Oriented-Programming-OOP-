""""
is a method of wrapping data and objects into a single entity
Example  a class encapsulates all the data methods and variables

Need for encapsulation
acts as a  proctective layer
Encapsulation means  internal rep of  an object is gen hidden  from outside of object definition 
"""
class Employee:
    def __init__(self,name,salary):
        #private
        self.name  = name
        #private member
        # not  accessible outside of  a class
        self.__salary  = salary
        
    def show(self):
        print("Name is", self.name, "and salary is", self.__salary)
    
    
emp = Employee("Jessa",  10000)
emp.show()    

# access salary from outside  of a class

print(emp.__salary)
