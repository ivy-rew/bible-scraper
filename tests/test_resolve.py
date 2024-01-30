import unittest
import resolve
from unittest.mock import Mock

resolve = resolve;
resolve.gateway = Mock()
resolve.book = 'Genesis';
resolve.gateway.lookup.return_value = 'Im Anfang schuf Gott die Himmel und die Erde.'

class TestMarkdownResolver(unittest.TestCase):

    def test_injecctFootnotes(self):
        expaned = resolve.expandVerse('1. Himmel und Erde !V1')
        self.assertEqual(expaned, '1. Himmel und Erde [^Genesis1:1]')
        print(resolve.notes[0])
        self.assertEqual(resolve.notes[0], '[^Genesis1:1]:   > Im Anfang schuf Gott die Himmel und die Erde.  \nGenesis 1:1\n\n')

    def test_bookOfFile(self):
        self.assertEqual(resolve.bookOfFile("tests/1-genesis.md"), 'genesis')

if __name__ == '__main__':
    unittest.main()
