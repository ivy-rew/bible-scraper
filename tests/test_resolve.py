import unittest
import scraper.resolve as resolve
from unittest.mock import Mock

resolve = resolve;
resolve.gateway = Mock()
resolve.book = 'Genesis';
resolve.gateway.lookup.return_value = 'Im Anfang schuf Gott die Himmel und die Erde.'

class TestMarkdownResolver(unittest.TestCase):

    def test_injectFootnotes_single(self):
        expander = resolve.MdExpand()
        expaned = expander.expandVerse('1. Himmel und Erde !V1')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1]')
        print(expander.notes[0])
        self.assertEqual(expander.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_injectFootnotes_multiple(self):
        expander = resolve.MdExpand()
        expaned = expander.expandVerse('1. Himmel und Erde !V1 !V3')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1] [^Genesis1:3]')
        print(expander.notes[0])
        self.assertEqual(expander.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_injectFootnotes_fullRefOtherBook(self):
        expander = resolve.MdExpand()
        expaned = expander.expandVerse('1. Himmel !VExodus30:12 und !V2. Erde !V1')
        self.assertEqual(expaned, '1. Himmel [^Exodus30:12] und [^Genesis1:2]. Erde [^Genesis1:1]')
        print(expander.notes[0])

    def test_fullQuote(self):
        expander = resolve.MdExpand()
        expaned = expander.expandVerse('1. Himmel und Erde !!V1')
        self.assertEqual(expaned, '1. Himmel und Erde \n\n    > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1  \n')

    def test_bookOfFile(self):
        self.assertEqual(resolve.bookOfFile("tests/1-genesis.md"), 'genesis')

    def test_fileInject(self):
        md = resolve.MdFile("tests/1-genesis.md")
        doc = resolve.MdDoc(md.read())
        doc.refsReplace()
        expect = resolve.MdFile("tests/1-genesis-resolved.md")
        
        expLines = expect.read()
        self.assertEqual(doc.lines[0], expLines[0])
        self.assertEqual(doc.lines[1], expLines[1])
        self.assertEqual(doc.lines[2], expLines[2])
        #self.assertEqual(doc.lines[3], expLines[3])
        self.assertEqual(doc.lines[4], expLines[4])
        #self.assertEqual(doc.lines[5], expLines[5])


if __name__ == '__main__':
    unittest.main()
