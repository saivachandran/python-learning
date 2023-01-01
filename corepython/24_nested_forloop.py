#!/usr/bin/env python3

string = "abcd"

for i in range(len(string)):

    for j in range(i+1):
    
        print(string[j],end="")
        
    print("")
    
    
print("-------------------------------")    


string = "abcd"

for i in range(len(string)-1,-1,-1):

    for j in range(i+1):
    
        print(string[j],end="")
        
    print("")
    