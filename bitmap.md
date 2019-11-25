Technische Übersicht Bitmaps
============================

Bitmaps sind eher einfach aufgebaut. Eine gute Übersicht gibt es in der Englischen [Wikipedia](https://en.wikipedia.org/wiki/BMP_file_format). Ich habe versucht, den Aufbau von Bitmaps hier zusammenzufassen. Eine Bitmap besteht normalerweise aus einem Bitmap Header, einem DIB-Header, einer Palette (wenn 1, 4 oder 8 bit pro Pixel) und den eigentlichen Bildinformationen.

Die Offsets sind hier immer von Beginn des jeweiligen Abschnitts angegeben. Alle Zahlen sind *[little endian](https://de.wikipedia.org/wiki/Byte-Reihenfolge)*.

In Q-Pop haben manche Bilder einen Bitmap Header, manche fangen direkt mit dem DIB-Header an. BX-Bitmaps wurden mit Take One (siehe [Animationen](animationen.md)) erstellt und enthalten mehrere Bilder, die in einer Animation verwendet werden. Der Aufbau folgt einer normalen Bitmap mit dem Bitmap-Header, DIB-Header und der Palette. Danach folgt ein Take-One-spezifischer Header, der 20 Byte pro enthaltenem Bild groß ist. Danach folgen die Bildinformationen für jedes Bild der Animation (jedes Frames).


Bitmap Header
-------------

Der Bitmap-Header ist immer 14 Byte groß.

Adresse | Länge (Byte) | Beschreibung
--------|--------------|-------------
0x0 | 2 | **BM** als Indikator für den Start. In Q-Pop ist dies oft **BX** (für Animationsbitmaps) oder **QP**.
0x2 | 4 | Totale Dateigröße in Byte
0x6 | 4 | Reserviert (nicht benutzt)
0xa | 4 | Offset (in Byte) bis zum Beginn der Bildinformationen


device-independent Bitmap (DIB) Header
--------------------------------------

Der DIB-Header kann je nach Version unterschiedlich groß sein, ist bei Q-Pop aber immer 40 Byte groß.

Adresse | Länge (Byte) | Beschreibung
--------|--------------|-------------
0x0 | 4 | Größe des DIB-Headers (bei Q-Pop immer 40 Byte)
0x4 | 4 | Bildbreite in Pixel
0x8 | 4 | Bildhöhe in Pixel
0xc | 2 | Bildebenen; ist immer 1
0xe | 2 | Bit pro pixel (bei Q-Pop 1, 4 oder 8)
0x10 | 4 | Bildkompression (siehe unten)
0x14 | 4 | Bildgröße in Bytes ohne Header (Breite x Höhe x BitProPixel/8)
0x18 | 4 | horizontale Auflösung; bei Q-Pop immer 0
0x1c | 4 | vertikale Auflösung; bei Q-Pop immer 0
0x20 | 4 | Anzahl Farben in Palette (wenn 0, dann 2^BitProPixel)
0x24 | 4 | “Wichtige” Farben; bei Q-Pop immer 0


Bildkompressionswerte in Q-Pop:

- 0: Keine Kompression
- 1: Lauflängenenkodiert für Bilder mit 8 bit pro Pixel
- 2: Lauflängenenkodiert für Bilder mit 4 bit pro Pixel


Palette
-------

Die Farbpalette definiert die Farben im Bild. Jede Farbe belegt vier Byte. Die ersten drei Byte stehen für Rot, Grün und Blau. Das vierte Byte ist 0. In den Pixelinformationen kann dann einfach auf die Position in der Palette verwiesen werden, was ein Byte (bei 8 Bit pro Pixel) oder ein halbes Byte (bei 4 Bit pro Pixel) kostet.

Die Palette wird mit 00 aufgefüllt, bis die Adresse auf 0 endet.


BX-Header
---------

Dieser Header ist nur in Multibitmaps vorhanden. Diese Dateien werden in Take1-Animationen verwendet. Er ist 20 * anzahl_der_grafiken Bytes groß. Für jede Grafik ist der Header wie folgt:

Adresse | Länge (Byte) | Beschreibung
--------|--------------|-------------
0x0  |  1 | Immer 0x00
0x1  |  2 | Anzahl der Bytes für dieses Bild
0x3  |  2 | Immer 0x00 0x00
0x5  | 10 | Der String "BILD%D.BMP"
0xf  |  3 | immer 0x00 0x00 0x00
0x12 |  1 | **Unbekannt.** Entweder 0, 1 oder 2. 1 Kommt mit Abstand am häufigsten vor.
0x13 |  1 | Immer 0x00


Pixelinformationen
------------------

Je nach Bit pro Pixel und Kompression sind die Informationen hier unterschiedlich. Im einfachsten Fall (8 Bit pro Pixel, keine Kompression) folgen hier Breite x Höhe Byte, wobei jedes Byte auf eine Position in der Palette verweist. Bitmaps werden (zumindest bei Q-Pop) von unten links horizontal nach oben rechts aufgebaut.
