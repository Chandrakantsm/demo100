
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
            