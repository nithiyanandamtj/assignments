##Write a program which will find all such numbers which are divisible by 7 but are not a
##multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
##in a comma-separated sequence on a single line.

result=[]
for i in range(2000,3201):
    if i%7==0:
        if i%5!=0:
            result.append(i)
            
i=0           
while i<len(result):  
    if i<len(result)-1:
        print(result[i],end=",")
    else:
        print(result[i])
    i=i+1
    
##Write a Python program to accept the user's first and last name and then getting them
##printed in the the reverse order with a space between first name and last name.

            
def reverse(string):
    string = string[::-1]
    return string
   

fname=input('Enter First Name:')
lname=input('Enter last Name:')

print("{} {}".format(reverse(fname),reverse(lname)))

##Write a Python program to find the volume of a sphere with diameter 12 cm.
##Formula: V=4/3 * π * r^3

import math

diameter=12 

volume=(4/3)*(math.pi)*diameter

print('Volume of Sphere with {} cm diamter is {} cm^3'.format(diameter,volume))