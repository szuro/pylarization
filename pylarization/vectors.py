"""
Module containing classes describing Jones and Stokes vectors.
Both are used in describing light polarization.
"""
from pylarization.ellipse import PolarizationEllipse


class JonesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Jones vector.
    """
    def __init__(self, Ex, Ey):
        pass

    def simplify(self):
        pass

    def normalize(self):
        pass


class StokesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Stokes vector.
    """
    pass
