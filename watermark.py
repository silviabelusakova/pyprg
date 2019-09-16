#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys

try:
    fox = Image.open("fox.jfif")

except:
    print("Unable to load image")
    sys.exit(1)
    
idraw = ImageDraw.Draw(fox)
text = "This is Fox!"

font = ImageFont.truetype("arial.ttf", size=38)

idraw.text((10, 10), text, font=font)
 
fox.save('fox_watermarked.jfif')
fox.show()
