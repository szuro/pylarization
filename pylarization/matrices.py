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

    def __mul__(self, jones):
        product = self._matrix * jones.vector
        new_jones = JonesVector(product[0].item(), product[1].item())
        return new_jones

    def __rmul__(self, jones):
        raise ValueError("Wrong operation order")

    @classmethod
    def from_list(cls, list_):
        return cls(list_[0], list_[1], list_[2], list_[3])


class MuellerMatrix(object):
    pass


class CoherencyMatrix(object):
    pass