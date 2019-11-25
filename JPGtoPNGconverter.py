import sys  # ? for terminal args
# from pathlib import Path
import os  # ? set path
from PIL import Image  # ? to convert the files

#! $python3 JPGtoPNGconverter.py Pokedex\ new\


# TODO grab first and second arguments
JPG_folder = sys.argv[1]
PNG_folder = sys.argv[2]

# TODO check is new\ exists, if not create
if not os.path.exists(PNG_folder):
    os.makedirs(PNG_folder)


# TODO loop through pokedex
# *      convert to PNG
# *      save to the new folder

for filename in os.listdir(JPG_folder):
    img = Image.open(f'{JPG_folder}{filename}')
    img.save(f'{PNG_folder}{filename}', 'png')
    print('All Done.')
