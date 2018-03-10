"""
Module containing classes describing Jones and Mueller matrices.
Both are used in transforming light polarization states.
It also contains the coherency matrix, which is used to describe polarization.
"""
import numpy as np
from pylarization.vectors import JonesVector, StokesVector
from pylarization.ellipse import PolarizationEllipse


class _Matrix(object):
    """
    Abstract matrix class.
    """

    _vector_class = None

    def _validate_shape(self, matrix_):
        if matrix_.shape != self._required_shape:
            raise ValueError("Wrong matrix shape")

    def __mul__(self, other):
        if isinstance(other, self._vector_class):
            product = self._matrix * other.vector
            return self._vector_class.from_matrix(product)
        elif isinstance(other, type(self)):
            product = self._matrix * other.matrix
            return type(self)(product)

    def __rmul__(self, other):
        raise ValueError("Wrong operation order")

    @property
    def matrix(self):
        return self._matrix


class JonesMatrix(_Matrix):
    """
    Class describing a light transforming optical object.
    Used when transforming a Jones vector.
    """

    _required_shape = (2, 2)
    _vector_class = JonesVector

    def __init__(self, matrix_):
        self._validate_shape(matrix_)
        self._matrix = np.matrix(matrix_, dtype=complex)


class MuellerMatrix(_Matrix):
    """
    Class describing a light transforming optical object.
    Used when transforming a Stokes vector.
    """

    _required_shape = (4, 4)
    _vector_class = StokesVector

    def __init__(self, matrix_):
        self._validate_shape(matrix_)
        self._matrix = np.matrix(matrix_, dtype=float)


class CoherencyMatrix(PolarizationEllipse):
    """
    Coherency matrix class.
    """
    def __init__(self, Ixx, Ixy, Iyx, Iyy):
        self._matrix = np.matrix([[Ixx, Ixy], [Iyx, Iyy]], dtype=complex)
        super().__init__(self.E0x, self.E0y, self.phase)

    @property
    def E0x(self):
        """Return the value of amplitude along x axis"""
        return np.sqrt(self._matrix.item(0)).real

    @property
    def E0y(self):
        """Return the value of amplitude along y axis"""
        return np.sqrt(self._matrix.item(3)).real

    @property
    def phase(self):
        """
        Return the phase difference of light amplitudes.
        """
        return np.angle(self._matrix.item(1))

    @classmethod
    def from_matrix(cls, matrix_):
        matrix = cls(matrix_.item(0),
                     matrix_.item(1),
                     matrix_.item(2),
                     matrix_.item(3)
                     )
        return matrix

    @property
    def matrix(self):
        return self._matrix
