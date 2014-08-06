import matplotlib.pyplot as plt
from math import ceil,sqrt
import numpy as np
import Feynman
import operator
import Diagram

class Cascade(object):
    
    def __init__(self):
        self.list_of_feynmans = []
        self.latex_string = ''
    
    def addFeynman(self,feyn):
        self.list_of_feynmans.append(feyn)
    
    def getFeynmanList(self):
        return self.list_of_feynmans

    def showDiagram(self):
        tuple_sets = []
        N_feynmans = len(self.list_of_feynmans)
        photon_lists = []
        vert_num = 0
        
        for i in range(N_feynmans):
            temp_photon_list = self.list_of_feynmans[i].getPhotonList()
            temp_tuple_set = self.list_of_feynmans[i].getTupleSet()
            photon_lists.append(temp_photon_list)
            tuple_sets.append(temp_tuple_set)
            
            for j in range(len(temp_photon_list)):
                if(temp_photon_list[j].isVirtual()):
                    tuple_sets[i][j][1] = 3
    
        if(N_feynmans==2):
            for i in range(len(photon_lists[-1])):
                if(photon_lists[-1][i].isVirtual()):
                    vert_num = i
        
#        return tuple_sets,vert_num,photon_lists

        Diagram.chain_diagram(tuple_sets[0],tuple_sets[1],0,vert_num)

    def getPermutedCascade(self):
        # get permutations for individual feynmans
        feyn_perm_sets = []
        N_feynmans = len(self.list_of_feynmans)
        num_perms = []
        casc_perms = []
        
        for i in range(N_feynmans):
            temp_perms = self.list_of_feynmans[i].getPermutedFeynmans()
            feyn_perm_sets.append(temp_perms)
            num_perms.append(len(temp_perms))
        
        
        for i in range(len(feyn_perm_sets[0])):
            temp_casc = Cascade.Cascade()
            temp_casc.addFeynman(feyn_perm_sets[0][i])
        
            for j in range(1,N_feynmans):
                for k in range
        
        

#       this total_num_permuations is the total number of permuations of
#       all feynman diagrams that are unique cascade diagrams
#       the total number of permutations is equal to the product of the number
#       of unique permutations of the individual feynman diagrams that make up
#       the original cascade object
        total_num_permuations = reduce(operator.mul,num_perms)



    def getPermutations(self):
        return 0

    def getLaTeX(self):
        # to be written
        return 0
    
    def showLaTeX(self):
        # to be written
        return 0