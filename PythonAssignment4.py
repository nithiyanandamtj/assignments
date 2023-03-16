# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:23:12 2023

@author: Nithi
"""

"""Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass."""


class areaoftriangle:
    
    def userinput(self):
        a=input('Enter 1st side of triangle:')
        b=input('Enter 2nd side of triangle:')
        c=input('Enter 3rd side of triangle:')
        
        return a,b,c
    
    class calculatearea:
        
        def area(self,length):
            a=int(length[0])
            b=int(length[1])
            c=int(length[2])
            s=(a+b+c)/2
            result=(s*(s-a)*(s-b)*(s-c)) ** 0.5
            return result 
        
        
area1=areaoftriangle()
val=area1.userinput()
output=area1.calculatearea().area(val)

print(output)

#Write a function filter_long_words() that takes a list of words and an integer n and returns
#the list of words that are longer than n.


def filter_long_words(lst,n):
    res=[]
    [res.append(i) for i in lst if len(i)>n]
    return res


lst=['Energy','Engineering','Company','MyComputer']
n=7

print(filter_long_words(lst, n))
    
#Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words.

#Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#Here 2,3 and 4 are the lengths of the words in the list.

def calculatewordlength(lst):
    result=[]
    [result.append(len(i)) for i in lst]
    return result
    

print(calculatewordlength(['ab','cde','erty']))


#rite a Python function which takes a character (i.e. a string of length 1) and returns True if
#it is a vowel, False otherwise.


def vowelcheck(userinput):
        vowel=['a','e','i','o','u']
        for i in vowel:
            if i==userinput:
                return True
                break
        return False
            
userinput=input('Enter a character to check if its vowel:')

print(vowelcheck(userinput))