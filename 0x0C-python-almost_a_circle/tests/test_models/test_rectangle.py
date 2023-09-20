#!/usr/bin/python3
"""this module contains the test for class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test class for Rectangle"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """tests the id"""
        r1 = Rectangle(11, 2)
        self.assertEqual(r1.id, 1)
        
        r2 = Rectangle(5, 4)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(3, 5, 5, 1, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(1, 2, 4, 5, -9)
        self.assertEqual(r4.id, -9)

    def test_attr(self):
        """tests the attributes"""
        r1 = Rectangle(10, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(9, 5, 3, 6, 89)
        self.assertEqual(r2.width, 9)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 6)

if __name__ == '__main__':
    unittest.main()
