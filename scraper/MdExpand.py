from scraper import gateway


import re

from scraper.BibleRef import BibleRef


class MdExpand():
    
    book = "";

    def __init__(self):
        self.notes = []

    def verseInject(self, bRef: BibleRef, quote, inline):
        indent = "   > "
        if inline: # full-quote; inlined
            br = "  "
            indent = " " + indent # 4whitspaces: in-between list content!
            mdQuote = indent+str(quote)+br+"\n"+bRef.printRef()
            return '\n\n' + mdQuote + br + '\n'
        else: # footnote
            foot = "[^"+bRef.book + bRef.numbers()+"]"
            mdQuote = indent+str(quote)+"  "+"\n"+bRef.printRef()
            self.notes.append(foot+":"+mdQuote+"\n")
            return foot

    def expandVerse(self, line):
        versPattern = "(\\!+)V([_0-9A-Za-z]+:)?([0-9\\-]+)"
        replaced = line
        matched = True
        while matched:
            incoming = replaced
            self.line = incoming
            replaced = re.sub(versPattern, self.expandVerseChap, incoming)
            matched = replaced != incoming
        return replaced

    def expandVerseChap(self, m):
        verse = m.group(3)
        bRef = BibleRef("", "", "")
        if m.group(2): # full-reference to other book
            fullRefMatcher = re.match("([0-9_]*[A-za-z]+)([0-9]+):", str(m.group(2)))
            if fullRefMatcher:
                bRef = BibleRef(fullRefMatcher.group(1), fullRefMatcher.group(2), verse)
        else:
            listMatch = re.match("^([0-9]+)(\\. [^!]+)", self.line)
            if (listMatch.group(1)):
                chapter = listMatch.group(1)
                bRef = BibleRef(MdExpand.book, chapter, verse)
        if (bRef.book != ""):
            quote=gateway.lookup(bRef)
            if quote is None:
                print("gateway lookup failed for "+bRef.printRef())
                return m.group(0)
            inline = m.group(1) == '!!'
            return self.verseInject(bRef, quote, inline)
        return m.group(0)    


