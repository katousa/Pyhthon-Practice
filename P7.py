#Write a program to calculate area and perimeter of a square or a rectangle using inheritance:

class Rectangle:

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def perimeter(self):
        return 2*(self.l + self.w)
    
    def area(self):
        return self.l * self.w
    

class Square(Rectangle):

    def __init__(self, s):
        self.l = s
        self.w = s

    
num = input("Enter the Sides of your Square or Rectangle: ")

n = num.split()

if len(n) > 1:
    o = Rectangle(float(n[0]),float(n[1]))
else: 
    o = Square(float(n[0]))

print("The Perimeter: ", o.perimeter(),'\n',"The Area: ", o.area())
