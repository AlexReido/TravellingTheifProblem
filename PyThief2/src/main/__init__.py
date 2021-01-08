#!/usr/bin/env python

"""
__init__.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

import random

from Problem import Problem
from algorithms.NTGA import NTGA
from Competition import Competition
from main.helpers.config import config

random_seed = config.get('basic_config', 'random_seed')
problem_folder = config.get('folder_config', 'problem_folder')
population_size = config.get('run_config', 'population_size')

if __name__ == "__main__":
    random.seed(random_seed)

    file_name = 'a280-n279'

    problem = Problem(problem_folder, file_name)
    algorithm = NTGA(problem)

    non_dominated_solutions = algorithm.solve()

    Competition().print_solutions(problem, non_dominated_solutions.entries)

