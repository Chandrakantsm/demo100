#  find the largest of three elements
a,b,c=8,6,7

#  checks weathet a is larger than both b and c
if (a>b) and (a>c):
    print(a,"is larger than",b,c  )
    
    #  checks wether b is larger than both c and a
elif (b>a) and(b>c):
    print(b,"is larger than",a,c)
    
    #directly prints c is the largest 
else:
    print(c,"is the larger than",a,c)    