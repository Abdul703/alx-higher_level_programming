#!/usr/bin/python3
"""Testing The file"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_assignment(self):
        """Test automatic ID assignment when not provided."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id(self):
        """Test object creation with a custom ID."""
        obj = Base(100)
        self.assertEqual(obj.id, 100)

    def test_no_id_provided(self):
        """Test that objects are assigned unique IDs when not provided."""
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)


if __name__ == "__main__":
    unittest.main()
