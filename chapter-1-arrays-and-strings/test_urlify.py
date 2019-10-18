import unittest

from urlify import urlify

class TestUrlify(unittest.TestCase):
    def test_urlify(self):
        input1 = "Mr John Smith"
        input2 = "Courtney"

        self.assertEqual("Mr%20John%20Smith", urlify(input1, 13))
        self.assertEqual("Courtney", urlify(input2, 8))

if __name__ == '__main__':
    unittest.main()
