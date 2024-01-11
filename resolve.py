#!/usr/bin/env python3
import sys, re
from pathlib import Path
import gateway

md = sys.argv[1]
f = open(md, "r")

def bookOfFile(file):
    mdNoExt=Path(file).stem
    return mdNoExt.split("-",1)[1]

book = bookOfFile(md)
print("book="+book)


def findRef(line):
    # https://docs.python.org/3/library/re.html
    m = re.match("([0-9])+\\. .+ !V([0-9\\-]+)", line) #"1. test !V19"
    if m:
        ref=m.group(1)+":"+m.group(2)
        return ref;

lines = f.readlines()
for line in lines:
    ref = findRef(line)
    if ref:
        quote=gateway.lookup(book, ref)
        indent = "\n    > "
        mdQuote = indent+str(quote)+indent+book.capitalize()+" "+ref
        print(line + mdQuote)
    else:
        print(line)
    #print(line)
