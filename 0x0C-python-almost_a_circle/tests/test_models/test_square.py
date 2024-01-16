#!/usr/bin/python3
"""Square Testing"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_creation(self):
        """Test Square creation"""
        square1 = Square(5)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.width, 5)
        self.assertEqual(square1.height, 5)
        self.assertEqual(square1.area(), 25)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)
        self.assertEqual(square1.id, 2)

        square2 = Square(8, 2, 3, 7)
        self.assertEqual(square2.size, 8)
        self.assertEqual(square2.width, 8)
        self.assertEqual(square2.height, 8)
        self.assertEqual(square2.area(), 64)
        self.assertEqual(square2.x, 2)
        self.assertEqual(square2.y, 3)
        self.assertEqual(square2.id, 7)

        square3 = Square(3, id=15)
        self.assertEqual(square3.size, 3)
        self.assertEqual(square3.width, 3)
        self.assertEqual(square3.height, 3)
        self.assertEqual(square3.area(), 9)
        self.assertEqual(square3.x, 0)
        self.assertEqual(square3.y, 0)
        self.assertEqual(square3.id, 15)

    def test_square_attributes(self):
        """Test Square Attributes"""
        square = Square(5)
        square.size = 15
        square.x = 3
        square.y = 5

        self.assertEqual(square.size, 15)
        self.assertEqual(square.width, 15)
        self.assertEqual(square.height, 15)
        self.assertEqual(square.area(), 225)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 5)

    def test_square_update(self):
        """Test Square update method"""
        square = Square(5)
        square.update(4, 8, 2, 5)  # Update with explicit values

        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 5)

    def test_square_update_with_kwargs(self):
        """Test Square update method with kwargs"""
        square = Square(5)
        square.update(id=4, size=8, x=2, y=5)  # Update with kwargs

        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 5)

    def test_square_update_with_mix_of_args_and_kwargs(self):
        """Test Square update method with a mix of args and kwargs"""
        square = Square(5)
        square.update(4, size=8, x=2, y=5)  # Update with a mix

        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_str_method(self):
        """Test Square __str__ method"""
        square = Square(5)
        self.assertEqual(str(square), "[Square] (3) 0/0 - 5")

        square.update(8, 12, 2, 5)
        self.assertEqual(str(square), "[Square] (8) 2/5 - 12")

    def test_square_to_dictionary_method(self):
        """Test Square to_dictionary method"""
        square = Square(5, 2, 3, id=8)
        dictionary = square.to_dictionary()

        self.assertEqual(dictionary, {'id': 8, 'size': 5, 'x': 2, 'y': 3})

if __name__ == "__main__":
    unittest.main()
