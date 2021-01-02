'''
Created on Dec 1, 2020

@author: areid
'''
from main.Competition import Competition
from main.Problem import Problem
from algorithms.Algorithm import Algorithm
from algorithms.RandomLocalSearch import RandomLocalSearch
from algorithms.NGTA import NGTA

if __name__ == "__main__":
    # Problem
    p = Problem()
    p.readProblem("a280-n279")
    
    print("number of items: ", p.numOfItems)
    
    algorithm = NGTA()
    nds = algorithm.solve(p)
    nds = sorted(nds, key=lambda s: s.time)
    
    
    
    print(len(nds), " non-dominated solutions found")
    print("here")
    for s in nds:
        print(s.time, " ", s.profit)
        
    comp = Competition()
    comp.writeSolutions(p, nds)
    
