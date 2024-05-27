#!/usr/bin/python3
""" Unittest for max_integer([...])
"""
import unittest
max_int = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):

    def test_max_start(self):
        self.assertEqual(max_int([3,2,1]), 3)

    def test_max_middle(self):
        self.assertEqual(max_int([1, 3, 2]), 3)

    def test_max_end(self):
        self.assertEqual(max_int([1, 2, 3]), 3)

    def test_negative(self):
        self.assertLessEqual(max_int([-1, -2, -3]), 0)

    def test_only_one(self):
        self.assertEqual(max_int([100]), 100)

    def test_empty(self):
        self.assertEqual(max_int([]), None)


if __name__ == '__main__':
    unittest.main()
