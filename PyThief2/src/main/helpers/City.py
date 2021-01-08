#!/usr/bin/env python

"""
City.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

from Item import Item


class City(object):
    def __init__(self, idx: int, x: float, y: float) -> None:
        self.idx = idx
        self.x = x
        self.y = y
        self.items = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)
