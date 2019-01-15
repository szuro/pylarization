import unittest
from numpy import pi


class DummyVector(object):
    def __init__(self,
                 ellipticity_angle=0.0,
                 azimuth=0.0,
                 phase=0.0,
                 diagonal_angle=0.0,
                 complement_diagonal_angle=0.0):
        self.ellipticity_angle = ellipticity_angle
        self.azimuth = azimuth
        self.phase = phase
        self.diagonal_angle = diagonal_angle
        self.complement_diagonal_angle = complement_diagonal_angle


class TestDummyVectorValues(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = DummyVector()
        self.linear_vertical = DummyVector(azimuth=pi/2, diagonal_angle=pi/2)
        self.linear_plus45 = DummyVector(azimuth=pi/4, diagonal_angle=pi/4)
        self.linear_minus45 = DummyVector(azimuth=-pi/4, phase=pi, diagonal_angle=pi/4)
        self.elliptic = DummyVector(ellipticity_angle=0.463647609, phase=pi/2)
        self.circular_left_handed = DummyVector(ellipticity_angle=-pi/4, phase=-pi/2, diagonal_angle=pi/4)
        self.circular_right_handed = DummyVector(ellipticity_angle=pi/4, phase=pi/2, diagonal_angle=pi/4)

    def test_azimuth(self):
        self.assertAlmostEqual(self.linear_horizontal.azimuth, 0.0)
        self.assertAlmostEqual(self.linear_vertical.azimuth, pi/2)
        self.assertAlmostEqual(self.linear_plus45.azimuth, pi/4)
        self.assertAlmostEqual(self.linear_minus45.azimuth, -pi/4)
        self.assertAlmostEqual(self.elliptic.azimuth, 0.0)
        self.assertIsNotNone(self.circular_left_handed)
        self.assertIsNotNone(self.circular_right_handed)

    def test_phase(self):
        self.assertAlmostEqual(self.linear_horizontal.phase, 0.0)
        self.assertAlmostEqual(self.linear_vertical.phase, 0.0)
        self.assertAlmostEqual(self.linear_plus45.phase, 0.0)
        self.assertAlmostEqual(self.linear_minus45.phase, pi)
        self.assertAlmostEqual(self.elliptic.phase, pi/2)
        self.assertAlmostEqual(self.circular_left_handed.phase, -pi/2)
        self.assertAlmostEqual(self.circular_right_handed.phase, pi/2)

    def test_ellipticity_angle(self):
        self.assertAlmostEqual(self.linear_horizontal.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_vertical.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_plus45.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_minus45.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.elliptic.ellipticity_angle, 0.463647609)
        self.assertAlmostEqual(self.circular_left_handed.ellipticity_angle, -pi/4)
        self.assertAlmostEqual(self.circular_right_handed.ellipticity_angle, pi/4)

    def test_diagonal_angle(self):
        self.assertAlmostEqual(self.linear_horizontal.diagonal_angle, 0.0)
        self.assertAlmostEqual(self.linear_vertical.diagonal_angle, pi/2)
        self.assertAlmostEqual(self.linear_plus45.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.linear_minus45.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.circular_left_handed.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.circular_right_handed.diagonal_angle, pi/4)


class TestDummyVectorNormalization(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = DummyVector()
        self.linear_vertical = DummyVector()
        self.linear_plus45 = DummyVector()
        self.linear_minus45 = DummyVector()
        self.elliptic = DummyVector()
        self.circular_left_handed = DummyVector()
        self.circular_right_handed = DummyVector()

        self.linear_horizontal_normalized = DummyVector()
        self.linear_vertical_normalized = DummyVector()
        self.linear_plus45_normalized = DummyVector()
        self.linear_minus45_normalized = DummyVector()
        self.elliptic_normalized = DummyVector()
        self.circular_left_handed_normalized = DummyVector()
        self.circular_right_handed_normalized = DummyVector()

    def test_normalized_azimuth(self):
        self.assertAlmostEqual(
            self.linear_horizontal.azimuth,
            self.linear_horizontal_normalized.azimuth)
        self.assertAlmostEqual(
            self.linear_vertical.azimuth,
            self.linear_vertical_normalized.azimuth)
        self.assertAlmostEqual(
            self.linear_plus45.azimuth,
            self.linear_plus45_normalized.azimuth)
        self.assertAlmostEqual(
            self.linear_minus45.azimuth,
            self.linear_minus45_normalized.azimuth)
        self.assertAlmostEqual(
            self.elliptic.azimuth,
            self.elliptic_normalized.azimuth)
        self.assertAlmostEqual(
            self.circular_left_handed.azimuth,
            self.circular_left_handed_normalized.azimuth)
        self.assertAlmostEqual(
            self.circular_right_handed.azimuth,
            self.circular_right_handed_normalized.azimuth)

    def test_normalized_phase(self):
        self.assertAlmostEqual(
            self.linear_horizontal.phase,
            self.linear_horizontal_normalized.phase)
        self.assertAlmostEqual(
            self.linear_vertical.phase,
            self.linear_vertical_normalized.phase)
        self.assertAlmostEqual(
            self.linear_plus45.phase,
            self.linear_plus45_normalized.phase)
        self.assertAlmostEqual(
            self.linear_minus45.phase,
            self.linear_minus45_normalized.phase)
        self.assertAlmostEqual(
            self.elliptic.phase,
            self.elliptic_normalized.phase)
        self.assertAlmostEqual(
            self.circular_left_handed.phase,
            self.circular_left_handed_normalized.phase)
        self.assertAlmostEqual(
            self.circular_right_handed.phase,
            self.circular_right_handed_normalized.phase)

    def test_normalized_ellipticity_angle(self):
        self.assertAlmostEqual(
            self.linear_horizontal.ellipticity_angle,
            self.linear_horizontal_normalized.ellipticity_angle)
        self.assertAlmostEqual(
            self.linear_vertical.ellipticity_angle,
            self.linear_vertical_normalized.ellipticity_angle)
        self.assertAlmostEqual(
            self.linear_plus45.ellipticity_angle,
            self.linear_plus45_normalized.ellipticity_angle)
        self.assertAlmostEqual(
            self.linear_minus45.ellipticity_angle,
            self.linear_minus45_normalized.ellipticity_angle)
        self.assertAlmostEqual(
            self.elliptic.ellipticity_angle,
            self.elliptic_normalized.ellipticity_angle)
        self.assertAlmostEqual(
            self.circular_left_handed.ellipticity_angle,
            self.circular_left_handed_normalized.ellipticity_angle)
        self.assertAlmostEqual(
            self.circular_right_handed.ellipticity_angle,
            self.circular_right_handed_normalized.ellipticity_angle)

    def test_normalized_diagonal_angle(self):
        self.assertAlmostEqual(
            self.linear_horizontal.diagonal_angle,
            self.linear_horizontal_normalized.diagonal_angle)
        self.assertAlmostEqual(
            self.linear_vertical.diagonal_angle,
            self.linear_vertical_normalized.diagonal_angle)
        self.assertAlmostEqual(
            self.linear_plus45.diagonal_angle,
            self.linear_plus45_normalized.diagonal_angle)
        self.assertAlmostEqual(
            self.linear_minus45.diagonal_angle,
            self.linear_minus45_normalized.diagonal_angle)
        self.assertAlmostEqual(
            self.elliptic.diagonal_angle,
            self.elliptic_normalized.diagonal_angle)
        self.assertAlmostEqual(
            self.circular_left_handed.diagonal_angle,
            self.circular_left_handed_normalized.diagonal_angle)
        self.assertAlmostEqual(
            self.circular_right_handed.diagonal_angle,
            self.circular_right_handed_normalized.diagonal_angle)
