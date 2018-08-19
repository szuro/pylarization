import unittest
from numpy import sqrt
from pylarization.vectors import JonesVector
from tests import DummyVector


class JonesVectorValues(DummyVector.DummyVectorValues):
    def setUp(self):
        self.linear_horizontal = JonesVector(1, 0)
        self.linear_vertical = JonesVector(0, 1)
        a = sqrt(2) * 0.5
        self.linear_plus45 = JonesVector(a, a)
        self.linear_minus45 = JonesVector(a, -a)
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVector(a, -a * 1j)
        self.circular_right_handed = JonesVector(a, a * 1j)


class JonesVectorNormalization(DummyVector.DummyVectorNormalization):
    def setUp(self):
        self.linear_horizontal = JonesVector(1, 0)
        self.linear_vertical = JonesVector(0, 1)
        a = sqrt(2) * 0.5
        self.linear_plus45 = JonesVector(a, a)
        self.linear_minus45 = JonesVector(a, -a)
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVector(a, -a * 1j)
        self.circular_right_handed = JonesVector(a, a * 1j)

        self.linear_horizontal_normalized = JonesVector(1, 0)
        self.linear_horizontal_normalized.normalize()

        self.linear_vertical_normalized = JonesVector(0, 1)
        self.linear_vertical_normalized.normalize()

        self.linear_plus45_normalized = JonesVector(a, a)
        self.linear_plus45_normalized.normalize()

        self.linear_minus45_normalized = JonesVector(a, -a)
        self.linear_minus45_normalized.normalize()

        self.elliptic_normalized = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.elliptic_normalized.normalize()

        self.circular_left_handed_normalized = JonesVector(a, -a * 1j)
        self.circular_left_handed_normalized.normalize()

        self.circular_right_handed_normalized = JonesVector(a, a * 1j)
        self.circular_right_handed_normalized.normalize()


if __name__ == '__main__':
    unittest.main()
