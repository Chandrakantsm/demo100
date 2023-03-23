def getmarks():
    sub1=int(input("Enter the marks for maths pls"))
    sub2=int(input("Enter the marks for stats pls"))
    print(sub1,sub2)
    result_avg=avg(sub1,sub2)
    exam_result(result_avg)
    
    
def avg(s1,s2):
    result=(s1+s2)/2
    print("avg:", result)
    return result
    

def exam_result(performance):    
    if (performance>35):
        print("student passes") 
    else:
        print(" student fails")    

getmarks()   






