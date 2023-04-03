import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):

    def test_englishToFrench(self):
        # Test translation of 'Hello'
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # Test translation of 'Good morning'
        self.assertEqual(englishToFrench('Good morning'), 'Bonjour')

    def test_frenchToEnglish(self):
        # Test translation of 'Bonjour'
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # Test translation of 'Bonne nuit'
        self.assertEqual(frenchToEnglish('Bonne nuit'), 'Good night')

    def test_null_input(self):
        # Test for null input for englishToFrench
        self.assertEqual(englishToFrench(None), None)
        # Test for null input for frenchToEnglish
        self.assertEqual(frenchToEnglish(None), None)

if __name__ == '__main__':
    unittest.main()