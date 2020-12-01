'''
Created on Nov 27, 2020

@author: areid
'''
from astropy.wcs.docstrings import name
import sys
import os
from pathlib import Path
class Problem(object):
    '''
    classdocs
    '''
    def readProblem(self, fileName):
        cwd = os.getcwd()
        print("cwd: " + cwd)
        newPath = Path(cwd).parent.parent
        newPath = os.path.join(newPath,"gecco19-thief-master", "src", "main", "resources", (fileName+".txt"))
        print(newPath)
        file = open(newPath,"r")
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
                    self.cityOfItem.append(float(a[3].strip()) - 1)
        

            line = file.readline()
        
        

    def __init__(self):
        '''
        Constructor
        '''
        self.name = name
        self.numOfCities = -1
        self.numOfItems = -1;

        # minimal speed of the salesman
        self.minSpeed = -1
    
        # maximal speed of the salesman
        self.maxSpeed = -1
    
        # maximal weight of the knapsack
        self.maxWeight = -1
    
        # Renting Rate (not needed for multi-objective version)
        self.R = sys.float_info.max#Double.POSITIVE_INFINITY
    
        # coordinate where the salesman could visit cities
        self.coordinates = [] # double[][]
    
        # corresponding city of each item
        self.cityOfItem = [] #int[] 
        
        # the weight of each item
        self.weight = [] # double[] 
    
        # the profit of each item
        self.profit = [] #double[] 
        
        


p = Problem()
p.readProblem("a280-n279")

print("number of items: ", p.numOfItems)
print("coordinates: ", p.coordinates)

"""
     /**
     * This is used for non-dominated sorting and returns the dominance relation
     * @param other solution to compare with
     * @return returns 1 if dominates, -1 if dominated and 0 if indifferent
     */
    public int getRelation(Solution other) {
        int val = 0;
        for (int i = 0; i < objectives.size(); i++) {

            if (objectives.get(i) < other.objectives.get(i)) {
                if (val == -1) return 0;
                val = 1;
            } elif (objectives.get(i) > other.objectives.get(i)) {
                if (val == 1) return 0;
                val = -1;
            }

        }

        return val;

    }

    /**
     * @param other solution to compare with
     * @return True if tour and packing plan is equal
     */
    public boolean equalsInDesignSpace(Solution other) {
        return pi.equals(other.pi) && z.equals(other.z);
    }
    """