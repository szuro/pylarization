"""
Module containing a class describing polarization state using trigonometry.
"""
import numpy as np


class PolariaztionEllipse(object):
    """
    Class for describing polarization state using trygonometry.
    _amplitudes - float matrix holding values of x and y amplitudes of
        electric field vector.
    _ellipticity_angle - assuming A is equal to half of the major axis and
        B is equal to half of the minor axis then the tangent of
        ellipticity_angle is equal to B/A. After removing denominators
        it's obvious that it's just a ratio of the two axes.
    _azimuth - angle between the major axis of the ellipse and the x-axis.
    _phase - the phase difference between x and y components.
    _diagonal_angle - ratio between amplitudes of light.
    _minor_axis - lenght of the minor axis of polarization ellipse.
    _major_axis -  lenght of the major axis of polarization ellipse.
    """
    def __init__(self, **kwargs):
        self._amplitudes = np.matrix([[0], [0]], dtype=float)
        self._amplitudes[0] = kwargs.get('E0x', 0.0)
        self._amplitudes[1] = kwargs.get('E0y', 0.0)
        self._ellipticity_angle = kwargs.get('ellipticity_angle')
        self._azimuth = kwargs.get('azimuth')
        self._phase = kwargs.get('phase')
        self._diagonal_angle = kwargs.get('diagonal_angle')
        self._minor_axis = 0
        self._major_axis = 0

    def _get_property(self, name, degrees=False):
        """
        Return given property in degrees or radians.
        """
        if degrees:
            return np.rad2deg(name)
        return name

    def get_phase(self, degrees=False):
        """
        Return the phase difference of light amplitudes.
        Degrees are optional as numpy uses radians internally.
        """
        return self._get_property(self._phase, degrees)

    def get_azimuth(self, degrees=False):
        """
        Return the azimuth property of light polarization.
        Degrees are optional as numpy uses radians internally.
        """
        return self._get_property(self._azimuth, degrees)

    def get_ellipticity_angle(self, degrees=False):
        """
        Return the ratio of minor to major ellipse axis.
        Degrees are optional as numpy uses radians internally.
        """
        return self._get_property(self._ellipticity_angle, degrees)

    def get_diagonal_angle(self, degrees=False):
        """
        Return the diagonal angle of th rectangle created by light amplitudes.
        Degrees are optional as numpy uses radians internally.
        """
        return self._get_property(self._diagonal_angle, degrees)

    def _calc_axes(self):
        """
        Calculate both axes of the ellipse.
        """
        E0 = np.square(self._amplitudes).sum()
        compelent = self._calc_complement_diagonal_angle()
        sqrt_in_numerator = np.sqrt(1 - np.square(np.sin(compelent)) *
                                    np.square(np.sin(self._phase))
                                    )
        self._minor_axis = E0 * np.sqrt(1 - sqrt_in_numerator) * np.sqrt(0.5)
        self._major_axis = E0 * np.sqrt(1 + sqrt_in_numerator) * np.sqrt(0.5)

    def _calc_complement_diagonal_angle(self):
        """
        Calculate the complement of diagonal angle.
        """
        return np.pi / 2 - self._diagonal_angle

    def _calc_azimuth(self):
        """
        Calculate the azimuth of polarization ellipse.
        """
        self._azimuth = 0.5 * np.arctan(
            np.tan(2 * self._diagonal_angle) * np.cos(self._phase)
            )

    def _calc_ellipticity_angle(self):
        """
        Calculate the ellipticity angle of polarization ellipse.
        """
        self._ellipticity_angle = 0.5 * np.arcsin(
            np.tan(2 * self._diagonal_angle) * np.sin(self._phase)
            )

    def _calc_diagonal_angle_from_amplitudes(self):
        """
        Calculate the diagtonal angle of polarization ellipse using amplitudes.
        """
        self._diagonal_angle = np.arctan(
            self._amplitudes[1],
            self._amplitudes[0]
            )

    def _calc_diagonal_angle_from_azimuth(self):
        """
        Calculate the diagtonal angle of polarization ellipse using azumuth
        and phase diference.
        """
        self._diagonal_angle = 0.5 * np.arctan(
            np.tan(2 * self._azimuth) / np.cos(self._phase)
            )

    def _calc_diagonal_angle_from_ellipticity_angle(self):
        """
        Calculate the diagtonal angle of polarization ellipse using
        ellipticity angle and phase diference.
        """
        self._diagonal_angle = 0.5 * np.arcsin(
            np.sin(2 * self._ellipticity_angle) / np.sin(self._phase)
            )

    def _calc_phase(self):
        """
        Calculate the phase difference.
        """
        self._phase = np.arctan(
            np.tan(2 * self._ellipticity_angle) /
            np.sin(2 * self._azimuth)
            )
