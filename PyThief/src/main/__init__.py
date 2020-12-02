'''
Created on Dec 1, 2020

@author: areid
'''
from main.Problem import Problem
from algorithms.Algorithm import Algorithm
# Problem
p = Problem()
p.readProblem("a280-n279")

print("number of items: ", p.numOfItems)

a = Algorithm()
a.solve(p)