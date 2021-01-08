#!/usr/bin/env python

"""
NonDominatedSet.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

from Solution import Solution


class NonDominatedSet(object):
    def __init__(self):
        self.entries = []

    def add(self, solution: Solution) -> bool:
        is_added = True

        for entry in self.entries:
            rel = solution.get_relation(entry)

            if rel == -1 or (rel == 0 and solution.equals_in_design(entry)):
                is_added = False
                break
            elif rel == 1:
                self.entries.remove(entry)

        if is_added:
            self.entries.append(solution)

        return is_added

    def adds(self, solutions: [Solution]) -> None:
        for solution in solutions:
            self.add(solution)
