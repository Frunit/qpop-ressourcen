Q-POP Grafiken
==============

Die Grafiken in Q-Pop sind verteilt über viele Dateien. Die meisten sind in der `QPOP.EXE` integriert, viele größere liegen als eigene Dateien im Installationsordner.

Alle Grafiken sind Windows Bitmaps in einer oder anderer Form. Ich habe den Aufbau einer Bitmap in [bitmap.md] zusammengefasst. Manche Bitmaps fehlt der Bitmap-Header, was sie zu *device-independent bitmaps* (DIB) macht. Manche sind unkomprimiert, manche sind lauflängenkodiert (*run-length encoded*, RLE). Es gibt Bitmaps mit 1, 4 oder 8 bit pro Pixel. Grafiken, die im Intro, Abspann oder in Katastrophenanimationen verwendet werden, sind in einem speziellen Format gespeichert, wo sich viele Bilder einen Header und eine Palette teilen. Diese Bilder wurden mit [Take One](http://www.take1.de) zu Animationen zusammengefasst. Take One ist heutzutage kostenlos verfügbar. Damit es nicht zu langweilig wird, gibt es auch noch ein paar Bilder, die keine eigene Palette haben.

Mit viel [Python](https://www.python.org)-Scripting ist es mir gelungen, die meisten Grafiken zu extrahieren.

Alle Grafiken liegen in `grafiken`. Ich habe Multibitmaps zusammengefasst. Außerdem habe ich Hintergründe, die Transparent sein sollten, transparent gemacht. Manche Grafiken haben auch Alpha-Masken (als zweite Grafik). Diese Masken habe ich angewendet, um fertige Bilder mit Transparenz zu erhalten. In all diesen Fällen liegt die Originaldatei (und ihre Maske) in `grafiken/original`.

In der folgenden Tabelle sind alle Grafiken angegeben, die ich extrahieren konnte. Für jede Grafik ist die Quelldatei und die Verwendung im Spiel angegeben. Wenn ein Name unter *Technische Bemerkung* angegeben ist, ist dies der Name der Originaldatei, soweit ich ihn aus `QPOP.EXE` ermitteln konnte. Die deutsche Version 1.02 ist die Referenz für die Adressen.

Die Tabellen sind auch in [grafiken.csv].


Bild | Quelle | Verwendung | Technische Bemerkung
-----|--------|------------|---------------------
BACKHELL.DAT.png | BACKHELL.DAT | Grauer Hintergrund |
ELEKTRO.DAT.png | ELEKTRO.DAT | Elektropflanze mit Hintergrund |
GENETIK.DAT.png | GENETIK.DAT | Monstren und Mutationen |
HINTEND.DAT.png | HINTEND.DAT | Abspann Hintergrund (Niederlage) |
HINTEND1.DAT.png | HINTEND1.DAT | Abspann Hintergrund (Sieg) |
INIT.DAT.png | INIT.DAT | Spielerauswahl (Startbildschirm) |
KAMPF.DAT.png | KAMPF.DAT | Fressen und gefressen werden |
KASTRO1.DAT.png | KASTRO1.DAT | Katastrophenhintergrund: Meteor, Mutation |
KASTRO2A.DAT.png | KASTRO2A.DAT | Katastrophenhintergrund: Vulkan |
KASTRO3.DAT.png | KASTRO3.DAT | Katastrophenhintergrund: Dürre, Kälte, Erdbeben |
KASTRO4.DAT.png | KASTRO4.DAT | Katastrophenhintergrund: Seuche, Menschen |
KASTRO5.DAT.png | KASTRO5.DAT | Katastrophenhintergrund: Flut |
LEBEN.DAT.png | LEBEN.DAT | Der Krieg der Arten |
MEER.DAT.png | MEER.DAT | Übersichtskartenteile | Masken angewendet und etwas neu arrangiert
POPHIN.DAT.png | POPHIN.DAT | Intro: Planetenhintergrund mit Transparenz | Transparenz hinzugefügt
POPHIN1.DAT.png | POPHIN1.DAT | Intro: Planetenhintergrund ohne Transparenz |
PREDATOR.0.png | PREDATOR.0 | Masken für Fleischfresser | auf PREDATOR.? angewendet
PREDATOR.1.png | PREDATOR.1 | Dino in Überlebensphase | maskiert mit PREDATOR.0
PREDATOR.2.png | PREDATOR.2 | Pilz in Überlebensphase | maskiert mit PREDATOR.0
PREDATOR.3.png | PREDATOR.3 | Mensch in Überlebensphase | maskiert mit PREDATOR.0
feuchtigkeit.png | QPOP.EXE | GUI: Feuchtigkeitsanzeiger | 2 Bilder; 40x100; selbst zusammengestellt
kalender.png | QPOP.EXE | GUI: Kalender | 2 Bilder; 60x44; selbst zusammengestellt
minimap.png | QPOP.EXE | GUI: Minimapicons | 5 Bilder; 8x8; selbst zusammengestellt
plus_minus_buttons.png | QPOP.EXE | GUI: Buttons plus/minus | 4 Bilder; 16x16; selbst zusammengestellt
pointer.png | QPOP.EXE | Mauszeiger | 1 Bild; 32x32; cursor file
QPOP.EXE_0x10a900.png | QPOP.EXE | Katastrophe: Dürre: Sonne | 5 Bilder; 70x70; SONNE2
QPOP.EXE_0x10bf00.png | QPOP.EXE | Intro: Raumschiff “Charles Darwin” | 1 Bild; 300x225; STATION2
QPOP.EXE_0x10f200.png | QPOP.EXE | Intro: Wolken “Karl L. von Wendt” | 7 Bilder; 105x71; STAUB
QPOP.EXE_0x115700.png | QPOP.EXE | Katastrophe: Dürre: Isnobug macht einen Liegestuhl | 16 Bilder; 100x64; STUHL
QPOP.EXE_0x120200.png | QPOP.EXE | Abspann: Monitor oben und unten | 2 Bilder; 273x66; TAFELDEC
QPOP.EXE_0x127800.png | QPOP.EXE | Intro: Buckcherry mit Schild “Music” wird gegrillt | 17 Bilder; 70x114; TAFELFRU
QPOP.EXE_0x133f00.png | QPOP.EXE | Intro: Drei Fluggeräte. Nur Papierflieger wird im Intro gezeigt | 3 Bilder; 80x50; UFOS
QPOP.EXE_0x13ce00.png | QPOP.EXE | Katastrophe: Flut: Amorph klettert | 18 Bilder; 64x64; AMOEGRO
QPOP.EXE_0x144600.png | QPOP.EXE | Katastrophe: Erdbeben: Baum | 1 Bild; 128x128; BAUMBE
QPOP.EXE_0x146600.png | QPOP.EXE | Katastrophe: Erdbeben: Bäume | 3 Bilder; 32x45; BAUMBEBE
QPOP.EXE_0x147400.png | QPOP.EXE | Katastrophe: Flut: Wasser steigt am Baum | 9 Bilder; 152x95; BAUMGRO
QPOP.EXE_0x155a00.png | QPOP.EXE | Katastrophe: Flut: Wasser steigt am Baum | 9 Bilder; 96x60; BAUWAS
QPOP.EXE_0x15d000_...png | QPOP.EXE | Katastrophe: Erdbeben: Spalte | 12 Bilder; 149x148; BEBEN\[\_123\]
QPOP.EXE_0x196400.png | QPOP.EXE | Abspann: Amorph in Kleidung | 6 Bilder; 64x64; ENDAMOE
QPOP.EXE_0x198f00.png | QPOP.EXE | Abspann: Buckcherry in Kleidung (2 verschiedene) | 6 Bilder; 64x64; ENDFRU
QPOP.EXE_0x19b800.png | QPOP.EXE | Abspann: Pesci mit Hut (2 verschiedene) | 8 Bilder; 64x64; ENDHAI
QPOP.EXE_0x1a0100.png | QPOP.EXE | Abspann: Ein Pesci mit Fischglas | 8 Bilder; 128x64; ENDHAI2
QPOP.EXE_0x1a8200.png | QPOP.EXE | Abspann: Isnobug mit Hut (2 verschiedene) | 8 Bilder; 64x80; ENDKAEF
QPOP.EXE_0x1ad200.png | QPOP.EXE | Abspann: Texte/Bilder aus dem Monitor | 15 Bilder; 251x100; ENDTEXT
QPOP.EXE_0x1b8700.png | QPOP.EXE | Katastrophe: Flut: Floß | 2 Bilder; 62x39; FLOSS
QPOP.EXE_0x1b9500.png | QPOP.EXE | Abspann: Purplus in Rakete | 4 Bilder; 235x119; FLUGMOBI
QPOP.EXE_0x1c2500.png | QPOP.EXE | Katastrophe: Vulkan: Feuergras verschwindet | 4 Bilder; 30x19; GRAS
QPOP.EXE_0x1c2e00_...png | QPOP.EXE | Katastrophe: Seuche: Pesciodyphus wird Krank groß | 18 Bilder; 124x117; HAI\[12\]
QPOP.EXE_0x1db400.png | QPOP.EXE | Katastrophe: Seuche: Pesciodyphus wird Krank mittelgroß | 16 Bilder; 64x64; HAI3
QPOP.EXE_0x1e5400.png | QPOP.EXE | Abspann: Polizeirakete | 1 Bild; 250x150; HUNTER
QPOP.EXE_0x1e8a00.png | QPOP.EXE | Katastrophe: Vulkan: Explosion | 9 Bilder; 50x50; KNALL
QPOP.EXE_0x1eaf00.png | QPOP.EXE | Katastrophe: Flut: Baumwipfel | 1 Bild; 77x76; KRONE
QPOP.EXE_0x1ebf00.png | QPOP.EXE | Katastrophe: Mutation: Purplus mutiert | 23 Bilder; 68x64; KUH2
QPOP.EXE_0x1f9300.png | QPOP.EXE | Katastrophe: Meteorit: Purplus unter Meteorit | 1 Bild; 120x35; KUHTOT
QPOP.EXE_0x1fa300.png | QPOP.EXE | Katastrophe: Meteoriten und Mutation: Meteorit | 1 Bild; 120x120; METEOR
QPOP.EXE_0x1fce00.png | QPOP.EXE | Abspann: Dino an der Leine | 4 Bilder; 70x60; MINIDINO
QPOP.EXE_0x1fe700.png | QPOP.EXE | Abspann: Pilz an der Leine | 3 Bilder; 90x70; MINIPILZ
QPOP.EXE_0x1ff900.png | QPOP.EXE | Abspann: Speeder mit Kiwiopteryx | 2 Bilder; 150x100; NEST
QPOP.EXE_0x203100.png | QPOP.EXE | Abspann: Speeder mit Kiwiopteryx | 2 Bilder; 110x50; NEST1
QPOP.EXE_0x204700.png | QPOP.EXE | Katastrophe: Flut: Pilzanimation | 8 Bilder; 32x32; PILZKLE
QPOP.EXE_0x206800.png | QPOP.EXE | Katastrophe: Erdbeben: Kiwiopteryx spreizt die Beine | 11 Bilder; 74x71; PUBEBEN
QPOP.EXE_0x20b100.png | QPOP.EXE | Katastrophe: Vulkan: Buckcherry jubelt klein | 1 Bild; 32x30; QPOPFRUK
QPOP.EXE_0x20aa00.png | QPOP.EXE | Katastrophe: Menschen: Menschenrakete | 4 Bilder; 150x150; RAKETE
QPOP.EXE_0x217500.png | QPOP.EXE | Katastrophe: Menschen: Menschenrakete landet | 5 Bilder; 200x65; RAKRAUCH
QPOP.EXE_0x220200.png | QPOP.EXE | Katastrophe: Menschen: Rampe fährt aus | 8 Bilder; 72x40; RAMPE
QPOP.EXE_0x221e00.png | QPOP.EXE | Abspann: Speeder mit Buckcherry | 4 Bilder; 110x30; SCHIFF
QPOP.EXE_0x223800.png | QPOP.EXE | Abspann: Speeder mit Purplus | 4 Bilder; 110x30; SCHIFF1
QPOP.EXE_0x225100.png | QPOP.EXE | Katastrophe: Seuche: Seuche infiziert | 3 Bilder; 47x32; SEUVIEH
QPOP.EXE_0x225f00.png | QPOP.EXE | Katastrophe: Mutation: Meteorit wechselt die Farbe | 4 Bilder; 120x120; SPUTNIK
QPOP.EXE_0x22f800.png | QPOP.EXE | Abspann: Steinstatuen der Spezies | 6 Bilder; 70x70; STATUEN
QPOP.EXE_0x236c00.png | QPOP.EXE | Katastrophe: Menschen: Menschen laufen | 4 Bilder; 64x64; TYP
QPOP.EXE_0x238700_...png | QPOP.EXE | Katastrophe: Vulkan: Vulkan entsteht, bricht aus, raucht | 18 Bilder; 150x120; VULKAN\[\_12\]
QPOP.EXE_0x257000.png | QPOP.EXE | Katastrophe: Vulkan: Buckcherry fällt | 18 Bilder; 64x64; VULKFRU
QPOP.EXE_0x2ab700.png | QPOP.EXE | Intro: Sternenhintergrund | 1 Bild; 600x420
QPOP.EXE_0x2c9500.png | QPOP.EXE | Programmicon | Falsche Höhenangabe; “Icon 1”
QPOP.EXE_0x2c9c00.png | QPOP.EXE | Bodenteile Überlebensphase | 640x896
QPOP.EXE_0x355d00.png | QPOP.EXE | Spezies für Säulen und Punkte | 448x512
QPOP.EXE_0x38de00.png | QPOP.EXE | Icons und Balken für Mutationsscreen | 600x120
QPOP.EXE_0x39f800.png | QPOP.EXE | Siegerkranz | 380x310
QPOP.EXE_0x3bc00.png | QPOP.EXE | "Intro: Buchstaben (A-Z ohne X 0-9 .-"": Ä)" | 40 Bilder; 15x18; ALPHA
QPOP.EXE_0x3bc500.png | QPOP.EXE | Wolken (Kampf und Sex) | 448x456
QPOP.EXE_0x3d800.png | QPOP.EXE | Intro: Amorph mit Schild “Lars Hammer” | 5 Bilder; 100x100; AMOESAUG
QPOP.EXE_0x3ee400.png | QPOP.EXE | Spezies im Kampf in Überlebensphase | 448x384
QPOP.EXE_0x41300.png | QPOP.EXE | Intro: Amorph mit Schild “Lars Hammer” wird eingesogen | 10 Bilder; 130x100; AMOEWEG
QPOP.EXE_0x47000.png | QPOP.EXE | Intro: Staub wird eingesaugt | 6 Bilder; 70x26; ASCHE
QPOP.EXE_0x54400.png | QPOP.EXE | Intro: Schild “Lars Hammer” kommt aus dem Boden | 6 Bilder; 65x70; BOSCHILD
QPOP.EXE_0x57000.png | QPOP.EXE | Abspann: Dino geht und hat gefressen | 11 Bilder; 64x64; DINO
QPOP.EXE_0x5cc00.png | QPOP.EXE | Katastrophe: Kälte: Chuckberry wird eingeschneit | 22 Bilder; 64x64; EISFRU
QPOP.EXE_0x67400.png | QPOP.EXE | Katastrophe: Kälte: Wolke | 3 Bilder; 120x70; EISWOLK
QPOP.EXE_0x69c00.png | QPOP.EXE | Strompflanze | 16 Bilder; 64x64; ELEKTRO
QPOP.EXE_0x6f100.png | QPOP.EXE | Abspann: Demo-Texte für den Abspannmonitor | 16 Bilder; 251x100; ENDTEXT2
QPOP.EXE_0x7b500.png | QPOP.EXE | Intro: Isnobug mit Besen | 4 Bilder; 73x70; FEGESEK
QPOP.EXE_0x7e200.png | QPOP.EXE | Katastrophe: Dürre: Fisch auf dem Trockenen | 3 Bilder; 50x24; FISCH
QPOP.EXE_0x7eb00.png | QPOP.EXE | Intro: Pesci mit Schild “Program” | 4 Bilder; 84x122; HASCHILD
QPOP.EXE_0x84700.png | QPOP.EXE | Intro: Glasscheibe “Game Design” | 4 Bilder; 140x97; INTFRU
QPOP.EXE_0x8e100.png | QPOP.EXE | Intro: Glasscheibe “Game Design” zerbricht und wird weggefegt | 12 Bilder; 140x97; INTFRU1
QPOP.EXE_0x9ac00.png | QPOP.EXE | Intro: Buckcherry lässt Scheibe fallen und läuft weg | 6 Bilder; 64x64; INTFRU2
QPOP.EXE_0x9e300.png | QPOP.EXE | Intro: Buckcherry läuft weg | 11 Bilder; 64x64; INTFRU3
QPOP.EXE_0xa3400.png | QPOP.EXE | Intro: Pesci mit Fahne “Graphics” | 4 Bilder; 124x70; INTHAI
QPOP.EXE_0xa6100.png | QPOP.EXE | Intro: Zerbröselnder Meteorit mit Fahne “Karl L. von Wendt” | 8 Bilder; 120x120; INTROME2
QPOP.EXE_0xaec00.png | QPOP.EXE | Intro: Pilz greift an. Außerdem: Dose mit Blankoetikett | 7 Bilder; 64x64; INTROPIL
QPOP.EXE_0xb4000.png | QPOP.EXE | Intro: Zwei Isnobug mit Banner “Stefan Beyer” | 4 Bilder; 134x116; INTSEK1
QPOP.EXE_0xbb600.png | QPOP.EXE | Katastrophe: Dürre und Kälte: Isnobug schwitzt | 16 Bilder; 64x64; KAEFER
QPOP.EXE_0xc3f00.png | QPOP.EXE | Intro: Kiwi mit “KiwiGames”-Fahne | 3 Bilder; 200x120; KIWI2
QPOP.EXE_0xc8300.png | QPOP.EXE | Intro und Katastrophe (Mutation, Meteorit): Purplus läuft und guckt | 24 Bilder; 68x64; KUH1
QPOP.EXE_0xd3e00.png | QPOP.EXE | Intro: Fahne “Karl L. von Wendt” weht weg | 4 Bilder; 100x72; LAKEN2
QPOP.EXE_0xd5500.png | QPOP.EXE | Katastrophe: Dürre: Pflanze geht ein | 6 Bilder; 110x130; PALME
QPOP.EXE_0xdde00.png | QPOP.EXE | Intro: Drei Planetoide | 3 Bilder; 100x100; PLANETEN
QPOP.EXE_0xe0c00.png | QPOP.EXE | Intro: Roter und schwarzer Punkt als Teil des Raumschiffs | 2 Bilder; 8x8; POSILICH
QPOP.EXE_0xe1100.png | QPOP.EXE | Intro: Satellitenschüssel des Raumschiffs | 4 Bilder; 18x17; RADAR
QPOP.EXE_0xe1900.png | QPOP.EXE | Intro: Isnobug mit Staubsauger “Karl L. von Wendt” | 6 Bilder; 175x64; SAUGSEK
QPOP.EXE_0xea000.png | QPOP.EXE | Intro: “Welcome to Q-POP”-Schild | 4 Bilder; 392x218; SCHIPOP2
QPOP.EXE_0xfc100.png | QPOP.EXE | Katastrophe: Kälte: Schnee fällt | 3 Bilder; 80x150; SCHNEE
QPOP.EXE_0xfd100.png | QPOP.EXE | Katastrophe: Dürre: Wasser geht zurück | 12 Bilder; 200x70; SEE
rotes_x.png | QPOP.EXE | GUI: Rotes X | 1 Bild; 11x12
stand_icons.png | QPOP.EXE | Icons für Standanzeige | 2 Bilder; 16x16; selbst zusammengestellt
thermometer.png | QPOP.EXE | GUI: Thermometer | 2 Bilder; 40x100; selbst zusammengestellt
titelmenu.png | QPOP.EXE | Titelmenübuttons | 5 Bilder; 10x12; selbst zusammengestellt
ueberleben_gui.png | QPOP.EXE | GUI: Überlebensereignisse | 3 Bilder; 16x16; selbst zusammengestellt
ueberleben_gui2.png | QPOP.EXE | GUI: verbleibende Zeit | 2 Bilder; 20x20; selbst zusammengestellt
RUNDEN.DAT.png | RUNDEN.DAT | Auswahl der Runden | Maskiert
RUNDEN2.DAT.png | RUNDEN2.DAT | Maske für Auswahl der Runden | Angewendet. Musste mit c:\windows\extract.exe extrahiert werden
SPECIES.0.png | SPECIES.0 | Masken für Pflanzenfresser | auf SPECIES.? angewendet
SPECIES.1.png | SPECIES.1 | Purplus in Überlebensphase | maskiert mit SPECIES.0
SPECIES.2.png | SPECIES.2 | Kiwiopteryx in Überlebensphase | maskiert mit SPECIES.0
SPECIES.3.png | SPECIES.3 | Pesciodyphus in Überlebensphase | maskiert mit SPECIES.0
SPECIES.4.png | SPECIES.4 | Isnobug in Überlebensphase | maskiert mit SPECIES.0
SPECIES.5.png | SPECIES.5 | Amorph in Überlebensphase | maskiert mit SPECIES.0
SPECIES.6.png | SPECIES.6 | Buckcherry in Überlebensphase | maskiert mit SPECIES.0
STAND.DAT.png | STAND.DAT | Bewertungsphase und Icons für Dialogfenster | Maskiert mit Maske aus QPOP.EXE


Ein paar Grafiken aus `QPOP.EXE` haben bisher Fehler nach dem Extrahieren. Die folgenden Grafiken fehlen daher in der Sammlung.


Startadresse | Bildtyp | Originalname | Beschreibung | Fehler
-------------|---------|--------------|--------------|-------
0x48e00 | MBM, 600x30, 8bit, c1 | BALKEN | Intro: Fading-Maske für Übergang zur Planetenoberfläche | Drei Frames fehlen
0x109500 | MBM, 31x31, 8bit, c1 | SONNE | Katastrophe: Dürre: Sonne | Nur ein Frame vorhanden, Rest gelb
0x1e2b00 | MBM, 32x32, 8bit, c1 | HAI4 | Katastrophe: Seuche: Pesciodyphus wird Krank *klein* | Letzter Frame fehlt
0x232000 | MBM, 35x49, 8bit, c0 | TUER | Katastrophe: Menschen: Raketenteil | Offset falsch
0x25fd00 | MBM, 50x147, 8bit, c1 | WELLE | Eine Küste | Der erste Frame ist weiß
0x2ab300 | DIB, 10x12, 4bit, c0 | Bitmap 975 | ??? | komplett schwarz


Die englische Version von Q-Pop hat ein paar Grafiken die nicht in der deutschen Version verwendet wurden, oder verändert wurden.


Bild | Quelle | Verwendung | Technische Bemerkung | Änderung ggü. deutscher Version
-----|--------|------------|----------------------|--------------------------------
en_QPOP.EXE_ENDTEXT_0xe6a00.png | QPOP.EXE_en | Abspann: Texte/Bilder aus dem Monitor | 6 Bilder; 250x100; ENDTEXT | anderer Text
en_QPOP.EXE_KIWI_0x163a00.png | QPOP.EXE_en | Intro: Kiwi mit “KiwiGames”-Fahne | 3 Bilder; 200x120; KIWI | anderes Kiwi-Logo
en_QPOP.EXE_PLANETEN_0x19bc00.png | QPOP.EXE_en | Intro: Fünf Planetoide | 5 Bilder; 100x100; PLANETEN | andere Planeten
en_QPOP.EXE_SCHIPOP_0x1c6d00.png | QPOP.EXE_en | Intro: “Welcome to Q-POP”-Schild | 4 Bilder; 392x218; SCHIPOP | Schriftzug “Danger...” fehlt
en_QPOP.EXE_STATION1_0x1f0e00.png | QPOP.EXE_en | Intro: Raumstation | 1 Bild; 300x225; STATION | Völlig andere Raumstation
en_QPOP.EXE_UFO_0x223b00.png | QPOP.EXE_en | Intro: Ufo mit “P.M. Präsentiert” | 1 Bild; 350x120; UFO | Nicht in deutscher Version vorhanden
