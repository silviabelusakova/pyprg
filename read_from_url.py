#!/usr/bin/python3

from PIL import Image
import requests
import sys

url = 'https://images.unsplash.com/photo-1505259839540-04105fcd8ba3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=985&q=80'

try:
    resp = requests.get(url, stream=True).raw

except requests.exceptions.RequestException as e:  
    sys.exit(1)

try:
    img = Image.open(resp)

except IOError:
    print("Unable to open image")
    sys.exit(1)

img.save('fox2.jfif', 'jpeg')
img.show()