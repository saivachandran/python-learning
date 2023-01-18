#!/usr/bin/env python3

user = {
      "name": "saiva",
      
      "age" : "32",
      
      "ismarried": "True",
      
  "user1":  {
        "name": "prem",
      
        "age" : "32",
      
        "ismarried": "True"
  }

}

print(user)

print(type(user))

print(user["name"])

print(user.get('age'))

print(user.keys())

print(user.values())

print(user.items())


for x ,y in user.items():

    print(x,y)
    
if "age" in user:    

    print("present")
    
user.update({"gender":"male"})    

print(user)

user["age"] = 33

print(user)