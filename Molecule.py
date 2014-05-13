import numpy as np

class Molecule(object):
    
    def __init__(self):
        self.orientation = np.array([0.0,0.0,0.0])
        self.position = np.array([0.0,0.0,0.0])
        self.mu = []
        self.Omega_list = []
    
    def setPosition(self,x,y,z):
        self.position = np.array([x,y,z],dtype=float)
    
    def getPosition(self):
        return self.position
    
    def setOrientation(self,rho,theta,phi):
        self.orientation = np.array([rho,theta,phi],dtype=float)
    
    def getOrientation(self):
        return self.orientation
    
    def setMu(self,new_mu):
        self.mu = np.array(new_mu,dtype=float)
    
    def getMu(self):
        return self.mu
    
    def addOmega(self,new_Omegas):
        new_Omegas = np.array(new_Omegas,dtype=float).flatten()
        [self.Omega_list.append(new_Omegas[i]) for i in range(len(new_Omegas))]

    def getOmegas(self):
        return np.array(self.Omega_list,dtype=float)