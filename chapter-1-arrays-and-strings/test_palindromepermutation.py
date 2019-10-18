import unittest
from palindromepermutation import palindrome_permutation

class TestPalindromePermutation (unittest.TestCase):
    
    def test_palindrome_permutation(self):
        is_palindrome = palindrome_permutation("atco cta")
        is_not_palindrome = palindrome_permutation("courtney")

        self.assertEqual(is_palindrome, True)
        self.assertEqual(is_not_palindrome, False)

if __name__ == '__main__':
    unittest.main()
