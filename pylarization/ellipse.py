"""
Module containing a class describing polarization state using trigonometry.
"""
import numpy as np


class PolariaztionEllipse(object):
    """
    Class for describing polarization state using trygonometry.
    _ellipticity_angle - assuming A is equal to half of the major axis and
        B is equal to half of the minor axis then the tangent of
        ellipticity_angle is equal to B/A.
    _azimuth - angle between the major axis of the ellipse and the x-axis.
    _phase - the phase difference between x and y components.
    _diagonal_angle - ratio between amplitudes of light.
    """
    def __init__(self, **kwargs):
        self._amplitudes = np.matrix([[0], [0]], dtype=complex)
        self._amplitudes[0] = kwargs.get('E0x', 0.0)
        self._amplitudes[1] = kwargs.get('E0y', 0.0)
        self._ellipticity_angle = kwargs.get('ellipticity_angle')
        self._azimuth = kwargs.get('azimuth')
        self._phase = kwargs.get('phase')
        self._diagonal_angle = kwargs.get('diagonal_angle')

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
