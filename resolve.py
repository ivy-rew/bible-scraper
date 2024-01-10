#!/usr/bin/env python3
import sys
from pathlib import Path
import re

md = sys.argv[1]
f = open(md, "r")

def bookOfFile(file):
    mdNoExt=Path(file).stem
    return mdNoExt.split("-",1)[1]

book = bookOfFile(md)
print("book="+book)

# https://docs.python.org/3/library/re.html
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match
m.group(1)       # The first parenthesized subgroup.
m.group(2)       # The second parenthesized subgroup.
m.group(1, 2)    # Multiple arguments give us a tuple.


lines = f.readlines()
for line in lines:
    if line.startswith("[0-9]+\."):
        print("GOT "+line)
    print(line)
