# list=[]
# for i in range (1,n+1):
#     if n%i==0:
#         list.append(i)
# print("The factors of ",n,"are:")        
# print(list)        

# 21 calculator
# a=float(input("Enter first number:"))
# b=float(input("Enter second number:"))
# c=int(input("Enter 1 for additon:\nEnter 2 for subtraction :\nEnter 3 for multiplication:\nEnter 4 for division :\n "))

# match c:
#     case 1:
#         print("The sum of ",a,"and",b,"is:",a+b)
#     case 2:
#         print("The difference of ",a,"and",b,"is:",a-b)    
#     case 3:
#         print("The product of ",a,"and",b,"is:",a*b) 
#     case 4:
#         print("The division of ",a,"and",b,"is:",a/b)  
#     case  _:
#         print("Pls enter the correct choice of number.")

#  22  add two matrices
# reading inputs for matrix1   not working
# mat1=[]
# mat2=[]
# mat3=[]
# i=3
# j=3

# for i in range(0,3):
#     for j in range(0,3):
#         element=int(input("Enter  the element of the first matrix:"))
#         mat1.append([element])
# print(mat1)        

# for i in range(0,3):
#     for j in range(0,3):
#         element=int(input("Enter  the element of the second matrix:"))
#         mat2.append([element])
# print(mat2)

# for i in range(0,3):
#     for j in range(0,3):
#         mat3[i][j]=mat1[i][j]+mat2[i][j]    
#         mat3.append([element])
# print(mat3)        

# # 23 transpose a matrix
# mat=[]
# i=3
# j=3

# for i in range(0,3):
#     for j in range(0,3):
#         element=int(input("Enter  the element of the first matrix:"))
#         mat.append([element])
# print(mat)

# for j in range(0,3):
#     for i in range(0,3):
#     # for j in range(0,3):
#         print(mat[i][j])

# # 24 multiply two matrices 
# A=[[1,2,3],[4,5,6,],[7,8,9]]
# B=[[1,2,3],[4,5,6,],[7,8,9]]
# result=[]
# # iterating by row of A
# for i in range(len(A)):
#     # iterartig by coloumn of B
#     for j in range(len (B[0])):
#         # iterating by rows of B
#         for k in range(len(B)):
#             result[i][j] +=(A[i][k] *B[k][j])
# for r in result:
#     print[r]            

# # # 25 prg to check weather a string
# s="malayalam"
# r=s[::-1]
# print(r)
# if s==r:
#     print(s, " is a palindrome")
# else :
#     print(s,"is not a palindrome")    

# 26 pyramid patterns of numbers  till 10   
# # how to break the rows
# n=10
# for rows in range(0,n):
#     for col in range(0,rows+1):
#         print(rows,end="+ ")

#  27 prg to merge two dictionaries
# A={1:"a",2:"b",3:"c"}
# B={5:"d",6:"e"}
# print(dict(A)|dict(B))
# print({**dict(A),**dict(B)})

# d1={1:"l",2:"m"}
# d2={3:"o",4:"p"}
# d3=d2.copy()
# d3.update(d1)
# print(d3)

# 28 access index of a list
# list=[0,1,2,"python",["hello","world" ]] 
# print(list[4][0],list[2])
# #  its not working
# for i in range(len(list[i])):
#     print(i)

# 29 concatenate two lists
# l1=[1,2,3,4,5]
# l2=["a","b","c",[1,2]]
# l3=l1+l2
# print(l3)

# 30 prg to get last element of the list
# l1=[1,2,3,4,5]
# print(l1[::-1])

# 31 prg to randomly select an element from the list
# import random
# l1=[1,2,3,4,5]
# i=random.randint(0,len(l1))
# print(l1[i])

#  32 print odd numbers in a list
# l1=[1,2,4,5,6,8,7,9,5,2,4,6,3,1,3]
# l_odd=[]
# for i in l1:
#     if l1[i]%2 != 0:
#         print(l1[i],end="   ")

# print("\n")       
# only_even=[num for num in l1 if num%2==0]
# print(only_even)

# 33 print even numbers in a range
# for i in range(12,35):
#     if i%2==0:
#        print(i,end="  ") 

# 34 find sum of array elements
# arr=[1,2,3,4,5,6.6]
# a=sum(arr)
# print(a)

# sum=0
# for i in arr:
#     sum=sum+i   
# print("sum is :",sum)         

# arr=['a','b','c']
# for i in arr:
#     print(i) 

# 35 chk if a string is a number(float)
# str="580001"
# x=str.isnumeric()
# y=str.isdigit()
# z=str.isalpha()
# print(x,y,z)
# if x==True:
#     print("its a number")

#  36 convert  two lists into a dictionry
# player=["a","b","c","d"]
# score=[10,20,30,40]
# match_score={player[i]:score[i] for i in range(len(player))}
# print(match_score)

#  37 reverse a number
# a=580001
# print(type(a))
# y=str(a)
# print(type(y))
# r=y[::-1]
# r_int=int(r)
# print(r)
# print(type(r))

# 38  find the power of number
# print(3**2)
# print(3**2**2)

# 39 count th number of digits in a number
# a=580001
# y=str(a)
# r=len(y)
# print(r)

#  40 remove duplicate element from a list
# l=[1,2,3,4,1,2,3,4,5,6,7,8,9]
# print(l)
# y=set(l)
# print(y)
# z=list(y)
# print(z)

# 41  prg to display a calender
# import calendar
# yy=2023   #year
# mm=4   #month

# print(calendar.month(yy,mm))

#  42 find sum of array
# arr=[1,2,3,4.5,5]
# sum=0
# for i in arr:
#     sum=sum+i   
# print("sum is :",sum)

# 43 chk for URL in a string

# 44 sort dictionary key values list
# not understanding it. not working
# test_dict={"y":20,"a":1,"b":2,"c":3,"m":15,"d":4}
# res=dict()
# for key in sorted(test_dict):
#     res[key]=sorted(test_dict[key])
# print("The sorted dictionry is :",res)

#  45 find the size of tupple
# y=(10,20,10.5,"hubli","dwd")
# print(len(y))

# 46 list of tuples from given list having number and its cube in each tuple 
# l=[1,2,3,4,5,6.6]
# res=[(val, pow(val,3)) for val in l ]
# print(res)

#  47 extract digits from list
l=[1,"a",2,"d",37,4.8,"g"]
print(l)
# l_digits=[num for i in l:]


# 48 delete all elements from the list
# l=[10,20,30,40,50,2,60,70]
# l=l.clear()
# print(l)    

#  49 based on basic salary print gross salary
# basic_salary=10000
# pf=basic_salary*.12
# hra=basic_salary*.1
# ta=basic_salary*.1
# da=basic_salary*.1
# gross_salary=basic_salary+pf+hra+ta+da
# print(gross_salary)

# 50   find avearge of numbers from a list
# l=[12,3,6]
# avg=sum(l)/len(l)  
# print(avg)
##prg to find the area of a circle
r=float(input("Enter the radius of the circle"))
area=3.142*r*r
print(" Area of the circle is ",area)    
print("prg running successfully")   15 prime numbers from 1 to 100
# flag=False
# for i in range(3,100):
#     if i%2==0:
#         print(i,"is not a prime number.")
#     else:
#         for j in range(3,i):
#             if i%j==0:
#                 flag=True
#                 break
#         if flag:
#             print(i,"is not a prime number.")
#         else:
#             print(i,"is a prime number.")

# 16 factorial number
# n=10
# fact=1
# while n>1:
#     fact=fact*n
#     n=n-1
#     print(fact)
# print("***")    
# print(fact)   
                    
#  17 Fibonacci sequence upto 1000
# n1=0
# n2=1
# fib=0
# while fib<1000:
#     fib=n1+n2
#     n1,n2=n2,fib
#     print(fib)

# 17 numbers divisible by another number

# 18 convert decimal to binary  octal hexadecimal
# n=15
# print("decimal",n," in binary system is", bin(n),".")
# print("decimal",n," in octal system is", oct(n),".")
# print("decimal",n," in binary system is", hex(n),".")

#  19 find value of a character
# c=")"
# print("The ASCHII value of    ",c,"     is  ",ord(c),".")

# 20 Factors of a number
# n=10000254