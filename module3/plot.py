# import pandas as pd
# import matplotlib.pyplot as plt

# #  creating data set
# # data=[['emp_no','emp_name','design','salary']
# data=[[101,'a','ex_eng',2],
#       [102,'b','sn_eng',4],
#       [52,'c','jn_eng', 6],
#       [104,'d','dep_eng',8]]

# # dataframe created for above array data
# df=pd.DataFrame(data,columns=['emp_no','emp_name','design','salary'])
# print(df)                

# # creat histogram for numeric data
# df.hist().

# # show plot
# plt.show()

# import pandas 
# import matplotlib.pyplot as plt

# data =[['EMP001','M',34,123,'Normal',350],['EMP002','F',25,124,'Normal',300],
#        ['EMP003','M',39,150,'Normal',350],
#        ['EMP006','M',39,160,'Normal',350],
#        ['EMP007','M',39,165,'Normal',250],
#        ['EMP004','M',29,110,'Obesity',150],
#        ['EMP005','F',23,140,'Underweight',300],
#        ['EMP005','F',23,129,'Underweight',300],]

# dataframe= pandas.DataFrame(data,columns = ['Name','Gender','Age','Sales','BMI','income'])
# dataframe.hist()
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt
data = [['vinayak',  34, 123, ],
        ['arun',  40, 114, ],
        ['varun',  37, 135, ],
        ['kiran',  30, 139, ],
        ['gourav',  44, 117, ],
        ['varsha',  36, 121, ],
         ]
# dataframe created with
df=pd.DataFrame(data,columns=["name","aze","roll_number"])
df.plot.bar()
plt.bar(df["name"],df["aze"],df["roll_number"])
# plt.xlabel("name")
# plt.ylabel("roll number")
# # plt.xlabel("roll number")
# # plt.xlabel('aze')
plt.show()