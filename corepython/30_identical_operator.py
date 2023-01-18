#!/usr/bin/env python3

a = [1,2]

b = [1,2]

c = a

print(id(a))

print(id(b))

print(a is b)

print(a is c)

print(a is not b)