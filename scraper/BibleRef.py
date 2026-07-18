class BibleRef():

    def __init__(self, book, chapter, verse):
        # Store original book name for display
        self.original_book = book
        self.book_full = book
        self.chapter = chapter
        self.verse = verse

    def numbers(self):
        return str(self.chapter)+':'+str(self.verse)

    def printRef(self):
        return self.original_book.capitalize() + ' ' + self.numbers()
