#!/usr/bin/env python3

'''
Liest Informationen aus Speicherstand und gibt sie auf stdout aus.
Funktioniert bisher nur für Q-Pop, nicht für Magnetic Planet!

python3 get_info_from_savegame.py speicherstand.qpp
'''

import sys

if len(sys.argv) != 2:
	print('Usage: ', sys.argv[0], 'qpp-file')
	sys.exit(1)

fn = sys.argv[1]

raw = open(fn, 'rb').read()

if raw[:14] != b'Q-POP Savegame':
	print('Die Datei {} ist kein Q-POP Savegame!'.format(fn), file=sys.stderr)
	sys.exit()

### Runde ###
print('Runde {}/{}'.format(raw[0xaa], raw[0xac]))

### Spieler ###
spielertypen = ['Mensch', 'Computer', 'Niemand']
iqs = ['Charles Darwin', 'Darwins Gehilfe', 'Darwins Tante', 'Darwins Hund']
status_adresse = 0x36
for i, address in enumerate(range(0x14, 0x20, 2)):
	try:
		spielertyp = spielertypen[raw[address] - 1]
	except IndexError:
		spielertyp = 'FEHLER'
	try:
		iq = iqs[raw[address + 1] - 1]
	except IndexError:
		iq = 'unbekannt'

	if raw[0x36 + (0x17 * i)]:
		status = 'tot'
	else:
		status = 'lebt'

	print('Spieler {}: {:>8} mit IQ {:<15} ({})'.format(i + 1, spielertyp, iq, status))

### Werte ###
namen = ['Rangonen',
'Blaublatt',
'Wulgpilze',
'Stinkbälle',
'Schlingwurz',
'Feuergras',
'Vermehrung',
'Angriff',
'Verteidigung',
'Tarnung',
'Geschwindigkeit',
'Sinnesorgane',
'Intelligenz',
'Individuen',
'Evolutionspunkte']
s1addresses = [0x30,
0x31,
0x32,
0x33,
0x34,
0x35,
0x22,
0x20,
0x21,
0x23,
0x24,
0x25,
0x26,
0x2a,
0x2b]
print('                     Sp. 1   Sp. 2   Sp. 3   Sp. 4   Sp. 5   Sp. 6')
for i in range(len(namen)):
	name = namen[i]
	address = s1addresses[i]
	s1 = raw[address]
	s2 = raw[address + 23]
	s3 = raw[address + 46]
	s4 = raw[address + 69]
	s5 = raw[address + 92]
	s6 = raw[address + 115]
	print('{:<17}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format(name, s1, s2, s3, s4, s5, s6))

s1 = int.from_bytes(raw[0x2e:0x30], byteorder='little', signed=False)
s2 = int.from_bytes(raw[0x45:0x47], byteorder='little', signed=False)
s3 = int.from_bytes(raw[0x5c:0x5e], byteorder='little', signed=False)
s4 = int.from_bytes(raw[0x73:0x75], byteorder='little', signed=False)
s5 = int.from_bytes(raw[0x8a:0x8c], byteorder='little', signed=False)
s6 = int.from_bytes(raw[0xa1:0xa3], byteorder='little', signed=False)
print('{:<17}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}'.format('Gesamtpunkte', s1, s2, s3, s4, s5, s6))

### Sonstiges ###
print('Wasserstand: ', raw[0xb1])
print('Feuchtigkeit:', raw[0xb3])
print('Temperatur:  ', raw[0xb5])
