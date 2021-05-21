#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unitest.TestCase):
    """test class for max_integer"""
    def test_ProperInput(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer([2.0, 2.1, 2.3]), 2.3)
    def test_EmptyInput(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
