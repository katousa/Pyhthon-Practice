#Write a program that solves a quadratic equation usind the given coefficients

import math
import sys

a=float(input("To Get The Quadratic Equation, Enter 'a': "))
b=float(input("Enter 'b': "))
c=float(input("Enter 'c': "))

def QuadEq(a ,b ,c):
    
    if a==0:
        print("'a' Can't be zero!")
        sys.exit()

    d=(b**2)-(4*a*c)
    if d>0:
        x=(-b+math.sqrt(d))/(2*a)
        x1=(-b-math.sqrt(d))/(2*a)
        print("Equation has Two Real Roots:",x,"and",x1)

    elif d==0:
        x=  -b/(2*a) 
        print("Equation has One Real Root:",x)

    else:
        print("Equation has no Real Root")

QuadEq(a,b,c)
