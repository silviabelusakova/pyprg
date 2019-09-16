#!/usr/bin/python3

words = { "spring", "table", "cup", "bottle", "coin" }

word = 'cup'

if (word in words):
    print("{0} is present in the set".format(word))
else:
    print("{0} is not present in the set".format(word))    

word = 'tree'

if (word not in words):
    print("{0} is not present in the set".format(word))
else:
    print("{0} is present in the set".format(word)) 