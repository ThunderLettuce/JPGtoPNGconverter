import sys  # ? for terminal args
import os  # ? set path
from PIL import Image  # ? to convert the files

#! $python3 JPGtoPNGconverter.py Pokedex\ new\


# TODO grab first and second arguments
JPG_folder = sys.argv[1]
PNG_folder = sys.argv[2]

print(JPG_folder, PNG_folder)

# TODO check is new\ exists, if not create

# TODO loop through pokedex
# *      convert to PNG
# *      save to the new folder
