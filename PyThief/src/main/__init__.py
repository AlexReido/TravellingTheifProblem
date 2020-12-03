'''
Created on Dec 1, 2020

@author: areid
'''
from main.Problem import Problem
from algorithms.Algorithm import Algorithm
from algorithms.RandomLocalSearch import RandomLocalSearch
# Problem
p = Problem()
p.readProblem("a280-n279")

print("number of items: ", p.numOfItems)

algorithm = RandomLocalSearch()
nds = algorithm.solve(p)
nds = sorted(nds, key=lambda s: s.time)

print(len(nds), " non-dominated solutions found")
for s in nds:
    print(s.time, " ", s.profit)
    
    