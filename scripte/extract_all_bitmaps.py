#!/usr/bin/env python3

'''
Versucht alle Bilder aus Q-Pop und Magentic Planet zu extrahieren, inklusive Multibitmaps, die in Animationen verwendet werden.
Diese Datei ist sehr stark "work in progress", deswegen sind noch viele hart-kodierte Hacks und Kommentare enthalten.

Benötigt Pillow

Erzeugt bmp-Dateien (siehe Zeile 233)

python3 extract_all_bitmaps.py qpop.exe
'''


import os
import sys
from PIL import Image
import io

# Es gibt drei Arten von Bildern (soweit bekannt):
# DIB
# BMP
# Eine Art MBM (Multibitmap)
# Alle haben einen DIB-Header, also such ich nach dem. Er geht (bisher gefunden) los mit "Header size = 40": b'\x28\x00\x00\x00'
# Theoretisch andere mögliche Header-sizes wären: 12, (52, 56, 64)



standard_palette = (0, 0, 0, 130, 0, 0, 0, 130, 0, 130, 130, 0, 0, 0, 130, 130, 0, 130, 0, 130, 130, 195, 195, 195, 195, 223, 195, 166, 203, 243, 16, 16, 16, 28, 28, 28, 44, 44, 44, 56, 56, 56, 73, 73, 73, 89, 89, 89, 101, 101, 101, 117, 117, 117, 134, 134, 134, 146, 146, 146, 162, 162, 162, 174, 174, 174, 190, 190, 190, 207, 207, 207, 219, 219, 219, 235, 235, 235, 251, 251, 251, 0, 0, 251, 0, 0, 211, 0, 0, 174, 0, 0, 134, 0, 0, 97, 0, 0, 56, 0, 0, 20, 0, 24, 0, 20, 20, 32, 65, 20, 32, 109, 20, 32, 154, 20, 32, 199, 20, 32, 243, 20, 32, 20, 20, 85, 65, 20, 85, 109, 20, 85, 154, 20, 85, 199, 20, 85, 243, 20, 85, 20, 20, 138, 65, 20, 138, 109, 20, 138, 154, 20, 138, 199, 20, 138, 243, 20, 138, 20, 20, 190, 65, 20, 190, 109, 20, 190, 154, 20, 190, 199, 20, 190, 243, 20, 190, 20, 20, 243, 65, 20, 243, 109, 20, 243, 154, 20, 243, 199, 20, 243, 243, 20, 243, 251, 0, 251, 0, 69, 0, 20, 65, 32, 65, 65, 32, 109, 65, 32, 154, 65, 32, 199, 65, 32, 243, 65, 32, 20, 65, 85, 65, 65, 85, 109, 65, 85, 154, 65, 85, 199, 65, 85, 243, 65, 85, 20, 65, 138, 65, 65, 138, 109, 65, 138, 154, 65, 138, 199, 65, 138, 243, 65, 138, 20, 65, 190, 65, 65, 190, 109, 65, 190, 154, 65, 190, 199, 65, 190, 243, 65, 190, 20, 65, 243, 65, 65, 243, 109, 65, 243, 154, 65, 243, 199, 65, 243, 243, 65, 243, 203, 0, 203, 0, 113, 0, 20, 109, 32, 65, 109, 32, 109, 109, 32, 154, 109, 32, 199, 109, 32, 243, 109, 32, 20, 109, 85, 65, 109, 85, 109, 109, 85, 154, 109, 85, 199, 109, 85, 243, 109, 85, 20, 109, 138, 65, 109, 138, 109, 109, 138, 154, 109, 138, 199, 109, 138, 243, 109, 138, 20, 109, 190, 65, 109, 190, 109, 109, 190, 154, 109, 190, 199, 109, 190, 243, 109, 190, 20, 109, 243, 65, 109, 243, 109, 109, 243, 154, 109, 243, 199, 109, 243, 243, 109, 243, 158, 0, 158, 0, 158, 0, 20, 154, 32, 65, 154, 32, 109, 154, 32, 154, 154, 32, 199, 154, 32, 243, 154, 32, 20, 154, 85, 65, 154, 85, 109, 154, 85, 154, 154, 85, 199, 154, 85, 243, 154, 85, 20, 154, 138, 65, 154, 138, 109, 154, 138, 154, 154, 138, 199, 154, 138, 243, 154, 138, 20, 154, 190, 65, 154, 190, 109, 154, 190, 154, 154, 190, 199, 154, 190, 243, 154, 190, 20, 154, 243, 65, 154, 243, 109, 154, 243, 154, 154, 243, 199, 154, 243, 243, 154, 243, 113, 0, 113, 0, 207, 0, 20, 199, 32, 65, 199, 32, 109, 199, 32, 154, 199, 32, 199, 199, 32, 243, 199, 32, 20, 199, 85, 65, 199, 85, 109, 199, 85, 154, 199, 85, 199, 199, 85, 243, 199, 85, 20, 199, 138, 65, 199, 138, 109, 199, 138, 154, 199, 138, 199, 199, 138, 243, 199, 138, 20, 199, 190, 65, 199, 190, 109, 199, 190, 154, 199, 190, 199, 199, 190, 243, 199, 190, 20, 199, 243, 65, 199, 243, 109, 199, 243, 154, 199, 243, 199, 199, 243, 243, 199, 243, 69, 0, 69, 0, 251, 0, 20, 243, 32, 65, 243, 32, 109, 243, 32, 154, 243, 32, 199, 243, 32, 243, 243, 32, 20, 243, 85, 65, 243, 85, 109, 243, 85, 154, 243, 85, 199, 243, 85, 243, 243, 85, 20, 243, 138, 65, 243, 138, 109, 243, 138, 154, 243, 138, 199, 243, 138, 243, 243, 138, 20, 243, 190, 65, 243, 190, 109, 243, 190, 154, 243, 190, 199, 243, 190, 243, 243, 190, 20, 243, 243, 65, 243, 243, 109, 243, 243, 154, 243, 243, 199, 243, 243, 243, 243, 243, 20, 0, 20, 20, 20, 0, 56, 56, 0, 97, 97, 0, 134, 134, 0, 174, 174, 0, 211, 211, 0, 251, 251, 0, 24, 0, 0, 52, 0, 0, 81, 0, 0, 109, 0, 0, 138, 0, 0, 166, 0, 0, 195, 0, 0, 223, 0, 0, 251, 0, 0, 0, 24, 24, 0, 56, 56, 0, 89, 89, 0, 130, 130, 255, 251, 243, 162, 162, 166, 130, 130, 130, 255, 0, 0, 0, 255, 0, 255, 255, 0, 0, 0, 255, 255, 0, 255, 0, 255, 255, 255, 255, 255)

standard_palette_4bit = (0, 0, 0, 0, 128, 0, 128, 0, 0, 128, 128, 0, 0, 0, 0, 0, 128, 0, 128, 0, 0, 192, 192, 0, 128, 128, 0, 0, 255, 0, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)



class RLE_Decoder():
	def __init__(self, bmp_header, dib_header, palette, rle, offset=0):
		''' header, palette and imgdata must be 0 '''

		self.header = bmp_header + dib_header
		self.palette = palette
		self.rle = rle
		self.current = offset

		self.img_data = []

		self.header_size = bti(self.header[14:18]) + 14
		self.width = bti(self.header[18:22])
		self.height = bti(self.header[22:26])
		self.bpp = bti(self.header[28:30])
		self.comp = bti(self.header[30:34])
		self.pal_start = self.header_size
		self.pal_end = self.pal_start + (2**self.bpp * 4) # 4 byte per entry

		if (self.width*self.bpp/8) % 4:
			self.four_width = int(((self.width*self.bpp/8) + (4-((self.width*self.bpp/8)%4)))*8/self.bpp)
		else:
			self.four_width = self.width

		if self.header_size != len(self.header):
			raise IOError('Given header size and real header size do not fit: {} vs {}'.format(self.header_size, len(self.header)))

		if self.pal_end - self.pal_start != len(palette):
			raise IOError('Given palette size and real palette size do not fit: {} vs {}'.format(self.pal_end - self.pal_start, len(palette)))

		if self.bpp not in (4, 8):
			raise IOError('Not 4-Bit or 8-Bit BMP file')

		if self.comp not in (1, 2):
			raise IOError('Not a compressed file')

		self.total_pixels = self.width * self.height
		self.rPix = 0
		self.lines = 1

		self.dec = ''
		self.buf = ''


	def Decode(self):

		result = 0

		# Extract byte pairs and apply function depending on the bytes
		while (self.lines * self.width) <= self.total_pixels:
			byte0 = self.rle[self.current]
			byte1 = self.rle[self.current+1]
			self.current += 2
			if byte0 == 0:
				if byte1 == 0:
					self.EOSL() # End of scan line
				elif byte1 == 1:
					result = self.EORLE() # End of Bitmap
					break
				elif byte1 == 2:
					self.MOFF() # Move offset
				else:
					self.UENCD(byte1)
			else:
				self.DENCD(byte0, byte1)

		return result, self.current


	def HPIX(self, pixel):
		''' Half-Byte Packing for 4-Bit and Pixel Data Handler '''

		#print('HPIX pixel', pixel, type(pixel))

		if self.bpp == 4:
			if self.buf == '':
				self.buf = pixel<<4
			else:
				self.buf = self.buf | pixel
				self.img_data.append(self.buf)
				self.buf = ''
		else:
			self.img_data.append(pixel)


	def EOSL(self, final=False):
		''' 00 00: End Of Scan Line '''

		#print('End of Scan Line')

		remain = self.four_width - self.rPix
		if not final:
			self.rPix = 0
			self.lines += 1
		#if remain == 0:
		#	remain = 1
		for i in range(remain):
			self.HPIX(0x00)


	def MOFF(self):
		''' 00 02: Move Offset '''

		#print('Move offset')

		mov = self.rle[self.current:self.current+2]
		self.current += 2
		mov = mov[0] + mov[1]*self.width
		for i in range(mov):
			self.HPIX(0x00)
		self.rPix += mov
		self.lines += self.rPix // mov
		self.rPix %= mov


	def UENCD(self, byte):
		''' 00 NN: Unencoded Data '''

		#print('Unencoded data')

		if self.bpp == 4:
			# read bytes with padding byte for 4 bit
			b = int(round(byte/2)) + (int(round(byte/2))%2 | byte%2)
		else:
			# read bytes with padding byte for 8 bit
			b = byte + byte%2
		ue = self.rle[self.current:self.current + b]
		self.current += b
		delta = self.rPix + byte
		for i in range(b):
			if self.rPix == delta:
				break
			if self.bpp == 4:
				for j in range(2):
					if self.rPix == delta:
						break
					self.HPIX((ue[i]&(0x0F<<(4*((j+1)%2))))>>(4*((j+1)%2)))
					self.rPix += 1
			else:
				self.HPIX(ue[i])
				self.rPix += 1


	def DENCD(self, byte0, byte1):
		''' NN PP: Decode Encoded Data '''

		#print('Decode encoded data')

		for i in range(byte0):
			if self.bpp == 4:
				self.HPIX((byte1 & (0x0F << (4*((i+1)%2)))) >> (4*((i+1)%2)))
			else:
				self.HPIX(byte1)
			self.rPix += 1


	def EORLE(self):
		''' 00 01: End Of RLE Data, Writing Decoded File '''

		#print('End of RLE data')

		self.EOSL(final=True)
		if not self.buf == '':
			self.img_data.append(self.buf)

		header = list(self.header)
		pal = list(self.palette)
		img = list(self.img_data)

		# Replace any faulty "magic number" with BM
		header[:2] = list(b'BM')

		# Write new file size
		fs = self.pal_end + len(self.img_data) # FileSize: (Header + Color Palette) + ImageData
		fsize = fs.to_bytes(4, byteorder='little')
		header[2:6] = list(fsize)

		# Write new offset
		offset = self.pal_end.to_bytes(4, byteorder='little')
		header[10:14] = list(offset)

		# Write no compression
		header[30:34] = [0,0,0,0]

		# Write image data size
		imgdsize = len(self.img_data).to_bytes(4, byteorder='little')
		header[34:38] = imgdsize

		return bytes(header + pal + img)


def extract(filename):
	raw = open(filename, 'rb').read()
	offset = 0
	num_images = 0

	findings = {}

	out_name = 'extracted/' + os.path.basename(filename) + '_{imgtype}_{hexstart}_{subimg:02d}_{hexend}_b{bpp}_c{comp}.bmp'

	while True:
		offset = find_next_candidate(raw, offset)

		# nothing found, we went through the whole file!
		if offset < 0:
			break

		#print('Offset {}'.format(hex(offset)))

		image_type = test_candidate(raw, offset)

		if not image_type:
			continue

		extract_image(raw, offset, image_type, findings, out_name)


	print(len(findings), file=sys.stderr)


def find_next_candidate(raw, offset):
	offset += 4
	# Header size 40 (4 byte)
	candidate = raw.find(b'\x28\x00\x00\x00', offset)
	#candidate = raw.find(b'\x0c\x00\x00\x00', offset)

	return candidate


def test_candidate(raw, offset):
	allowed_range = range(3, 1025) # Min and max width or height that is allowed

	image_type = 'DIB'

	if raw[offset - 14] == 66:
		image_type = 'BMP'
		bmp_header_size = 14
		data_offset = bti(raw[10:14])
	else:
		data_offset = -1
		bmp_header_size = 0

	dib_header_size = bti(raw[offset:offset + 4])
	if dib_header_size not in (12, 40):
		print(hex(offset), 'Unknown DIB header size found:', dib_header_size, file=sys.stderr)
		return False

	if dib_header_size == 40:
		color_planes = bti(raw[offset + 12:offset + 14])
		bits_per_pixel = bti(raw[offset + 14:offset + 16])
	else: # 12
		color_planes = bti(raw[offset + 8:offset + 10])
		bits_per_pixel = bti(raw[offset + 10:offset + 12])

	if color_planes != 1:
		# this must be one, otherwise it is not an image but just some random occurance of the search string
		print(hex(offset), 'Unknown color plane found:', color_planes, file=sys.stderr)
		return False

	if bits_per_pixel not in (1, 4, 8):
		print(hex(offset), 'Unknown bits_per_pixel found:', bits_per_pixel, file=sys.stderr)
		return False

	width = bti(raw[offset + 4:offset + 8])
	height = bti(raw[offset + 8:offset + 12])

	if width not in allowed_range or height not in allowed_range:
		print(hex(offset), 'too small or large', width, height, file=sys.stderr)
		return False

	if dib_header_size == 40:
		compression = bti(raw[offset + 16:offset + 20])
		if compression > 2:
			print(hex(offset), 'Unknown compression found!', compression, file=sys.stderr)
			return False

	return image_type


def extract_image(raw, offset, image_type, findings, outname):


	def uncompressed(sub_img_offset):
		if (width*bits_per_pixel/8) % 4:
			four_width = int(((width*bits_per_pixel/8) + (4-((width*bits_per_pixel/8)%4))))#*8/bits_per_pixel)
		else:
			four_width = int(width*bits_per_pixel/8)
		img_data_bytes = four_width * height

		myheader = list(bmp_header) + list(dib_header)
		# Replace any faulty "magic number" with BM
		myheader[:2] = list(b'BM')

		# Write new file size
		fs = len(myheader) + len(palette) + img_data_bytes
		fsize = fs.to_bytes(4, byteorder='little')
		myheader[2:6] = list(fsize)

		# Write new offset
		myoffset = (len(myheader) + len(palette)).to_bytes(4, byteorder='little')
		myheader[10:14] = list(myoffset)

		# Write no compression
		myheader[30:34] = [0,0,0,0]

		# Write image data size
		imgdsize = img_data_bytes.to_bytes(4, byteorder='little')
		myheader[34:38] = imgdsize

		new_offset = sub_img_offset + img_data_bytes

		new_bmp = bytes(myheader + list(palette) + list(img_data[sub_img_offset:new_offset]))
		return new_offset, new_bmp


	def compressed(sub_img_offset):
		obj = RLE_Decoder(bmp_header, dib_header, palette, img_data, sub_img_offset)
		try:
			new_bmp, new_offset = obj.Decode()
		except TypeError:
			print(hex(offset))
			raise
		return new_offset, new_bmp


	################
	#if offset != 0x2acd00:
	#	return
	################


	dib_header_size = bti(raw[offset:offset + 4])

	if image_type == 'BMP':
		bmp_header = raw[offset - 14:offset]
	else:
		bmp_header = b'BM' + b'\x00'*12

	data_offset = bti(bmp_header[10:14])

	num_images = 1

	dib_header = raw[offset:offset + dib_header_size]

	if dib_header_size == 40:
		width = bti(dib_header[4:8])
		height = bti(dib_header[8:12])
		bits_per_pixel = bti(dib_header[14:16])
		compression = bti(dib_header[16:20])
		colors = bti(dib_header[32:36])
	else: # 12
		width = bti(dib_header[4:6])
		height = bti(dib_header[6:8])
		bits_per_pixel = bti(dib_header[10:12])
		compression = 0
		colors = 0

	if colors == 0:
		colors = 2**bits_per_pixel
	pal_len = colors * 4
	pal_start = offset + dib_header_size
	pal_end = pal_start + pal_len

	if pal_len:
		palette = raw[pal_start:pal_end]
	else:
		if bits_per_pixel == 8:
			palette = standard_palette
		elif bits_per_pixel == 4:
			palette = standard_palette_4bit
		else:
			palette = []

	if data_offset:
		img_data = raw[offset + data_offset - 14:]
		num_images = (offset + data_offset - 14 - pal_end) // 20
		image_type = 'MBM'
	else:
		img_data = raw[pal_end:]


	sub_img_offset = 0
	for num in range(1, num_images + 1):
		if compression == 0:
			sub_img_offset, new_bmp = uncompressed(sub_img_offset)
		elif (compression == 1 and bits_per_pixel == 8) or (compression == 2 and bits_per_pixel == 4):
			sub_img_offset, new_bmp = compressed(sub_img_offset)
		else:
			raise NotImplementedError('Unknown combination type, comp, bpp:', image_type, compression, bits_per_pixel)

		'''if bits_per_pixel == 1:
			new_bmp = convert_1_to_8_bpp(new_bmp)
		elif bits_per_pixel == 4:
			new_bmp = convert_4_to_8_bpp(new_bmp)'''

		if image_type == 'DIB':
			hex_start = offset
		else:
			hex_start = offset - 14

		if data_offset:
			hex_end = hex_start + data_offset + sub_img_offset
		else:
			hex_end = pal_end + sub_img_offset

		filename = outname.format(imgtype=image_type, hexstart=hex(hex_start), hexend=hex(hex_end), subimg=num, bpp=bits_per_pixel, comp=compression)

		####################################
		#open('test123.dat', 'wb').write(new_bmp)
		#sys.exit()
		####################################

		save_fig(new_bmp, filename)

	if num_images > 1:
		buf_image_type = '{}({})'.format(image_type, num_images)
	else:
		buf_image_type = image_type
	print('{}\t{}\t{}, {}x{}, {}bit, c{}'.format(hex_start, hex_end, buf_image_type, width, height, bits_per_pixel, compression))

	return num_images


def save_fig(bmp, filename):

	#if os.path.isfile(filename):
	#	return

	try:
		b = io.BytesIO(bmp)
	except TypeError as e:
		print('Could not read {}'.format(filename), file=sys.stderr)
		print(e, file=sys.stderr)
		return

	try:
		im = Image.open(b)
		im = im.convert('RGB')
		im.save(filename.replace('.bmp', '.png'))
	except OSError as e:
		print('Could not write {}'.format(filename), file=sys.stderr)
		print(e, file=sys.stderr)
		return



	return
	try:
		open(filename, 'wb').write(bmp)
	except TypeError as e:
		print('Could not write {}'.format(filename), file=sys.stderr)
		print(e, file=sys.stderr)


def bti(data):
	''' bytes to integer '''

	return int.from_bytes(data, byteorder='little')


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: ', sys.argv[0], 'filename')
		sys.exit(1)

	filename = sys.argv[1]
	extract(filename)
