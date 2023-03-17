
#Write a function to compute 5/0 and use try/except to catch the exceptions.

a=5
b=0

try:
    print(a/b)
except Exception as e:
    print("Error Occured:",e)
"""
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
"""

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in subjects:
    for j in verbs:
        for k in objects:
            print('{} {} {}'.format(i,j,k))
