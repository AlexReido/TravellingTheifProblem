'''
Created on Dec 20, 2020

@author: areid
'''
from algorithms.Algorithm import Algorithm
import random
from main.Solution import Solution
from main.Problem import Problem
from sympy.core.evalf import rnd
from astropy.units import count

class NGTA(Algorithm):
    
    
    # Martyna 
    def generateInitialPopulation(self, n):
        """Generate random population of length N
            Return list of tuple (z, pi)
        """ 
        pop = [] 
        cities = [i for i in range(1,self.numOfCities+1)]
        
        for _ in range(n):
            z = random.choice([0, 1], size=len(self.cityOfItem)) 
            pi = cities.copy()
            random.shuffle(pi)
            
            individual = (z, pi)      
            pop.append(individual)
                                    
        return pop
    
    # Alex 
    def selectTour(self, pop):
        """Tournament selection first given number (6) of individuals randomly drawn from population,
            They are compared to according to thier rank, lowest rank selected, in case of draw 
            first is selected. Do not use crowding distance.
            Return  
        """
        n = 6
        initial = []
        for i in range(n):
            solution = sellectrandom(pop)
            initial.append(solution) 
        ranking = [1] * n
        
        for i in range(n):
            for j in range(n):# 1 if dominates
                if (initial[i].getrelation(initial[j]) == 1):
                    ranking[i] += 1
                
                    
          
    # Alex 
    def crossover(self):
        """ Use the edge operator on the TSP route
            use uniform crossover on the packing plan - each item is selected randomly from parent """
        # edge operator 
         
        return True
    
    # Yudong 
    def mutate(self, preSolution):
        """  mutates a solution of tuple(z , p) 
        Swap mutation for TSP part two random cities swapped
        Bitflip for packing plan random item"""
        return True 

    
    def evaluate(self, children):
        """ loop through all children and return list of solutions"""
        solutions = []
        for child in children:
            solutions.append(Problem.evaluate(self, child.pi, child.z))
        return solutions
    
    
    def updateArchive(self, newSolutions, nds):
        """ adds new solutions to non-dominated set solution is if non-dominated
        loop through solutions, if any solutions in  non-dominated set are now dominated by new solutions then remove them
         """
        dominated = False
        for newSolution in newSolutions:
            for nd in nds:
                # if new solution dominates nd 
                if (newSolution.getrelation(nd) == 1):
                    nds.remove(nd)
                # if new solution is dominated by nd
                elif(newSolution.getrelation(nd) == -1):
                    dominated = True
            if (dominated== False):
                nds.append(newSolution)
        return nds

    def __init__(self, trials=100):
        '''
        Constructor
        '''
        self.maxNumOfTrials = trials;

        self.pi = None  #List<Integer> 
        
    def solve(self, problem):
        generationLimit = 100
        popSize = 10
        # TODO implement non dominated set Class
        nds = [] # non-dominated first rank 
        
        pCurrent = self.generateInitialPopulation(popSize)
        # returns list of tuple (z, pi)
        self.evaluate(pCurrent)
        self.updateArchive(pCurrent)
        
        
        for i in range(generationLimit):
            nextPop = [] 
            while (len(nextPop) < len(pCurrent)):
                parents = self.selecttour(pCurrent)
                children = self.crossover(parents)
                children = self.mutate(children)
                while (children in nextPop): # remove clones 
                    children = self.mutate(children)
            
            self.evaluate(children)
            nextPop = nextPop + children
            self.updateArchive(children, nds)
        
            Pcurrent = nextPop
            
        return nds
            
            
            
            
            