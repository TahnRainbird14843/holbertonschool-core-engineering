#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
This creates and abstract base class
and two subclasses
"""


class Animal(ABC):
    """this is the abstract animal base class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """this is the dog class"""

    def sound(self):
        return ("Bark")


class Cat(Animal):
    """this is the cat class"""

    def sound(self):
        return ("Meow")
