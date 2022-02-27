import unittest
from final_project.machinetranslation.translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('null'), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('null'), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

unittest.main()