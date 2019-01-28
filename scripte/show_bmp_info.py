#!/usr/bin/env python3

'''
Zeigt Information über Bitmap (oder Bitmap-artige Datei).

python3 show_bmp_info.py bild.bmp
'''

# https://gist.github.com/j-marjanovic/5319384ad6606d6fd6d6

import sys
import struct
from collections import OrderedDict

METER_IN_INCH = 39.3700787


class BMP_inspector(object):
	''' Gets BMP (bitmap file) information, such as size, bits per color, ...
		and also parses the pixel array '''

	_dib_header_type = {
		12: 'BITMAPCOREHEADER',
		64: 'OS22XBITMAPHEADER',
		40: 'BITMAPINFOHEADER',
		52: 'BITMAPV2INFOHEADER',
		56: 'BITMAPV3INFOHEADER',
		108: 'BITMAPV4HEADER',
		124: 'BITMAPV5HEADER'
	}

	_dib_method_type = {
		0: 'BI_RGB (none)',
		1: 'BI_RLE8',
		2: 'BI_RLE4',
		3: 'BI_BITFIELDS',
		4: 'BI_JPEG',
		5: 'BI_PNG',
		6: 'BI_ALPHABITFIELDS',
		11: 'BI_CMYK',
		12: 'BI_CMYKRLE8',
		13: 'BI_CMYKRLE4',
	}

	def __init__(self, filename, verbose=True):
		''' Open file, parses information and shows some information '''
		self.array_offset = None
		self.image_size = None
		self.bits_per_pixel = None
		self.bitmap_width = None
		self.bitmap_height = None
		self.dib_header_size = None
		self.pal_ending = None
		self.verbose = verbose

		self.buff = open(filename, 'rb').read()

		self.parse_header()
		self.parse_dib_header()
		self.parse_palette()
		self.parse_gap()
		self.parse_img()


	def parse_header(self):
		''' Parses header -> gets pixel array offset '''

		header = self.buff[0:14]

		magic_num = header[0:2].decode('ascii')
		filesize = int.from_bytes(header[2:6], byteorder='little')
		reserved = ''.join('x{:02X}'.format(x) for x in header[6:10])
		self.array_offset = int.from_bytes(header[10:14], byteorder='little')

		print('BMP header: {} - {}'.format(hex(0), hex(14)))
		print('  File format:   {:>20}'.format(magic_num))
		print('  File size:     {:>20} {:>10}'.format(filesize, hex(filesize)))
		if self.verbose:
			print('  Reserved:      {:>20}'.format(reserved))
		print('  Offset:        {:>20} {:>10}'.format(self.array_offset, hex(self.array_offset)))


	def parse_12B_dib_header(self):
		''' Parses 12 Byte DIB header structure -> get image size, bits per pixel '''

		dib_header_size = int.from_bytes(self.buff[14:18], byteorder='little')

		header = self.buff[14:14 + dib_header_size]
		bitmap_width = int.from_bytes(header[4:6], byteorder='little')
		bitmap_height = int.from_bytes(header[6:8], byteorder='little')
		color_planes = int.from_bytes(header[8:10], byteorder='little')
		bits_per_pixel = int.from_bytes(header[10:12], byteorder='little')

		print('DIB header: {} - {}'.format(hex(14), hex(14 + dib_header_size)))
		print('  Header size:   {:>20} {:>10}'.format(dib_header_size, hex(dib_header_size)))
		print('  Type:          {:>20}'.format(self._dib_header_type[dib_header_size]))
		print('  Width:         {:>20} {:>10}'.format(bitmap_width, hex(bitmap_width)))
		print('  Height:        {:>20} {:>10}'.format(abs(bitmap_height), hex(abs(bitmap_height))))
		print('  Color planes:  {:>20}'.format(color_planes))
		print('  Bits per pixel:{:>20}'.format(bits_per_pixel))


	def parse_dib_header(self):
		''' Parses DIB header structure -> get image size, bits per pixel '''

		dib_header_size = int.from_bytes(self.buff[14:18], byteorder='little')

		if dib_header_size == 12:
			self.parse_12B_dib_header()
			return

		header = self.buff[14:14 + dib_header_size]
		bitmap_width = int.from_bytes(header[4:8], byteorder='little')
		bitmap_height = int.from_bytes(header[8:12], byteorder='little')
		color_planes = int.from_bytes(header[12:14], byteorder='little')
		bits_per_pixel = int.from_bytes(header[14:16], byteorder='little')
		comp_method = int.from_bytes(header[16:20], byteorder='little')
		image_size = int.from_bytes(header[20:24], byteorder='little')
		hor_resolution = int.from_bytes(header[24:28], byteorder='little')
		ver_resolution = int.from_bytes(header[28:32], byteorder='little')
		color_palette = int.from_bytes(header[32:36], byteorder='little')
		imp_colors_used = int.from_bytes(header[36:40], byteorder='little')

		if bitmap_height > 0:
			direction = 'bottom-up'
		else:
			direction = 'top-down'

		self.image_size = image_size
		self.bits_per_pixel = bits_per_pixel
		self.bitmap_width = bitmap_width
		self.bitmap_height = bitmap_height
		self.dib_header_size = dib_header_size

		print('DIB header: {} - {}'.format(hex(14), hex(14 + dib_header_size)))
		print('  Header size:   {:>20} {:>10}'.format(dib_header_size, hex(dib_header_size)))
		print('  Type:          {:>20}'.format(self._dib_header_type[dib_header_size]))
		print('  Width:         {:>20} {:>10}'.format(bitmap_width, hex(bitmap_width)))
		print('  Height:        {:>20} {:>10}'.format(abs(bitmap_height), hex(abs(bitmap_height))))
		print('  Direction:     {:>20}'.format(direction))
		print('  Color planes:  {:>20}'.format(color_planes))
		print('  Bits per pixel:{:>20}'.format(bits_per_pixel))
		print('  Compr method:  {:>20} {:>10}'.format(comp_method, self._dib_method_type[comp_method]))
		print('  Image size:    {:>20} {:>10}'.format(image_size, hex(image_size)))
		print('  Hor resolution:{:>16} DPI'.format(hor_resolution // METER_IN_INCH))
		print('  Ver resolution:{:>16} DPI'.format(ver_resolution // METER_IN_INCH))
		print('  Colors in pal: {:>20}'.format(color_palette))
		if self.verbose:
			print('  Imp colors:    {:>20}'.format(imp_colors_used))


	def parse_palette(self):
		''' Show palette size if present (if bits per pixel is 1, 4, or 8)'''

		if self.bits_per_pixel in (1, 4, 8):
			pal_start = 14 + self.dib_header_size
			self.pal_ending = pal_start + (2**self.bits_per_pixel * 4) # 4 byte per entry
			print('Palette: {} - {}'.format(hex(pal_start), hex(self.pal_ending)))
		else:
			print('No expected palette')
			self.pal_ending = 14 + self.dib_header_size


	def parse_gap(self):
		''' If there is a gap between the palette and the given offset, analyse it. '''

		gap_size = self.array_offset - self.pal_ending
		if not gap_size:
			return

		print('Gap size:', gap_size)

		if not gap_size % 20:
			print('Might be MBM...')

			pos = [{} for _ in range(20)]

			for i in range(gap_size // 20):
				for j in range(20):
					x = self.buff[self.pal_ending+i*20+j:self.pal_ending+i*20+j+1]
					if x not in pos[j]:
						pos[j][x] = 0
					pos[j][x] += 1

			for i, elem in enumerate(pos):
				if len(elem) > 1:
					print([int.from_bytes(x, byteorder='little') for x in sorted(elem)])
				else:
					print(i, elem)


	def parse_img(self):
		''' Parse image data '''

		pass



if __name__ == '__main__':

	if len(sys.argv) != 2:
		print('Usage: ', sys.argv[0], 'bmp-file')
		sys.exit(1)

	filename = sys.argv[1]
	bpmInspector = BMP_inspector(filename)
