"""
Module containing classes used for describing light polarization.
"""


class Ellipse(object):
    """
    Class for describing polarization state using trygonometry.
    _ellipticity_angle - assuming A is equal to half of the major axis and
        B is equal to half of the minor axis then the tangent of
        ellipticity_angle is equal to B/A.
    _azimuth - angle between the major axis of the ellipse and the x-axis.
    _phase - the phase difference between x and y components.
    """
    def __init__(self):
        self._ellipticity_angle = 0
        self._azimuth = 0
        self._phase = 0


class Jones(Ellipse):
    """
    Class for describing polarization state using Jones vector.
    """
    pass


class Stokes(Ellipse):
    """
    Class for describing polarization state using Stokes vector.
    """
    pass
