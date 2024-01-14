#!/usr/bin/python3
"""Testing The Rectangle class"""
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
        self.assertEqual(rectangle1.id, 6)

        rectangle2 = Rectangle(8, 4, 2, 3, 7)
        self.assertEqual(rectangle2.width, 8)
        self.assertEqual(rectangle2.height, 4)
        self.assertEqual(rectangle2.area(), 32)
        self.assertEqual(rectangle2.x, 2)
        self.assertEqual(rectangle2.y, 3)
        self.assertEqual(rectangle2.id, 7)

        rectangle3 = Rectangle(3, 6, id=15)
        self.assertEqual(rectangle3.width, 3)
        self.assertEqual(rectangle3.height, 6)
        self.assertEqual(rectangle3.area(), 18)
        self.assertEqual(rectangle3.x, 0)
        self.assertEqual(rectangle3.y, 0)
        self.assertEqual(rectangle3.id, 15)

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

    def test_rectangle_update(self):
        """Test Rectangle update method"""
        rectangle = Rectangle(5, 10)
        rectangle.update(4, 8, 12, 2, 5)  # Update with explicit values

        self.assertEqual(rectangle.id, 4)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 5)

    def test_rectangle_update_with_two_arguments(self):
        """Test Rectangle update method with two arguments"""
        rectangle = Rectangle(5, 10)
        rectangle.update(8, 12)  # Update width and height

        self.assertEqual(rectangle.id, 8)
        self.assertEqual(rectangle.width, 12)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

        # Test with three arguments
        rectangle.update(8, 12, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.width, 12)
        self.assertEqual(rectangle.y, 0)
        self.assertEqual(rectangle.id, 8)

        # Test with four arguments
        rectangle.update(8, 12, 2, 5)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.id, 8)

        # Test with five arguments
        rectangle.update(8, 12, 2, 5, 4)
        self.assertEqual(rectangle.id, 8)

    def test_rectangle_update_with_kwargs(self):
        """Test Rectangle update method with kwargs"""
        rectangle = Rectangle(5, 10)
        rectangle.update(id=4, width=8, height=12, x=2, y=5)  # Update with kwargs

        self.assertEqual(rectangle.id, 4)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 5)

    # def test_rectangle_update_with_mix_of_args_and_kwargs(self):
    #     """Test Rectangle update method with a mix of args and kwargs"""
    #     rectangle = Rectangle(5, 10)
    #     rectangle.update(4, width=8, height=12, x=2, y=5)  # Update with a mix

    #     self.assertEqual(rectangle.id, 4)
    #     self.assertEqual(rectangle.width, 8)
    #     self.assertEqual(rectangle.height, 12)
    #     self.assertEqual(rectangle.x, 2)
    #     self.assertEqual(rectangle.y, 5)

    def test_rectangle_str_method(self):
        """Test Rectangle __str__ method"""
        rectangle = Rectangle(5, 10)
        self.assertEqual(str(rectangle), "[Rectangle] (9) 0/0 - 5/10")

    def test_rectangle_display_method(self):
        """Test Rectangle display method"""
        rectangle = Rectangle(3, 4, 2, 2)
    
        # Redirect stdout to capture print output
        from io import StringIO
        import sys

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        rectangle.display()

        # Get the printed output
        printed_output = sys.stdout.getvalue()

        # Restore stdout
        sys.stdout = original_stdout

        # Check the printed output
        expected_output = "\n\n  ###\n  ###\n  ###\n  ###\n"
        self.assertEqual(printed_output, expected_output)

    def test_rectangle_width_setter_exception(self):
        """Test Rectangle width setter exception handling"""
        rectangle = Rectangle(5, 10)
    
        with self.assertRaises(TypeError):
            rectangle.width = "invalid_width"

        with self.assertRaises(ValueError):
            rectangle.width = 0

    def test_rectangle_height_setter_exception(self):
        """Test Rectangle height setter exception handling"""
        rectangle = Rectangle(5, 10)
    
        with self.assertRaises(TypeError):
            rectangle.height = "invalid_height"

        with self.assertRaises(ValueError):
            rectangle.height = 0

    def test_rectangle_x_setter_exception(self):
        """Test Rectangle x setter exception handling"""
        rectangle = Rectangle(5, 10)
    
        with self.assertRaises(TypeError):
            rectangle.x = "invalid_x"

        with self.assertRaises(ValueError):
            rectangle.x = -1

    def test_rectangle_y_setter_exception(self):
        """Test Rectangle y setter exception handling"""
        rectangle = Rectangle(5, 10)
    
        with self.assertRaises(TypeError):
            rectangle.y = "invalid_y"

        with self.assertRaises(ValueError):
            rectangle.y = -1


if __name__ == "__main__":
    unittest.main()
