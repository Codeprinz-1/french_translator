from translator import frenchToEnglish, englishToFrench
from unittest import TestCase

class TestFrenchToEnglish(TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish(), 'Hello')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestEnglishToFrench(TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench(), 'Bonjour')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')