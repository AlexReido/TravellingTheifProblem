'''
Created on Dec 1, 2020

@author: areid
'''
from algorithms.Algorithm import Algorithm
import random
from main.Solution import Solution
from main.Problem import Problem
from sympy.core.evalf import rnd
from astropy.units import count


class RandomLocalSearch(Algorithm):
    '''
    classdocs
    '''
    def solve(self, Problem):
        counter = 0
        # TODO implement non dominated set Class
        nds = [] # non-dominated set
        
        while True:
            if (self.pi == None):
                pi = random.choices(range(1, Problem.numOfCities), Problem.numOfCities)
                pi.insert(0, 0)
            else:
                pi = self.pi
                
            z = [False]*Problem.numOfCities #Packing plan
            
            s = Problem.evaluate(Problem, pi, z)
            
            # TODO change to nds class function
            nds.append(s)
            counter += 1
            
            rnd = random.choices(range(1, Problem.numOfCities), Problem.numOfCities)
            assert Problem.numOfCities == len(rnd)
            weight = 0.0
            for j in range(len(rnd)):
                item = rnd[j]
                
                if ((weight + Problem.weight[item]) < Problem.maxWeight ):
                    z[item] = True
                    weight += Problem.weight[item]
                    
                    s = Problem.evaluate(Problem, pi, z)
                    # TODO change to nds class function 
                    nds.append(s)
                    counter += 1
                    
                    
                if (counter >= Problem.maxNumOfTrials): 
                    break

    

            if (counter >= Problem.maxNumOfTrials):
                break

        return nds;


        
    def __init__(self, trials=100):
        '''
        Constructor
        '''
        self.maxNumOfTrials = trials;

        self.pi = None  #List<Integer> 
        
        