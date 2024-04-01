#!/usr/bin/env python3
import sys, re
from pathlib import Path
from scraper import gateway
from scraper.MdDoc import MdDoc
from scraper.MdFile import MdFile
from scraper.MdExpand import MdExpand


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
    MdExpand.book = bookOfFile(mdPath)
    mdFile = MdFile(mdPath)
    doc = MdDoc(mdFile.read())
    doc.refsReplace()

    if len(sys.argv) > 2 and sys.argv[2] == "-i":
        mdFile.write(doc.lines)
    else:
        doc.print()
