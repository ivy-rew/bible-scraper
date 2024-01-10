#!/usr/bin/env python3
import requests
import sys
from contextlib import closing
from bs4 import BeautifulSoup

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

def gateway(book, ref):
    base_url = "https://www.biblegateway.com/passage/?search="

    #translation = str(input("Please enter the translation to use.\n")).upper()
    translation = "SCH2000"
    full_url = base_url + book + "+" + ref + "&version=" + translation

    page = requests.get(full_url)
    return toPlainText(page.text)

def toPlainText(html):
    soup = BeautifulSoup(html, "lxml")

    foot = soup.findAll(class_="footnotes")
    [line.extract() for line in foot]

    h2 = soup.findAll("h2")
    [line.extract() for line in h2]

    h3 = soup.findAll("h3")
    [line.extract() for line in h3]

    sup = soup.findAll("sup")
    [note.extract() for note in sup]

    chapNos = soup.findAll(class_="chapternum")
    [no.extract() for no in chapNos]

    link = soup.find_all(class_="full-chap-link")
    [l.extract() for l in link]

    result = soup.find(class_="text-html")
    return result

#print("verse="+str(result.prettify()))
result = gateway(book, ref)

print(str(result.text.strip())+"  ")
print(book.capitalize()+" "+ref)