#!/usr/bin/env python3

m1=int(input("Enter your mark: "))

m3=int(input("Enter your mark: "))

m2=int(input("Enter your mark: "))

total = m1+m2+m3

average= total/3.0

print("Total is ", total)

print("Average is ", average)

if m1>=35 and m2>=35 and m3>35:

    print("Result is: pass ")
    
    
    if average >= 90 and average <=100:
    
        print("Grade: A")
    
    elif average >= 80 and average <= 89:
    
          print("Grade: B")
       
       
    elif average >= 70 and average <= 79:
    
          print("Grade: c")
       
    else:
    
        print("Grade: D")
else:

   print("Result is: fail")
   
   print("Grade: No Grade")