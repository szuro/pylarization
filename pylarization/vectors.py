"""
Module containing classes describing Jones and Stokes vectors.
Both are used in describing light polarization.
"""
import numpy as np
from pylarization.ellipse import PolarizationEllipse


class JonesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Jones vector.
    """
    def __init__(self, Ex, Ey):
        self._vector = np.matrix([[Ex], [Ey]], dtype=complex)

    @property
    def vector(self):
        """
        Return full Jones vector.
        """
        return self._vector[0].item(), self._vector[1].item()

    def simplify(self):
        pass

    def normalize(self):
        pass


class StokesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Stokes vector.
    """
    pass
