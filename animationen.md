Q-POP Animationen
=================

Kompliziertere Animationen wurden mit [Take One](http://www.take1.de) erstellt. Folgende Animationen sind im `QPOP.EXE` enthalten.

Startadresse | Länge (Byte) | Beschreibung
-------------|--------------|-------------
0x36f00  | 2816 | Intro1
0x37a00  | 2560 | Intro2
0x38400  | 2560 | Intro3
0x38e00  | 2816 | Dürrekatastrophe
0x39900  | 2048 | Kältekatastrophe
0x3a100  | 4864 | Introanfang
0x3b400  | 2048 | Abspann verloren mit Demotext (nicht in Vollversion verwendet)
0x134d00 | 2048 | Meteorkatastrophe
0x135500 | 2560 | Mutationskatastrophe
0x135f00 | 3072 | Seuchenkatastrophe
0x136b00 | 2560 | Vulkankatastrophe
0x137500 | 2304 | Flutkatastrophe
0x137e00 | 3328 | Menschenkatastrophe
0x138b00 | 2816 | Erdbebenkatastrophe
0x139600 | 2048 | Abspann verloren
0x139e00 | 2048 | Abspann gewonnen Purplus
0x13a600 | 1792 | Abspann gewonnen Kiwiopteryx
0x13ad00 | 2304 | Abspann gewonnen Pesciodyphus
0x13b600 | 2048 | Abspann gewonnen Isnobug
0x13be00 | 1792 | Abspann gewonnen Amorph
0x13c500 | 2304 | Abspann gewonnen Buckcherry


Animationsaufbau
================

Allgemeiner Aufbau:

1. Format und Header (Startet bei 0x00)
2. Zu ladende Grafiken (Startet bei 0x64)
3. Animationsblöcke (Startet bei 0xEE + 0x44 * anzahl_der_grafiken)

Animationsteile funktionieren relativ zueinander, es gibt keine "zentrale" Uhr für die Animationsteile.

Mehrbytige Integer sind "little endian".

Ein Script zum Darstellen von Infos über Animationen ist in [animation_reader.py](scripte/animation_reader.py).


Header
------

Der Header ist 0x64 (100) Byte lang.

Animationen fangen mit "AN" an.
0x04 ist die Anzahl der Grafiken im nächsten Block.
0x05 ist die Anzahl der "Animationsobjekte"/Animationsblöcke
0x13 ist der String "Animation". Der String sollte wohl bis zu 64 Byte lang sein, der Rest sind 0-Bytes.
0x59 (2 Byte) ist die Breite der Animation in Pixel
0x5B (2 Byte) ist die Höhe der Animation in Pixel

Unbekannte Byte sind die folgenden, jeweils mit möglichen Werten in den 22 gegebenen Animationen aus Q-Pop und MPlanet:

- Position 0x02
  * 0x01 (alle Katastrophen, intro1-3)
  * 0x51 (alle Abspanne, intro-anfang und intro-mplanet)
- Position 0x08
  * 0x00 (alle Abspanne, Vulkan und Menschen)
  * 0x01 (Meteor)
  * 0x02 (Kälte)
  * 0x03 (Seuche und intro2)
  * 0x04 (intro3)
  * 0x05 (Mutation und intro-anfang)
  * 0x07 (Dürre, Flut, intro1 und intro-mplanet)
  * 0x09 (Erdbeben)
- Position 0x53
  * 0x0C (alle Q-Pop-Animationen)
  * 0x1C (intro-mplanet)
- Position 0x5D
  * 0xe0 (alle anderen)
  * 0xe8 (intro1 und intro2)
  * 0xf0 (intro-anfang)
- Position 0x60
  * 0x00 (alle anderen)
  * 0xff (Kälte, Menschen, Meteor und Mutation)

Alle anderen Bytes sind entweder bekannt (siehe oben) oder immer 0x00.


Zu ladende Grafiken
-------------------

Der Grafikenblock hat eine Variable Länge (0x8a + 68 * anzahl_der_grafiken). Offsets hier sind relativ zum Start des Grafikblocks.

0x00: der Pfad zur Hintergrundgrafik (BMP). 64 Byte; ungenutzte sind 0x00.

0x40: hier *kann* ein Pfad zu einer Animationsdatei liegen, die im Anschluss an die aktuelle gestartet werden soll. Wenn es so ist, sind die ersten 4 Byte 0x00. Die folgenden 64 Byte sind wieder der Pfad zur Datei mit ungenutzten Byte = 0x00. Nach dem Animationspfad kommen zwei Byte 0x04 und 0x03 und dann vier Byte die 0x00 sind. Wenn der Pfad nicht da ist, sind alle 74 Byte = 0x00.

0x8A: ab hier kommen die Grafiken, die für die Animation benötigt werden (BMX). Jeder Block ist 68 Byte lang. Die Anzahl der Grafiken wird im Header definiert.

BMX-Objekte sind 68 Byte lang:

- 1 Byte: Anzahl der Frames in der Grafik
- 1 Byte: unbekannt (bisher 0x00, 0x02, 0x04, 0x06, 0x0A, 0x0C, 0x0D, 0x0E, 0x0F, 0x80) Könnten dass Flags sein? binär: x000xxxx Evtl. eine Markierung für Transparenz? Nicht-transparente Bilder haben (glaube ich) immer 0x80 (also binär 10000000). Transparente (glaube ich) immer binär 0000xxxx.
- 1 Byte: immer 0x00, außer bei ENDTEXT.BMX und ENDTEXT2.BMX, dann 0x10
- 1 Byte: immer 0x01, außer bei ENDTEXT.BMX und ENDTEXT2.BMX, dann 0x00
- 64 Byte: Pfad zur BMX-Datei. Alle ungenutzten Byte sind 0.


Animationsblöcke
----------------

Der eigentliche Animationsteil hat eine Variable Länge. Er besteht aus aneinandergereihten Animationsblöcken. Jeder Animationsblock hat auch eine variable Länge, die jeweils am Anfang des Blocks angegeben ist. Offsets hier sind relativ zum Start des Animationsblocks.

0x00 ist die 0-basierten Nummer der Grafik, die für dieses Animationsobjekt verwendet werden soll in der Reihenfolge, wie sind im Grafikenblock definiert sind (0 für die erste Grafik, 1 für die zweite usw.).

0x01 ist der Name der Animation (0x00-terminiert, aber nicht mit einer festen Länge!).

Direkt danach *können* ein paar Byte (etwa 1-3?) folgen, die nicht 0x00 sind und deren Bedeutung unbekannt ist. Danach folgen dann 0-Bytes

0x21 ist ein Byte mit dem Wert 0x01.

0x22 ist die Anzahl der Elemente in der Animation. Danach kommen 21 Byte, die meistens 0 sind, aber manchmal auch einen Block mit 0x6B 0xFF 0xBB 0xFF enthalten (unbekannt), die Gesamtlänge von 21 Byte aber nicht ändern.

0x36 ist der Beginn der Elemente, die die Animation definieren. Zur Anzahl, siehe Header Byte 0x05. Jedes Element ist 16 Byte lang. Offset hier vom Beginn eines Elements.


Byte | Länge  | Beschreibung
-----|--------|-------------
0x00 | 1 Byte | Nummer des Unterbildes zu zeigen (0-basiert). Durch die Gesamtbreite der Grafik und die Anzahl der Frames in der Grafik (siehe "Zu ladende Grafiken") ist die Breite eines Unterbildes definiert.
0x01 | 1 Byte | Verzögerung (in Frames) zum nächsten Frame
0x02 | 1 Byte | Siehe unten.
0x03 | 2 Byte | (signed int) X-Koordinate absolut von der Mitte oder relativ zur letzten Koordinate. Bedeutung abhängig von 0x02.
0x05 | 2 Byte | (signed int) Y-Koordinate absolut von der Mitte oder relativ zur letzten Koordinate. Bedeutung abhängig von 0x02.
0x07 | 2 Byte | 0x00 oder 0xff (siehe unten)
0x09 | 1 Byte | Unbekannt, immer 0x00
0x0a | 1 Byte | Wenn dieses Byte 0x01 ist, wird ein Loop angestoßen (siehe unten)
0x0b | 1 Byte | Wiederhole so oft... (oder unendlich oft, wenn dieses Byte 0 ist)
0x0c | 1 Byte | Springe zu diesem Frame. Weitere Erklärung, siehe unten
0x0d | 1 Byte | Unbekannt, immer 0x00
0x0e | 2 Byte | (little endian!) Die Position der Bits(!) gibt an, welche Animationssequenzen fortgeführt/gestartet werden sollen. z.B. 0000 0000 0010 0001 -> Erste und sechste Sequenz fortsetzen


### Byte 0x02

Dies scheinen Flags zu sein. Mit den Bits 12345678:
Bit 1: Wenn gesetzt, ist die X-Koordinate absolut, sonst relativ zur vorherigen Position
Bit 2: Wenn gesetzt, ist die Y-Koordinate absolut, sonst relativ zur vorherigen Position
Bit 3: Wenn gesetzt, wird das aktuelle Bild fixiert, wird also nicht beim nächsten Bild gelöscht
Bit 4: Markiert das Ende der Animation (scheint aber nicht unbedingt notwendig zu sein)
Bit 5: Wenn gesetzt, pausiert die Animationssequenz hier, bis sie von einer anderen Sequenz gestartet werden. Sequenzen, derer erster Schritt dieses Bit *nicht* gesetzt haben, starten mit Animationsbeginn.

Die anderen Bits sind unbekannt und bei Q-Pop immer 0.
Bit 6 ist bei Magnetic Planet an einer Stelle gesetzt und scheint, wie Bit 4 das Ende der Animation zu markieren.


### Bytes 0x07 und 0x08

Die Bytes sind in allen Abspann-Animationen, Introanfang und MPlanet-Intro 0 (0x00 0x00).
Sie sind -1 (0xFF 0xFF) in Intro 1-3 und allen Katastrophen.
Der Grund dafür ist unbekannt.


### Bytes 0x0a bis 0x0c

Im folgenden Pseudocode gilt Ba = Das Byte bei 0x0a usw.

```
if(Ba == 1) {
  if(Bb == 0) {
    Bb = Unendlich
  }

  while(Bb > 0) {
    Springe zu Position Bc in diesem Animationsblock
    Bb--
  }
}
```


Animation darstellen
--------------------

### Grundsätzliches

Koordinatenursprung ist immer die Mitte. Das gilt für die Animationsfläche und die einzelnen Bilder, die gezeichnet werden.

Jeder Animationsblock muss über seine eigenen Parameter Buch führen. Diese sind: Position (für relative Bewegungen), aktueller Frame (für Schleifen und Verzögerungen), aktuelle Verzögerung und Schleifenposition und die Info, ob sie gerade aktiv sind oder nicht.

Die Gesamtanimation muss jeden Frame prüfen, ob die Animation noch aktiv ist. Sie wird abgeschlossen, wenn ein Animationsblock auf ein "Ende"-Bit trifft (Bit 5 in Byte 0x02 in "Animationsblöcke"), oder wenn keine Animationsblöcke mehr aktiv sind.

### Einleitende Zeichnungen

Zunächst wird der Hintergrund neu gezeichnet, sodass alles sichtbare gelöscht wird.

Es werden immer zuerst fixierte Grafiken gezeichnet, dann pausierte und dann alle anderen. Innerhalb jeder dieser drei "Gruppen" werden die Grafiken immer in der Reihenfolge ihres ersten Erscheinens gezeichnet. Wenn zwei Grafiken gleichzeitig erscheinen, wird die Grafik aus dem Animationsblock mit der kleineren Nummer zuerst gezeichnet.

Jedes Bild, dass als "fixed" markiert ist (Bit 3 in Byte 0x02 in "Animationsblöcke") und schon gezeichnet wurde, wird wieder gezeichnet. Es gibt keine Möglichkeit ein einmal fixiertes Bild wieder zu löschen, außer ein anderes Bild drüber zu zeichnen (wie der schwarze Balken über der Schrift am Q-Pop-Introanfang). Ein fixiertes Bild behält stets seine Position.

Nun werden Grafiken gezeichnet, deren Animationsblock auf "Pause" steht (Bit 5 in Byte 0x02 in "Animationsblöcke"). Wenn Grafiken nicht sichtbar sein sollen, müssen ihre Koordinaten so gewählt werden, dass sie außerhalb der Leinwand gezeichnet werden. Die gilt auch für alle Grafiken, die zu Beginn der Animation nicht unsichtbar sein sollen (z.B. der Papierflieger in Q-Pop-Introanfang).

### Bewegungen, Schleifen, Verzögerungen

Jetzt geht der eigentliche Spaß los. Die Animationsblöcke werden nacheinander geprüft.

Wenn der Block inaktiv ist (also beim letzten Frame angelangt ist), wird er übersprungen.

Wenn der Block gerade keine aktive Verzögerung hast, führe die Bewegung aus. Dazu wird die Position geändert (absolut oder relativ zur aktuellen Position je nach (Bits 1 und 2 in Byte 0x02 in "Animationsblöcke")). Ist das Bild durch eine relative Bewegung *vollständig* außerhalb der Leinwand, wird es genau auf die äußere Kante des Leinwandrands auf der *gegenüberliegenden* Seite gesetzt. Das gilt für die X- und die Y-Koordinate, aber nicht, wenn das Bild durch eine absolute Koordiante außerhalb der Leinwand gesetzt wurde. Ist der aktuelle Frame als "fixed" markiert (Bit 3 in Byte 0x02 in "Animationsblöcke"), wird das aktuelle Bild in der aktuellen Position entsprechend gespeichert. Ist der aktuelle Frame als "aktivierend" gekennzeichnet (Bytes 0x0E und 0x0F in "Animationsblöcke"), werden die entsprechenden Animationsblöcke aktiviert (also die Pause auf false gesetzt). Ist der aktuelle Frame als "beendend" markiert (Bit 4 in Byte 0x02 in "Animationsblöcke"), wird die gesamte Animation beendet.

Unabhängig, ob die Position verändert wurde oder nicht (also auch wenn der Block gerade "verzögert" ist), wird das Bild gezeichnet.

Wenn der aktuelle Block verzögert ist, wird der Verzögerungszähler dekrementiert. Wenn er nicht verzögert ist, aber als "verzögernd" gekennzeichnet (Byte 0x01 in "Animationsblöcke"), wird die Verzögerung aktiviert.

Wenn keine Verzögerung aktiv ist und eine Schleife angegeben ist (Bytes 0x0A bis 0x0C in "Animationsblöcke"), wird zu dem Schleifenziel gesprungen und der Schleifenzähler dekrementiert. Ist der Schleifenzähler bei 0 angelangt, wird die Schleife ignoriert.

Wenn der Block aktiv ist, nicht pausiert, nicht verzögert und keine Schleife aktiviert, wird der Positionszähler zum nächsten Teil des Animationsblocks inkrementiert. Wenn der letzte Teil des Blocks abgeschlossen ist, wird er als inaktiv markiert und künftig ignoriert. Es gibt keine möglichkeit, Blöcke, die an ihrem Ende angelangt sind, wieder zu aktivieren.
