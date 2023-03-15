# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:44:31 2023

@author: NINTJ
"""

#Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()

def myreduce(function,iterable):
    result=iterable[0]
    for i in iterable[1:]:
        result=function(result,i)
    return result        


j=[1,2,3,4]

print(myreduce(lambda x,y:x+y,j))

#Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()


def myfilter(function,iterable):
    j=[]
    for i in iterable:
        if function(i) is True:
            j.append(i)
    return j



m=[3,5,4,6,7,8,9,11,1,3,45,65,76,88,98]

print(list(myfilter(lambda x:x%2==0,m)))


#Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists

#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

lst=['x','y','z']    

print([i*j for i in lst for j in range(1,5)])


#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']


print([i*j for i in range(1,5) for j in lst])


#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 


print([[i+j] for i in range(3) for j in range(2,5)])       
       
#[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]


print([[i+j for i in range(4)] for j in range(2,6)])


#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

        
print([(j+1,i+1) for i in range(3) for j in range(3)])