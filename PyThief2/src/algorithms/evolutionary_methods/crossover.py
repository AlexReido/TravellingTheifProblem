#!/usr/bin/env python

"""
crossover.py
"""

__author__ = 'Manish Dawash'
__date__ = '08 Jan 2021'
__version__ = '1.1.0'

import random
import sys
from collections import defaultdict

from helpers.config import config
from helpers.Chromosome import Chromosome


class Crossover(object):

    @staticmethod
    def ordered_crossover(self, parent_a: Chromosome, parent_b: Chromosome) -> (Chromosome, Chromosome):
        seq = random.sample(range(0, len(parent_a.order_city) - 1), k=2)
        seq.sort()
        i, j = seq

        seq = random.sample(range(0, len(parent_a.pick_items) - 1), k=2)
        seq.sort()
        p, q = seq

        cities_a = parent_a.order_city[1:]
        items_a = parent_a.pick_items
        cities_b = parent_b.order_city[1:]
        items_b = parent_b.pick_items

        b_without_a = [x for x in parent_b.order_city[j:] + parent_b.order_city[1:j] if x not in cities_a[i:j]]
        a_without_b = [x for x in parent_a.order_city[j:] + parent_a.order_city[1:j] if x not in cities_b[i:j]]
        b_i_a = parent_b.pick_items[q:] + parent_b.pick_items[:q]
        a_i_b = parent_a.pick_items[q:] + parent_a.pick_items[:q]

        for x in range(j, len(cities_a) + i - 1):
            cities_a[x % len(cities_a)] = b_without_a[x - j]
            cities_b[x % len(cities_b)] = a_without_b[x - j]

        for x in range(q, len(items_a) + p - 1):
            items_a[x % len(items_a)] = b_i_a[x - q]
            items_b[x % len(items_b)] = a_i_b[x - q]

        cities_b.insert(0, parent_b.order_city[0])
        cities_a.insert(0, parent_a.order_city[0])

        return Chromosome(cities_a, items_a), Chromosome(cities_b, items_b)

    @staticmethod
    def edge_crossover_single(parent_a: Chromosome, parent_b: Chromosome) -> Chromosome:
        cities_a = parent_a.order_city
        cities_b = parent_b.order_city

        edge_map = defaultdict(list)

        for c in range(len(cities_a)):
            edge_map.setdefault(c, [])

        edge_map[cities_a[0]].append(cities_a[-1])
        edge_map[cities_b[0]].append(cities_b[-1])
        edge_map[cities_a[-1]].append(cities_a[0])
        edge_map[cities_b[-1]].append(cities_b[0])

        for i, c in enumerate(cities_a[0:-2]):
            edge_map[c].append(cities_a[i + 1])
            edge_map[cities_a[i + 1]].append(c)

        for i, c in enumerate(cities_b[0:-2]):
            edge_map[c].append(cities_b[i + 1])
            edge_map[cities_b[i + 1]].append(c)

        current_city = cities_a[0]

        new_cities = [current_city]

        while len(edge_map.keys()) > 1:
            current_city_edge_list = edge_map.pop(current_city)

            if not current_city_edge_list:
                next_city = random.choice(list(edge_map.keys()))
            else:
                minx = sys.maxsize
                for city in current_city_edge_list:
                    edge_map[city].remove(current_city)
                    if len(edge_map[city]) < minx:
                        minx = len(edge_map[city])
                        next_city = city
                    elif len(edge_map[city]) == minx:
                        next_city = random.choice([city, next_city])

            current_city = next_city
            new_cities.append(current_city)

        new_items = []
        items_a = parent_a.pick_items
        items_b = parent_b.pick_items

        for i in range(len(items_a)):
            if random.randrange(1) == 1:
                new_items.append(items_a[i])
            else:
                new_items.append(items_b[i])

        return Chromosome(new_cities, new_items)

    def edge_crossover(self, parent_a: Chromosome, parent_b: Chromosome) -> (Chromosome, Chromosome):
        child_a = self.edge_crossover_single(parent_a, parent_b)
        child_b = self.edge_crossover_single(parent_a, parent_b)

        while child_a == child_b:
            child_b = self.edge_crossover_single(parent_a, parent_b)

        return child_a, child_b


def crossover(parents: [Chromosome]) -> (Chromosome, Chromosome):
    parent_a, parent_b = parents
    child_a, child_b = getattr(Crossover, config.get('algorithm_config', 'crossover').lower().strip())(Crossover(),
                                                                                                       parent_a,
                                                                                                       parent_b)
    return [child_a, child_b]
