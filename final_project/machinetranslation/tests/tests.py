import unittest
from translator import french_to_english, english_to_french

class Teste2F(unittest.TestCase):
    def test1(self):
       self.assertEqual(english_to_french('Hello'),'Bonjour')
       self.assertIsNotNone(english_to_french(None))

class Testf2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertIsNotNone(french_to_english(None))


unittest.main()