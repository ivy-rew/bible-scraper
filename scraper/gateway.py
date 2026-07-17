import requests
from bs4 import BeautifulSoup

from scraper.BibleRef import BibleRef

plain=True

def lookup(bibRef: BibleRef):
    html = lookupHtml(bibRef)
    result = render(html, plain)
    return result

def lookupHtml(bibRef: BibleRef):
    # Use biblegateway.com as primary source (reliable API)
    base_url = "https://www.biblegateway.com/passage/?search="
    if plain:
        print("lookup "+str(bibRef.printRef()))
    translation = "SCH2000"
    full_url = base_url + bibRef.book + "+" + bibRef.chapter + ":" + bibRef.verse + "&version=" + translation + "&interface=print"

    page = requests.get(full_url)
    
    # Parse book name from HTML response
    soup = BeautifulSoup(page.text, "lxml")
    title_tag = soup.find("title")
    if title_tag:
        title_text = title_tag.get_text()
        # Extract book name from title (format: "Book Chapter:Verse Translation - ...")
        # Example: "Genesis 1:1 SCH2000 - Die Urzeit: Von der Schöpfung bis - Bible Gateway"
        import re
        title_match = re.match(r'^([A-Za-z\s]+)\s+\d+:\d+\s+', title_text)
        if title_match:
            parsed_book = title_match.group(1).strip()
            # Update the BibleRef object with the parsed book name for display
            bibRef.book = parsed_book
            bibRef.original_book = parsed_book
    
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
        return ""
    if (plain):
        return str(result.text.strip())
    
    return str(result);
