#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """square class with it's size and proper validation"""
    __size = None

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.size:
            print("")
        for i in range(self.size):
            print("#" * self.size)
