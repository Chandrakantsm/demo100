
#create a 5 classes of engineers with their attributes with job descriptions using inheritance

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
            
            
class Electronic_communications(Engineering):
    def EC_fun(self,Name,des,salary):
        self.name=Name
        self.des=des
        self.salary=salary
    
    def display(self):
        print("Department of Electronic and communication",self.name,self.des,self.salary)
        

class Civil(Engineering):
    def CV_fun(self,Name,des,salary):
        self.name=Name
        self.des=des
        self.salary=salary
    
    def display(self):
        print("Department of Civil",self.name,self.des,self.salary)
        

class Mechanical(Engineering):
    def MC_fun(self,Name,des,salary):
        self.name=Name
        self.des=des
        self.salary=salary
    
    def display(self):
        print("Department of Mechanical",self.name,self.des,self.salary)
        

class Industrial(Engineering):
    def IN_fun(self,Name,des,salary):
        self.name=Name
        self.des=des
        self.salary=salary
    
    def display(self):
        print("Department of Industrial engg",self.name,self.des,self.salary)
        
csobj=Computer_Science()
csobj.CS_fun("Laxmi","Backend Developer",80000)
csobj.display()

ecobj=Electronic_communications()
ecobj.EC_fun("Rani","Test Engineer",70000)
ecobj.display()

cvobj=Civil()
cvobj.CV_fun("Arun","Design Engineer",60000)
cvobj.display()

mcobj=Mechanical()
mcobj.MC_fun("Ankit","Quality Engineer",50000)
mcobj.display()

inobj=Industrial()
inobj.IN_fun("Shweta","Manufacturing Technician",45000)
inobj.display()
        
# Department of Computer Science Laxmi Backend Developer 80000
# Department of Electronic and communication Rani Test Engineer 70000
# Department of Civil Arun Design Engineer 60000
# Department of Mechanical Ankit Quality Engineer 50000
# Department of Industrial engg Shweta Manufacturing Technician 45000