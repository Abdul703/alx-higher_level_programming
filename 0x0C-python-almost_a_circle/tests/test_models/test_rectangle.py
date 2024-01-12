#!/usr/bin/python3
"""Testing The file"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_creation(self):
        """Test Rectangle creation"""
        rectangle1 = Rectangle(5, 10)
        self.assertEqual(rectangle1.width, 5)
        self.assertEqual(rectangle1.height, 10)
        self.assertEqual(rectangle1.area(), 50)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)
        self.assertEqual(rectangle1.id, 2)

        rectangle2 = Rectangle(8, 4, 2, 3, 7)
        self.assertEqual(rectangle2.width, 8)
        self.assertEqual(rectangle2.height, 4)
        self.assertEqual(rectangle2.area(), 32)
        self.assertEqual(rectangle2.x, 2)
        self.assertEqual(rectangle2.y, 3)
        self.assertEqual(rectangle2.id, 7)

    def test_rectangle_attributes(self):
        """Test Rectangle Attributes"""
        rectangle = Rectangle(5, 10)
        rectangle.width = 15
        rectangle.height = 8
        rectangle.x = 3
        rectangle.y = 5

        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.area(), 120)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 5)


if __name__ == "__main__":
    unittest.main()
