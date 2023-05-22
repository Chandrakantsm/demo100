#  prg to calculate compound interest
p=int(input("Enter principle amount in rs"))
t=int(input("Enter time in years "))
r=float(input("Enter rate of interest "))
n=int(input(" how many times interest to be compounded per year"))
compint=p(1+((r/n)**n*t))
print("compound Interest on Rs",p," for",t," years at the rate", r,"% is Rs ",compint) 
print("\nThe total amount is Rs", compint+p)
