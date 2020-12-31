'''
Created on Dec 1, 2020

@author: areid
'''
from main.Problem import Problem


class Algorithm(object):
    
    
    def add(self, solution, nds):
        """
         Add a solution to the non-dominated set
        @param s The solution to be added.
        @param  nds: 
        @return The non dominated solutions
        """
        isAdded = True;
        
        for other in nds:

            rel = solution.getrelation(other)
            # if dominated by or equal in design space
            if (rel == -1 or (rel == 0 and solution.equalsInDesignSpace(other))):
                isAdded = False
                break;
            elif(rel == 1):
                nds.remove(other)

        if (isAdded):
            nds.append(solution)

        return nds;

    def solve(self, problem):
#         problem = problem()
#         print("Sovlving problem "+ str(problem.numOfCities))
        raise NotImplementedError("should be in derived class")