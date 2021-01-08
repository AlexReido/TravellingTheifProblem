#!/usr/bin/env python

"""
crossover.py
"""

__author__ = 'Manish Dawash'
__date__ = '08 Jan 2021'
__version__ = '1.1.0'

import random

from helpers.config import config
from helpers.Chromosome import Chromosome


class Crossover(object):

    def ordered_crossover(self, parent_a: Chromosome, parent_b: Chromosome) -> (Chromosome, Chromosome):
        seq = random.sample(range(0, len(parent_a.order_city) - 1), k=2)
        seq.sort()
        i, j = seq

        cities_a = parent_a.order_city[1:]
        items_a = parent_a.pick_items
        cities_b = parent_b.order_city[1:]
        items_b = parent_b.pick_items

        b_without_a = [x for x in parent_b.order_city[j:] + parent_b.order_city[1:j] if x not in cities_a[i:j]]
        a_without_b = [x for x in parent_a.order_city[j:] + parent_a.order_city[1:j] if x not in cities_b[i:j]]

        for p in range(j, len(cities_a) + i - 1):
            cities_a[p % len(cities_a)] = b_without_a[p - j]
            cities_b[p % len(cities_b)] = a_without_b[p - j]

        cities_b.insert(0, parent_b.order_city[0])
        cities_a.insert(0, parent_a.order_city[0])

        return Chromosome(cities_a, items_a), Chromosome(cities_b, items_b)


def crossover(parents: [Chromosome]) -> (Chromosome, Chromosome):
    parent_a, parent_b = parents
    child_a, child_b = getattr(Crossover, config.get('algorithm_config', 'crossover').lower().strip())(Crossover(), parent_a, parent_b)
    return [child_a, child_b]
