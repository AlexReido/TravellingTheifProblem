'''
Created on Dec 20, 2020

@author: areid
'''
from algorithms.Algorithm import Algorithm
import random
from main.Solution import Solution
from main.Problem import Problem
from _collections import defaultdict
import sys


class NGTA(Algorithm):

    # Martyna 
    def generateInitialPopulation(self, n, problem):
        """Generate random population of length N
            Return list of tuple (z, pi)
        """
        pop = []
        cities = [i for i in range(1, problem.numOfCities)]

        for _ in range(n):
            z = random.choices([False, True], weights=[0.9, 0.1], k=problem.numOfItems)
            pi = cities.copy()
            random.shuffle(pi)
            pi.insert(0, 0)
            individual = (z, pi)
            pop.append(individual)

        return pop

    # Alex
    def selectTour(self, pop):
        """Tournament selection first given number (6) of individuals randomly drawn from population,
            They are compared to according to thief rank, lowest rank selected, in case of draw
            first is selected. Do not use crowding distance.
            Return  
        """
        n = 6
        initial = random.sample(pop, n)
        ranking = [1] * n

        for i in range(n - 1):
            for j in range(i + 1, n):  # 1 if dominates
                # if i dominates j 
                if initial[i].getrelation(initial[j]) == 1:
                    ranking[j] += 1
                # if j dominates i 
                elif initial[i].getrelation(initial[j]) == -1:
                    ranking[i] += 1

        minx = 20
        for i, rank in enumerate(ranking):
            if rank < minx:
                minx = rank
                index = i
        return initial[index]

    # Alex 
    def crossover(self, parentA, parentB):
        """ Use the edge operator on the TSP route
            use uniform crossover on the packing plan - each item is selected randomly from parent """
        # edge operator 

        tourA = parentA.pi
        tourB = parentB.pi
        cityLen = len(tourA)
        edgeMap = defaultdict(list)

        for c in range(cityLen):
            edgeMap.setdefault(c, [])

        edgeMap[tourA[0]].append(tourA[-1])
        edgeMap[tourB[0]].append(tourB[-1])
        edgeMap[tourA[-1]].append(tourA[0])
        edgeMap[tourB[-1]].append(tourB[0])

        for i, c in enumerate(tourA[0:-2]):
            edgeMap[c].append(tourA[i + 1])
            edgeMap[tourA[i + 1]].append(c)

        for i, c in enumerate(tourB[0:-2]):
            edgeMap[c].append(tourB[i + 1])
            edgeMap[tourB[i + 1]].append(c)

        currentCity = 0
        newTour = [currentCity]

        while len(edgeMap.keys()) > 1:
            currentCityEdgelist = edgeMap.pop(currentCity)

            if currentCityEdgelist == []:
                nextCity = random.choice(list(edgeMap.keys()))
            else:
                # Chooses the city with fewest edges from the current cities neighbours.
                # TODO random on equal
                min = sys.maxsize
                for city in currentCityEdgelist:
                    edgeMap[city].remove(currentCity)
                    #                 edgeMap[city].remove()
                    #                     if (not city in newTour):
                    if (len(edgeMap[city]) < min):
                        min = len(edgeMap[city])
                        nextCity = city
            currentCity = nextCity
            newTour.append(currentCity)

        newPackingPlan = []
        packingPlanA = parentA.z
        packingPlanB = parentB.z
        itemLen = len(packingPlanA)

        for i in range(itemLen):
            if random.randrange(1) == 1:
                newPackingPlan.append(packingPlanA[i])
            else:
                newPackingPlan.append(packingPlanB[i])

        return (newPackingPlan, newTour)

        # Yudong

    #     def mutate(self, preSolution):
    #         """  mutates a solution of tuple(z , pi)
    def mutate(self, preSolution, chance_of_mutation):
        """  mutates a solution of tuple(z , p) 
        Swap mutation for TSP part two random cities swapped
        Bitflip for packing plan random item"""

        newTour = preSolution[1]
        selectedForSwap = random.choices(newTour[1:], k=2)

        index0 = newTour.index(selectedForSwap[0])
        index1 = newTour.index(selectedForSwap[1])

        newTour[index0] = selectedForSwap[1]
        newTour[index1] = selectedForSwap[0]

        newPackingPlan = []
        for x in range(len(preSolution[0])):
            if random.random() < chance_of_mutation:
                newPackingPlan.append(preSolution[0][x])
            else:
                newPackingPlan.append(random.choice([False, True]))
        #         mutated.append((newPackingPlan, newTour))
        return (newPackingPlan, newTour)  # mutated

    def evaluate(self, children, problem):
        """ loop through all children and return list of solutions"""
        solutions = []

        for child in children:
            solutions.append(problem.evaluate(child[1], child[0]))

        return solutions

    def updateArchive(self, newSolutions, nds):
        """ adds new solutions to non-dominated set solution is if non-dominated
        loop through solutions, if any solutions in  non-dominated set are now dominated by new solutions then remove them
         """
        dominated = False
        for newSolution in newSolutions:
            for nd in nds:
                # if new solution dominates nd 
                if newSolution.getrelation(nd) == 1:
                    nds.remove(nd)
                # if new solution is dominated by nd
                elif newSolution.getrelation(nd) == -1:
                    dominated = True

            if dominated == False:
                nds.append(newSolution)

        return nds

    def __init__(self, trials=100):
        """
        Constructor
        """
        self.maxNumOfTrials = trials

        self.pi = None  # List<Integer>

    def solve(self, problem):
        generationLimit = 1000
        popSize = 10
        # TODO implement non dominated set Class
        nds = []  # non-dominated first rank

        pCurrent = self.generateInitialPopulation(popSize, problem)

        pCurrent = self.evaluate(pCurrent, problem)
        nds = self.updateArchive(pCurrent, nds)

        for i in range(generationLimit):
            print("Generation ", str(i))
            nextPop = []
            while len(nextPop) < len(pCurrent):
                parentA = self.selectTour(pCurrent)
                parentB = self.selectTour(pCurrent)

                while parentA == parentB:
                    parentB = self.selectTour(pCurrent)

                child = self.crossover(parentA, parentB)
                child = self.mutate(child, 0.98)

                while child in nextPop:  # remove clones
                    child = self.mutate(child, 0.98)
                child = problem.evaluate(child[1], child[0])
                nextPop.append(child)

                nds = self.updateArchive(nextPop, nds)

            pCurrent = nextPop

        return nds
