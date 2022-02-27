import unittest
from translator import frenchToEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish('null'), 'Hello')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench('null'), 'Bonjour')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

unittest.main()