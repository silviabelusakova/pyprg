#!/usr/bin/python3

from PIL import Image
import sys

try:
    fox = Image.open("fox.jfif")
    
except IOError:
    print("Unable to load image")
    sys.exit(1)
    
grayscale = fox.convert('L')
grayscale.show()