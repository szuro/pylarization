"""
Module containing a class describing polarization state using trigonometry.
"""
import numpy as np


class PolarizationEllipse(object):
    """
    Class for describing polarization state using trygonometry.
    amplitudes - float matrix holding values of x and y amplitudes of
        electric field vector.
    ellipticity_angle - assuming A is equal to half of the major axis and
        B is equal to half of the minor axis then the tangent of
        ellipticity_angle is equal to B/A. After removing denominators
        it's obvious that it's just a ratio of the two axes.
    azimuth - angle between the major axis of the ellipse and the x-axis.
    phase - the phase difference between x and y components.
    diagonal_angle - ratio between amplitudes of light.
    complement_diagonal_angle - the complement of the diagonal angle.
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
        """
        return self._phase

    @property
    def azimuth(self):
        """
        Return the azimuth property of light polarization.
        Values should be in range:
        -diagonal angle <= azimuth <= diagonal angle
        """
        numerator = 2 * self.E0x * self.E0y * np.cos(self.phase)
        denominator = self.E0x**2 + self.E0y**2
        azimuth = 0.5 * np.arctan2(numerator, denominator)
        return azimuth

    @property
    def ellipticity_angle(self, degrees=False):
        """
        Return the ratio of minor to major ellipse axis.
        Values should be in range:
        -pi/4 <= ellipticity angle <= pi/4
        """
        ellipticity_angle = 0.5 * np.arcsin(
            np.tan(2 * self.diagonal_angle) * np.sin(self._phase)
            )
        return ellipticity_angle

    @property
    def diagonal_angle(self, degrees=False):
        """
        Return the diagonal angle of th rectangle created by light amplitudes.
        Values should be in range:
        0 <= diagonal angle <= pi/2
        """
        diagonal_angle = np.arctan2(
            self._amplitudes[1].item(),
            self._amplitudes[0].item()
            )
        return diagonal_angle

    @property
    def complement_diagonal_angle(self):
        """
        Calculate the complement of diagonal angle.
        Values should be in range:
        0 <= complement of diagonal angle <= pi/2
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

    def _calc_diagonal_angle_from_azimuth(self):
        """
        Calculate the diagtonal angle of polarization ellipse using azumuth
        and phase diference.
        """
        diagonal_angle = 0.5 * np.arctan(
            np.tan(2 * self.azimuth) / np.cos(self._phase)
            )
        return diagonal_angle

    def _calc_diagonal_angle_from_ellipticity_angle(self):
        """
        Calculate the diagtonal angle of polarization ellipse using
        ellipticity angle and phase diference.
        """
        diagonal_angle = 0.5 * np.arcsin(
            np.sin(2 * self.ellipticity_angle) / np.sin(self._phase)
            )
        return diagonal_angle

    def _calc_phase(self):
        """
        Calculate the phase difference.
        """
        phase = np.arctan(
            np.tan(2 * self.ellipticity_angle) /
            np.sin(2 * self.azimuth)
            )
        return phase

    def __str__(self):
        return "E0x={}, E0y={}, phase={}".format(
            self._amplitudes[0].item(),
            self._amplitudes[0].item(),
            self._phase
            )
