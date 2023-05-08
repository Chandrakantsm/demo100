import csv
with open("C:/Users/User4/Desktop","r") as ipl:
    file=csv.reader(ipl)
    
    for i in file:
        print(i) 