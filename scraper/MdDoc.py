from scraper.MdExpand import MdExpand


class MdDoc():

    def __init__(self, lines):
        self.lines = lines

    def refsReplace(self):
        lines = []
        expander = MdExpand()
        for line in self.lines:
            lines.append(expander.expandVerse(line))
        if (len(expander.notes) > 0):
           lines += '\n'
        self.lines = lines
        self.lines += expander.notes

    def print(self):
        for line in self.lines:
            print(line)