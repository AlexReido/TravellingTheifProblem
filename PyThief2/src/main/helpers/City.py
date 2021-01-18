#!/usr/bin/env python
__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

from Item import Item


class City(object):
    """
        This class is used to represent a city in the problem
    """
    def __init__(self, idx: int, x: float, y: float) -> None:
        self.idx = idx
        self.x = x
        self.y = y
        self.items = []

    def __eq__(self, other):
        return self.idx == other.idx

    def __ne__(self, other):
        return self.idx != other.idx

    def add_item(self, item: Item) -> None:
        """
            This Method is used to add an item to a city
        """
        self.items.append(item)
