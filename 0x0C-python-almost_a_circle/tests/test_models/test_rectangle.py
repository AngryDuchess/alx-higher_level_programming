#!/usr/bin/python3
"""this module contains the test for class Rectangle"""
import unittest
import os
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

    def test_raise_except(self):
        """exceptions"""
        with self.assertRaises(TypeError) as r:
            r1 = Rectangle("hello", 4, 5, 6, 3)
        self.assertEqual("width must be an integer", str(r.exception))
        
        with self.assertRaises(TypeError) as r:
            r2 = Rectangle(12, "red")
        self.assertEqual("height must be an integer", str(r.exception))
        
        with self.assertRaises(TypeError) as r:
            r3 = Rectangle(12, 22, "ret", 43)
        self.assertEqual("x must be an integer", str(r.exception))
        
        with self.assertRaises(TypeError) as r:
            r4 = Rectangle(12, 1, 4, "fry")
        self.assertEqual("y must be an integer", str(r.exception))

        with self.assertRaises(ValueError) as r:
            r1 = Rectangle(-2, 4, 5, 6, 3)
        self.assertEqual("width must be > 0", str(r.exception))

        with self.assertRaises(ValueError) as r:
            r1 = Rectangle(2, 0, 5, 6, 3)
        self.assertEqual("height must be > 0", str(r.exception))

        with self.assertRaises(ValueError) as r:
            r1 = Rectangle(2, 3, -2, 6, 3)
        self.assertEqual("x must be >= 0", str(r.exception))

        with self.assertRaises(ValueError) as r:
            r1 = Rectangle(2, 4, 5, -6, 3)
        self.assertEqual("y must be >= 0", str(r.exception))

    def test_area(self):
        """tests the area"""
        r5 = Rectangle(3, 2)
        self.assertEqual(r5.area(), 6)

        r6 = Rectangle(3, 2, 0, 0, 9)
        self.assertEqual(r6.area(), 6)

        """times when errors occur"""
        with self.assertRaises(ValueError) as r:
            r7 = Rectangle(-3, 2)
            r7.area()
        self.assertEqual( "width must be > 0", str(r.exception))

        with self.assertRaises(ValueError) as r:
            r8 = Rectangle(3, 0)
            r8.area()
        self.assertEqual("height must be > 0", str(r.exception))

    def test_display(self):
        """test for display function"""

if __name__ == '__main__':
    unittest.main()
