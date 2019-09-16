#!/usr/bin/env python 

from pathlib import Path

import os 
from PIL import Image

home_dir =str(Path.home() / 'Documents')
directories = os.walk(home_dir) # os.walk(dir) nie je funkcia vracajuca sadu hodnot ale ide o generator objektov, ktore postupne v jednotl krokoch vypise objekt, pointa je nezahltenie pamate velkym mn vysledkov 
                                #lazy loading 

for (root, dirs, files) in directories:
    # print(root, dirs, files)

    for file in files:
        if file.endswith('jpg') or file.endswith('jfif'):
            # print(file)

            p = Path(file)
            img = Image.open(os.path.join(root, file))
            if img:
                print("name: {} | format: {}| size: {} | mode: {} ".format(file, img.format, img.size, img.mode))


# print(list(directories))