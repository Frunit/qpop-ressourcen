#!/usr/bin/env python3

'''
Extrahiert alle Wave-Dateien aus einer Datei, die aus vielen Wave-Dateien besteht.

Erzeugt waveXX.wav

python3 all_waves_from_bundle_wave.py file_to_extract.wav
'''

import sys

if len(sys.argv) != 2:
	print('{} file_to_extract.wav'.format(sys.argv[0]), file=sys.stderr)
	sys.exit()

raw = open(sys.argv[1], 'rb').read()

current_offset = 0
next_offset = 0

num = 1

while True:
	next_offset = raw.find(b'RIFF', current_offset + 4)

	if next_offset < 0:
		next_offset = None

	wav = raw[current_offset:next_offset]

	open('wave{:02d}.wav'.format(num), 'wb').write(wav)

	if next_offset is None:
		break

	current_offset = next_offset
	num += 1

