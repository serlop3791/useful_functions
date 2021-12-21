import unittest
import random
from search_fixture import Utility as Util
from linear_search import linear_search
from binary_search import binary_search
from binary_search import binary_search_recursive


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        range_start = 0
        range_end = 10
        size = 20
        self.number_to_find = random.randint(range_start, range_end)
        self.unsorted_numbers = Util(range_start, range_end,
                                     size, self.number_to_find).get_random_numbers()

    def xtest_linear_search(self):
        index_of_number = linear_search(self.unsorted_numbers, self.number_to_find)
        self.assertNotEqual(index_of_number, -1)
        self.assertEqual(self.unsorted_numbers[index_of_number], self.number_to_find)

    def xtest_binary_search(self):
        print("Searching for number: " + str(self.number_to_find))
        print("In list: " + str(self.unsorted_numbers))
        sorted_numbers = sorted(self.unsorted_numbers)
        index_of_number = binary_search(sorted_numbers, self.number_to_find)
        self.assertNotEqual(index_of_number, -1)
        self.assertEqual(sorted_numbers[index_of_number], self.number_to_find)

    def test_binary_search_recursive(self):
        sorted_numbers = sorted(self.unsorted_numbers)
        left = 0
        right = len(sorted_numbers)
        index_of_number = binary_search_recursive(sorted_numbers,
                                                  self.number_to_find,
                                                  left,
                                                  right)
        self.assertNotEqual(index_of_number, -1)
        self.assertEqual(sorted_numbers[index_of_number], self.number_to_find)


if __name__ == '__main__':
    unittest.main()
