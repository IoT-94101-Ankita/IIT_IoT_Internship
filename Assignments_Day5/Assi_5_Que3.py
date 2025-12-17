from geometry import area_of_circle as c
from geometry import area_of_rect as re

r=float(input("enter radius:"))
print(f"area f circle :{c(r)}")

l=float(input("enter length : "))
b=float(input("enter breadth:"))
print(f"area of rectangle:{re(l,b)}")