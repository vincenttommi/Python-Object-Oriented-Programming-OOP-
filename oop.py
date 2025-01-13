"""_summary_
Is a programming paradigm based on the concept of objects 
object contains both  data and code  
creating class and object in python
"""
class Employee:
    #class variables
    company_name =  'ABC Company'
    
    
    #constructor  to initialize the object
    def __init__(self,name,salary):
        #instance variables
        self.name  = name
        self.salary = salary
        
    
    def  show(self):
        print("Employee:", self.name, self.salary,self.company_name)  
        
#creating first object
emp1  =  Employee("Harry", 12000)
emp1.show()


#creating second object
emp2 =  Employee("Emma",10000)
emp2.show()
        