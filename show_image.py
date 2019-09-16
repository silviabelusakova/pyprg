#!/usr/bin/python3

from PIL import Image     #PIL je hist nazov pre pillow package
import sys

try:
    fox = Image.open("fox.jfif")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
fox.show()