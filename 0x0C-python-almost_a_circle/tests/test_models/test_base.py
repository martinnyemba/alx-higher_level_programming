#!/usr/bin/python3
"""This module defines the test case for moudle named base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_instance_creation_with_id(self):
        # Create an instance with a specified id
        obj1 = Base(id=1)
        self.assertEqual(obj1.id, 1)

    def test_instance_creation_without_id(self):
        # Create instances without specifying id
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)  # First instance should have id 1
        self.assertEqual(obj2.id, 2)  # Second instance should have id 2


if __name__ == '__main__':
    unittest.main()
