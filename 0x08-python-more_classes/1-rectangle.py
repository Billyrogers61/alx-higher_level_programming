#!/usr/bin/python3
class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """__init_method.
        Args:
             width (int): integer width
             height (int): interger height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: return width
        Return: rectangle width
        """
        return (self.__width)

    @property
    def height(self):
        """height: returns height
        Returns: rectangle height
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
