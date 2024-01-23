import sys
#Write a program that in a class with 10 students,Calculates:

def average(num):
    ave = (sum(num))/(len(num))
    return ave

def distinction_counter(num):
    c = 0
    for i in range(len(num)):
        if num[i] >= 17:
            c = c+1
    return c

def failed_counter(num):
    c = 0
    for i in range(len(num)):
        if num[i] < 10:
            c = c+1
    return c

# __main__

grades = []
for x in range(10):
    n = float(input("Enter Grade:"))
    if 0 <= n < 21:
        grades.append(n)
    else:
        print("Grades should be between 0 to 20. Try Again.")
        sys.exit()

#a)The class avrerage grade:

print("The Average Grade is:", average(grades))

#b)Number of distinction students:

print("Number of Distinction Students:", distinction_counter(grades))

#c)Number of failed students:

print("Number of Failed Students:", failed_counter(grades))
