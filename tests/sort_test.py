import unittest
import sort_fixture
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
# from quick_sort import _quicksort
from timeit import default_timer as timer
from datetime import timedelta

size = 5
print("Size: " + str(size))


class TestSortAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted_list = sort_fixture.get_random_nums(size)
        self.sorted_list = sorted(self.unsorted_list)
        self.start = timer()

    def log_time(self):
        print(str(timedelta(milliseconds=timer() - self.start)) + ' milliseconds')

    def xtest_bubble_sort(self):
        my_sorted_list = bubble_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, my_sorted_list)
        print('bubble sort:', end=' ')
        self.log_time()

    def xtest_insertion_sort(self):
        my_sorted_list = insertion_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, my_sorted_list)
        print('insertion sort:', end=' ')
        self.log_time()

    def test_merge_sort(self):
        my_sorted_list = merge_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, my_sorted_list)
        print('mergesort:', end=' ')
        self.log_time()

    def xtest_quick_sort(self):
        my_sorted_list = _quicksort(self.unsorted_list)
        self.assertEqual(self.sorted_list, my_sorted_list)
        print('quick sort:', end=' ')
        self.log_time()

    def xtest_selection_sort(self):
        my_sorted_list = selection_sort(self.unsorted_list)
        self.assertEqual(self.sorted_list, my_sorted_list)
        print('selection sort:', end=' ')
        self.log_time()


if __name__ == '__main__':
    unittest.main()
