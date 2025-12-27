import unittest
from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        list = []
        insertion_sort(list)
        self.assertEqual(list, [])

    def test_single_element(self):
        list = [5]
        insertion_sort(list)
        self.assertEqual(list, [5])

    def test_sorted_list(self):
        list = [1, 2, 3, 4, 5]
        insertion_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        list = [5, 4, 3, 2, 1]
        insertion_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        list = [3, 1, 4, 5, 2]
        insertion_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_edge_case_insertion(self):
        list = [10, 2, 3, 4, 5]
        insertion_sort(list)
        self.assertEqual(list, [2, 3, 4, 5, 10])