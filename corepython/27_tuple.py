#!/usr/bin/env python3

a=(1,2.5,True,"ram")

print(a)

print(type(a))

print(a[2])

# incase change value 

b=list(a)

print(b)

b.append("saiva")

print(b)

a= tuple(b)

print(a)

# use if condtion and for

for i in a:

    print(i)
    
if "saivam" in i:

      print("saiva is found")
      
else:

   print("saiva not found")