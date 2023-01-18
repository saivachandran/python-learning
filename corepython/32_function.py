#!/usr/bin/env python3


"""

def sai():

     a = 10
     
     b = 8900
     
     print(a+b)
     
     
sai()     
"""
# 9 types of function python

# no return type without argument type in python
"""
def add():

    a=int(input("Enter the value A : "))

    b=int(input("Enter the value B : "))

    c=a+b
    
    print("Total is" , c)

add()
"""

"""
# No return with argument type in python
def sub(a, b):
 
    c= a-b  
    
    print("diffrenece is ",c)
    
sub(26,7)    

"""    

# Return type without argument

"""
def mul():

    a = int(input("Enter the value A : "))
    
    b = int(input("Enter the value B : "))
    
    c = a*b

    return c
    
x=mul()    

print("mul", x)

"""

# Return type with argument in python

"""
def div(a,b):

   c=a/b
   
   return c
   
x = div(25, 5)   


print("Division", x)

"""     

# arbitary argument in python

def class_10(*students):

    print(students)
    
    for user in students:
    
         print(user)
    
class_10("sai","prem","ram")    
    