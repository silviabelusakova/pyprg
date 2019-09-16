#!/usr/bin/env python

# iterator.py
#string 


text = "formidable"

for e in text:
    print(e, end=" ")

print()

it = iter(text)

# print(next(it))
# print(next(it))
# print(next(it))

print(list(it))

#tuple 

# mytuple = ('apple', 'banana', 'cherry', 'orange')
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

