"""
Module containing classes describing Jones and Stokes vectors.
Both are used in describing light polarization.
"""
from pylarization.ellipse import PolarizationEllipse


class JonesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Jones vector.
    """
    pass


class StokesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Stokes vector.
    """
    pass
