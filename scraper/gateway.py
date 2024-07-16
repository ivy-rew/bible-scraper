import requests
from bs4 import BeautifulSoup

from scraper.BibleRef import BibleRef

plain=True

def lookup(bibRef: BibleRef):
    html = lookupHtml(bibRef)
    result = render(html, plain)
    return result

def lookupHtml(bibRef: BibleRef):
    base_url = "https://www.biblegateway.com/passage/?search="
    if plain:
        print("lookup "+str(bibRef.printRef()))
    translation = "SCH2000"
    full_url = base_url + bibRef.book + "+" + bibRef.chapter + ":" + bibRef.verse + "&version=" + translation + "&interface=print"

    page = requests.get(full_url)
    return page.text

def render(html, plain:bool):
    soup = BeautifulSoup(html, "lxml")

    foot = soup.findAll(class_="footnotes")
    [line.extract() for line in foot]
    footRef = soup.findAll(class_="footnote")
    [no.extract() for no in footRef]

    h2 = soup.findAll("h2")
    [line.extract() for line in h2]

    h3 = soup.findAll("h3")
    [line.extract() for line in h3]

    chapNos = soup.findAll(class_="chapternum")
    [no.extract() for no in chapNos]

    link = soup.find_all(class_="full-chap-link")
    [l.extract() for l in link]

    if (plain):
        sup = soup.findAll("sup")
        [note.extract() for note in sup]

    result = soup.find(class_="text-html")
    if result is None:
        return result
    if (plain):
        return str(result.text.strip())
    
    return str(result);
