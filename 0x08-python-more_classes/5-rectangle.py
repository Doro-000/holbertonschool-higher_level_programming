#!/usr/bin/python3
"""Module consisting of Rectangle class to represent rectangles"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        if type(width) is not str:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not str:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not str:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not str:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (not self.__width) or (not self.__height):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if i != (self.__height - 1):
                rect += '\n'
        return rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
