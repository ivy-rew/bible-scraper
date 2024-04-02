from scraper import gateway


import re

from scraper.BibleRef import BibleRef


class MdExpand():
    
    book = "";
    chapter = "";

    def __init__(self):
        self.notes = []

    def verseInject(self, m):
        verseChap = MdExpand.chapter
        verseChap = m.group(1)
        bRef = BibleRef(MdExpand.book, verseChap, m.group(5))
        if m.group(4): # full-reference to other book
            fullRefMatcher = re.match("([0-9_]*[A-za-z]+)([0-9]+):", str(m.group(4)))
            if fullRefMatcher:
                bRef = BibleRef(fullRefMatcher.group(1), fullRefMatcher.group(2), m.group(5))
        quote=gateway.lookup(bRef)
        if quote is None:
            print("gateway lookup failed for "+bRef.printRef())
            return m.group(0)
        indent = "   > "
        if m.group(3) == '!!': # full-quote; inlined
            br = "  "
            indent = " " + indent # 4whitspaces: in-between list content!
            mdQuote = indent+str(quote)+br+"\n"+bRef.printRef()
            return m.group(1)+m.group(2)+ '\n\n' + mdQuote + br + '\n'
        else: # footnote
            foot = "[^"+bRef.book + bRef.numbers()+"]"
            mdQuote = indent+str(quote)+"  "+"\n"+bRef.printRef()
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
    


