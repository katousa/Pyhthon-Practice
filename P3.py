#Write a program to find the maximum of three given numbers

a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))
c = int(input("Enter Your Third Number: "))

def Max(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max

print("The Maximum Number is ",Max(a,b,c))
