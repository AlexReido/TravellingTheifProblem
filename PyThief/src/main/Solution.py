'''
Created on Dec 2, 2020

@author: areid
'''

class Solution(object):
    '''
    classdocs
    '''
    # TODO implement getrelation for non-dominated sorting
    # TODO implement if two solutions are equal in design space (same tour and packing plan)


    def __init__(self):
        '''
        Constructor
        '''
        # tour of thief
        self.pi = []
        # packing plan list of boolean
        self.z = []
        # Time taken on tour
        self.time = -1.0
        #profit made from tour
        self.profit = -1.0
        # single objective 
        self.singleObjective = -1.0
        # list of objectives (floats)
        self.objectives = []
        
        
    
        
        