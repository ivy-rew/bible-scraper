#!/usr/bin/env python3
import unittest
from scraper.gateway import parseRev

class TestBibleRefAbbreviations(unittest.TestCase):

    def test_parseRev(self):
        """Test that parseRev correctly extracts the book name from HTML"""
        html = '<div class="bcv">Johannes 3:16</div>'
        result = parseRev(html)
        self.assertEqual(result, "Johannes 3:16")

if __name__ == '__main__':
    unittest.main()