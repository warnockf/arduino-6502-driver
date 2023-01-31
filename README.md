ca65 osi_bas.s -o osi_bas.o -l osi_bas.lst --feature force_range
ld65 -C osi_bas.cfg osi_bas.o -o osi_bas.bin
xxd -i mem.hex mem.c