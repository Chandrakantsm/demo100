n=int(input("Enter a number"))
Flag=False

for j in range(2,n+1):
    # if n%2==0:
    #  print(j,"is  not a prime number ")
    # else:
     for i in range(3,n+1):
        if n%i==0:
            Flag=True   
            break 
     if Flag:
      print(j,"is not a prime number") 
     else:
      print(j,"is  a prime number")       