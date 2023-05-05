import csv

with open("C:/Users/User4/Desktop/ipl_2023_dataset","r")as ipl:
    file_handle = csv.reader(ipl)

    for i in file_handle:
        print(i)