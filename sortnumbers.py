#prg to sort list numbers and sort numbers
# read the numbers in list format
list1=[]
n=(int(input("enter how many numbers: ")))
for i in range(n):
    list1.append(int(input()))
print(list1) 

#sorting numbers usinf for loop
for i in range(0,n-1):
    for j in range(i+1,n):
        # print("compairing",list1[i],list1[j])
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
            print(list1)
print("*****************************")
print(list1)


        