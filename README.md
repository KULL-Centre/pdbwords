## ABOUT ##
pdbwords was written by Kresten Lindorff-Larsen, University of Copenhagen, in 2015.

I cannot guarantee that your eyes will not start to bleed if you read the code.

The main ingredient of pdbwords is a protein alphabet, developed by Mark Howarth:
http://www.bioch.ox.ac.uk/howarth/alphabet.htm

The python code is distributed under GNU General Public License v3.0

## THIS IS HOW YOU RUN PDB WORDS ##
./pdbwords.py Just write your text here to set it in PDBWORDS

## Requirements ##
The code is essentially a wrapper for ImageMagick, which needs to be installed separately; see
http://www.imagemagick.org

I have only tested the code under macOS

## More information ##
Currently the letters A-Z can be used, and it is also possible to use . , ! ? :

All letters will be set as uppercase letters, but you can input as either lower or upper.

Every unknown characters will be set as a space.

Lines will be broken up so that there are no more than MAXCHARS (hardcoded in script) characters on each line. If you want to force a line break, just write xLBx as a (case sensitive) word (again, hardcoded in LINEBREAK in script).

The two last features makes the following hack work to insert blank lines xLBx @ xLBx (which forces a line break, then the @ is converted to a space (it is unknown) and then a new linebreak. Not elegant, but it works.

## Background ##
The letters were mostly discovered by Mark Howarth and are described in a paper:
http://www.nature.com/nsmb/journal/v22/n5/full/nsmb.3011.html
and a website:
http://www.bioch.ox.ac.uk/howarth/alphabet.htm
