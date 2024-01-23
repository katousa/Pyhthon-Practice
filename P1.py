#Write a program to calculate the sum of odd and even numbers from zero to a given number

n=int(input("Enter a number:"))
s1 =0
s2 =0

for i in range(0,n+1,2):
    s1=s1+i

for i in range(1,n+1,2):
    s2=s2+i

print("The Sum of Even Numbers from 0 to",n,"is:",s1,'\n',"and",'\n',"The Sum of odd Numbers from 0 to",n,"is:",s2)
