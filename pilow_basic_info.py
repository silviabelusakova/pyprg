#!/usr/bin/python3

from PIL import Image
import sys

try:
    fox = Image.open("fox.jfif")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
print("Format: {0}\nSize: {1}\nMode: {2}".format(fox.format, 
    fox.size, fox.mode))