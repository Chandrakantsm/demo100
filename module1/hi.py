class Engineering():
    Name=""
    des=""
    salary=""
    def display(self):
        pass
    
class Computer_Science(Engineering):
    def CS_fun(self,Name,des,salary):
        self.name=Name
        self.des=des
        self.salary=salary
        
    def display(self):
        print("Department of Computer Science",self.name,self.des,self.salary)
        
       
csobj=Computer_Science()
csobj.CS_fun("Laxmi","Backend Developer",80000)
csobj.display()

