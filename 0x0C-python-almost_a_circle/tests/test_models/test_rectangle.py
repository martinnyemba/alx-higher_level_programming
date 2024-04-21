#!/usr/bin/python3
"""Defines Test case for the Rectangle (model/rectangle)  module"""
#  import required modules
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

"""Test Cases for public method def area(self): 
    that returns the area value of the Rectangle
"""

class TestRectangleArea(unittest.TestCase):
    def test_area_with_valid_values(self):
        # Create a rectangle with width 5 and height 10
        rectangle = Rectangle(5, 10)
        # Check if the area is calculated correctly
        self.assertEqual(rectangle.area(), 50)
    
    def test_area_with_zero_values(self):
        # Create a rectangle with width 0 and height 0
        # Check if the area is 0
        with self.assertRaises(TypeError):
            rectangle = Rectangle(6, "martin")
            rectangle = Rectangle("nyemba", 10)
            rectangle = Rectangle("10", 10)
    
    def test_area_with_negative_values(self):
        with self.assertRaises(ValueError):
            # Create a rectangle with width -5 and height 10
            rectangle = Rectangle(-5, 10)
            rectangle = Rectangle(-5, -10)
            rectangle = Rectangle(-5, 10)
            rectangle = Rectangle(5, -5)
