import unittest

from DictionaryQuery.dictionary import get_definition


class MyUnitTest(unittest.TestCase):

    def test_get_definition(self):
        word = 'exercise'
        definition = get_definition(word)
        self.assertIn("ˈek-sər-ˌsīz  ( noun ) : the act of bringing into play or realizing in action", definition)
