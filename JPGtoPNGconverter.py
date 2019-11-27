import sys  # ? for terminal args
import os  # ? set path
from PIL import Image  # ? to convert the files

#! $python3 JPGtoNGconverter.py Pokedex\ new\

# TODO grab first and second arguments
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

# TODO check is new\ exists, if not create
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

for filename in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{filename}')
    Image.save(f'{png_folder}{filename}', 'png')
    print('all done')

# TODO loop through pokedex
# *      convert to PNG
# *      save to the new folder
