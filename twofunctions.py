# prg to create marks card

def getmarks(sub1,sub2): 
    sub1=int(input("maths marks pls"))
    sub2=int(input("stats marks pls"))
    
def avg(): 
    result = (sub1+sub2)/2
    return result
    
def exam_result(): 
    if ((avg)>35):   
        print("student passes")
    else:   
        print("student fails")
        
print(exam_result())


