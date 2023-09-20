#!/usr/bin/python3
"""this module contains the test for class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test class for Rectangle"""
    def setUp(self):
        Base._Base__nb_object = 0

    def test_id(self):
        r1 = Rectangle(11, 2)
        self.assertEqual(r1.id, 1)
        
        r2 = Rectangle(5, 4)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(3, 5, 5, 1, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(1, 2, 4, 5, -9)
        self.assertEqual(r4.id, -9)
