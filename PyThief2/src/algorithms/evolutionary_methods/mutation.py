#!/usr/bin/env python

"""
mutation.py
"""

__author__ = 'Manish Dawash'
__date__ = '08 Jan 2021'
__version__ = '1.1.0'

import random

from helpers.config import config
from helpers.Chromosome import Chromosome


class Mutation:

    @staticmethod
    def reverse_sequence_mutation(self, parent: Chromosome, rate: float) -> None:
        seq = random.sample(range(1, len(parent.order_city)), k=2)
        seq.sort()
        i, j = seq

        order_city = parent.order_city[:i] + parent.order_city[i:j][::-1] + parent.order_city[j:]
        pick_items = parent.pick_items[:i] + parent.pick_items[i:j][::-1] + parent.pick_items[j:]

        for x in range(len(pick_items)):
            if random.random() > rate:
                pick_items[x] = random.choice([False, True])

        parent.order_city = order_city
        parent.pick_items = pick_items

    @staticmethod
    def partial_shuffle_mutation(self, parent: Chromosome, rate: float) -> None:
        for i in range(1, len(parent.order_city)):
            if random.random() < rate:
                j = random.randint(1, len(parent.order_city) - 1)
                city_i = parent.order_city[i]
                parent.order_city[i] = parent.order_city[j]
                parent.order_city[j] = city_i

        for x in range(len(parent.pick_items)):
            if random.random() < rate:
                parent.pick_items[x] = random.choice([False, True])


def mutation(parents: [Chromosome]) -> [Chromosome]:
    parent_a, parent_b = parents
    mutation_rate = float(config.get('run_config', 'mutation_rate'))
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent_a, mutation_rate)
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent_b, mutation_rate)

    return parents


def mutate(parent: Chromosome) -> Chromosome:
    mutation_rate = float(config.get('run_config', 'mutation_rate'))
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent, mutation_rate)
    return parent
