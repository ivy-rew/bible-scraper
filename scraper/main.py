#!/usr/bin/env python3
import sys
from scraper import gateway
from scraper.BibleRef import BibleRef

if len(sys.argv) > 1:
    book = sys.argv[1];
else:
    book = str(input("Please enter a the book.\n"))

if len(sys.argv) > 2:
    chapter_num = sys.argv[2];
else:
    chapter_num = str(input("Please enter a chapter no.\n"))

if len(sys.argv) > 3:
    verse_num = sys.argv[3];
else:
    verse_num = str(input("Please enter a verse to fetch.\n"))

ref=chapter_num;
ref=ref+ ":" +verse_num

#print("verse="+str(result.prettify()))
result = gateway.lookup(BibleRef(book, chapter_num, verse_num))

print(result+"  ")
print(book.capitalize()+" "+ref)