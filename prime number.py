n=int(input("Enter a number"))
Flag=False

if n%2==0:
    print(n,"is  not a prime number ")
else:
    for i in range(3,n):
        if n%i==0:
            Flag=True   
            break 
    if Flag:
        print(n,"is not a prime number") 
    else:
        print(n,"is  a prime number")       