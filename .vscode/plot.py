import pandas as pd
import matplotlib.pyplot as plt

#  creating data set
# data=[['emp_no','emp_name','design','salary']
data=[[101,'a','ex_eng',2],
      [102,'b','sn_eng',4],
      [103,'c','jn_eng', 6],
      [104,'d','dep_eng',8]]

# dataframe created for above array data
df=pd.DataFrame(data,columns=['emp_no','emp_name','design','salary'])

# creat histogram for numeric data
df.hist()

# show plot
plt.show()