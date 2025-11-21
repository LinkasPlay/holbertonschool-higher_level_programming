#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    This class represents a square with a private size.
    """

    def __init__(self, size):
        """
        Initializes a new square instance with a private size attribute.
        """
        self.__size = size
