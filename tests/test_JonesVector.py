import unittest
from numpy import sqrt
from pylarization.vectors import JonesVector
from tests import DummyVector


E = sqrt(2) * 0.5


class TestJonesVectorValues(DummyVector.TestDummyVectorValues):
    def setUp(self):
        self.linear_horizontal = JonesVector(1, 0)
        self.linear_vertical = JonesVector(0, 1)
        self.linear_plus45 = JonesVector(E, E)
        self.linear_minus45 = JonesVector(E, -E)
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVector(E, -E * 1j)
        self.circular_right_handed = JonesVector(E, E * 1j)


class TestJonesVectorNormalization(DummyVector.TestDummyVectorNormalization):
    def setUp(self):
        self.linear_horizontal = JonesVector(1, 0)
        self.linear_vertical = JonesVector(0, 1)
        self.linear_plus45 = JonesVector(E, E)
        self.linear_minus45 = JonesVector(E, -E)
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVector(E, -E * 1j)
        self.circular_right_handed = JonesVector(E, E * 1j)

        self.linear_horizontal_normalized = JonesVector(1, 0)
        self.linear_horizontal_normalized.normalize()

        self.linear_vertical_normalized = JonesVector(0, 1)
        self.linear_vertical_normalized.normalize()

        self.linear_plus45_normalized = JonesVector(E, E)
        self.linear_plus45_normalized.normalize()

        self.linear_minus45_normalized = JonesVector(E, -E)
        self.linear_minus45_normalized.normalize()

        self.elliptic_normalized = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.elliptic_normalized.normalize()

        self.circular_left_handed_normalized = JonesVector(E, -E * 1j)
        self.circular_left_handed_normalized.normalize()

        self.circular_right_handed_normalized = JonesVector(E, E * 1j)
        self.circular_right_handed_normalized.normalize()


class TestJonesVectorAddition(unittest.TestCase):
    def setUp(self):
        self.circular_left_handed = JonesVector(E, -E * 1j)
        self.circular_right_handed = JonesVector(E, E * 1j)

    def test_addition(self):
        expected_sum = JonesVector(2 / sqrt(2), 0)
        vector_sum = self.circular_right_handed + self.circular_left_handed
        self.assertEqual(expected_sum.vector.all(), vector_sum.vector.all())


if __name__ == '__main__':
    unittest.main()
