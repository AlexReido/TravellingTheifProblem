#!/usr/bin/env python

"""
Item.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'


class Item(object):
    def __init__(self, idx: int, profit: float, weight: float, city: int) -> None:
        self.idx = idx
        self.profit = profit
        self.weight = weight
        self.city = city
