"""
Module containing classes describing Jones and Mueller matrices.
Both are used in transforming light polarization states.
It also contains the coherency matrix, which is used to describe polarization.
"""
import numpy as np
from pylarization.vectors import JonesVector, StokesVector


class JonesMatrix(object):
    def __init__(self, a11, a12, a21, a22):
        self._matrix = np.matrix([[a11, a12], [a21, a22]], dtype=complex)

    def __mul__(self, other):
        if isinstance(other, JonesVector):
            product = self._matrix * other.vector
            return JonesVector(product[0].item(), product[1].item())
        elif isinstance(other, JonesMatrix):
            product = self._matrix * other.matrix
            return JonesMatrix.from_matrix(product)

    def __rmul__(self, jones):
        raise ValueError("Wrong operation order")

    @classmethod
    def from_list(cls, list_):
        return cls(list_[0], list_[1], list_[2], list_[3])

    @classmethod
    def from_matrix(cls, matrix_):
        a11, a12 = matrix_.tolist()[0]
        a21, a22 = matrix_.tolist()[1]
        return cls(a11, a12, a21, a22)

    @property
    def matrix(self):
        return self._matrix


class MuellerMatrix(object):
    pass


class CoherencyMatrix(object):
    pass
