# prg to create marks card

# def getmarks(sub1,sub2): 
#     sub1=int(input("maths marks pls"))
#     sub2=int(input("stats marks pls"))
#     return 

sub1=50
sub2=60


def avg(sub1,sub2): 
    result = (sub1+sub2)/2
    return result
    
def exam_result(): 
    if (avg()>35):
        print("student passes")
    else:   
        print("student fails")
        
exam_result()


