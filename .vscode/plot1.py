import pandas as pd 
import matplotlib.pyplot as mat 
data=[[]
    
]
marks1=[]
database=[]
column_names_list=[]

    
    for i in file_handle:
        if  i[1]!="marks1":
            marks1.append(int(i[1]))
            