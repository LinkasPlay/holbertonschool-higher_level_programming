#!/usr/bin/python3
"""
This module defines a Square class with size validation and accessors.
"""


class Square:
    """
    This class represents a square and offers controlled access to its size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size  # use the setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The square area.
        """
        return self.__size * self.__size
