#!/usr/bin/env python

"""
Competition.py
"""

__author__ = 'Manish Dawash'
__date__ = '07 Jan 2021'
__version__ = '1.1.0'

import os
import sys
from pathlib import Path

from Problem import Problem
from Solution import Solution
from helpers.config import config


class Competition(object):
    def __init__(self):
        self.team_name = config.get('team_config', 'team_name')
        self.instances = config.get('instance_config', 'instances').replace(' ', '').split(',')
        self.num_dict = {s.split(':')[0]: int(s.split(':')[1]) for s in
                         config.get('instance_config', 'number_of_solutions').replace(' ', '').split(',')}

    def number_of_solutions(self, problem: Problem) -> int:
        if problem.name.split('-')[0].strip() in self.num_dict:
            return self.num_dict[problem.name.split('-')[0].strip()]
        else:
            return sys.maxsize

    def write_solutions(self, output_folder: str, problem: Problem, solutions: [Solution]) -> None:
        number_of_solutions = self.number_of_solutions(problem)

        if len(solutions) > number_of_solutions:
            print("WARNING: Finally the competition allows only" + str(number_of_solutions) +
                  " solutions to be submitted. \nYour algorithm found " +
                  str(len(solutions)) + " solutions.")

        cwd = os.getcwd()
        var_path = os.path.join(Path(cwd).parent.parent, output_folder, (self.team_name + '_' + problem.file_name + '.x'))
        obj_path = os.path.join(Path(cwd).parent.parent, output_folder, (self.team_name + '_' + problem.file_name + '.f'))

        var_file = open(var_path, 'w')
        obj_file = open(obj_path, 'w')

        for solution in solutions:
            pi = "".join((str(c) + " ") for c in solution.chromosome.order_city) + "\n"
            var_file.write(pi)

            z = "".join((str(int(item)) + " ") for item in solution.chromosome.pick_items) + "\n\n"
            var_file.write(z)

            obj_file.write(f'{solution.time:.16f} {solution.profit:.16f}\n')

        var_file.close()
        obj_file.close()

    def print_solutions(self, problem: Problem, solutions: [Solution], print_variables: bool = False) -> None:
        print(f'Problem: {problem.file_name} \t Team: {self.team_name}')
        print(f'Number of non-dominated solutions: {len(solutions)}')

        for solution in solutions:
            if print_variables:
                print(" ".join(str(c) for c in solution.chromosome.order_city))
                print(" ".join(str(int(item)) for item in solution.chromosome.pick_items))

            print(f'{solution.time:.16f} {solution.profit:.16f}')
