#!/usr/bin/python3

import re

n=input("Enter the Mobile Number: ")

r=re.fullmatch('[6-9][0-9]{9}',n) 

if r!=None:

   print('Valid Number')

else:

   print('Invalid Mobile Number')