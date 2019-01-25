import unittest
from numpy import sqrt
from pylarization.vectors import JonesVector
from pylarization.polarizations import JonesVectorState
from tests import DummyVector


E = sqrt(2) * 0.5


class TestJonesVectorValues(DummyVector.TestDummyVectorValues):
    def setUp(self):
        self.linear_horizontal = JonesVectorState.LINEAR_HORIZONTAL.value
        self.linear_vertical = JonesVectorState.LINEAR_VERTICAL.value
        self.linear_plus45 = JonesVectorState.LINEAR_DIAGONAL.value
        self.linear_minus45 = JonesVectorState.LINEAR_ANTIDIAGONAL.value
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)
        self.circular_left_handed = JonesVectorState.CIRCULAR_LEFT_HANDED.value
        self.circular_right_handed = JonesVectorState.CIRCULAR_RIGHT_HANDED.value


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
