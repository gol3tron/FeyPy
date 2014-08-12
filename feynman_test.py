import Feynman
import Photon
import CalcChi
import Permutation
import Molecule
import Cascade
import numpy as np

#create feynman object
feyn = Feynman.Feynman()

#create photons
photon1 = Photon.Photon(1,0)
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

# show feynman diagram
feyn.showDiagram()

# check out the latex code!
# we can either render it on a figure:
feyn.showLaTeX()

# or we can return it as a string for easy copying into TeX editors
feyn.getLaTeX()

# getChi!
feyn.getChi()

# test out permutations
# returns a set of feynman diagrams with photon frequency,polarization
# tuples permuted according to Kyle's permutations code
list_of_feynmans = feyn.getPermutedFeynmans()
feyn.showDiagSet()


