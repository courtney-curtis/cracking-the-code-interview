import unittest

from check_permutation import check_permutation, check_permutation_dict

class TestCheckPermutation(unittest.TestCase):
    def test_check_permutation(self):
        result1 = check_permutation("penguin", "gepninu")
        result2 = check_permutation("trash", "can")

        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

    def test_check_permutation_dict(self):
        result1 = check_permutation_dict("penguin", "gepninu")
        result2 = check_permutation_dict("trash", "can")

        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

if __name__ == "__main__":
    unittest.main()
