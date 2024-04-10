#!usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_list(self):
        #  Test with a normal list
        self.assertEqual(max_integer([1,3,2]), 3)

    def test_empty_list(self):
        #  Test max integer with an empty list
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        #  Test lsit with negative numbers
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_duplicate_numbers(self):
        #  Test with duplicate numbers
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_single_element(self):
        #  Test with single element
        self.assertEqaul(max_integer([5]), 5)

    def test_mixed_numbers(self):
        #  Test with a list of mixed numbers
        self.assertEqual(max_integer([5, -3, 10, -20, 15, 0]), 15)

    def test_large_list(self):
        #  Test with a large list
        self.assertEqual(max_integer(list(range(1000000)), 999999)


if __name__ == '__main__':
    unittest.main()
