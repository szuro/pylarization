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
    """
    def __init__(self):
        self._amplitudes = np.matrix([[0], [0]])
        self._ellipticity_angle = 0
        self._azimuth = 0
        self._phase = 0

    def get_phase(self, degrees=False):
        """
        Return the phase difference of light amplitudes.
        Degrees are optional as numpy uses radians internally.
        """
        if degrees:
            return np.rad2deg(self._phase)
        return self._phase

    def get_azimuth(self, degrees=False):
        """
        Return the phase difference of light amplitudes.
        Degrees are optional as numpy uses radians internally.
        """
        if degrees:
            return np.rad2deg(self._azimuth)
        return self._azimuth

    def get_ellipticity_angle(self, degrees=False):
        """
        Return the phase difference of light amplitudes.
        Degrees are optional as numpy uses radians internally.
        """
        if degrees:
            return np.rad2deg(self._ellipticity_angle)
        return self._ellipticity_angle
