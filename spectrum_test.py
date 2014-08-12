import Feynman
import Photon
import CalcChi
import Permutation
import Molecule
import Cascade
import numpy as np

feyn = Feynman.Feynman()

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

# show feynman diagram
feyn.showDiagram()

# getChi!
chi = feyn.getChi()
CalcChi.showChiSpectrum(chi[0],chi[1])


