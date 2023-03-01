# creating a list
newlist=['python',25,2022]
#print(newlist)

print("+ve and -ve indexing of the first element\n+ive index",newlist[0],"\n-ve index",newlist[-3] )

print(" +ve and -ve indexing of the second element\n+ive index",newlist[1],"\n-ve index",newlist[-2] )

print("+ve and -ve  indexing of the third element\n+ive index",newlist[2],"\n-ive index",newlist[-1] )

newlist=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
newlist

print(len(newlist))

#slicing
print(newlist[0:2])

#print(newlist[2:4],newlist[4:6])

#print(newlist[4:6])
#extending th elist

newlist.extend(["hello world!",1.618])
print(newlist)

#append
newlist.append(["hello world!",1.618])
print(newlist)

# further functions
list=[1,2,3,4,5,6,7]
print(len(list))
list.append(4)
print(list)
print(list.count(4))
print(list.index(2))
list.insert(8,9)
print(list)
print(max(list),min(list),sum(list))

newlist=['python',3.14,2022,[1,1,2,3,5,8,13,21,34],('hello','python',3.14,2022)]
print("Before changing",newlist)
print(newlist[0])
print("after changing",newlist)
newlist[1]=1.618
print("after changing",newlist)
newlist[2]=[3.14,2022]
print("after changing\n",newlist)



