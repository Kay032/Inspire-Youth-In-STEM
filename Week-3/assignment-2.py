#write a program that solves quadratic equation
#using for loop draw a diamond 
  #draw a triangle
  #draw pascals triangle

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


d = (b**2) - (4*a*c)

sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)





print("The solutions are {0} and {1}".format(sol1, sol2))
