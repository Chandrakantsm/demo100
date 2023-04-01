#program find wheather sum is odd or even

def getdata():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print("The two numbers are",a,b)
    addition(a,b)
    
def addition(a,b):
    sum=a+b
    print("The sum of two number is", sum)
    oddeven(sum)
    
def oddeven(sum):
    if sum%2==0:
        print("The sum ",sum," is even")
    else:
        print("The sum ",sum," is odd")  
getdata()          