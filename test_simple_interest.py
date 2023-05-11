#  python prg to find simple interest for rs 7500
p=7500
t=int(input("enter the time in years."))
r=float(input("eneter the rate of interest."))

#  calculation of simple interst
simple_interest = (p*t*r)/100

print("simple interst for rs 7500 for",t,"years, @ ",r,"% rate of interst is Rs",simple_interest)