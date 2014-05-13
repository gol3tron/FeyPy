import numpy as np
import math
import matplotlib.pyplot as plt
from Permutation import getPermutations


def calcChi(w, mu, Omega):
    """Calculates the sum over states contribution to the appropriate 
    nonlinearity for the collection of input and output photon frequencies, w,
    the electronic system defined by the transition moments mu and the energy
    levels Omega."""

    
    #Make sure the inputs were entered as numpy arrays
    w = np.array(w,dtype=float)         #Phton info, freq n polariz
    mu = np.array(mu,dtype=float)       #dipole transition moments
    Omega = np.array(Omega,dtype=float) #Energy diff
    
    
    #Constants
    hbar = 1               #hbar
    N  = len(w) - 1        #Photon - 1, nonlinearity
    NumStates = len(mu[0]) #Number of electronic states
    omegasigma = float(w[0,0])    #To begin with
    
    
    
    #Physics Check for consistancy between transitions and energies
    if NumStates != len(Omega)+1:
        print('Err: Inconsistant electronic state information.')
        return 0



    #Determine vector term for first vertex
    if omegasigma >= 0:
        xi = mu[w[0,1], 1:, 0]/(Omega - omegasigma)
    else:
        xi = mu[w[0,1], 1:, 0]/(Omega.conjugate() - omegasigma)
    
    #Dot in from the left each additional propogator matrix
    for i in np.arange(1, N):
        omegasigma += w[i,0]
        prop = np.array(mu[w[i,1],1:,1:] - mu[w[i,1],0,0])
        if omegasigma > 0:
            prop = np.transpose(np.divide(np.transpose(prop),(Omega - omegasigma)))
        else:
            prop = np.transpose(np.divide(np.transpose(prop),(Omega.conjugate() - omegasigma)))
        xi = np.dot(prop, xi)

    #Dot in the last transition, back to the ground state
    xi = np.dot(mu[w[-1,1],0,1:],xi)
    xi = xi / hbar**N
    
    return xi

#def calcChiSpectrum(F,w1,w2,dw,mu,Omega,w):
def calcChiSpectrum(F,freq_list,mu,Omega,w):
    """Graphs Chi varrying only the Fth w, aka w[F]
        
        F  = Fth fixed photon
        freq_list = a list of photons from w1 to w2 in increments of dw"""
    
    w = np.array(w,dtype=float) #Phton info, freq n polariz
    mu = np.array(mu,dtype=float) #dipole transition moments
    Omega = np.array(Omega,dtype=float) #Energy diff
    wlist = np.array(freq_list,dtype=float) # frequency spectrum
   
    N = len(wlist) #number of freq
    Chi = np.zeros(N) #list to store the Chi of each freq

    #Old Code
    #N     = int(math.ceil(float(w2-w1)/float(dw)))
    #wlist = [w1+i*dw for i in range(N)]
    
    
    
    #Calc X for each w
    for i in range(N):
        w[F]   = [wlist[i],w[F,1]]
        #w[F,0]  = wlist[i]
        Chi[i]  = calcChi(w,mu,Omega)
    
    return wlist,Chi

def calcTotalChiSpectrum(F,freq_list,mu,Omega,w):
    """Graphs Chi varrying only the Fth w, aka w[F]
        
        F  = Fth fixed photon
        freq_list = a list of photons from w1 to w2 in increments of dw"""
    
    w = np.array(w,dtype=float) #Photon info, freq n polariz
    mu = np.array(mu,dtype=float) #dipole transition moments
    Omega = np.array(Omega,dtype=float) #Energy diff
    wlist = np.array(freq_list,dtype=float) # frequency spectrum
    
    N = len(wlist) #number of freq
    Chi = np.zeros(N) #list to store the Chi of each freq
    
    #Old Code
    #N     = int(math.ceil(float(w2-w1)/float(dw)))
    #wlist = [w1+i*dw for i in range(N)]
    
    
    #Calc X for each w
    for i in range(N):
        w[F]   = [wlist[i],w[F,1]]
        #w[F,0]  = wlist[i]
        Chi[i]  = calcChiPermutations(w,mu,Omega)
    
    return wlist,Chi


def showChiSpectrum(wlist,Chi):

    #Graphing
    ReChi    = Chi.real                #Re[Chi]
    ImChi    = Chi.imag                #Im[Chi]

    plt.plot(wlist,ReChi,label = r'$Re(X)$')
    plt.plot(wlist,ImChi,label = r'$Im(X)$')
    plt.xlabel(r'$\omega$',fontsize=17)
    plt.ylabel(r'$Susceptibility$',fontsize=17)
    plt.legend(loc='upper right')
    plt.show()

def calcChiPermutations(w, mu, Omega):
    
    w = np.array(w,dtype=float)       #Phton info, freq n polariz
    mu = np.array(mu,dtype=float)      #dipole transition moments
    Omega = np.array(Omega,dtype=float)   #Energy diff
    permutearray = getPermutations(w) #permutations of w
    chi = 0.0
    
    for i in range(len(permutearray)):
        chi += calcChi(permutearray[i], mu, Omega)
    
    return chi


