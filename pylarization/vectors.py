"""
Module containing classes describing Jones and Stokes vectors.
Both are used in describing light polarization.
"""
import numpy as np
from pylarization.ellipse import PolarizationEllipse


class JonesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Jones vector.

    Parameters
    ----------
    :Ex:
        Scalar component of electric field vector along the X axis.
    :Ey:
        Scalar component of electric field vector along the Y axis.

    Attributes
    ----------
    :_vector:
        Full Jones Vector.
    :_x_phase:
        Absolute phase of the Ex component.
    :_y_phase:
        Absolute phase of the Ey component.
    """
    def __init__(self, Ex, Ey):
        self._vector = np.array([[Ex], [Ey]], dtype=complex)
        self._x_phase = np.angle(Ex)
        self._y_phase = np.angle(Ey)
        super().__init__(
                         self._get_amplitude(0),
                         self._get_amplitude(1),
                         self._y_phase - self._x_phase
                        )

    @classmethod
    def from_matrix(cls, matrix_):
        vector = cls(matrix_.item(0),
                     matrix_.item(1)
                     )
        return vector

    @property
    def vector(self):
        """
        Return full Jones vector.
        """
        return self._vector

    def _simplify(self):
        """
        Method for transforming Jones vector to its simplified version.
        Simplification is required to calculate phase.
        """
        asqrt = np.abs(self._vector[0])
        if asqrt == 0.0:
            asqrt = 1
        a = self._vector[0] / asqrt
        if np.isnan(a) or a == 0.0:
            a = 1.0
        np.divide(self._vector, a, out=self._vector)

    def normalize(self):
        """
        Normalizes a vector by dividing each part by common number.
        After normalization the magnitude should be equal to ~1.
        """
        absW2 = np.abs(self._vector[0])**2 + np.abs(self._vector[1])**2
        if absW2 == 0:
            absW2 = 1
        np.divide(self._vector, np.sqrt(absW2), out=self._vector)
        super().__init__(
                         self._get_amplitude(0),
                         self._get_amplitude(1),
                         self._y_phase - self._x_phase
                        )

    def _get_amplitude(self, index):
        """
        Returns the amplitude along specified axis.
        Amplitudes are always real.
        """
        return np.abs(
                self._vector[index]
            ).item().real

    def __add__(self, other):
        vector = self.vector + other.vector
        return JonesVector.from_matrix(vector)

    __radd__ = __add__


class StokesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Stokes vector.

    Parameters
    ----------
    :I:
        Intensity of the light beam. Sometimes described as S_0.
    :M:
        Similarity of a beam to a light to a linearly polarized beam
        oriented horizontally. Sometimes described as S_1 or Q.
    :C:
        Similarity to a right-hand polarized beam.
        Sometimes described as S_2 or U.
    :S:
        Describes the circularity of polarization.
        Sometimes described as S_3 or V.

    Attributes
    ----------
    :_vector:
        Full Stokes Vector.
    """
    def __init__(self, I, M, C, S):
        self._vector = np.array([[I], [M], [C], [S]], dtype=float)
        super().__init__(
                         self._calc_E0x(),
                         self._calc_E0y(),
                         self._calc_phase()
                        )

    @classmethod
    def from_matrix(cls, matrix_):
        vector = cls(matrix_.item(0),
                     matrix_.item(1),
                     matrix_.item(2),
                     matrix_.item(3)
                     )
        return vector

    @property
    def vector(self):
        """
        Return full Stokes vector.
        """
        return self._vector

    def _calc_E0x(self):
        return np.sqrt(
            (self._vector[0] +
             self._vector[1]) / 2
            ).item()

    def _calc_E0y(self):
        return np.sqrt(
            (self._vector[0] -
             self._vector[1]) / 2
            ).item()

    def _calc_phase(self):
        """
        Calculates the phase difference.
        """
        return np.arctan2(self._vector[3], self._vector[2]).item()

    def normalize(self):
        """
        Normalizes a vector by dividing each part by common number.
        After normalization the magnitude should be equal to ~1.
        """
        np.divide(self._vector, self._vector[0], out=self.vector)
        super().__init__(
                         self._calc_E0x(),
                         self._calc_E0y(),
                         self._calc_phase()
                        )

    def __str__(self):
        return "I={}, M={}, C={}, S={}".format(
            self._vector[0].item(),
            self._vector[1].item(),
            self._vector[2].item(),
            self._vector[3].item()
            )

    def __add__(self, other):
        vector = self.vector + other.vector
        return StokesVector.from_matrix(vector)

    __radd__ = __add__
