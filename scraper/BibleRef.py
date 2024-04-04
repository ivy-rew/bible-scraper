class BibleRef():

    def __init__(self, book, chapter, verse):
        self.book = book
        self.chapter = chapter
        self.verse = verse

    def numbers(self):
        return str(self.chapter)+':'+str(self.verse)

    def printRef(self):
        return self.book.capitalize() + ' ' + self.numbers()
