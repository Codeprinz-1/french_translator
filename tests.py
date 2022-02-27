from translator import frenchToEnglish, englishToFrench
from unittest import TestCase

class TestFrenchToEnglish(TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(), 'Hello')
        self.assertEqual(frenchToEnglish('Hello'))

