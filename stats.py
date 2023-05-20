import csv
import statistics as st
marks1=[]
marks2=[]
marks3=[]
i=0
j=0

with open("C:/Users/User4/Desktop/stats.csv","r") as marks:
    file_handle = csv.reader(marks)
    
    for i in file_handle:
        if  i[1]!="marks1":
            marks1.append(int(i[1]))
                # marks2.append(int(i[2]))
                # marks3.append(int(i[3]))
            
           
            
    # for j in file_handle:        
    #     if   j[2]!="marks2":
    #         marks2.append(int(j[2]))   
            
    # for i in file_handle:
    #         if  i[1]!="marks1":
    #         marks1.append(int(i[1]))        
            
print("marks1 =",marks1)        
mean=round(st.mean(marks1),3) 
median=round(st.median(marks1),3)
mode=round(st.mode(marks1),3)

print("Mean=",mean,". median=",median,". mode=",mode)

print("marks2= ",marks2)
print("std deviation of marks1= ",round((st.pstdev(marks1)),3))


         
    
    