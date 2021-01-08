#!/usr/bin/env python

"""
Chromosome.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

from City import City


class Chromosome(object):
    def __init__(self, order_city: [City], pick_items: [bool]) -> None:
        self.order_city = order_city
        self.pick_items = pick_items

    def __eq__(self, other):
        return self.order_city == other.order_city and self.pick_items == other.pick_items

    def __ne__(self, other):
        return not self.__eq__(other)
