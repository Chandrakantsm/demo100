#  python program to find weather a number is prime or not
n=29
flag=False

# skipping 0 and 1, as there are no nums between them 
for i in range(2,n):
    if (n%i==0):
        flag=True
        print(n,"is not a prime number")
        break
    print(n,"is prime number.")  
    
    
      