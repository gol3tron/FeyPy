import Feynman
import Photon
import CalcChi
import Permutation
import Molecule
import Cascade
import numpy as np

feyn = Feynman.Feynman()

useFixed = True #set to false for fixed frequency photons

if(useFixed is True):
    # testing fixed frequency photons
    photon1 = Photon.Photon(1,0)
    photon2 = Photon.Photon(1,0)
    photon3 = Photon.Photon(-2,0)
    photon4 = Photon.Photon(1,0)
    photon5 = Photon.Photon(-1,0)

else:
    # testing spectrum frequency photons
    photon1 = Photon.Photon(1,0,spectrum=True,stepfreq=0.001,startfreq=0.0,endfreq=5.0)
    photon2 = Photon.Photon(1,0)
    photon3 = Photon.Photon(-2,0)


# make a molecule!
molecule = Molecule.Molecule()

# define mu's
mu = np.array([[[0, 1, 2],
                [1, 2, 3],
                [2, 3, 4]],
               
               [[0, 1, 2],
                [1, 2, 3],
                [2, 3, 4]],
               
               [[0, 1, 2],
                [1, 2, 3],
                [2, 3, 4]]])

# add Mu matrix to molecule
molecule.setMu(mu)

# add omega's to molecule
molecule.addOmega([1.5,2.5])

# link molecule to Feynman object
feyn.linkMolecule(molecule)

# add vertices to diagram
feyn.addPhoton(photon1)
feyn.addPhoton(photon2)
feyn.addPhoton(photon3)
feyn.addPhoton(photon4)
feyn.addPhoton(photon5)

# show feynman diagram
#feyn.showDiagram()

# check out the latex code!
# we can either render it on a figure:
#feyn.showLaTeX()

# or we can return it as a string for easy copying into TeX editors
#feyn.getLaTeX()

# getChi!
#if(useFixed is True):
#    chi = feyn.getChi()
#    print(chi)
#
#else:
#    a = feyn.getChi()
#CalcChi.showChiSpectrum(wlist,chi)


# test out permutations
# returns a set of feynman diagrams with photon frequency,polarization
# tuples permuted according to Kyle's permutations code
#list_of_feynmans = feyn.getPermutedFeynmans()
#feyn.showDiagSet()

# make phton3 virtual
photon5.toggleVirtual()
photon3.toggleVirtual()

# make some more photons
photon6 = Photon.Photon(1,0)
photon7 = Photon.Photon(1,0)
photon8 = Photon.Photon(-2,0)

photon6.toggleVirtual()
photon7.toggleVirtual()

next_feyn = Feynman.Feynman()
next_feyn.addPhoton(photon6)
next_feyn.addPhoton(photon7)
next_feyn.addPhoton(photon8)

list_of_feynmans = feyn.getPermutedFeynmans()
list_of_feynmans_next = next_feyn.getPermutedFeynmans()

next_feyn.linkMolecule(molecule)

# make a cascade object
cascade = Cascade.Cascade()

# add feynman objects to cascade
cascade.addFeynman(feyn)
cascade.addFeynman(next_feyn)

# show cascaded diagram
cascade.showDiagram()

