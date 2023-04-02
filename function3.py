def main():
    a=10
    result=concat_function(a)
    my_string="the entered value"+str(a)+"is even" "with remainder: " +str(result)
    display_result(my_string,result)
    
        
def concat_function(x):
    return x % 2
          
def display_result(my_string,result): 
    if(result % 2 == 0):
        print("Entered value is even\n",my_string)
    else:
        print("Entered value is odd\n",my_string)    
    
main()            