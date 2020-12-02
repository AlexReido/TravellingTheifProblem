'''
Created on Dec 1, 2020

@author: areid
'''
from algorithms.Algorithm import Algorithm
import random

class RandomLocalSearch(Algorithm):
    '''
    classdocs
    '''
    def solve(self, Problem):
        counter = 0
        nds = 0 # non-dominated set
        
        while True:
            if (self.pi == None):
                pi = random.choices(range(1, Problem.numOfCities), Problem.numOfCities)
                pi.insert(0, 0)
            else:
                pi = self.pi
                
            z = [False]*Problem.numOfCities #Packing plan
            
            
            
        return n


        
    def __init__(self, trials=100):
        '''
        Constructor
        '''
        self.maxNumOfTrials = trials;

        self.pi = None  #List<Integer> 
        
        