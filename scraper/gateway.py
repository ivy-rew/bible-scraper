import requests
from bs4 import BeautifulSoup

from scraper.BibleRef import BibleRef

def lookup(bibRef: BibleRef):
    base_url = "https://www.biblegateway.com/passage/?search="

    #translation = str(input("Please enter the translation to use.\n")).upper()
    translation = "SCH2000"
    full_url = base_url + bibRef.book + "+" + bibRef.chapter + ":" + bibRef.verse + "&version=" + translation + "&interface=print"

    page = requests.get(full_url)
    result = toPlainText(page.text)
    return result

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
    if result is None:
        return result
    return str(result.text.strip())
