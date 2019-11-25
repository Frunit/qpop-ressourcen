Q-POP und Magnetic Planet Speicherstände
========================================

Jede Runde kann man bei Q-Pop und Magnetic Planet einen Speicherstand anlegen, um später weiter spielen zu können. Die Speicherstände sind zwischen den beiden Spielen sehr ähnlich. Q-Pop-Speicherstände sind genau 4172 Byte groß, Magnet-Planet-Speicherstände genau 4176 Byte. Ich habe die Speicherstände der Übersicht halber in Blöcke unterteilt. Alle Zahlen sind *[little endian](https://de.wikipedia.org/wiki/Byte-Reihenfolge)*. Bei Angaben mir Schrägstrichen bezieht sich die erste Zahl auf Q-Pop und die zweite auf Magnetic Planet.


Anfangsblock 0x0 – 0x1f bzw. 0x0 – 0x29
---------------------------------------

Q-Pop | MPlanet | Größe | Beschreibung
------|---------|-------|-------------
0x0 | 0x0 | 14/24 | String: "Q-POP Savegame" bzw. "Magnetic Planet Savegame"
0xe | 0x18 | 2 | Immer 00
0x10 | 0x1a | 1 | Musik an/aus (1/0)
0x11 | 0x1b | 1 | Musik Lautstärke (0-255)
0x12 | 0x1c | 1 | Sound an/aus (1/0)
0x13 | 0x1d | 1 | Sound Lautstärke (0-255)
0x14 | 0x1e | 1 | S1 Spielertyp (1-3)
0x15 | 0x1f | 1 | S1 IQ (1-4)
0x16 | 0x20 | 1 | S2 Spielertyp (1-3)
0x17 | 0x21 | 1 | S2 IQ (1-4)
0x18 | 0x22 | 1 | S3 Spielertyp (1-3)
0x19 | 0x23 | 1 | S3 IQ (1-4)
0x1a | 0x24 | 1 | S4 Spielertyp (1-3)
0x1b | 0x25 | 1 | S4 IQ (1-4)
0x1c | 0x26 | 1 | S5 Spielertyp (1-3)
0x1d | 0x27 | 1 | S5 IQ (1-4)
0x1e | 0x28 | 1 | S6 Spielertyp (1-3)
0x1f | 0x29 | 1 | S6 IQ (1-4)

Spielertyp kann 1 (Mensch), 2 (Computer) oder 3 (inaktiv) sein. D.h. man kann durch Ändern des Speicherstands an dieser Stelle zum Beispiel mit einem Computer tauschen.

IQ ist die Spielschwierigkeit für menschliche Spiele, bzw. die Spielstärke für Computerspieler. Der IQ reicht von 1 (Charles Darwin) bis 4 (Darwins Hund).


Spielerstatistiken 0x20 – 0xa9 bzw. 0x2a – 0xb3
-----------------------------------------------

Die Statistiken wiederholen sich für die sechs Spieler. Hier sind die Werte beispielhaft für den ersten Spieler (Purplus) angegeben. Die anderen fünf Spieler sind genau so aufgebaut.

Q-Pop | MPlanet | Größe | Beschreibung
------|---------|-------|-------------
0x20 | 0x2a | 1 | Angriff (10-100)
0x21 | 0x2b | 1 | Verteidigung (10-100)
0x22 | 0x2c | 1 | Vermehrung (10-100)
0x23 | 0x2d | 1 | Tarnung (10-100)
0x24 | 0x2e | 1 | Geschwindigkeit (10-100)
0x25 | 0x2f | 1 | Sinnesorgane (10-100)
0x26 | 0x30 | 1 | Intelligenz (10-100)
0x27 | 0x31 | 1 | Tote in der letzten Überlebensphase
0x28 | 0x32 | 1 | Kampferfahrung (besiegte Gegner)
0x29 | 0x33 | 1 | Gefressene Nahrung
0x2a | 0x34 | 1 | Anzahl Individuen
0x2b | 0x35 | 1 | Evolutionspunkte für diese Runde
0x2c | 0x36 | 1 | Bewegungspunkte für diese Runde
0x2d | 0x37 | 1 | Vermehrungspunkte für diese Runde
0x2e | 0x38 | 2 | Punktzahl (Summe aller Evolutionspunkte)
0x30 | 0x3a | 1 | Rangonen (10-100)
0x31 | 0x3b | 1 | Blaublatt (10-100)
0x32 | 0x3c | 1 | Wulgpilze (10-100)
0x33 | 0x3d | 1 | Stinkbälle (10-100)
0x34 | 0x3e | 1 | Schlingwurz (10-100)
0x35 | 0x3f | 1 | Feuergras (10-100)
0x36 | 0x40 | 1 | Tot/lebt (1/0)
...  | ...  | ... | ...
0x37 | 0x41 | 23 | Spieler 2
0x4e | 0x58 | 23 | Spieler 3
0x65 | 0x6f | 23 | Spieler 4
0x7c | 0x86 | 23 | Spieler 5
0x93 | 0x9d | 23 | Spieler 6


Anderes 0xaa – 0xb6 bzw. 0xb4 – 0xbd
------------------------------------

Q-Pop | MPlanet | Größe | Beschreibung
------|---------|-------|-------------
0xaa | 0xb4 | 2 | Aktuelle Runde
0xac |  —   | 1 | Totale Anzahl Runden (nicht in Magnetic Planet)
0xad |  —   | 1 | Menschen da/weg (1/0) (durch Katastrophe; nicht in Magnetic Planet)
0xae | 0xb6 | 2 | Immer 00
0xb0 | 0xb8 | 1 | Unbekannt. 0 bis 6
0xb1 | 0xb9 | 2 | Wasserstand
0xb3 | 0xbb | 2 | Feuchtigkeit
0xb5 | 0xbd | 2 | Temperatur

Die Totale Anzahl Runden ist je nach Startwert 5, 10, 20 oder 255 (für “bis zum bitteren Ende”). Im Prinzip ist es hier möglich, die Rundenzahl zu ändern, wenn es gerade besonders gut oder schlecht läuft. Der Wasserstand startet bei 20. Temperatur und Feuchtigkeit starten bei 50 und sind anscheinend immer durch 10 teilbar.


Karte 0xb7 – 0x9e6 bzw. 0xbf – 0x9ee
------------------------------------

Q-Pop | MPlanet | Größe | Beschreibung
------|---------|-------|-------------
0xb7  | 0xbf  | 784 | Karte
0x3c7 | 0x3cf | 784 | Höhenreliefkarte
0x6d7 | 0x6df | 784 | Einheitenpositionen

Die Karte (ab 0xb7/0xbf) entspricht genau der sichtbaren Übersichtskarte mit 28x28 Feldern. Sie wird von oben links horizontal nach unten rechts aufgebaut. Jedes Byte steht für einen Geländetyp:

Geländetyp | Bedeutung
-----------|----------
0 | Wasser
1 | Rangonen
2 | Blaublatt
3 | Wulgpilze
4 | Stinkbälle
5 | Schlingwurz
6 | Feuergras
7 | Wüste (kommt normalerweise nicht vor)
8 | Berg
9 | Krater
10 | Menschenbasis

Das Höhenrelief (ab 0x3c7/0x3cf) kann genau auf die Übersichtskarte gelegt werden, wobei die X- und Y-Achse gespiegelt sind (warum auch immer...). Über das Höherelief wird die Verteilung der Pflanzen bestimmt. Bis zu einer Höhe definiert über *Wasserstand* (siehe oben; 0xb1/0xb9) ist Wasser. Ab der Höhe 80 sind Berge. Dazwischen sind Pflanzen, wenn sich keine Menschen auf dem Feld breit gemacht haben. Der Pflanzentyp ist abhängig von der Temperatur, Feuchtigkeit, Höhe und Y-Koordinate (Nord-Süd-Achse).

Die Einheitenpositionen (ab 0x6d7/0x6df) können genau auf die Übersichtskarte gelegt werden von oben links nach unten rechts. Spieler 1 wird durch eine 1 repräsentiert, Spieler 2 durch eine 2 usw. Eine 0 bedeutet kein Spieler.


Unbekannt 0x9e7 – 0x104b bzw. 0x9ef – 0x104f
--------------------------------------------

Q-Pop | MPlanet | Größe | Beschreibung
------|---------|-------|-------------
0x9e7 | 0x9ef | 1568 | immer 0 (genau so groß wie zwei Karten!)
0x1007 | 0x100f | 23 | Mutationswerte wie beschrieben in 0x20/0x2a.
0x101e | 0x1026 | 36/32 | Unbekannt.
0x1042 | 0x1046 | 1 | Gesetzt, wenn Spieler 1 tot
0x1043 | 0x1047 | 1 | Gesetzt, wenn Spieler 2 tot
0x1044 | 0x1048 | 1 | Gesetzt, wenn Spieler 3 tot
0x1045 | 0x1049 | 1 | Gesetzt, wenn Spieler 4 tot
0x1046 | 0x104a | 1 | Gesetzt, wenn Spieler 5 tot
0x1047 | 0x104b | 1 | Gesetzt, wenn Spieler 6 tot
0x1048 | 0x104c | 1 | Unbekannt.
0x1049 | 0x104d | 1 | Gesetzt, wenn das Spiel „unendlich“ ist
0x104a | 0x104e | 1 | Gesetzt, wenn alle Gegner tot sind und man alleine weiter spielt
0x104b | 0x104f | 1 | Scrollingoption an/aus 1/0

Die Bytes, die als “Mutationswerte” markiert sind, verhalten sich genau so, wie die Spielwerte der sechs Spieler wie beschrieben in 0x20/0x2a. Es scheinen die Werte des letzte aktiven (Mensch oder Computer) Spielers der Vorrunde zu sein. Warum auch immer.
