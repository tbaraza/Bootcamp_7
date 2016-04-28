"""Test suite for super_sum. """
import unittest
from unittest import TestCase
from super_sum import super_sum


class SuperSumTestCase(TestCase):
	def set
    """Test case for super sum"""

    def test_empty_input(self):
        '''Test empty input'''
        self.assertEqual(super_sum(), 0)

    def test_string_input_returns(self):
        """Test string input type"""
        self.assertEqual(super_sum("string"), 0)
        self.assertEqual(super_sum("string"), 0)

    def test_sum_of_integers(self):
        """Test sum of integers"""
        self.assertEqual(super_sum(1, 2, 3), 6)
        self.assertNotEqual(super_sum(10, 20, 30), 100)
        self.assertEqual(super_sum(-1, 1), 0)

    def test_sum_of_items_in_one_list(self):
        """Test sum of list"""
        self.assertEqual(super_sum([1, 2, 3]), 6)
        self.assertEqual(super_sum([1, 2], [2, 3]), 8)


# if __name__ == "__main__":
# 	unittest.main()
