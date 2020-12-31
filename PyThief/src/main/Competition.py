'''
Created on Dec 3, 2020

@author: areid
'''
from pathlib import Path
import os

class Competition(object):

    def __init__(self):
        
        self.TEAM_NAME = "EPSILON";
    
    
    def numberofSolutions(self, problem):
        """
           return Number of solutions to be submitted for the corresponding problem
        """
        name = problem.name;
        if (name.contains("a280")): 
            return 100;
        elif (name.contains("fnl4461")):
            return 50;
        elif (name.contains("pla33810")): 
            return 20;
        else: 
            return int.__ceil__();
    
    
   
    
    
    
    def writeSolutions(self, outputFolder, teamName="Epsilon", problem, solutions):  
        numberofSolutions = self.numberofSolutions(problem)
        if (len(solutions) > numberofSolutions):
            print("WARNING: Finally the competition allows only" + str(numberofSolutions) + 
                  " solutions to be submitted. " +  "\nYour algorithm found " +
                  str(len(solutions)) + " solutions.")
            
            
        cwd = os.getcwd()
        newPath = Path(cwd).parent.parent.parent
        varPath = os.path.join(newPath,"TravellingThief", "results", (teamName + problem.name+".x"))
        varFile = open(varPath, "w")
        objPath = os.path.join(newPath,"TravellingThief", "results", (teamName + problem.name+".f"))
        objFile = open(objPath, "w")
        
#         print(newPath)
        
        for solution in solutions:
            modTour = [(c + 1) for c in solution.pi]
            pi = "".join((str(c)+" ") for c in modTour)
            varFile.write(pi)
            z = "".join((str(item)+" ") for item in solution.z)
            varFile.write(z)
            varFile.write('\n')
            
            #write into objective file
            objFile.write(("%.2f" % solution.time)+ " " +  ("%.2f" % solution.profit))
        varFile.close()
        objFile.close()
# 
#         varBw.close();
#         objBw.close();
# 
# 
# 
#     }