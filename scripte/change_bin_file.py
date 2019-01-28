#!/usr/bin/env python3

'''
Liest und schreibt Binärdateien. Sehr rudimentär, aber praktisch auch um Speicherstände zu manipulieren.

python3 change_bin_file.py binaerdatei.exe
'''

import sys

if len(sys.argv) != 2:
	print('{} bin_file.exe'.format(sys.argv[0]), file=sys.stderr)
	sys.exit()

fn = sys.argv[1]

raw = list(open(fn, 'rb').read())

print('Type "help" to get a list of commands')

helptext = '''Commands:

¤ help
print this text

¤ save path/to/filename.end
save current bytes in buffer to given file

¤ exit
Exits (without saving!)

¤ num
Prints the value at address num. Num may be either written as decimals or hex numbers. Hex numbers must start with 0x. E.g.:
0x3b # Tells the value at 0x3b

¤ address value
Writes value to address. value must be between 0 and 255 (inclusive). Both numbers
may be either written as decimals or hex numbers. Hex numbers must start
with 0x. E.g.:
0x3b 27 # write 27 to 0x3b'''



while True:
	cmd = input('¤ ').lower()

	cmdl = cmd.split()

	if cmd == 'help':
		print(helptext)
		continue

	if cmdl[0] == 'save' and len(cmdl) == 2:
		open(cmdl[1], 'wb').write(bytes(raw))
		print('Wrote to file "{}"'.format(cmdl[1]))
		continue

	if cmd == 'exit':
		break

	if len(cmdl) == 1:
		try:
			if cmd.startswith('0x'):
				where = int(cmd, base=16)
			else:
				where = int(cmd)
		except ValueError:
			print('Unknown command')
			continue

		print('{}   {}'.format(hex(raw[where]), raw[where]))
		continue


	if len(cmdl) == 2:
		try:
			if cmdl[0].startswith('0x'):
				where = int(cmdl[0], base=16)
			else:
				where = int(cmdl[0])
		except ValueError:
			print('Unknown command')
			continue

		try:
			if cmdl[1].startswith('0x'):
				what = int(cmdl[1], base=16)
			else:
				what = int(cmdl[1])

			if not 0 <= what <= 255:
				raise ValueError
		except ValueError:
			print('Not a number or not within 0 and 255')
			continue

		raw[where] = what

		print('Written {} to {}'.format(hex(what), hex(where)))
		continue


	print('Unknown command.')
