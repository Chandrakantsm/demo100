
# class bird():
#     def intro(self):
#         print("there are many types of birds")
#     def flight(self):
#         print("most of the birds can fly, but some cant")
        
# class sparrow    


class Bird():
    def Intro (self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow (Bird):
    def display(self):
        print("You are in display")
        

class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly.")

obj_Bird = Bird()
obj_Sparrow =Sparrow()
obj_Ostrich=Ostrich()

obj_Bird.Intro()
obj_Sparrow.Intro()
obj_Ostrich.Intro()

obj_Bird.flight()
obj_Sparrow.flight()
obj_Ostrich.flight()
class car():
    def display(self):
        print("car info display")
class truck():
    def display(self):
        print("truck info display")    
obj1=car()
obj2=truck()
def func(obj):
    obj.display() 
func(obj1)   
func(obj2)           

# Encapsulation
# class parent():
#     a=0
#     __c=0
#     def __init__(self):
#         self.a="python" 
#         self.__c="programming"
# class child(parent):  
#     def __init__(self):
#         parent .__init__(self)
#         print(self.__c)
# obj1=parent()
# print(obj1.a)  

# obj2=child()
# print(obj2.__c)         

#  to inherit values from parents
class base():
    a=10
    
class derive(base):
    b=20
    def add(self):
        c=self.a+self.b
        print(c)
obj1=derive() 
obj1.add()       
#   abstraction

from abc import ABC, abstractmethod
class polygan(ABC):
    @abstractmethod
    def sides(self):  
        pass   
class triangle(polygan):    
    def triangle(self):  
        print(" i have three sides")
class pentagon(polygan) :       
    def pentagon(self):
        print(" i have five sides")    

# driver code    
r=triangle()
r.sides()    
        
            