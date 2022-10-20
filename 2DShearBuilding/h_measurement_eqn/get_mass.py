import numpy as np

# this is to get the mass matrix
def get_mass(m0, DOF):
    return m0*np.identity(DOF)