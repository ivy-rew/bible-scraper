class BibleRef():

    # Book name abbreviations to full names mapping
    BOOK_NAMES = {
        'gen': 'genesis', 'ge': 'genesis',
        'ex': 'exodus', 'exo': 'exodus',
        'lev': 'leviticus', 'le': 'leviticus',
        'num': 'numbers', 'nu': 'numbers',
        'deut': 'deuteronomy', 'de': 'deuteronomy',
        'jos': 'joshua', 'josh': 'joshua',
        'judg': 'judges', 'jdg': 'judges',
        'ruth': 'ruth',
        '1sam': '1 samuel', '2sam': '2 samuel',
        '1ki': '1 kings', '2ki': '2 kings',
        '1chr': '1 chronicles', '2chr': '2 chronicles',
        'ezr': 'ezra', 'neh': 'nehemiah',
        'est': 'esther',
        'job': 'job',
        'ps': 'psalms', 'psalm': 'psalms',
        'prov': 'proverbs', 'pr': 'proverbs',
        'eccl': 'ecclesiastes', 'ecc': 'ecclesiastes',
        'song': 'song of solomon', 'sos': 'song of solomon',
        'isa': 'isaiah', 'is': 'isaiah',
        'jer': 'jeremiah', 'je': 'jeremiah',
        'lam': 'lamentations', 'la': 'lamentations',
        'ezek': 'ezekiel', 'eze': 'ezekiel',
        'dan': 'daniel',
        'hos': 'hosea', 'ho': 'hosea',
        'joel': 'joel', 'jl': 'joel',
        'amos': 'amos', 'am': 'amos',
        'obad': 'obadiah', 'ob': 'obadiah',
        'jonah': 'jonah', 'jon': 'jonah',
        'mic': 'micah', 'mi': 'micah',
        'nah': 'nahum', 'na': 'nahum',
        'hab': 'habakkuk', 'ha': 'habakkuk',
        'zeph': 'zephaniah', 'zp': 'zephaniah',
        'hag': 'haggai', 'hg': 'haggai',
        'zech': 'zechariah', 'zc': 'zechariah',
        'mal': 'malachi', 'ma': 'malachi',
        'matt': 'matthew', 'mat': 'matthew',
        'mark': 'mark', 'mr': 'mark',
        'luke': 'luke', 'lk': 'luke',
        'john': 'john', 'joh': 'john',
        'acts': 'acts', 'act': 'acts',
        'rom': 'romans', 'ro': 'romans',
        '1cor': '1 corinthians', '2cor': '2 corinthians',
        '1tim': '1 timothy', '2tim': '2 timothy',
        '1pet': '1 peter', '2pet': '2 peter',
        '1john': '1 john', '2john': '2 john', '3john': '3 john',
        'jude': 'jude', 'rev': 'revelation'
    }

    def __init__(self, book, chapter, verse):
        # Store original book name for display
        self.original_book = book
        # Expand abbreviation to full name if needed
        self.book = self.BOOK_NAMES.get(book.lower(), book.lower())
        self.chapter = chapter
        self.verse = verse

    def numbers(self):
        return str(self.chapter)+':'+str(self.verse)

    def printRef(self):
        return self.original_book.capitalize() + ' ' + self.numbers()
