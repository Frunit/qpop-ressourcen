Q-POP Speicherstände
====================

Jede Runde kann man bei Q-Pop einen Speicherstand anlegen, um weiter zu spielen. Ich habe die Speicherstände der Übersicht halber in Blöck unterteilt. Alle Zahlen sind *[little endian](https://de.wikipedia.org/wiki/Byte-Reihenfolge)*.


Anfangsblock 0x0 - 0x1f
-----------------------

Adresse | Beschreibung
--------|-------------
0x0-0xd | String: "Q-POP Savegame"
0xe | Muss 0 sein
0xf | Muss 0 sein
0x10 | Musik an/aus (1/0)
0x11 | Musik Lautstärke (0-255)
0x12 | Sound an/aus (1/0)
0x13 | Sound Lautstärke (0-255)
0x14 | S1 Spielertyp (1-3)
0x15 | S1 IQ (1-4)
0x16 | S2 Spielertyp (1-3)
0x17 | S2 IQ (1-4)
0x18 | S3 Spielertyp (1-3)
0x19 | S3 IQ (1-4)
0x1a | S4 Spielertyp (1-3)
0x1b | S4 IQ (1-4)
0x1c | S5 Spielertyp (1-3)
0x1d | S5 IQ (1-4)
0x1e | S6 Spielertyp (1-3)
0x1f | S6 IQ (1-4)

Spielertyp kann 1 (Mensch), 2 (Computer) oder 3 (inaktiv) sein. D.h. man kann durch Ändern des Speicherstands an dieser Stelle zum Beispiel mit einem Computer tauschen.

IQ ist die Spielschwierigkeit für menschliche Spiele, bzw. die Spielstärke für Computerspieler. Der IQ reicht von 1 (Charles Darwin) bis 4 (Darwins Hund).


Spielerstatistiken 0x20 - 0xa9
------------------------------

Die Statistiken wiederholen sich für die sechs Spieler. Hier sind die Werte beispielhaft für den ersten Spieler (Purplus) angegeben. Die anderen fünf Spieler sind genau so aufgebaut.


Adresse | Beschreibung
--------|-------------
0x20 | Angriff (10-100)
0x21 | Verteidigung (10-100)
0x22 | Vermehrung (10-100)
0x23 | Tarnung (10-100)
0x24 | Geschwindigkeit (10-100)
0x25 | Sinnesorgane (10-100)
0x26 | Intelligenz (10-100)
0x27 | Unbekannt.
0x28 | Unbekannt.
0x29 | Unbekannt. Nur gesetzt, wenn Spieler menschlich.
0x2a | Anzahl Individuen
0x2b | Evolutionspunkte für diese Runde
0x2c | Unbekannt. Nur gesetzt wenn tot?
0x2d | Unbekannt. Nur gesetzt wenn tot?
0x2e-0x2f | Punktzahl (Summe aller Evolutionspunkte)
0x30 | Rangonen (10-100)
0x31 | Blaublatt (10-100)
0x32 | Wulgpilze (10-100)
0x33 | Stinkbälle (10-100)
0x34 | Schlingwurz (10-100)
0x35 | Feuergras (10-100)
0x36 | Tot/lebt (1/0)
...  | ...
0x37 | Spieler 2
0x4e | Spieler 3
0x65 | Spieler 4
0x7c | Spieler 5
0x93 | Spieler 6


Anderes 0xaa - 0xb6
-------------------

Adresse | Beschreibung
--------|-------------
0xaa-0xab | Aktuelle Runde
0xac | Totale Anzahl Runden
0xad | Menschen da/weg (1/0) (durch Katastrophe)
0xae-0xaf | immer 0
0xb0 | Unbekannt. 0, 1 oder 2
0xb1-0xb2 | Wasserstand
0xb3-0xb4 | Feuchtigkeit
0xb5-0xb6 | Temperatur

Die Totale Anzahl Runden ist je nach Startwert 5, 10, 20 oder 255 (für “bis zum bitteren Ende”). Im Prinzip ist es hier möglich, die Rundenzahl zu ändern, wenn es gerade besonders gut oder schlecht läuft. Der Wasserstand startet bei 20. Temperatur und Feuchtigkeit starten bei 50 und sind anscheinend immer durch 10 teilbar.


Karte 0xb7 - 0x9e6
------------------

Adresse | Beschreibung
--------|-------------
0xb7-0x3c6 | Karte
0x3c7-0x6d6 | Höhenreliefkarte
0x6d7-0x9e6 | Einheitenpositionen

Die Karte (ab 0xb7) entspricht genau der sichtbaren Übersichtskarte mit 28x28 Feldern. Sie wird von oben links horizontal nach unten rechts aufgebaut. Jedes Byte steht für einen Geländetyp:

Geländetyp | Bedeutung
-----------|----------
0 | Wasser
1 | Rangonen
2 | Blaublatt
3 | Wulgpilze
4 | Stinkbälle
5 | Schlingwurz
6 | Feuergras
7 | Fläche ohne Pflanze (kommt normalerweise nicht vor)
8 | Berg
9 | Krater
10 | Menschenbasis

Das Höhenrelief (ab 0x3c7) kann genau auf die Übersichtskarte gelegt werden, wobei die X- und Y-Achse gespiegelt sind (warum auch immer...). Über das Höherelief wird die Verteilung der Pflanzen bestimmt. Bis zu einer Höhe definiert über *Wasserstand* (siehe oben; 0xb1) ist Wasser. Ab der Höhe 80 sind Berge. Dazwischen sind Pflanzen, wenn sich keine Menschen auf dem Feld breit gemach haben. Wie genau bestimmt wird, welche Pflanze wo wächst, habe ich noch nicht rausbekommen. Der Pflanzentyp ist aber abhängig von Der Temperatur, Feuchtigkeit, Höhe und Y-Koordinate (Nord-Süd-Achse).

Die Einheitenpositionen (ab 0x6d7) können genau auf die Übersichtskarte gelegt werden von oben links nach unten rechts. Spieler 1 wird durch eine 1 repräsentiert, Spieler 2 durch eine 2 usw. Eine 0 bedeutet kein Spieler.


Unbekannt 0x9e7 - 0x1006
------------------------

Adresse | Beschreibung
--------|-------------
0x9e7-0x1006 | immer 0
0x1007 | Mutationswerte
0x1008 | Mutationswerte
0x1009 | Mutationswerte
0x100a | Mutationswerte
0x100b | Mutationswerte
0x100c | Mutationswerte
0x100d | Mutationswerte
0x100e-0x1016 | immer 0
0x1017 | Mutationswerte
0x1018 | Mutationswerte
0x1019 | Mutationswerte
0x101a | Mutationswerte
0x101b | Mutationswerte
0x101c | Mutationswerte
0x101d-0x1035 | Unbekannt.
0x1036-0x1041 | immer 0
0x1042 | Gesetzt, wenn Spieler 1 tot
0x1043 | Gesetzt, wenn Spieler 2 tot
0x1044 | Gesetzt, wenn Spieler 3 tot
0x1045 | Gesetzt, wenn Spieler 4 tot
0x1046 | Gesetzt, wenn Spieler 5 tot
0x1047 | Gesetzt, wenn Spieler 6 tot
0x1048-0x104a | Unbekannt. (siehe unten)
0x104b | Scrollingoption an/aus 1/0


Die Bytes, die als “Mutationswerte” markiert sind, verhalten sich genau so, wie die Spielwerte der sechs Spieler. Zu Beginn werden alle Werte auf 10 gesetzt. In der ersten Runde werden insgesamt 100 Punkte verteilt. In den darauffolgenden Runden werden 10, 15, 20 oder 25 Punkte verteilt. Nach einer Mutationskatastrophe werden die Werte genau so durcheinander gewürfelt, wie man es von den Spielerwerten kennt. Hypothese: Sind dies Werte für die Fleischfresser?

0x1048-0x104a: Einer von den Dreien wird gesetzt, wenn der menschliche Spieler alleine weiter spielt
