#!/usr/bin/python3

import sqlite3 as lite
from prettytable import from_db_cursor

con = lite.connect('test.db')
    
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT * FROM Cities')   
    
    x = from_db_cursor(cur) 
    
# print(x)

print(x.get_string(title="Australian cities", fields=["Name", "Population"]))
# print(x.get_string(title="Australian cities"))