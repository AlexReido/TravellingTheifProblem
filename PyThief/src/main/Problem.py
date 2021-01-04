'''
Created on Nov 27, 2020

@author: areid
'''
import sys
import os
from collections import deque
from pathlib import Path
import math
from main.Solution import Solution
from cmath import pi


class Problem(object):
    '''
    classdocs
    '''

    def readProblem(self, fileName):
        cwd = os.getcwd()
        #         print("cwd: " + cwd)
        newPath = Path(cwd).parent.parent.parent
        newPath = os.path.join(newPath, "TravellingThief", "src", "main", "resources", (fileName + ".txt"))
        #         print(newPath)
        file = open(newPath, "r")
        line = file.readline()
        while (line):
            if "self NAME" in line:
                self.name = line.split(":")[1].strip()
            elif "KNAPSACK DATA TYPE" in line:
                pass
            elif "DIMENSION" in line:
                self.numOfCities = int(line.split(":")[1].strip())
            elif "NUMBER OF ITEMS" in line:
                self.numOfItems = int(line.split(":")[1].strip())
            elif "RENTING RATIO" in line:
                self.R = float(line.split(":")[1].strip())
            elif "CAPACITY OF KNAPSACK" in line:
                self.maxWeight = int(line.split(":")[1].strip())
            elif "MIN SPEED" in line:
                self.minSpeed = float(line.split(":")[1].strip())
            elif "MAX SPEED" in line:
                self.maxSpeed = float(line.split(":")[1].strip())
            elif "EDGE_WEIGHT_TYPE" in line:
                edgeWeightType = line.split(":")[1].strip()
                if not edgeWeightType == "CEIL_2D":
                    raise ValueError("Only edge weight type of CEIL_2D supported.")
            elif "NODE_COORD_SECTION" in line:
                for i in range(self.numOfCities):
                    line = file.readline()
                    a = line.split();
                    self.coordinates.append([float(a[1].strip()), float(a[2].strip())])



            elif "ITEMS SECTION" in line:
                for i in range(self.numOfItems):
                    line = file.readline()
                    a = line.split()
                    self.profit.append(float(a[1].strip()))
                    self.weight.append(float(a[2].strip()))
                    self.cityOfItem.append(int(a[3].strip()) - 1)

            line = file.readline()
        self.itemsAtCity = []
        for i in range(self.numOfCities):
            self.itemsAtCity.append([])
        for i in range(len(self.cityOfItem)):
            self.itemsAtCity[self.cityOfItem[i]].append(i)

    #         print(self.cityOfItem)
    #         print(self.itemsAtCity)
    #         print(self.profit)
    #         print("len of weights: ", len(self.weight))

    def evaluate(self, pi, z):
        if len(pi) != self.numOfCities or len(z) != self.numOfItems:
            print(str(len(pi)), " ", str(self.numOfCities), " ", str(len(z)), " ", str(self.numOfItems))
            raise RuntimeError("Wrong input for traveling thief evaluation!")
        elif pi[0] != 0:
            raise RuntimeError("Thief must start at city 0")

        time = 0
        p = 0
        weight = 0
        #         print(z)
        #         print(pi)
        for i in range(self.numOfCities):
            city = pi[i]

            for j in self.itemsAtCity[city]:
                if z[j]:
                    weight += self.weight[j]
                    p += self.profit[j]
            #             print(p)
            if weight > self.maxWeight:
                time = sys.float_info.max
                p = -sys.float_info.max
                break

            speed = self.maxSpeed - (weight / self.maxWeight) * (self.maxSpeed - self.minSpeed)

            # increase time by considering the speed - do not forget the way from the last city to the first!
            nextCity = pi[(i + 1) % self.numOfCities]

            distance = math.ceil(self.euclideanDistance(city, nextCity))
            #             print(distance)
            time += distance / speed
            #print(time)

        #         print("profit is: " + str(p))
        singleObjective = p - (self.R * time)
        objectives = [time, -p]
        s = Solution(z, pi, p, time, singleObjective, objectives)
        return s

    #         self.pi = pi
    #         self.z = z
    #

    def euclideanDistance(self, cityA, cityB):
        xdist = self.coordinates[cityA][0] - self.coordinates[cityB][0]
        ydist = self.coordinates[cityA][1] - self.coordinates[cityB][1]
        return math.sqrt((xdist ** 2) + (ydist ** 2))

    def __init__(self):
        '''
        Constructor
        '''
        self.name = ""
        self.numOfCities = -1
        self.numOfItems = -1

        # minimal speed of the salesman
        self.minSpeed = -1

        # maximal speed of the salesman
        self.maxSpeed = -1

        # maximal weight of the knapsack
        self.maxWeight = -1

        # Renting Rate (not needed for multi-objective version)
        self.R = sys.float_info.max  # Double.POSITIVE_INFINITY

        # coordinate where the salesman could visit cities
        self.coordinates = []  # double[][]

        # corresponding city of each item
        self.cityOfItem = []  # int[]

        # the weight of each item
        self.weight = []  # double[]

        # the profit of each item
        self.profit = []  # double[]
