import unittest
from src.palindrome import is_palindrome


class GoodPalindromeTest(unittest.TestCase):

    def test_word(self):
        self.assertTrue(is_palindrome('lol'))

    def test_sentence(self):
        self.assertTrue(is_palindrome('a man, a plan, a canal: Panama'))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_white_spaces(self):
        self.assertTrue(is_palindrome('abc      cba'))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('chair'))


if __name__ == '__main__':
    unittest.main()
