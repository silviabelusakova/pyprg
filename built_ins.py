#!/usr/bin/python3

nums = { 21, 11, 42, 29, 22, 71, 18 }
nums2 = { 229, 22, 71, 18 }
nums3 = { 21, 11, 42, 71, 18 }

print(nums)
print(nums2)
print(nums3)

print("Number of elements: {0}".format(len(nums)))
# print("Number of elements: {0}, {1}".format(len(nums),len(nums2)))   #ak uvadzame viac ako 1 argument, treba ich cislovat, zvlast ak ich nevypisujeme v poradi ako su definovane 
print("Number of elements: {0}".format(len(nums)))
print("Minimum: {0}".format(min(nums)))
print("Maximum: {0}".format(max(nums)))
print("Sum: {0}".format(sum(nums)))

print("Sorted elements:")

print(sorted(nums))