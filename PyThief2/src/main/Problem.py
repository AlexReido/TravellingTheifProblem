#!/usr/bin/env python

"""
Problem.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

import math
import os
import sys
from pathlib import Path
from typing import Union

from Solution import Solution
from helpers.City import City
from helpers.Item import Item
from helpers.Chromosome import Chromosome

dict_var = {
    'PROBLEM NAME': 'name',
    'KNAPSACK DATA TYPE': 'knapsack_type',
    'DIMENSION': 'number_of_cities',
    'NUMBER OF ITEMS': 'number_of_items',
    'CAPACITY OF KNAPSACK': 'max_weight',
    'MIN SPEED': 'min_speed',
    'MAX SPEED': 'max_speed',
    'RENTING RATIO': 'renting_ratio',
    'EDGE_WEIGHT_TYPE': 'edge_weight_type',
    'NODE_COORD_SECTION': 'cities',
    'ITEMS SECTION': 'items'
}


class Problem(object):
    def __init__(self, folder_name: str, file_name: str) -> None:
        self.file_name = file_name
        self.folder_name = folder_name
        self.name = ''
        self.number_of_cities = -1
        self.number_of_items = -1
        self.max_weight = -1
        self.min_speed = -1
        self.max_speed = -1
        self.renting_ratio = sys.float_info.max
        self.cities = []
        self.items = []
        self.read_problem()

    def read_problem(self):
        cwd = os.getcwd()
        file_path = os.path.join(Path(cwd).parent.parent, self.folder_name, (self.file_name + '.txt'))

        with open(file_path, 'r') as file:
            for ind, line in enumerate(file):
                if ind <= 8:
                    setattr(self, dict_var[line.split(":")[0].strip()], convert_type(line.split(":")[1].strip()))
                else:
                    setattr(self, dict_var[line.split("\t")[0].strip()], [])
                    current = dict_var[line.split("\t")[0].strip()]
                    for idr, liner in enumerate(file):
                        a = liner.split()
                        if current == 'cities':
                            self.cities.append(City(int(a[0]), float(a[1]), float(a[2])))
                            if idr == self.number_of_cities - 1:
                                break
                        elif current == 'items':
                            item = Item(int(a[0]), float(a[1]), float(a[2]), int(a[3]))
                            self.items.append(item)
                            self.cities[item.city - 1].add_item(item)
                            if idr == self.number_of_items - 1:
                                break

    def evaluate(self, chromosome: Chromosome) -> Solution:
        if chromosome.order_city[0].idx != 1:
            raise RuntimeError('Thief must start at city id 1')

        time = 0
        profit = 0
        weight = 0

        for i in range(self.number_of_cities):
            city = chromosome.order_city[i]

            for item in city.items:
                if chromosome.pick_items[item.idx-1]:
                    weight += item.weight
                    profit += item.profit

            if weight > self.max_weight:
                time = sys.float_info.max
                profit = -sys.float_info.max
                break

            speed = self.max_speed - (weight / self.max_weight) * (self.max_speed - self.min_speed)
            next_city = chromosome.order_city[(i + 1) % self.number_of_cities]
            distance = math.ceil(euclidean_distance(city, next_city))
            time += distance / speed

        return Solution(chromosome, profit, time, profit - self.renting_ratio * time, [time, -profit])


def euclidean_distance(city_a: City, city_b: City) -> float:
    return math.sqrt((city_a.x - city_b.x) ** 2 + (city_a.y - city_b.y) ** 2)


def convert_type(num: str) -> Union[int, float, str]:
    try:
        int(num)
        return int(num)
    except ValueError:
        try:
            float(num)
            return float(num)
        except ValueError:
            return num
