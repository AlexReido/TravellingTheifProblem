#!/usr/bin/env python

"""
NTGA.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

import random

from crossover import crossover
from helpers.config import config
from NonDominatedSet import NonDominatedSet
from Problem import Problem
from Solution import Solution
from helpers.Chromosome import Chromosome
from mutation import mutation
from mutation import mutate


class NTGA(object):
    def __init__(self, problem: Problem) -> None:
        self.xyz = 1
        self.problem = problem
        self.population_size = int(config.get('run_config', 'population_size'))
        self.non_dominated_set = NonDominatedSet()
        self.population = []

    def generate_initial_population(self) -> None:
        for _ in range(self.population_size):
            order_city = self.problem.cities[1:]
            random.shuffle(order_city)
            order_city.insert(0, self.problem.cities[0])
            pick_items = random.choices([False, True], weights=[0.9, 0.1], k=self.problem.number_of_items)
            self.population.append(Chromosome(order_city, pick_items))

    def selection(self) -> [Chromosome]:
        parent_a = self.tournament_selection()
        parent_b = self.tournament_selection()

        while parent_a == parent_b:
            parent_b = self.tournament_selection()

        return [parent_a, parent_b]

    def tournament_selection(self) -> Chromosome:
        n = 6
        initial = random.sample(self.population, k=n)
        ranking = [1] * n

        for i in range(n - 1):
            for j in range(i + 1, n):
                dom = initial[i].get_relation(initial[j])
                if dom == 1:
                    ranking[j] += 1
                elif dom == -1:
                    ranking[i] += 1

        min_rank = min(ranking)

        return initial[random.choice([i for i, x in enumerate(ranking) if i == min_rank])].chromosome

    def evaluate(self, children: [Chromosome]) -> [Solution]:
        return [self.problem.evaluate(chromosome) for chromosome in children]

    def solve(self):
        generation_limit = int(config.get('run_config', 'generation_limit'))
        self.generate_initial_population()

        new_population = []

        for i in range(generation_limit):
            self.population = self.evaluate(self.population)
            self.non_dominated_set.adds(self.population)

            while len(new_population) < self.population_size:
                parents = self.selection()
                children = mutation(crossover(parents))

                for child in children:
                    count = 0
                    while (child in new_population) or children[0] == children[1]:
                        count += 1
                        mutate(child)
                        if count > 100:
                            break

                new_population += children

            self.population = new_population

        return self.non_dominated_set
