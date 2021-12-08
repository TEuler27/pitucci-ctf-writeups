from os import listdir
import hashlib
from PIL import Image
import cv2
import os
import numpy as np
from PIL.ExifTags import TAGS
import os.path, time

puzzle = []

for fh in os.listdir('jigsaw_pieces'):
	puzzle.append((os.path.getmtime(f'jigsaw_pieces/{fh}'), fh))
	
puzzle.sort()	
out = ''
row = ''
for i,j in enumerate(puzzle):	
	if i%29 == 0:
		out += row
		row = ''
	im = Image.open(f'jigsaw_pieces/{j[1]}')
	im.load()
	row += im.info['Comment'].split('\'')[1]

print(out)
