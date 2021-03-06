#!/usr/bin/env python
__author__ = 'Manish Dawash'
__date__ = '08 Jan 2021'
__version__ = '1.1.0'

import random

from helpers.config import config
from helpers.Chromosome import Chromosome


class Mutation:

    @staticmethod
    def reverse_sequence_mutation(self, parent: Chromosome, rate: float) -> None:
        """
            This method implements reverse sequence mutation algorithm
        """
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
        """
            This method implements the partial shuffle mutation algorithm
        """
        for i in range(1, len(parent.order_city)):
            if random.random() < rate:
                j = random.randint(1, len(parent.order_city) - 1)
                city_i = parent.order_city[i]
                parent.order_city[i] = parent.order_city[j]
                parent.order_city[j] = city_i

        for x in range(len(parent.pick_items)):
            if random.random() < rate:
                parent.pick_items[x] = random.choice([False, True])

    @staticmethod
    def swap_mutation(self, parent: Chromosome, rate: float) -> None:
        """
            This method implements the swap mutation algorithm
        """
        selected_for_swap = random.choices(parent.order_city[1:], k=2)

        index0 = parent.order_city.index(selected_for_swap[0])
        index1 = parent.order_city.index(selected_for_swap[1])

        parent.order_city[index0] = selected_for_swap[1]
        parent.order_city[index1] = selected_for_swap[0]

        for x in range(len(parent.pick_items)):
            if random.random() < rate:
                parent.pick_items[x] = random.choice([False, True])


def mutation(parents: [Chromosome]) -> [Chromosome]:
    """
        Gets a list of parents and mutates the children according to mutation method in .ini file
    """
    parent_a, parent_b = parents
    mutation_rate = float(config.get('run_config', 'mutation_rate'))
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent_a, mutation_rate)
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent_b, mutation_rate)

    return parents


def mutate(parent: Chromosome) -> Chromosome:
    """
        Takes a child and mutates it according to mutation method in .ini file
    """
    mutation_rate = float(config.get('run_config', 'mutation_rate'))
    getattr(Mutation, config.get('algorithm_config', 'mutation').lower().strip())(Mutation(), parent, mutation_rate)
    return parent
