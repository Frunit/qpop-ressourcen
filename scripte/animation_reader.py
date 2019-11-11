#!/usr/bin/env python3

'''
Liest Animationen aus einer Datei und gibt Informationen auf stdout aus.

python3 an_reader.py datei_zum_lesen
'''

import sys

if len(sys.argv) != 2:
	print('Usage: ', sys.argv[0], 'file')
	sys.exit(1)


def bti(b, byteorder='little', signed=True):
	''' Turn given bytes array into integer given byteorder and signed. '''

	return int.from_bytes(b, byteorder=byteorder, signed=signed)


def short_hex(b):
	''' Return given bytes array as formatted string '''

	return ' '.join(f'{white}{char:02X}{end}' if char == 0 else format(char, '02X') for char in b)


def header(raw, offset):
	'''
	Read and print all header information in the raw data, starting with
	the offset.
	Return offset of the end of the header, the number of images and the
	number of animations.
	'''

	print('HEADER')
	assert raw[offset:offset+2] == b'AN'
	assert raw[offset+0x13:offset+0x13+9] == b'Animation'
	assert raw[offset+0x13+9:offset+0x13+64] == b'\x00'*(64-9)

	num_images = raw[offset+4]
	num_animations = raw[offset+5]
	ani_width = bti(raw[offset+0x59:offset+0x5b])
	ani_height = bti(raw[offset+0x5b:offset+0x5d])

	print(f'Animation ({ani_width}x{ani_height}) starting at 0x{offset:X}')

	assert raw[offset+3] == 2
	assert raw[offset+6:offset+8] == b'\x00'*2
	assert raw[offset+9:offset+0x13] == b'\x00\x00\x00\x00\x00\x80\x04\x00\x00\x00'
	assert raw[offset+0x54:offset+0x59] == b'\x00\x00\x00\x00\x01'
	assert raw[offset+0x5e:offset+0x60] == b'\x00'*2
	assert raw[offset+0x60] == raw[offset+0x61] == raw[offset+0x62]
	assert raw[offset+0x63] == 0x80

	unknown = short_hex([raw[offset+2], raw[offset+8], raw[offset+0x53], raw[offset+0x5d], raw[offset+0x60]])
	print(f'0x02 0x08 0x53 0x5D 0x60: {unknown}')

	return offset + 0x64, num_images, num_animations


def files(raw, offset, num_images):
	'''
	Read and print all image files in the raw data, starting with the
	offset and given the number of image files.
	Return offset of the end of the file block and a list with image
	file names.
	'''

	print('FILES')
	background_path = raw[offset:offset+64].rstrip(b'\x00').replace(b'\x00', b'.').decode('ascii')

	print(f'Back.: {background_path:42}')

	assert raw[offset+64:offset+64+4] == b'\x00'*4
	assert raw[offset+132:offset+132+6] == b'\x04\x03\x00\x00\x00\x00'

	animation_path = raw[offset+64+4:offset+128+4].rstrip(b'\x00').replace(b'\x00', b'.').decode('ascii')

	if animation_path:
		print(f'Anim.: {animation_path:42}')

	offset = offset + 0x8a

	images = []

	for i in range(num_images):
		num_frames = raw[offset]
		mod_hex = format(raw[offset+1], '02X')
		mod_bin = ''.join([f'{white}0{end}' if x == '0' else '1' for x in format(raw[offset+1], '08b')])
		path = raw[offset+4:offset+68].rstrip(b'\x00').replace(b'\x00', b'.').decode('ascii')

		if 'ENDTEXT' in path:
			assert raw[offset+2] == 16 and raw[offset+3] == 0
		else:
			assert raw[offset+2] == 0 and raw[offset+3] == 1

		images.append(path.split('\\')[-1].replace('.BMX', ''))

		print(f'Image: {path:42} ({num_frames:2} frames) {mod_bin} {mod_hex}')

		offset += 68

	return offset, images


def blocks(raw, offset, num_animations, images):
	'''
	Read and print all animation blocks in the raw data, starting with
	the offset and given the number of animation blocks and a list of
	image file names.
	Return offset of the end of the last block.
	'''

	print('BLOCKS')
	for anim_num in range(num_animations):
		ref_image = images[raw[offset]]

		fragment = raw[offset+1:offset+64].split(b'\x00', maxsplit=2)
		title = fragment[0].decode('ascii')
		sub_title = fragment[1]
		if sub_title:
			sub_title = '{}{}{}'.format(red, short_hex(sub_title), end)
		else:
			sub_title = ''

		#offset += len(title) + len(fragment[1])
		#offset = raw.find(b'\x01', offset)
		offset += 33
		num_frames = raw[offset+1]

		assert num_frames > 0

		print(f'{anim_num+1:>2} {title:8} {ref_image:8} ({num_frames:2} frames) {sub_title}')

		if raw[offset+2:offset+21] != b'\x00'*19:
			assert raw[offset+2:offset+21] == b'\x00'*5 + b'\x6b\xff\xbb\xff' + b'\x00'*10
			print(f'{red}!NB! Has 6B FF BB FF before frames!{end}')

		offset += 21

		for sequenznummer in range(num_frames):
			img_num = raw[offset]
			delay = raw[offset+1]
			flags = raw[offset+2]
			x_abs = '!' if 0x80 & flags else ''
			y_abs = '!' if 0x40 & flags else ''
			fixate = ' Fix' if 0x20 & flags else ''
			ende = f' {red}ENDE{end}' if 0x10 & flags else ''
			pause = ' Pause' if 0x08 & flags else ''

			if 0x04 & flags:
				print(f'{red}Unbekannter Flag: 0x04{end}')
			assert 0x02 & flags == 0
			assert 0x01 & flags == 0

			x = bti(raw[offset+3:offset+5])
			y = bti(raw[offset+5:offset+7])

			unknown = short_hex(raw[offset+7:offset+16])

			doublebyte = 0 if raw[offset+7:offset+9] == b'\x00\x00' else -1
			doublebyte = f'{green}{doublebyte:2}{end}'

			assert raw[offset+7:offset+10] == b'\x00'*3 or raw[offset+7:offset+10] == b'\xFF\xFF\x00'
			assert raw[offset+13] == 0

			sprung = ''
			if raw[offset+10] == 1:
				anzahl = raw[offset+11]
				ziel = raw[offset+12]

				if anzahl:
					sprung = f' Jmp {anzahl}x → pos {ziel}'
				else:
					if ziel == sequenznummer:
						sprung = f' Bleib bei pos {ziel}'
					else:
						sprung = f' Loop unendlich zu pos {ziel}'

			akt = bti(raw[offset+14:offset+16], signed=False)
			aktlist = []
			aktivieren = ''
			if akt:
				for i in range(16):
					if (akt >> i) & 1:
						aktlist.append(str(i+1))
				aktivieren = ' Akt Seqs ' + ', '.join(aktlist)


			print(f' {sequenznummer:2} Img{img_num:2}; Lag:{delay:2}; ({x:4}{x_abs}:{y:4}{y_abs}) {doublebyte}{fixate}{pause}{sprung}{aktivieren}{ende}')
			offset += 16

	return offset


def get_info(raw, offset):
	'''
	Read header, files and blocks from the raw data starting at the offset.
	Return the offset of the end of the last block.
	'''

	offset, num_images, num_animations = header(raw, offset)
	offset, images = files(raw, offset, num_images)
	offset = blocks(raw, offset, num_animations, images)

	return offset


# Print colors if using interactively (e.g. not piped to file or less)
if sys.stdout.isatty():
	red = '\033[1;31m'
	green = '\033[32m'
	white = '\033[37m'
	end = '\033[0m'
else:
	red = ''
	green = ''
	white = ''
	end = ''

fn = sys.argv[1]
raw = open(fn, 'rb').read()
old_offset = 0
first = True

# Loop through all available animations in the given file
while True:
	offset = raw.find(b'Animation', old_offset) - 0x13

	if offset < 0:
		break

	if not first:
		print('\n\n---------\n\n')
	first = False

	old_offset = get_info(raw, offset)
