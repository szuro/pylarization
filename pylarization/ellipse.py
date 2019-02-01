"""
Module containing a class describing polarization state using trigonometry.
"""
import numpy as np


class PolarizationEllipse(object):
    """
    Class for describing polarization state using trygonometry.

    Parameters
    ----------
    :E0x:
        Amplitude of the electric field vector along the X axis.
    :E0y:
        Amplitude of the electric field vector along the Y axis.
    :phase:
        Phase difference between E0x and E0y.

    Attributes
    ----------
    :_ellipse:
        Float matrix holding values of X and Y amplitudes of
        electric field vector as well as the phase.
    """

    def __init__(self, E0x, E0y, phase):
        self._ellipse = np.array([[E0x], [E0y], [phase]], dtype=float)

    @classmethod
    def from_matrix(cls, matrix_):
        ellipse = cls(matrix_.item(0),
                      matrix_.item(1),
                      matrix_.item(2)
                      )
        return ellipse

    @property
    def E0x(self):
        """
        Return the value of amplitude along X axis

        Returns
        -------
        float
            Amplitude along X axis.
        """
        return self._ellipse[0].item()

    @property
    def E0y(self):
        """
        Return the value of amplitude along Y axis

        Returns
        -------
        float
            Amplitude along Y axis.
        """
        return self._ellipse[1].item()

    @property
    def phase(self):
        """
        Return the phase difference of light amplitudes.

        Returns
        -------
        float
            Phase in radians.
        """
        return self._ellipse[2].item()

    @property
    def intensity(self):
        """
        The intensity of a beam.

        Returns
        -------
        float
            Intensity of the light beam.
        """
        return np.square(self._ellipse[:2]).sum()

    @property
    def azimuth(self):
        """
        Azimuth (orientation angle) of polarized light.

        Returns
        -------
        float
            Azimuth value in radians.

            Expected values are in the range of:

            -diagonal_angle <= azimuth <= diagonal_angle
        """
        cos_phase = np.cos(self.phase)
        try:
            tan_b = self.E0y / self.E0x
            tan_2b = 2 * tan_b / (1 - tan_b**2)
            azimuth = 0.5 * np.arctan(tan_2b * cos_phase)
        except ZeroDivisionError:
            denominator = self.E0x**2 - self.E0y**2
            numerator = 2 * self.E0x * self.E0y * cos_phase
            azimuth = 0.5 * np.arctan2(numerator, denominator)
        finally:
            return azimuth

    @property
    def ellipticity_angle(self, degrees=False):
        """
        Ellipticity angle of polarized light.

        Returns
        -------
        float
            Ellipticity angle in radians.

            Expected values are in the range of:

            -pi/4 <= ellipticity_angle <= pi/4
        """
        numerator = 2 * self.E0x * self.E0y * np.sin(self.phase)
        denominator = self.E0x**2 + self.E0y**2
        ellipticity_angle = 0.5 * np.arcsin(numerator / denominator)
        return ellipticity_angle

    @property
    def diagonal_angle(self, degrees=False):
        """
        Diagonal angle of the rectangle created by light amplitudes.

        Returns
        -------
        float
            Diagonal angle in radians.

            Expected values are in the range of:

            0 <= diagonal_angle <= pi/2
        """
        diagonal_angle = np.arctan2(
            self.E0y,
            self.E0x
            )
        return np.abs(diagonal_angle)

    @property
    def complement_diagonal_angle(self):
        """
        Complement of diagonal angle.

        Returns
        -------
        float
            Complement of the diagonal angle in radians.

            Expected values are in the range of:

            0 <= complement_diagonal_angle <= pi/2
        """
        return np.pi / 2 - self.diagonal_angle

    def __str__(self):
        return "E0x = {:5.3f}, E0y = {:5.3f}, phase = {:5.3f}".format(
            self.E0x,
            self.E0y,
            self.phase
            )

    def __add__(self, other):
        ellipse = self._ellipse + other._ellipse
        return PolarizationEllipse.from_matrix(ellipse)

    ___radd__ = __add__
