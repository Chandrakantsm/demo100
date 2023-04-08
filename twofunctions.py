# prg to create marks card

#  This function will get the marks in sub1 and sub2
def getmarks(sub1,sub2): 
    sub1 = int(input("maths marks pls"))
    sub2 = int(input("stats marks pls"))
 
#This function will calculte th percentage    
    
def calculate(): 
    total = sub1 + sub2   
    avg = total/2
 
# This function will classify the result    
def exam_result(): 
    if (avg>35):   
        result = pass
    else:   
        result = fail 
        
print(exam_result)


