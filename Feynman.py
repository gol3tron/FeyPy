#Import Modules/CLasses
import Photon
import CalcChi
import Permutation
import Diagram
import LaTeX
import itertools

#Import Libraries
import matplotlib.pyplot as plt
import numpy as np

class Feynman(object):
    
    def __init__(self):
        self.photon_list = []
        self.linkedMol = None
        self.latex_string = ''
    
    def linkMolecule(self,molecule):
        self.linkedMol = molecule
    
    def getLinkedMolecule(self):
        return self.linkedMol

    def getChi(self):
        # use this method expressly to get nonlinearity for single diagram for either
        # spectrum or specific set of frequencies
        freq_list  = self.getTupleSet()
        mu_list    = self.getLinkedMolecule().getMu()
        Omega_list = self.getLinkedMolecule().getOmegas()
        photons = self.getPhotonList()
        
        # are there any "spectrum" photons? if so, need to use calcChiSpectrum()
        # else, for only fixed photons, use calcChi()
        # FIRST: Check for spectrum photons!
        
        num_spectrum_photons = 0
        spectrum_photon_index = []
        
        for p in range(len(photons)):
            if (photons[p].isSpectrum() is True):
                # found a spectrum photon, save it's index
                num_spectrum_photons += 1
                spectrum_photon_index.append(p)
        
        
        # SECOND: If no spectrum photons, get single valued Chi
        
        if(num_spectrum_photons==0):
            return CalcChi.calcChi(freq_list, mu_list, Omega_list)
        
        # THIRD: If only one spectrum photon, get Chi spectrum
        
        elif(num_spectrum_photons==1):
            freq_spectrum = photons[spectrum_photon_index[0]].getSpectrum()
            wlist,chi = CalcChi.calcTotalChiSpectrum(spectrum_photon_index[0],freq_spectrum,mu_list,Omega_list,freq_list)
            return wlist,chi
        
        # FOURTH: If more than one spectrum photon, return 0 (for now)
        
        else:
            # This will return data to make a 3D plot (featuring a 2D chi surface)
            return 0

    def getTotalChi(self):
        # use this method expressly to get total nonlinearity for either
        # spectrum or specific set of frequencies
        freq_list  = self.getTupleSet()
        mu_list    = self.getLinkedMolecule().getMu()
        Omega_list = self.getLinkedMolecule().getOmegas()
        photons = self.getPhotonList()
        
        # are there any "spectrum" photons? if so, need to use calcChiSpectrum()
        # else, for only fixed photons, use calcChi()
        # FIRST: Check for spectrum photons!
        
        num_spectrum_photons = 0
        spectrum_photon_index = []
        
        for p in range(len(photons)):
            if (photons[p].isSpectrum() is True):
                # found a spectrum photon, save it's index
                num_spectrum_photons += 1
                spectrum_photon_index.append(p)
        
        
        # SECOND: If no spectrum photons, get single valued Chi
        
        if(num_spectrum_photons==0):
            return CalcChi.calcChiPermutations(freq_list, mu_list, Omega_list)
        
        # THIRD: If only one spectrum photon, get Chi spectrum
        
        elif(num_spectrum_photons==1):
            freq_spectrum = photons[spectrum_photon_index[0]].getSpectrum()
            wlist,chi = CalcChi.calcTotalChiSpectrum(spectrum_photon_index[0],freq_spectrum,mu_list,Omega_list,freq_list)
            return wlist,chi
        
        # FOURTH: If more than one spectrum photon, return 0 (for now)
        
        else:
            # This will return data to make a 3D plot (featuring a 2D chi surface)
            return 0
    
    def getLaTeX(self):
        self.updateLaTeX()
        return self.latex_string
    
    def showLaTeX(self):
        self.updateLaTeX()
        plt.text(7.0,8.0,'$%s$'%self.latex_string)

    def updateLaTeX(self):
        freq_list = self.getTupleSet()  #list of frequency,polarization tuples
        chi_string = LaTeX.latex(freq_list)
        self.latex_string = chi_string
    
    def showDiagram(self,**kwargs):
        
        showtex = False
        
        # check if photon is spectrum photon!
        # can add other conditional arguments here as necessary
        for k,v in kwargs.iteritems():
            if(k=="latex" and v==True):
                showtex = True
            else:
                showtex = False
    
        freq_list = self.getTupleSet()
        Diagram.diagram(freq_list)
        if(showtex == True):
            self.showLaTeX()

    def showDiagSet(self):
        
        feyn_list = self.getPermutedFeynmans()
        n_diagrams = len(feyn_list)
    
        for i in range(n_diagrams):
            feyn_list[i].showDiagram()
    

    def addPhoton(self,photon):
        self.photon_list.append(photon)
    
    def remPhoton(self):
        self.photon_list.remove(self.photon_list[-1])

    def getPhotonList(self):
        return self.photon_list

    def getPermutedFeynmans(self):
        # This method finds all possible permutaions of a list of photon
        # objects, returns a list of Feynman objects, each with a different
        # possible permutation
        
        feyn_list = []  #list of feynman diagrams
        photon_list = self.getTupleSet()
        N_photons = len(photon_list)

        permuted_photons = Permutation.getPermutations(photon_list)
        N_permutations = len(permuted_photons)

        # create list of feynman objects for each permutation
        for i in range(N_permutations):
            temp_feyn = Feynman()   #new feynman diagram
            for j in range(N_photons):
                # generate temp_photon from permutation
                temp_tuple = permuted_photons[i][j]
                temp_photon = Photon.Photon(temp_tuple[0],temp_tuple[1])
                #add new photon to new feynman diagram
                temp_feyn.addPhoton(temp_photon)
            
            # make Omegas and Mus consistent for all permutations of feyn
            temp_feyn.linkMolecule(self.linkedMol)
            
            # add new feynman diagram to list of feynman diagrams
            feyn_list.append(temp_feyn)

        return feyn_list

    def getTupleSet(self):
        # This method generates a list of tuples from self.photon_list
        
        tuple_set = []
        photons = self.getPhotonList()
        N_photons = len(photons)
        
        for i in range(N_photons):
            tuple_set.append(photons[i].getTuple())
        
        return tuple_set

