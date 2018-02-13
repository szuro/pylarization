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
        self.simplify()
        super().__init__(self.E0x, self.E0y, self.phase)

    @property
    def vector(self):
        """
        Return full Jones vector.
        """
        return self._vector[0].item(), self._vector[1].item()

    @property
    def E0x(self):
        """Return the value of amplitude along x axis"""
        return self._get_amplitude(0)

    @property
    def E0y(self):
        """Return the value of amplitude along y axis"""
        return self._get_amplitude(1)

    @property
    def phase(self):
        """
        Return the phase difference of light amplitudes.
        """
        asqrt = np.sqrt(self._vector[1] * np.conj(self._vector[1]))
        if asqrt == 0.0:
            asqrt = 1
        a = self._vector[1] / asqrt
        return np.angle(a)

    def simplify(self):
        """
        Method for transforming Jones vector to its simplified version.
        Simplification is required to calculate phase.
        """
        asqrt = np.sqrt(self._vector[0] * np.conj(self._vector[0]))
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

    def _get_amplitude(self, index):
        """
        Returns the amplitude along specified axis.
        Amplitudes are always real.
        """
        return np.sqrt(
            self._vector[index] * np.conj(self._vector[index])
            ).item().real


class StokesVector(PolarizationEllipse):
    """
    Class for describing polarization state using Stokes vector.
    """
    pass
