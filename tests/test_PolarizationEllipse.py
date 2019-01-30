import unittest
from numpy import pi, sqrt
from pylarization.ellipse import PolarizationEllipse
from pylarization.polarizations import PolarizationEllipseState
from tests import DummyVector


E = sqrt(2) * 0.5


class TestPolarizationEllipseValues(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = PolarizationEllipseState.LINEAR_HORIZONTAL.value
        self.linear_vertical = PolarizationEllipseState.LINEAR_VERTICAL.value
        self.linear_plus45 = PolarizationEllipseState.LINEAR_DIAGONAL.value
        self.linear_minus45 = PolarizationEllipseState.LINEAR_ANTIDIAGONAL.value
        self.circular_left_handed = PolarizationEllipseState.CIRCULAR_LEFT_HANDED.value
        self.circular_right_handed = PolarizationEllipseState.CIRCULAR_RIGHT_HANDED.value
        self.elliptic = PolarizationEllipse(0.445, 0.89, pi/2)

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
        self.assertAlmostEqual(self.circular_left_handed.phase, pi/2)
        self.assertAlmostEqual(self.circular_right_handed.phase, -pi/2)

    def test_ellipticity_angle(self):
        self.assertAlmostEqual(self.linear_horizontal.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_vertical.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_plus45.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.linear_minus45.ellipticity_angle, 0.0)
        self.assertAlmostEqual(self.elliptic.ellipticity_angle, 0.463647609)
        self.assertAlmostEqual(self.circular_left_handed.ellipticity_angle, pi/4)
        self.assertAlmostEqual(self.circular_right_handed.ellipticity_angle, -pi/4)

    def test_diagonal_angle(self):
        self.assertAlmostEqual(self.linear_horizontal.diagonal_angle, 0.0)
        self.assertAlmostEqual(self.linear_vertical.diagonal_angle, pi/2)
        self.assertAlmostEqual(self.linear_plus45.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.linear_minus45.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.circular_left_handed.diagonal_angle, pi/4)
        self.assertAlmostEqual(self.circular_right_handed.diagonal_angle, pi/4)


class TestPolarizationEllipseAddition(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = PolarizationEllipse(2.0, 0.0, 0.5)
        self.linear_vertical = PolarizationEllipse(0.0, 1.0, 0.0)

    def test_addition(self):
        expected_sum = PolarizationEllipse(2.0, 1.0, 0.5)
        vector_sum = self.linear_horizontal + self.linear_vertical
        self.assertEqual(
            expected_sum._ellipse[0].item(),
            vector_sum._ellipse[0].item()
            )
        self.assertAlmostEqual(
            expected_sum._ellipse[1].item(),
            vector_sum._ellipse[1].item()
            )
        self.assertAlmostEqual(expected_sum.phase, vector_sum.phase)


if __name__ == '__main__':
    unittest.main()
