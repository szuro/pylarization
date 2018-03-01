"""
Module containing classes describing Jones and Mueller matrices.
Both are used in transforming light polarization states.
It also contains the coherency matrix, which is used to describe polarization.
"""
import numpy as np
from pylarization.vectors import JonesVector, StokesVector


class JonesMatrix(object):
    """
    Class describing a light transforming optical object.
    Used when transforming a Jones vector.
    """
    def __init__(self, matrix_):
        self._matrix = np.matrix(matrix_, dtype=complex)

    def __mul__(self, other):
        if isinstance(other, JonesVector):
            product = self._matrix * other.vector
            return JonesVector(product[0].item(), product[1].item())
        elif isinstance(other, JonesMatrix):
            product = self._matrix * other.matrix
            return JonesMatrix(product)

    def __rmul__(self, jones):
        raise ValueError("Wrong operation order")

    @property
    def matrix(self):
        return self._matrix


class MuellerMatrix(object):
    """
    Class describing a light transforming optical object.
    Used when transforming a Stokes vector.
    """
    def __init__(self, matrix_):
        self._matrix = np.matrix(matrix_, dtype=float)

    def __mul__(self, other):
        if isinstance(other, StokesVector):
            product = self._matrix * other.vector
            return StokesVector(product[0].item(),
                                product[1].item(),
                                product[2].item(),
                                product[3].item()
                                )
        elif isinstance(other, MuellerMatrix):
            product = self._matrix * other.matrix
            return MuellerMatrix(product)

    def __rmul__(self, jones):
        raise ValueError("Wrong operation order")

    @property
    def matrix(self):
        return self._matrix



class CoherencyMatrix(object):
    pass
