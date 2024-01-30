import unittest
import gateway

class TestStringMethods(unittest.TestCase):

    def test_gateway_parse(self):
        with open('tests/genesis1-1.html', 'r') as file:
            html = file.read(); #.replace('\n', '')
        result = gateway. toPlainText(html)
        clean = str(result.text.strip())
        self.assertEqual(clean, 'Im Anfang schuf Gott die Himmel und die Erde.')

if __name__ == '__main__':
    unittest.main()