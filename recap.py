#!/usr/bin/python3


#types of input

#tuple 

vals = (1, 2, 3, 4)
print(vals)
print(f'There are {len(vals)} elements in the tuple')

for e in vals:
    print(e)


#list 

vals2 = [1, 2, 3, 4, 5]
vals2.append(6)
vals2.append(7)

print(f'There are {len(vals2)} elements in the list')

for e in vals2:
    print(e)


#dictionary

items = {"coins": 23, "pens": 11}

for c, d in items.items():     #mozno zadat aj: items.keys() / items.values()
    print(c, d)


#matrix 

data = {1, 5, 8, 9, 4}
print(data)


