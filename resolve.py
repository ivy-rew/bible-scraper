#!/usr/bin/env python3
import sys, re
from pathlib import Path
import gateway

style = 'inline' # or 'notes'
notes = []


def bookOfFile(file):
    mdNoExt=Path(file).stem
    return mdNoExt.split("-",1)[1]

def verseInject(m):
    ref=m.group(1)+":"+m.group(3)
    quote=gateway.lookup(book, ref)
    indent = "   > "
    foot = "[^"+book+ref+"]"
    mdQuote = indent+str(quote)+"  "+"\n"+book.capitalize()+" "+ref
    notes.append(foot+":"+mdQuote+"\n\n")
    return m.group(1)+m.group(2) + foot

def expandVerse(line):
    replaced = line
    matched = True
    while matched:
        incoming = replaced
        replaced = re.sub("([0-9]+)(\\. .+)!V([0-9\\-]+)", verseInject, incoming, flags=re.IGNORECASE)
        matched = replaced != incoming
    return replaced

def findRef(line):
    # https://docs.python.org/3/library/re.html
    m = re.match("(([0-9])+\\. .+) !V([0-9\\-]+)", line) #"1. test !V19"
    if m:
        ref=m.group(1)+":"+m.group(2)
        return ref;

def mdRefsReplace(mdPath):
    with open(mdPath, 'r') as file:
        lines = []
        for line in file.readlines():
            lines.append(expandVerse(line))
        return lines

def write(mdPath, lines):
    with open(mdPath, 'w', encoding='utf-8') as file: 
        file.writelines(lines) 

#print(expandVerse('1. test !V19'))
if len(sys.argv) > 1:
    mdPath = sys.argv[1]
    book = bookOfFile(mdPath)
    lines = mdRefsReplace(mdPath)
    lines += notes;

    if len(sys.argv) > 2 and sys.argv[2] == "-i":
        write(mdPath,lines)
    else:
        for line in lines:
            print(line)