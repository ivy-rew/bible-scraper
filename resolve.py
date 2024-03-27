#!/usr/bin/env python3
import sys, re
from pathlib import Path
import gateway

style = 'inline' # or 'notes'

class MdExpand():

    def __init__(self):
        self.notes = []
    
    def verseInject(self, m):
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
            self.notes.append(foot+":"+mdQuote+"\n")
            return m.group(1)+m.group(2) + foot

    def expandVerse(self, line):
        replaced = line
        matched = True
        while matched:
            incoming = replaced
            replaced = re.sub("^([0-9]+)(\\. [^!]+)(\\!+)V([_0-9A-Za-z]+:)?([0-9\\-]+)", 
                self.verseInject, incoming, flags=re.IGNORECASE | re.MULTILINE)
            matched = replaced != incoming
        return replaced


class MdDoc():

    def __init__(self, lines):
        self.lines = lines

    def refsReplace(self):
        lines = []
        expander = MdExpand(self)
        for line in self.lines:
            lines.append(expander.expandVerse(line))
        self.lines = lines
        if (len(expander.notes) > 0):
            self.lines += '\n'
        self.lines += expander.notes;


class MdFile():

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as file:
            return file.readlines();
        
    def write(self, lines):
        with open(self.path, 'w', encoding='utf-8') as file: 
            file.writelines(lines)


def bookOfFile(file):
    mdNoExt=Path(file).stem
    splitted = mdNoExt.split("-",1)
    if len(splitted) > 1:
        return splitted[1]
    else:
        return ""


#print(expandVerse('1. test !V19'))
if len(sys.argv) > 1:
    mdPath = sys.argv[1]
    book = bookOfFile(mdPath)
    mdFile = MdFile(mdPath)
    doc = MdDoc(mdFile.read())    
    doc.refsReplace()

    if len(sys.argv) > 2 and sys.argv[2] == "-i":
        mdFile.write(doc.lines)
    else:
        for line in doc.lines:
            print(line)
