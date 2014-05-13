import matplotlib.pyplot as plt
from math import ceil,sqrt
import numpy as np

class Photon(object):
    
    def __init__(self,frequency,polarization,**kwargs):
        self.tuple = [frequency,polarization]
        self.virtual = False
        self.spectrum = False
        self.dw = None
        self.start_freq = None
        self.end_freq = None
    
        # check if photon is spectrum photon!
        # can add other conditional arguments here as necessary
        for k,v in kwargs.iteritems():
            if(k=="spectrum" and v==True):
                self.spectrum = v
            elif(k=="stepfreq"):
                self.dw = v
            elif(k=="startfreq"):
                self.start_freq = v
            elif(k=="endfreq"):
                self.end_freq = v
    
        if (self.spectrum==True):
            Npoints = int(ceil(float(self.end_freq - self.start_freq)/float(self.dw)))
            self.freq_spectrum = [ i*self.dw for i in range(Npoints) ]
    
    def getTuple(self):
        return self.tuple

    def setTuple(self,new_tuple):
        self.tuple = new_tuple

    def isVirtual(self):
        return self.virtual

    def toggleVirtual(self):
        # if virtual == true, set to false
        # if virtual == false, set to true
        self.virtual = not self.virtual

    def isSpectrum(self):
        return self.spectrum

    def getSpectrum(self):
        return self.freq_spectrum

    def setSpectrum(self,start,end,dw):
        Npoints = int(ceil(float(end - start)/float(dw)))
        self.freq_spectrum = [ start+i*dw for i in range(Npoints) ]

    def toggleSpectrum(self):
        # if spectrum == true, set to false
        # if spectrum == false, set to true
        self.spectrum = not self.spectrum

    def isMatch(self,photon):
        my_tuple = self.getTuple()
        test_tuple = photon.getTuple()
    
        if (my_tuple==test_tuple):
            return True
        else:
            return False

