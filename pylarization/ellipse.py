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
    :_amplitudes:
        Float matrix holding values of x and y amplitudes of
        electric field vector.
    :_phase:
        The phase difference between x and y components.
    """

    def __init__(self, E0x, E0y, phase):
        self._amplitudes = np.matrix([[E0x], [E0y]], dtype=float)
        self._phase = phase

    @property
    def E0x(self):
        """Return the value of amplitude along x axis"""
        return self._amplitudes[0].item()

    @property
    def E0y(self):
        """Return the value of amplitude along y axis"""
        return self._amplitudes[1].item()

    @property
    def phase(self):
        """
        Return the phase difference of light amplitudes.

        Returns
        -------
        float
            Phase in radians.

        Examples
        --------
            >>> light = PolarizationEllipse(0.445, 0.89, 3.1415/2)
            >>> round(light.phase, 2)
            1.57
        """
        return self._phase

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

        Examples
        --------
            >>> light = PolarizationEllipse(0.445, 0.89, 3.1415/2)
            >>> round(light.azimuth, 2)
            0.0
            >>> light = PolarizationEllipse(1, 0, 0)
            >>> round(light.azimuth, 2)
            0.0
            >>> light = PolarizationEllipse(0, 1, 0)
            >>> round(light.azimuth, 2)
            1.57
        """
        cos_phase = np.cos(self.phase)
        try:
            tanb = self.E0y / self.E0x
            tan2b = 2 * tanb / (1 - tanb**2)
            azimuth = 0.5 * np.arctan(tan2b * cos_phase)
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

        Examples
        --------
            >>> light = PolarizationEllipse(0.445, 0.89, 3.1415/2)
            >>> round(light.ellipticity_angle, 2)
            0.46
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

        Examples
        --------
            >>> light = PolarizationEllipse(0.445, 0.89, 3.1415/2)
            >>> round(light.diagonal_angle, 2)
            1.11
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

        Examples
        --------
            >>> light = PolarizationEllipse(0.445, 0.89, 3.1415/2)
            >>> round(light.complement_diagonal_angle, 2)
            0.46
        """
        return np.pi / 2 - self.diagonal_angle

    def calc_axes(self):
        """
        Calculate both axes of the ellipse.
        """
        E0 = np.square(self._amplitudes).sum()
        compelent = self.complement_diagonal_angle()
        sqrt_in_numerator = np.sqrt(1 - np.square(np.sin(compelent)) *
                                    np.square(np.sin(self._phase))
                                    )
        minor_axis = E0 * np.sqrt(1 - sqrt_in_numerator) * np.sqrt(0.5)
        major_axis = E0 * np.sqrt(1 + sqrt_in_numerator) * np.sqrt(0.5)
        return major_axis, minor_axis

    def __str__(self):
        return "E0x={}, E0y={}, phase={}".format(
            self.E0x,
            self.E0y,
            self.phase
            )
