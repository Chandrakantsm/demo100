# creating a list
# newlist=['python',25,2022]
# #print(newlist)

# print("+ve and -ve indexing of the first element\n+ive index",newlist[0],"\n-ve index",newlist[-3] )

# print(" +ve and -ve indexing of the second element\n+ive index",newlist[1],"\n-ve index",newlist[-2] )

# print("+ve and -ve  indexing of the third element\n+ive index",newlist[2],"\n-ive index",newlist[-1] )

# newlist=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# newlist

# print(len(newlist))

# #slicing
# print(newlist[0:2])

#print(newlist[2:4],newlist[4:6])

#print(newlist[4:6])
#extending th elist

# newlist.extend(["hello world!",1.618])
# print(newlist)

# #append
# newlist.append(["hello world!",1.618])
# print(newlist)

# further functions
# list=[1,2,3,4,5,6,7]
# print(len(list))
# list.append(4)
# print(list)
# print(list.count(4))
# print(list.index(2))
# list.insert(8,9)
# print(list)
# print(max(list),min(list),sum(list))

# newlist=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# print("Before changing",newlist)
# print(newlist[0])
# print("after changing",newlist)
# newlist[1]=1.618
# print("after changing",newlist)
# newlist[2]=[3.14,2022]
# print("after changing\n",newlist)


#delete
# newlist=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# del(newlist[0])
# print("After changing\n",newlist)
# del(newlist[-1])
# print(newlist)

# newlist=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# print("Before deleting\n",newlist )
# del(newlist)
# print("After deleting",newlist)

#converting string to list using split function
# message="python is programmimg language."
# print(message.split())

#use of split() function with a delimiter
# text='p,y,t,h,o,n'
# print(text.split(','))

# nlis_1=['a','b','hello','python']
# nlis_2=[1,2,3,4,5,6,]
# print(len(nlis_1))
# print(len(nlis_2))
# print(nlis_1+nlis_2)
# print(nlis_1*3)
# print(nlis_2*2)
# for i in nlis_1:
#     print(i)

# for i in nlis_2:
#     print(i)
# print(4 in nlis_1)    
# print(4 in nlis_2)

# copy th list

# nlis=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# copy_list=nlis
# print("nlis",nlis)
# print("copy_list",copy_list)

#changes in original list wil reflect in copied list also
# nlis=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# print(nlis)
# copy_list=nlis
# print(copy_list)
# print("copy_list[0] :",copy_list[0])
# nlis[0]="hello python"
# print(copy_list)
# print("copy_list[0]:",copy_list[0])

# #clone the list: the cloned list is a new copy of original list
# nlis=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# clone_lis=nlis[:]
# print(clone_lis)

#changes in original list ,willnot reflect in cloned list.
# nlis=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
# print(nlis)
# clone_lis=nlis[:]
# print("clone_lis:", clone_lis)
# nlis[0]= "hello python"
# print("nlis",nlis)
# print("clone_lis",clone_lis)

# #concatenate the list
# a_list=['a', 'b', ['c', 'd'], 'e']
# b_list = [1,2,3,4,5,(6,7), True, False] 
# new_list=a_list+b_list
# print("new_list",new_list)

#INPUT() functions: to supply inputs during runtime
# text=input("Enter a string:")
# print("The text is:",text)
# print(type(text))

# number=input("enter an integer:")
# print(number,type(number))

# number=int(input("enter a number"))
# print(number,type(number)) 

# number=float(input("enter a number"))
# print(number,type(number))

# eval() function converts a string into a float or int
expression="8+7"
total=eval(expression)
print("sumof the expression is:",total)
print(type(expression))
print(type(total))












