#!/usr/bin/python3
""" Animal Class from abc """
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Animal subclass
    inheriting ABC parent

    Args:
        ABC

    Returns:
        string

    """

    @abstractmethod
    def sound(self) -> str:
        """ sound by the animal

            Return:
                string
        """

        return ""


class Dog(Animal):
    """ Dog subclass
    to Animal parent class
    """
    def sound(self) -> str:
        """override Animal method"""

        return "Bark"


class Cat(Animal):
    """ Cat subclass
    to Animal parent class
    """
    def sound(self) -> str:
        """override Animal method"""

        return "Meow"
