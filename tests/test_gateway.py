import unittest
import scraper.gateway

class TestHtmlParser(unittest.TestCase):

    def test_gateway_parse(self):
        with open('tests/genesis1-1.html', 'r') as file:
            html = file.read(); #.replace('\n', '')
        result = scraper.gateway.toPlainText(html)
        self.assertEqual(result, 'Im Anfang schuf Gott die Himmel und die Erde.')

if __name__ == '__main__':
    unittest.main()
