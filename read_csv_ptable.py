#!/usr/bin/python3

from prettytable import from_csv
    
with open("data2.csv", "r") as fp: 
    x = from_csv(fp)

x.align["City name"] = "l"
x.align["Area"] = "r"
x.align["Population"] = "r"
x.align["Annual Rainfall"] = "r"

# x.sortby = 'Population'

print(x.get_string(sortby='Population', sort_key=lambda row: int(row[0])))

# print("Table sorted by city in descendig order:")
# x.sortby = "City name"
# x.reversesort = True
# print(x)