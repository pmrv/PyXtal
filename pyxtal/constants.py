import numpy as np

# Constants
# ------------------------------
tol_m = 0.3  # seperation tolerance in Angstroms
max1 = 40  # Attempts for generating lattices
max2 = 10  # Attempts for a given lattice
max3 = 10  # Attempts for a given Wyckoff position
max4 = 4  # Attempts for orientation
minvec = 1.0  # minimum vector length
rad = np.pi / 180.0  # converting degrees to radians
deg = 180.0 / np.pi  # converting radians to degrees
pyxtal_verbosity = 1  # constant for printx function
# Max number of atoms per molecule before using fast distance check
max_fast_mol_size = 30
