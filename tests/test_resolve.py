import unittest
import resolve
from unittest.mock import Mock

resolve = resolve;
resolve.gateway = Mock()
resolve.book = 'Genesis';
resolve.gateway.lookup.return_value = 'Im Anfang schuf Gott die Himmel und die Erde.'

class TestMarkdownResolver(unittest.TestCase):

    def test_injectFootnotes_single(self):
        resolve.notes = []
        expaned = resolve.expandVerse('1. Himmel und Erde !V1')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1]')
        print(resolve.notes[0])
        self.assertEqual(resolve.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_injectFootnotes_multiple(self):
        resolve.notes = []
        expaned = resolve.expandVerse('1. Himmel und Erde !V1 !V3')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1] [^Genesis1:3]')
        print(resolve.notes[0])
        self.assertEqual(resolve.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n')

    def test_fullQuote(self):
        resolve.notes = []
        expaned = resolve.expandVerse('1. Himmel und Erde !!V1')
        self.assertEqual(expaned, '1. Himmel und Erde \n\n   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1  \n')

    def test_bookOfFile(self):
        self.assertEqual(resolve.bookOfFile("tests/1-genesis.md"), 'genesis')

if __name__ == '__main__':
    unittest.main()
