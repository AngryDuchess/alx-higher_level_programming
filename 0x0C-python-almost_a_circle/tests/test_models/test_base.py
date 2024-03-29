#!/usr/bin/python3
"""this module contains the test for the base class"""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """test class for the Base class"""
    def setUp(self):
        Base._Base__nb_object = 0

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(14)
        self.assertEqual(b3.id, 14)

        b4 = Base()
        self.assertEqual(b4.id, 3)
    
if __name__ == '__main__':
    unittest.main()
