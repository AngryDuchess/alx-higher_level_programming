#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-4,-6,-1,-7,-3]), -1)
        self.assertEqual(max_integer([9, -1, -3, 5]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([102423]), 102423)
