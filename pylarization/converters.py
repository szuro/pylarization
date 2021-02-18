"""
Module with converters for different polarization notations.
"""
import numpy as np
from pylarization.vectors import JonesVector, StokesVector


def jones_to_stokes(jones):
    """
    Converts a single JonesVector instance to a StokesVector
    """
    Ex, Ey = jones.vector
    I = 1
    M = Ex * np.conj(Ex) - Ey * np.conj(Ey)
    C = Ex * np.conj(Ex) + Ey * np.conj(Ey)
    S = (Ex * np.conj(Ex) + Ey * np.conj(Ey)).imag

    return StokesVector(I, M, C, S)

def stokes_to_jones(stokes):
    """
    Converts a single StokesVector instance to a JonesVector
    """
    pass