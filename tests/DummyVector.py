import unittest
import math
from math import pi


class DummyVector(object):
    def __init__(self,
                 ellipticity_angle=0.0,
                 azimuth=0.0,
                 phase=0.0,
                 diagonal_angle=0.0,
                 complement_diagonal_angle=0.0
                 ):
        self.ellipticity_angle = ellipticity_angle
        self.azimuth = azimuth
        self.phase = phase
        self.diagonal_angle = diagonal_angle
        self.complement_diagonal_angle = complement_diagonal_angle


class DummyVectorValues(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = DummyVector()
        self.linear_vertical = DummyVector(azimuth=pi/2)
        self.linear_plus45 = DummyVector(azimuth=pi/4)
        self.linear_minus45 = DummyVector(azimuth=-pi/4)
        self.elliptic = DummyVector(ellipticity_angle=0.46373398,
                                    phase=1.57079632)
        self.circular_left_handed = DummyVector(phase=pi/2)
        self.circular_right_handed = DummyVector(phase=-pi/2)

    def test_azimuth(self):
        self.assertAlmostEqual(self.linear_horizontal.azimuth, 0.0)
        self.assertAlmostEqual(self.linear_vertical.azimuth, pi/2)
        self.assertAlmostEqual(self.linear_plus45.azimuth, pi/4)
        self.assertAlmostEqual(self.linear_minus45.azimuth, -pi/4)
        self.assertAlmostEqual(self.elliptic.azimuth, 0.0)

    def test_phase(self):
        self.assertAlmostEqual(self.linear_horizontal.phase, 0.0)
        self.assertAlmostEqual(self.linear_vertical.phase, 0.0)
        self.assertAlmostEqual(self.linear_plus45.phase, 0.0)
        self.assertAlmostEqual(self.linear_minus45.phase, 0.0)
        self.assertAlmostEqual(self.elliptic.phase, pi/2)

    def test_ellipticity_angle(self):
        self.assertAlmostEqual(self.linear_horizontal.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_vertical.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_plus45.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_minus45.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.elliptic.ellipticity_angle, 0.46373398)

    def test_diagonal_angle(self):
        self.assertAlmostEqual(self.linear_horizontal.diagonal_angle, 0.0)
        self.assertAlmostEqual(self.linear_vertical.diagonal_angle, pi/2)
        self.assertAlmostEqual(self.linear_plus45.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.linear_minus45.diagonal_angle, -pi/4)
