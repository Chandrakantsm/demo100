import numpy as np
import scipy as sp
import matplotlib.pyplot as plt 
# %matplotlib inline
k=np.arange(0,8)
x=np.cos(2*k*np.pi/4)
y=plt.stem(k,x,use_line_collection=True)
print(y)