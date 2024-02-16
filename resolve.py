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
    verseBook = book
    ref=m.group(1)+":"+m.group(5)
    if m.group(4): # full-reference to other book
        fullRefMatcher = re.match("([0-9_]*[A-za-z]+)([0-9]+):", str(m.group(4)))
        if fullRefMatcher:
            verseBook = fullRefMatcher.group(1)
            ref = fullRefMatcher.group(2)+":"+m.group(5)
    quote=gateway.lookup(verseBook, ref)
    if quote is None:
        print("gateway lookup failed for "+verseBook+" "+ref)
        return m.group(0)
    indent = "   > "
    if m.group(3) == '!!': # full-quote; inlined
        br = "  "
        indent = " " + indent # 4whitspaces: in-between list content!
        mdQuote = indent+str(quote)+br+"\n"+verseBook.capitalize()+" "+ref
        return m.group(1)+m.group(2)+ '\n\n' + mdQuote + br + '\n'
    else: # footnote
        foot = "[^"+verseBook+ref+"]"
        mdQuote = indent+str(quote)+"  "+"\n"+verseBook.capitalize()+" "+ref
        notes.append(foot+":"+mdQuote+"\n")
        return m.group(1)+m.group(2) + foot

def expandVerse(line):
    replaced = line
    matched = True
    while matched:
        incoming = replaced
        replaced = re.sub("^([0-9]+)(\\. [^!]+)(\\!+)V([_0-9A-Za-z]+:)?([0-9\\-]+)", verseInject, incoming, flags=re.IGNORECASE | re.MULTILINE)
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
    if (len(notes) > 0):
        lines += '\n'
    lines += notes;

    if len(sys.argv) > 2 and sys.argv[2] == "-i":
        write(mdPath,lines)
    else:
        for line in lines:
            print(line)