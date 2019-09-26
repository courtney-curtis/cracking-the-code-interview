import unittest

from uniquecharacters import unique_characters_best, unique_characters_single_data_structure

class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters(self):
        test_string1 = "Bee"
        test_string2 = "Courtney"
        test_string3 = "Eve"
        
        self.assertEqual(False, unique_characters_single_data_structure(test_string1))
        self.assertEqual(True, unique_characters_single_data_structure(test_string2))
        self.assertEqual(True, unique_characters_single_data_structure(test_string3))

    def test_unique_characters(self):
        test_string1 = "Bee"
        test_string2 = "Courtney"
        test_string3 = "Eve"
        
        self.assertEqual(False, unique_characters_best(test_string1))
        self.assertEqual(True, unique_characters_best(test_string2))
        self.assertEqual(True, unique_characters_best(test_string3))
        
if __name__ == '__main__':
    unittest.main()
