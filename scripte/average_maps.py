#!/usr/bin/env python3

'''
Liest Höhenreliefs aus Q-Pop-Speicherständen und generiert ein Bild mit drei Panelen:
- links: Durchschnittliche Höhe
- mitte: Minimale Höhe
- rechts: Maximale Höhe

Benötigt:
- Pillow
- Numpy

Erzeugt average_map.png

python3 average_maps.py speicherstand1.qpp speicherstand2.qpp ...
oder
python3 average_maps.py *.qpp
'''

import sys
import numpy as np
from glob import glob
from PIL import Image, ImageDraw

delta = 16
num_tiles = 28
offset = 0x3c7

if len(sys.argv) != 2:
	print('{} savegame.qpp savegame*.qpp ...'.format(sys.argv[0]), file=sys.stderr)
	sys.exit()

values = np.zeros(num_tiles**2, dtype=np.uint32)
maxs = np.zeros(num_tiles**2, dtype=np.uint8)
mins = np.empty(num_tiles**2, dtype=np.uint8)
mins[:] = 255
seen = set()

fnlist = []
for f in sys.argv[1:]:
	fnlist.extend(glob(f))

numtaken = 0

for fn in fnlist:
	raw = open(fn, 'rb').read()

	current = np.frombuffer(raw[offset:offset + num_tiles**2], dtype=np.uint8)

	if str(current) in seen:
		continue

	numtaken += 1
	seen.add(str(current))
	print(fn)

	values = values + current
	maxs = np.maximum(maxs, current)
	mins = np.minimum(mins, current)


values = values / numtaken

im = Image.new('RGB', (num_tiles*delta*3, num_tiles*delta), (0,0,0))
draw = ImageDraw.Draw(im)

for i in range(num_tiles**2):
	color = values[i]

	if color:
		rgb = (int(color*2.5), int(color*2.5), int(color*2.5))

		y = int(i % num_tiles) * delta
		x = int(i // num_tiles) * delta
		xy = ((x, y), (x+delta, y+delta))
		draw.rectangle(xy, fill=rgb)

	color = mins[i]

	if color:
		rgb = (int(color*2.5), int(color*2.5), int(color*2.5))

		y = int(i % num_tiles) * delta
		x = int(i // num_tiles) * delta + num_tiles*delta
		xy = ((x, y), (x+delta, y+delta))
		draw.rectangle(xy, fill=rgb)

	color = maxs[i]

	if color:
		rgb = (int(color*2.5), int(color*2.5), int(color*2.5))

		y = int(i % num_tiles) * delta
		x = int(i // num_tiles) * delta + num_tiles*delta*2
		xy = ((x, y), (x+delta, y+delta))
		draw.rectangle(xy, fill=rgb)

im.save('average_map.png')
