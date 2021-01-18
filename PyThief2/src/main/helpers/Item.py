#!/usr/bin/env python
__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'


class Item(object):
    """
        This Class is used to represent each item that is available to pick.
    """
    def __init__(self, idx: int, profit: float, weight: float, city: int) -> None:
        self.idx = idx
        self.profit = profit
        self.weight = weight
        self.city = city

    def __eq__(self, other):
        return self.idx == other.idx

    def __ne__(self, other):
        return self.idx != other.idx
