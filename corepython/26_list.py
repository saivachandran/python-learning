#!/usr/bin/env python3

"""

a= [1,2,3,4,5,6,7,8,9,10]

print(a)

print(type(a))

print(a[0])

print(a[-1])

print(a[2:5])


print(a[5:])

print(a[0:-4])

"""

fruits=["apple","banana","orange","mango"]

print(fruits[2])

#fruits.append("starwberry")

fruits.insert(0, "starwberry")

print(fruits)

print("----------------------------------------")

a = [10,20,30,40,50]

print(a)

a.clear()

print(a)

a = [15,25,35,45,55]

b= a.copy()

print(b)

a = [15,25,35,45,55,35,25,35,25]

print(a.count(35))

print(a.index(35))

print(len(a))

print(max(a))

print(min(a))

a.pop(0) # remove based on index value

print(a)

a.remove(35)  # remove based on value

print(a)


print("-----------------------------------")

names=["saiva"]

print(names)

names.append("kaviya")

names.append("Daksha")

names.append("varun")

names.append("vicky")

print(names)

city=["madurai","chennai"]

names.extend(city)


print(names)

