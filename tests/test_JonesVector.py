import unittest
from numpy import sqrt, pi
from pylarization.vectors import JonesVector
from pylarization.ellipse import PolarizationEllipse
from pylarization.polarizations import JonesVectorState, PolarizationEllipseState
from tests import DummyVector


E = sqrt(2) * 0.5


class TestJonesVectorValues(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = JonesVectorState.LINEAR_HORIZONTAL.value
        self.linear_vertical = JonesVectorState.LINEAR_VERTICAL.value
        self.linear_plus45 = JonesVectorState.LINEAR_DIAGONAL.value
        self.linear_minus45 = JonesVectorState.LINEAR_ANTIDIAGONAL.value
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVectorState.CIRCULAR_LEFT_HANDED.value
        self.circular_right_handed = JonesVectorState.CIRCULAR_RIGHT_HANDED.value

    def test_E0x(self):
        self.assertAlmostEqual(self.linear_horizontal.E0x, PolarizationEllipseState.LINEAR_HORIZONTAL.value.E0x)
        self.assertAlmostEqual(self.linear_vertical.E0x, PolarizationEllipseState.LINEAR_VERTICAL.value.E0x)
        self.assertAlmostEqual(self.linear_plus45.E0x, PolarizationEllipseState.LINEAR_DIAGONAL.value.E0x)
        self.assertAlmostEqual(self.linear_minus45.E0x, PolarizationEllipseState.LINEAR_ANTIDIAGONAL.value.E0x)
        self.assertAlmostEqual(self.circular_left_handed.E0x, PolarizationEllipseState.CIRCULAR_LEFT_HANDED.value.E0x)
        self.assertAlmostEqual(self.circular_right_handed.E0x, PolarizationEllipseState.CIRCULAR_RIGHT_HANDED.value.E0x)
        self.assertAlmostEqual(self.elliptic.E0x, PolarizationEllipse(0.445, 0.89, pi/2).E0x)

    def test_E0y(self):
        self.assertAlmostEqual(self.linear_horizontal.E0y, PolarizationEllipseState.LINEAR_HORIZONTAL.value.E0y)
        self.assertAlmostEqual(self.linear_vertical.E0y, PolarizationEllipseState.LINEAR_VERTICAL.value.E0y)
        self.assertAlmostEqual(self.linear_plus45.E0y, PolarizationEllipseState.LINEAR_DIAGONAL.value.E0y)
        self.assertAlmostEqual(self.linear_minus45.E0y, PolarizationEllipseState.LINEAR_ANTIDIAGONAL.value.E0y)
        self.assertAlmostEqual(self.circular_left_handed.E0y, PolarizationEllipseState.CIRCULAR_LEFT_HANDED.value.E0y)
        self.assertAlmostEqual(self.circular_right_handed.E0y, PolarizationEllipseState.CIRCULAR_RIGHT_HANDED.value.E0y)
        self.assertAlmostEqual(self.elliptic.E0y, PolarizationEllipse(0.445, 0.89, pi/2).E0y)

    def test_phase(self):
        self.assertAlmostEqual(self.linear_horizontal.phase, PolarizationEllipseState.LINEAR_HORIZONTAL.value.phase)
        self.assertAlmostEqual(self.linear_vertical.phase, PolarizationEllipseState.LINEAR_VERTICAL.value.phase)
        self.assertAlmostEqual(self.linear_plus45.phase, PolarizationEllipseState.LINEAR_DIAGONAL.value.phase)
        self.assertAlmostEqual(self.linear_minus45.phase, PolarizationEllipseState.LINEAR_ANTIDIAGONAL.value.phase)
        self.assertAlmostEqual(self.circular_left_handed.phase, PolarizationEllipseState.CIRCULAR_LEFT_HANDED.value.phase)
        self.assertAlmostEqual(self.circular_right_handed.phase, PolarizationEllipseState.CIRCULAR_RIGHT_HANDED.value.phase)
        self.assertAlmostEqual(self.elliptic.phase, PolarizationEllipse(0.445, 0.89, pi/2).phase)


class TestJonesVectorNormalization(DummyVector.TestDummyVectorNormalization):
    def setUp(self):
        self.linear_horizontal = JonesVectorState.LINEAR_HORIZONTAL.value
        self.linear_vertical = JonesVectorState.LINEAR_VERTICAL.value
        self.linear_plus45 = JonesVectorState.LINEAR_DIAGONAL.value
        self.linear_minus45 = JonesVectorState.LINEAR_ANTIDIAGONAL.value
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVectorState.CIRCULAR_LEFT_HANDED.value
        self.circular_right_handed = JonesVectorState.CIRCULAR_RIGHT_HANDED.value

        self.linear_horizontal_normalized = JonesVectorState.LINEAR_HORIZONTAL.value
        self.linear_horizontal_normalized.normalize()

        self.linear_vertical_normalized = JonesVectorState.LINEAR_VERTICAL.value
        self.linear_vertical_normalized.normalize()

        self.linear_plus45_normalized = JonesVectorState.LINEAR_DIAGONAL.value
        self.linear_plus45_normalized.normalize()

        self.linear_minus45_normalized = JonesVectorState.LINEAR_ANTIDIAGONAL.value
        self.linear_minus45_normalized.normalize()

        self.elliptic_normalized = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.elliptic_normalized.normalize()

        self.circular_left_handed_normalized = JonesVectorState.CIRCULAR_LEFT_HANDED.value
        self.circular_left_handed_normalized.normalize()

        self.circular_right_handed_normalized = JonesVectorState.CIRCULAR_RIGHT_HANDED.value
        self.circular_right_handed_normalized.normalize()


class TestJonesVectorAddition(unittest.TestCase):
    def setUp(self):
        self.circular_left_handed = JonesVectorState.CIRCULAR_LEFT_HANDED.value
        self.circular_right_handed = JonesVectorState.CIRCULAR_RIGHT_HANDED.value

    def test_addition(self):
        expected_sum = JonesVector(2 / sqrt(2), 0)
        vector_sum = self.circular_right_handed + self.circular_left_handed
        self.assertEqual(expected_sum.vector.all(), vector_sum.vector.all())


if __name__ == '__main__':
    unittest.main()
