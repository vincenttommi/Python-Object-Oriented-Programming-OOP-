"""_summary_

Inheritance Is the process of iheriting properties of the parent class into child class

main purpose is to support code reusability
"""



class Vechicle:
    
    def __init__(self, name, color, price):
        self.name = name
        self.color =  color
        self.price  = price 
        
        
    def info(self):
        print(self.name, self.color, self.price)
        
    
    
class  Car(Vechicle):
    
    def change_gear(self,no):
        print(self.name, 'change gear to number', no)
            
    
    
    
#Creating object of the car

car =  Car('BMW X1', 'Black', 35000)
car.info()
car.change_gear(5) 