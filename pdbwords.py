#!/usr/bin/env python

# By Kresten Lindorff-Larsen, University of Copenhagen, 2015

import sys
import os

LETTERDIR="letters"
MAXCHARS=25
LINEBREAK="xLBx"

def letter_to_fn(letter):
    if letter==".": letter="stop"
    if letter=="!": letter="exclamation"
    if letter=="?": letter="question"
    if letter==",": letter="comma"
    if letter==":": letter="colon"
    if letter=="-": letter="hyphen"
    letter_fn=LETTERDIR+"/"+letter.lower()+".jpg"
    if os.path.isfile(letter_fn):
        return letter_fn
    else:
        sys.stderr.write("I don't know the letter %s so I am replacing it with a space" % letter)
        letter="_"
        letter_fn=LETTERDIR+"/"+letter.lower()+".jpg"
        return letter_fn


def add_letter(letter, image_fn):
    letter_fn=letter_to_fn(letter)
    tmp_fn="tmp.jpg"
    cmd="convert +append %s %s %s" % (image_fn, letter_fn, tmp_fn) 
    os.system(cmd)
    cmd="mv %s %s" %(tmp_fn, image_fn)
    os.system(cmd)

def make_empty_image(image_fn):
    cmd="rm %s" % (image_fn) 
    os.system(cmd)
    cmd="touch %s" % (image_fn) 
    os.system(cmd)

def add_space(image_fn):
    letter="_"
    add_letter(letter, image_fn)

def line_to_image(line, fn):
    make_empty_image(fn)
    for word in line:
        for letter in word:
            add_letter(letter, fn)
        if word!=line[-1]:
            add_space(fn)

def words_to_lines(words):
    lines=[]
    line=[]
    chars_in_line=0
    for word in words:
        if word==LINEBREAK:
            lines.append(line)
            line=[]
            chars_in_line=0
        elif chars_in_line+len(word)+1<MAXCHARS:
            line.append(word)
            chars_in_line+=len(word)
        else:
            lines.append(line)
            line=[word]
            chars_in_line=len(word)
    if len(line)>0:
        lines.append(line)
    return lines

def make_image(lines, image_fn):
    for i,line in enumerate(lines):
        line_fn="line%02d.jpg" % i
        line_to_image(line, line_fn)

    make_empty_image(image_fn)
    tmp_fn="tmp.jpg"
    for i,line in enumerate(lines):
        line_fn="line%02d.jpg" % i
        cmd="convert -append %s %s %s" % (image_fn, line_fn, tmp_fn) 
        os.system(cmd)
        cmd="mv %s %s" %(tmp_fn, image_fn)
        os.system(cmd)
        cmd="rm %s" %(line_fn)
        os.system(cmd)

if __name__ == '__main__':
    words=sys.argv[1:]
    lines=words_to_lines(words)
    make_image(lines, "proteinword.jpg")


