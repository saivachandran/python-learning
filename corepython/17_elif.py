#!/usr/bin/python3

days = int(input("Enter the Number of days: "))

if days == 0:

   print("Good No fine: ")
   
elif days >= 1 and days <=5:
 
    print("Fine Amount is : ", days*0.5)
    
elif days > 5 and days <=10:

     print("Fine Amount is : ", days*1)
     
elif days > 11 and days <=30:

     print("Fine Amount is: ", days*5)
    
    
else:

   print("Memebership cancelled")
    