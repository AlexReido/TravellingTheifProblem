"""
Created on Dec 3, 2020

@author: areid
"""
from pathlib import Path
import os
import sys


class Competition(object):

    def __init__(self):
        self.TEAM_NAME = "EPSILON";

    def numberofSolutions(self, problem):
        """
           return Number of solutions to be submitted for the corresponding problem
        """
        name = problem.name
        if "a280" in name:
            return 100
        elif "fnl4461" in name:
            return 50
        elif "pla33810" in name:
            return 20
        else:
            return sys.maxsize

    def writeSolutions(self, problem, solutions, teamName="Epsilon"):
        numberofSolutions = self.numberofSolutions(problem)

        if len(solutions) > numberofSolutions:
            print("WARNING: Finally the competition allows only" + str(numberofSolutions) +
                  " solutions to be submitted. " + "\nYour algorithm found " +
                  str(len(solutions)) + " solutions.")

        cwd = os.getcwd()
        newPath = Path(cwd).parent.parent.parent

        varPath = os.path.join(newPath, "TravellingThief", "results", (teamName + problem.name + ".x"))
        varFile = open(varPath, "w")

        objPath = os.path.join(newPath, "TravellingThief", "results", (teamName + problem.name + ".f"))
        objFile = open(objPath, "w")

        for solution in solutions:
            modTour = [(c + 1) for c in solution.pi]
            pi = "".join((str(c) + " ") for c in modTour) + "\n"
            varFile.write(pi)
            z = map(lambda item: "1" if item else "0", solution.z)
            z = "".join((item + " ") for item in list(z)) + "\n"
            varFile.write(z)
            varFile.write('\n')

            # write into objective file
            objFile.write(("%.16f" % solution.time) + " " + ("%.16f" % solution.profit) + "\n")

        varFile.close()
        objFile.close()
