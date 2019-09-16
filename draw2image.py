#!/usr/bin/python3

from PIL import Image, ImageDraw

img = Image.new('RGBA', (200, 200), 'white')    
idraw = ImageDraw.Draw(img)

idraw.rectangle((10, 10, 100, 100), fill='#4B0082')
idraw.text((10, 20), 'Sunny day', fill='#4B8862')

 
img.save('rectangle.png')
img.show()