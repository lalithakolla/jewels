import unittest
from src.palindrome import is_palindrome


class PalindromeTest(unittest.TestCase):

    def test_01(self):
        result = is_palindrome('lol')
        self.assertTrue(result)

    # def test_02(self):
    #     result = is_palindrome('a man, a plan, a canal: Panama')
    #     self.assertTrue(result)

    def test_03(self):
        result = is_palindrome('')
        self.assertTrue(result)

    def test_04(self):
        result = is_palindrome('abc      cba')
        self.assertTrue(result)

    def test_05(self):
        result = is_palindrome('chair')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
