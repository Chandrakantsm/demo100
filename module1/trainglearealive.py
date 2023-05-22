
# prg to find the area of triangle

def getdata():
    b=float(input("enter base value:"))
    h=float(input("enter height value:"))
    ans=tri_area(b,h)
    return ans
    
def tri_area(b,h):
    area= b*h/2   
    return area


a=getdata()
print(a)
