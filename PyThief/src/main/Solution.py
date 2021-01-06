'''
Created on Dec 2, 2020

@author: areid
'''


class Solution(object):
    """
    classdocs
    """

    # TODO implement getrelation for non-dominated sorting
    # TODO implement if two solutions are equal in design space (same tour and packing plan)
    def __init__(self, z, pi, profit, time, singleObjective, objectives):
        self.z = z
        self.pi = pi
        self.profit = profit
        self.time = time

        # single objective 
        self.singleObjective = singleObjective
        # list of objectives (floats)
        self.objectives = objectives


    def getrelation(self, other):
        """    This is used for non-dominated sorting and returns the dominance relation between objectives
         return returns 1 if objective dominates, -1 if objective is dominated and 0 if objectives are indifferent
        """
        val = 0
        for i in range(len(self.objectives)):
            if self.objectives[i] < other.objectives[i]:
                if val == -1:
                    return 0
                val = 1
            elif self.objectives[i] > other.objectives[i]:
                if val == 1:
                    return 0
                val = -1
            else:
                return 0
        return val

    def equalsInDesignSpace(self, otherSolution):
        """
        @param other solution to compare with
        @return True if tour and packing plan is equal
        """
        if self.pi == otherSolution.pi and self.z == otherSolution.z:
            return True
        else:
            return False
