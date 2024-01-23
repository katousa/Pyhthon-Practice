#Write a program to give academic status report based on given grades

n = input("Enter The Student's Grades and Seperate Them by Space: ")

grade = n.split()
ave = 0

for num in grade:
    i=float(num)
    if 20>=i>=0:
        ave = ave + i
    else: 
        print("grades should be between 0 to 20.")
        exit()

if ave/len(grade)>=17:
    print("Pass With Distinction.")
elif ave/len(grade)<=12:
    print("Failed.")
else:
    print("Pass.")
