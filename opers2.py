#!/usr/bin/python3

set1 = { 'a', 'b', 'c', 'c', 'd' }
set2 = { 'a', 'b', 'x', 'y', 'z' }

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1 & set2)
print("union:", set1 | set2)
print("difference:", set1 - set2)
print("symmetric difference:", set1 ^ set2)