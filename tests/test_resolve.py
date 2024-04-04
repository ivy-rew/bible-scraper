import unittest
import scraper.resolve as resolve
import scraper.MdExpand as MdExpand
from unittest.mock import Mock

exDef = MdExpand
exDef.MdExpand.book = 'Genesis';
exDef.gateway = Mock()
exDef.gateway.lookup.return_value = 'Im Anfang schuf Gott die Himmel und die Erde.'

class TestMarkdownResolver(unittest.TestCase):

    def test_injectFootnotes_single(self):
        expander = exDef.MdExpand()
        expaned = expander.expandVerse('1. Himmel und Erde !V1')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1]')
        print(expander.notes[0])
        self.assertEqual(expander.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_injectFootnotes_multiple(self):
        expander = exDef.MdExpand()
        expaned = expander.expandVerse('1. Himmel und Erde !V1 !V3')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1] [^Genesis1:3]')
        print(expander.notes[0])
        self.assertEqual(expander.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_injectFootnotes_fullRefOtherBook(self):
        expander = exDef.MdExpand()
        expaned = expander.expandVerse('1. Himmel !VExodus30:12 und !V2. Erde !V1')
        self.assertEqual(expaned, '1. Himmel [^Exodus30:12] und [^Genesis1:2]. Erde [^Genesis1:1]')
        print(expander.notes[0])

    def test_fullQuote(self):
        expander = exDef.MdExpand()
        expaned = expander.expandVerse('1. Himmel und Erde !!V1')
        self.assertEqual(expaned, '1. Himmel und Erde \n\n    > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1  \n')

    def test_injectFootnotes_freeStyleDoc(self):
        expander = exDef.MdExpand()
        expaned = expander.expandVerse('Himmel und Erde !VGenesis1:1')
        self.assertEqual(expaned, 'Himmel und Erde [^Genesis1:1]')
        self.assertEqual(expander.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_bookOfFile(self):
        self.assertEqual(resolve.bookOfFile("tests/1-genesis.md"), 'genesis')

    def test_fileInject(self):
        md = resolve.MdFile("tests/1-genesis.md")
        doc = resolve.MdDoc(md.read())
        doc.refsReplace()
        actual = sanitize(doc.lines)
        expect = resolve.MdFile("tests/1-genesis-resolved.md")
        expLines = expect.read()
        self.assertEqual(actual, expLines)

    def test_fileInject_freeStyleDoc(self):
        md = resolve.MdFile("tests/2-exodus.md")
        doc = resolve.MdDoc(md.read())
        doc.refsReplace()
        actual = sanitize(doc.lines)
        expect = resolve.MdFile("tests/2-exodus-resolved.md")
        expLines = expect.read()
        self.assertEqual(actual, expLines)

if __name__ == '__main__':
    unittest.main()

def sanitize(lines):
    all = ''.join(lines)
    return all.splitlines(keepends=True)