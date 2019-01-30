"""
Module containing classes describing Jones and Mueller matrices.
Both are used in transforming light polarization states.
It also contains the coherency matrix, which is used to describe polarization.
"""
import numpy as np
import abc
from pylarization.vectors import JonesVector, StokesVector
from pylarization.ellipse import PolarizationEllipse


class _Matrix(abc.ABC):
    """
    Abstract matrix class.
    Not to be used directly.
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

    Parameters
    ----------
    :matrix_:
        2 x 2 matrix representing an optical element.
    """

    _required_shape = (2, 2)
    _vector_class = JonesVector

    def __init__(self, matrix_):
        self._validate_shape(matrix_)
        self._matrix = np.array(matrix_, dtype=complex)


class MuellerMatrix(_Matrix):
    """
    Class describing a light transforming optical object.
    Used when transforming a Stokes vector.

    Parameters
    ----------
    :matrix_:
        4 x 4 matrix representing an optical element.
    """

    _required_shape = (4, 4)
    _vector_class = StokesVector

    def __init__(self, matrix_):
        self._validate_shape(matrix_)
        self._matrix = np.array(matrix_, dtype=float)


class CoherencyMatrix(PolarizationEllipse):
    """
    Coherency matrix class.

    Parameters
    ----------
    :Ixx:
        Product of electric field vector component along the X axis
        and it's conjugated number.
    :Ixy:
        Product of electric field vector component along the X axis
        and conjugated number of the component along the Y axis.
    :Iyx:
        Product of electric field vector component along the Y axis
        and conjugated number of the component along the X axis.
    :Iyy:
        Product of electric field vector component along the Y axis
        and it's conjugated number.

    Attributes
    ----------
    :_matrix:
        Full Coherency Matrix
    """
    def __init__(self, Ixx, Ixy, Iyx, Iyy):
        self._matrix = np.array([[Ixx, Ixy], [Iyx, Iyy]], dtype=complex)
        super().__init__(
                         self._calc_E0x(),
                         self._calc_E0y(),
                         self._calc_phase()
                        )

    def _calc_E0x():
        return np.sqrt(self._matrix.item(0)).real

    def _calc_E0y(self):
        return np.sqrt(self._matrix.item(3)).real

    def _calc_phase(self):
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

    def __add__(self, other):
        matrix = self._matrix + other._matrix
        return CoherencyMatrix.from_matrix(matrix)

    __radd__ = __add__
