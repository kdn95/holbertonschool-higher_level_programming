#!/usr/bin/python3
""" Shape abstract class and subclasses"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Shape

    Args:
        ABC
    
    Return:
        N/A
    
    """

    @abstractmethod
    def area(self) -> int:
        """area of shape method
        
            Return:
                Default 0
        """

        return 0
    
    @abstractmethod
    def perimeter(self) -> int:
        """ perimeter of shape method

            Return:
                Default 0

        """

        return 0
    

class Circle(Shape):
    """Circle subclass
    to Shape parent class
    """

    __radius = 0

    def __init__(self, radius=0):
        self.radius = radius
    
    @property
    def radius(self):
        """Private property of radius
        using Getter

            Return:
                __radius as an int
        """
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        """Set value of private radius

            Return:
                None
        """
        if value < 0:
            value = abs(value)

        self.__radius = value

    def area(self) -> float:
        """replace method of area"""

        area = math.pi * self.radius * self.radius
        print("Area: {:0.1f}".format(area))

        return area

    def perimeter(self) -> float:
        """replace method of area"""

        perimeter = 2 * math.pi * self.radius
        print("Perimeter: {:0.1f}".format(perimeter))

        return perimeter


class Rectangle(Shape):
    """Rectangle subclass
    to Shape parent class
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private width using Getter

            Return:
                __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Value of private prop width

            Return:
                None
        """

        self.__width = value

    @property
    def height(self):
        """Private height using Getter

            Returns:
                __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Private height using Getter

            Return:
                None
        """


        self.__height = value

    def area(self) -> float:
        """Replace method of area"""

        area = self.width * self.height
        print("Area: {:0.1f}".format(area))

        return area

    def perimeter(self) -> float:
        """Replace method of area"""

        perimeter = 2 * (self.width + self.height)
        print("Perimeter: {:0.1f}".format(perimeter))

        return perimeter


def shape_info(shape :Shape):
    """main function"""

    area :float = shape.area()
    perimeter :float = shape.perimeter()

    return {'area': area, 'perimeter': perimeter }