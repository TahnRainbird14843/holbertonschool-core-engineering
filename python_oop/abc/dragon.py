#!/usr/bin/env python3

"""
This demonstrates mixins
"""


class SwimMixin:
    """Swim mixin class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """fly mixin class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """dragon class"""
    def roar(self):
        print("The dragon roars!")
