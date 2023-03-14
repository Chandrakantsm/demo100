n=int(input("Enter the number"))
flag=False

#for j in range(2,n): 
    
for i in range (2,n):
        if(n%2==0):
            flag = True
            break
if flag:
            print(n,"is not a prime number")
else:
            print(n,"is a prime number")    