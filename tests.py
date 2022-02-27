import unittest
from translator import frenchToEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish(), 'Hello')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench(), 'Bonjour')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

unittest.main()