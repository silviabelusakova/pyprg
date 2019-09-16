#!/usr/bin/python3

from PIL import Image
import sys

try:
    fox = Image.open("fox.jfif")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
cropped = fox.crop((100, 200, 350, 350))
cropped.save('fox_cropped.jfif')
cropped.show()