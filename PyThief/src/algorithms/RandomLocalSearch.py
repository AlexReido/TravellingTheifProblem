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
    def solve(self, problem):
        counter = 0
    
        nds = [] # non-dominated set
        print("max weight = " + str(problem.maxWeight))
        while True:
            if (self.pi == None):
                pi = list(range(1, problem.numOfCities))
#                 print(pi)
                random.shuffle(pi)
#                 print(pi)
                pi.insert(0, 0)
            else:
                pi = self.pi
                
            z = [False]*problem.numOfItems #Packing plan
       
            counter += 1
            rnd = list(range(1, problem.numOfCities-1))
            random.shuffle(rnd)
#             print(len(rnd))
#             assert problem.numOfCities == len(rnd)
            weight = 0.0
            for j in range(len(rnd)):
                item = rnd[j]
#                 print(z[item])
#                 print(counter)
                if ((weight + problem.weight[item]) < problem.maxWeight ):
#                     print("item ", item)
                    z[item] = True
#                     
                    weight += problem.weight[item]
                    
#                     print(weight)
#                     print("ndslen:" + str(len(nds)))
                    
                    #TODO add parameter to limit number of trials
            
            
            
            s = problem.evaluate(pi, z)
            nds = super().add(s, nds)

            if (counter >= 500):#problem.maxNumOfTrials
                break

        return nds;


        
    def __init__(self, trials=100):
        '''
        Constructor
        '''
        self.maxNumOfTrials = trials;

        self.pi = None  #List<Integer> 
        
        