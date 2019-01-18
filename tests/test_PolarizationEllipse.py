import unittest
from numpy import pi, sqrt
from pylarization.ellipse import PolarizationEllipse
from tests import DummyVector


E = sqrt(2) * 0.5


class TestPolarizationEllipseValues(DummyVector.TestDummyVectorValues):
    def setUp(self):
        self.linear_horizontal = PolarizationEllipse(1.0, 0.0, 0.0)
        self.linear_vertical = PolarizationEllipse(0.0, 1.0, 0.0)
        self.linear_plus45 = PolarizationEllipse(E, E, 0.0)
        self.linear_minus45 = PolarizationEllipse(E, E, pi)
        self.elliptic = PolarizationEllipse(0.445, 0.89, pi/2)
        self.circular_left_handed = PolarizationEllipse(E, E, -pi/2)
        self.circular_right_handed = PolarizationEllipse(E, E, pi/2)


class TestPolarizationEllipseAddition(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = PolarizationEllipse(2.0, 0.0, 0.5)
        self.linear_vertical = PolarizationEllipse(0.0, 1.0, 0.0)

    def test_addition(self):
        expected_sum = PolarizationEllipse(2.0, 1.0, 0.5)
        vector_sum = self.linear_horizontal + self.linear_vertical
        self.assertEqual(
            expected_sum._amplitudes[0].item(),
            vector_sum._amplitudes[0].item()
            )
        self.assertAlmostEqual(
            expected_sum._amplitudes[1].item(),
            vector_sum._amplitudes[1].item()
            )
        self.assertAlmostEqual(expected_sum.phase, vector_sum.phase)


if __name__ == '__main__':
    unittest.main()
