#!/usr/bin/env python3
import unittest
from scraper.BibleRef import BibleRef

class TestBibleRefAbbreviations(unittest.TestCase):
    
    def test_full_book_name(self):
        """Test that full book names work"""
        ref = BibleRef("john", "3", "16")
        self.assertEqual(ref.book, "john")
        self.assertEqual(ref.original_book, "john")
    
    def test_abbreviated_book_name(self):
        """Test that abbreviated book names are expanded"""
        ref = BibleRef("joh", "3", "16")
        self.assertEqual(ref.book, "john")
        self.assertEqual(ref.original_book, "joh")
    
    def test_case_insensitive_abbreviation(self):
        """Test that abbreviations work regardless of case"""
        ref1 = BibleRef("JOH", "3", "16")
        ref2 = BibleRef("Joh", "3", "16")
        ref3 = BibleRef("joh", "3", "16")
        
        self.assertEqual(ref1.book, "john")
        self.assertEqual(ref2.book, "john")
        self.assertEqual(ref3.book, "john")
    
    def test_other_abbreviations(self):
        """Test other common abbreviations"""
        ref1 = BibleRef("gen", "1", "1")
        ref2 = BibleRef("ex", "1", "1")
        ref3 = BibleRef("ps", "23", "1")
        ref4 = BibleRef("isa", "53", "1")
        
        self.assertEqual(ref1.book, "genesis")
        self.assertEqual(ref2.book, "exodus")
        self.assertEqual(ref3.book, "psalms")
        self.assertEqual(ref4.book, "isaiah")
    
    def test_unknown_abbreviation(self):
        """Test that unknown abbreviations are kept as-is"""
        ref = BibleRef("unknown", "1", "1")
        self.assertEqual(ref.book, "unknown")
        self.assertEqual(ref.original_book, "unknown")
    
    def test_printRef_with_abbreviation(self):
        """Test that printRef works correctly with abbreviations"""
        ref = BibleRef("joh", "3", "16")
        self.assertEqual(ref.printRef(), "Joh 3:16")
    
    def test_numbers_method(self):
        """Test the numbers method"""
        ref = BibleRef("joh", "3", "16")
        self.assertEqual(ref.numbers(), "3:16")

if __name__ == '__main__':
    unittest.main()