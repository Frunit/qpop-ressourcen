Scripte
=======

Ich habe diverse Pythonscripte geschrieben, um mehr über Q-Pop zu erfahren. Ein paar dieser Scripte möchte ich hier nun teilen. Die Scripte sind im Ordner `scripte/`.

Außerdem habe ich vieles mit dem Disassembler [Semblance](https://github.com/zfigura/semblance) herausgefunden.


### all_waves_from_bundle_wave.py

Extrahiert alle Wave-Dateien aus einer Datei, die aus vielen Wave-Dateien besteht.


### average_maps.py

Liest Höhenreliefs aus Q-Pop-Speicherständen und generiert ein Bild mit drei Panelen:
- links: Durchschnittliche Höhe
- mitte: Minimale Höhe
- rechts: Maximale Höhe


### change_bin_file.py

Liest und schreibt Binärdateien. Sehr rudimentär, aber praktisch auch um Speicherstände zu manipulieren.


### extract_all_bitmaps.py

Versucht alle Bilder aus Q-Pop und Magentic Planet zu extrahieren, inklusive Multibitmaps, die in Animationen verwendet werden. Diese Datei ist sehr stark "work in progress", deswegen sind noch viele hart-kodierte Hacks und Kommentare enthalten.


### extract_pictures.py

Versucht alle .DAT-Dateien im aktuellen Ordner in png umzuwandeln.


### get_info_from_savegame.py

Liest Informationen aus Speicherstand und gibt sie auf stdout aus.
Funktioniert bisher nur für Q-Pop, nicht für Magnetic Planet!


### show_bmp_info.py

Zeigt Information über Bitmap (oder Bitmap-artige Datei).
