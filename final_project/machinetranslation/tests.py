import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrenchEqual(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestenglishToFrenchNotEqual(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench("Hello"),"Oui")

class TestfrenchToEnglishEqual(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

class TestfrenchToEnglishNotEqual(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"),"Goodbye")

unittest.main()
