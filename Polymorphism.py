"""_summary_
is the ability of an object to take many forms
"""




class  Circle:
    
    
    pi = 3.14   
    
    def __init__(self,radius):
        self.radius = radius
        
        
    def calculate_area(self):
        print("Area of circle:", self.pi * self.radius * self.radius)
        
        
        
class  Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width  
    
    
    
    def calculate_area(self):
        print("Area of a reactangle: ", self.length * self.width)
                
            


def area(shape):
    #call action
    shape.calculate_area()







#creating an object 
cir = Circle(5)
rect = Rectangle(10,5) 
     
        




#calling from common function
area(cir)
area(rect) 
        