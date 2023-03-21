n=int(input("Enter a number"))
flag=False
if(n<2):
    print("not a prime number")   
elif(n%2==0):
    print("not a prime number")
else:
    for i in range (3,n):
        if(n%2==0):
            flag=True
            break
if flag==True:
    print("non prime number") 
else:
    print("prime number")                     

