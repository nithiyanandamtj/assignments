# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:35:50 2023

@author: NINTJ
"""

"""Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""
n=10
for i in range(n):
    if i<=5:
        for j in range(i):
            print('*',end=" ")
        
    if i>5:
        for k in range(i,n):
            print('*',end=" ")     
    print(end='\n')
    

"""Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: ineuron
Output: norueni
"""

userinput=input("Enter the word for reversing:")

result=""
for i in userinput:
    result=i+result
  
print(result)