#!/usr/bin/env python3
import sys
from pathlib import Path

md = sys.argv[1]
f = open(md, "r")

def bookOfFile(file):
    mdNoExt=Path(file).stem
    return mdNoExt.split("-",1)[1]

book = bookOfFile(md)
print("book="+book)



lines = f.readlines()
for line in lines:
    if line.startswith("[0-9]+\."):
        print("GOT "+line)
    print(line)
