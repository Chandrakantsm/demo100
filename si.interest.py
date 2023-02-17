# # # prg to calculate simple interest
# p=int(input("Enter principle amount in rs"))
# t=int(input("Enter time in years "))
# r=float(input("Enter rate of interest "))
# si=(p*t*r)/100
# print("simple Interest on Rs",p," for",t," years at the rate", r,"% is Rs ",si, "\nThe total amount is Rs", si+p)



def getdata():
    p=int(input("Enter principle amount in rs"))
    t=int(input("Enter time in years "))
    r=float(input("Enter rate of interest "))    
    display(p,t,r,)

def calc():  
     si=p*t*r/100  
     #display(si)

def display(p,t,r,si):
      print(p,t,r,si)

getdata()      

# def calc():    
#     si=(p*t*r)/100

# def display():
# print("simple Interest on Rs",p," for",t," years at the rate", r,"% is Rs ",si, "\nThe total amount is Rs", si+p)
